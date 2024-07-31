# End-To-End Data Engineering Project

## Project Overview

This project demonstrates an end-to-end data engineering pipeline using Apache Airflow and Python. The pipeline extracts data from the Twitter API, transforms the data, and saves the final results to Amazon S3. The entire workflow is orchestrated using Apache Airflow, and the code is deployed on an EC2 instance.

## Objectives

1. **Extract Data**: Fetch data from the Twitter API.
2. **Transform Data**: Process and transform the data using Python.
3. **Deploy**: Deploy the workflow on Apache Airflow running on EC2.
4. **Save Results**: Store the final processed data in Amazon S3.

## Components

- **Twitter API**: Used to extract raw data.
- **Python**: Used for data transformation.
- **Apache Airflow**: Orchestrates the ETL pipeline.
- **Amazon S3**: Stores the final processed data.

## Setup Instructions

### 1. Install Dependencies

Create a virtual environment and install the required Python packages:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Twitter API

Create a `config.py` file in the project root with your Twitter API credentials:

```python
# config.py
TWITTER_API_KEY = 'your_twitter_api_key'
TWITTER_API_SECRET_KEY = 'your_twitter_api_secret_key'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_TOKEN_SECRET = 'your_twitter_access_token_secret'
```

### 3. Configure Airflow

Set up Apache Airflow on your EC2 instance:

1. Follow the [Airflow installation guide](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html).
2. Place the Airflow DAGs (located in `dags/`) in the Airflow DAGs folder.

### 4. Deploy on EC2

1. Launch an EC2 instance with appropriate IAM roles for S3 and Airflow.
2. Transfer your project files to the EC2 instance.
3. Configure and start Apache Airflow on EC2.

### 5. Create Amazon S3 Bucket

Create an S3 bucket where the final results will be stored.

### 6. Run the Airflow DAG

Trigger the DAG in Airflow to start the data extraction, transformation, and loading process.

## Directory Structure

```
.
├── dags
│   ├── twitter_etl_dag.py
├── src
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
├── requirements.txt
├── config.py
└── README.md
```

## Scripts

- **`extract.py`**: Contains code to fetch data from the Twitter API.
- **`transform.py`**: Contains code to process and clean the data.
- **`load.py`**: Contains code to save the final data to Amazon S3.
- **`twitter_etl_dag.py`**: Apache Airflow DAG for orchestrating the ETL process.

## Requirements

- Python 3.x
- Apache Airflow
- boto3 (for AWS S3 interactions)
- tweepy (for Twitter API interactions)
- pandas (for data transformation)

## License

This project is licensed under the [MIT Licence](License).

## Author

[Arun Kumar Pandey](https://arunp77.github.io/)
```

### `requirements.txt`

```text
apache-airflow==2.7.0
boto3==1.26.0
pandas==2.0.2
tweepy==4.12.1
```

### `dags/twitter_etl_dag.py`

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.extract import extract_twitter_data
from src.transform import transform_data
from src.load import load_to_s3

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'twitter_etl_dag',
    default_args=default_args,
    description='An ETL pipeline that extracts data from Twitter, transforms it, and loads it to S3.',
    schedule_interval='@daily',
    start_date=datetime(2024, 7, 31),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract_twitter_data',
        python_callable=extract_twitter_data,
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id='load_to_s3',
        python_callable=load_to_s3,
    )

    extract_task >> transform_task >> load_task
```

### `src/extract.py`

```python
import tweepy
import pandas as pd
from config import TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

def extract_twitter_data():
    # Authentication with Twitter API
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY,
        TWITTER_API_SECRET_KEY,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_TOKEN_SECRET
    )
    api = tweepy.API(auth)
    
    # Fetch tweets (example)
    tweets = api.home_timeline(count=100)
    data = [{'text': tweet.text, 'created_at': tweet.created_at} for tweet in tweets]
    
    df = pd.DataFrame(data)
    df.to_csv('/tmp/twitter_data.csv', index=False)
```

### `src/transform.py`

```python
import pandas as pd

def transform_data():
    df = pd.read_csv('/tmp/twitter_data.csv')
    
    # Example transformation
    df['text'] = df['text'].str.lower()
    
    df.to_csv('/tmp/processed_data.csv', index=False)
```

### `src/load.py`

```python
import boto3

def load_to_s3():
    s3 = boto3.client('s3')
    bucket_name = 'your-s3-bucket-name'
    file_path = '/tmp/processed_data.csv'
    
    s3.upload_file(file_path, bucket_name, 'processed_data.csv')
```