# Spotify Playlist Data Analytics

## Overview

This project is designed for analyzing data from a Spotify playlist using Python and the Spotify API. It provides insights into the songs, artists, and more within a specific Spotify playlist.

## Prerequisites

Before running the project, make sure you have the following prerequisites:

- Python 3.x
- Spotify Developer Account
- Access to the Spotify playlist you want to analyze

## Getting Started

1. **Spotify API Setup**: Create a Spotify Developer App and obtain your Client ID and Client Secret. These credentials will be used for authentication.

    - **Create a Spotify Developer Account:** If you don't already have one, go to the Spotify Developer Dashboard (https://developer.spotify.com/dashboard/) and create a Spotify Developer account. You can use your existing Spotify account to log in.
    - **Create a Spotify Developer App:** 
      - After logging in, click on the `Create an App` button on the Spotify Developer Dashboard. 
      - Fill in the required information for your app. You'll need to provide a name and description. 
      - Agree to the terms and conditions, and click "Create."
    - **Obtain Your Client ID and Client Secret:**
      - Once your app is created, you will see a dashboard for your app.
      - On the app's dashboard, you'll find your Client ID and a "Show Client Secret" button. Click on this button to reveal your Client Secret.
      - **Store Your Client ID and Client Secret Securely:** 
        - It's crucial to store your Client ID and Client Secret securely. 
        - You can create a `.env` file in your project directory and store these credentials as environment variables.
        - Open the `.env` file with a text editor. Inside the file, add the following lines and replace `your_client_id`
         and `your_client_secret` with your actual Spotify API credentials:

         ```
            SPOTIPY_CLIENT_ID=your_client_id
            SPOTIPY_CLIENT_SECRET=your_client_secret
         ```
        - Save and close the file.

2. **Project Setup**:
   
   - Clone this repository to your local machine.
   - If you haven't already, you can clone the Bitbucket repository to your local machine. Open your terminal/command prompt and navigate to the directory where you want to store the project, then run:
    ```
    git clone <repository_url>
    ```
    Replace <repository_url> with the URL of your Bitbucket repository.
   - Create a virtual environment and activate it.
     - In your project directory, create a virtual environment to isolate your project's dependencies. Use the following commands in your terminal:
        ```
        python -m venv venv
        ```
        This will create a virtual environment named "venv." You can replace "venv" with any other name you prefer.

     - **Activating the Virtual Environment:** Activate the virtual environment to work within it:
       - On Windows:
        ```
        venv\Scripts\activate
        ```
       - On macOS and Linux:
        ```
        source venv/bin/activate
        ```
   - Install the required dependencies from `requirements.txt` using `pip install -r requirements.txt`. This will install the libraries listed in the requirements.txt file, including libraries for working with Spotify data and data analysis. In my case, my requirements.txt contains:
        ```
        # Spotify API
        spotipy==2.22.0

        # Data manipulation and analysis
        pandas==1.3.3
        numpy==1.21.2
        matplotlib==3.4.3
        seaborn==0.11.2

        # Machine learning and statistics (if needed)
        scikit-learn==0.24.2 
        statsmodels==0.13.0
        scipy==1.7.3
        plotly==5.1.0
        pytorch==1.10.0
        xarray==0.21.0

        # Database and SQL (if needed)
        SQLAlchemy==1.4.28
        pymysql==1.0.2

        # Environment management
        python-decouple==3.6

        # Optional web development (if needed)
        flask==2.1.1

        # Optional Jupyter Notebook support (for interactive data analysis)
        jupyterlab==4.1.1
        ```

3. **Running the Project**:
   
   - Open and edit the `ETL-pipeline.py` script to customize your data analysis.
   - Execute the script to access and analyze the Spotify playlist data.
        ```
        python ETL-pipeline.py
        ```

## Project Structure

    | project directory |
    |-------------------|
                        |
                        |---> .env
                        |---> README.md
                        |---> requirements.txt
                        |---> Licence.md
                        |---> ETL-pipeline.py
                        |---> .gitignore

- `ETL-pipeline.py`: The main Python script for data extraction, transformation, and loading.
- `requirements.txt`: A list of project dependencies for easy environment setup.
- `README.md`: This documentation.
- `.gitignore`: Configuration file for Git to specify which files and folders should be excluded from version control.

## Contribution

Contributions are welcome. If you have any improvements or feature additions, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
