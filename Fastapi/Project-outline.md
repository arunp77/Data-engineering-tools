# Project outline

Develop a FastAPI-based API for generating multiple-choice questions (MCQs) from an Excel dataset. The API should allow users to specify test type, categories, and the number of questions, returning them in random order.

## Dataset:
The dataset is represented by an Excel file named `questions_en.xlsx`, containing columns:

| 'question', | 'subject', | 'use', | 'correct', | 'responseA', | 'responseB', | 'responseC', | 'responseD', | 'remark' |

- 'question': The question itself
- 'subject': The category of the question (e.g., 'Databases', 'Data Streaming')
- 'use': Type of test ('Positioning test', 'Validation test', 'Total Boot Camp')
- 'correct': Correct option(s) ('A', 'B', 'C', 'D', 'B,C', 'A C', 'B C', 'A B C D', NaN)
- 'responseA', 'responseB', 'responseC', 'responseD': Multiple-choice responses
- 'remark': Additional remarks

Few lines of the dataset are:

| question	| subject	| use	| correct	| responseA	| responseB	| responseC	| responseD	| remark |
|-----------|-----------|-------|-----------|-----------|-----------|-----------|-----------|--------|
| What does No-SQL stand for?	| Databases	Positioning test	| A	| Not OnlySQL	| NoSQL	| Not all SQL	| NaN	| NaN |
| Cassandra and HBase are databases	| Databases	Positioning test	| C	| relational database	| object-oriented	| column-oriented	| graph-oriented	| NaN |
| MongoDB and CouchDB are databases	| Databases	Positioning test	| B	| relational database	| object-oriented	| column-oriented	| graph-oriented	| NaN |
| OrientDB and Neo4J are databases	| Databases	Positioning test	| D	| relational database	| object-oriented	| column-oriented	| graph-oriented	| NaN |
| To index textual data, I can use	| Databases	Positioning test	| A	| ElasticSearch	Neo4J	| mysql	| NaN	| NaN

#### API Functionality:

1. **Authentication:**
   - Implement basic authentication using 'username' and 'password' strings passed in the Authorization header.
   - Users with access:
     - alice: wonderland
     - bob: builder
     - clementine: mandarine
   - Admin credentials: admin: 4dm1N

2. **Endpoints:**
   - **/questions/:**
     - Method: GET
     - Parameters:
       - 'use' (required): Type of test ('Positioning test', 'Validation test', 'Total Boot Camp')
       - 'subject' (optional): Category/categories of questions
       - 'num_questions' (required): Number of questions to generate (5, 10, 20)
     - Returns: JSON response containing MCQs in random order.

   - **/verify/:**
     - Method: GET
     - Returns: JSON response confirming the API is functional.

#### Additional Considerations:
- MCQs should be randomly selected from the dataset to ensure variability.
- API responses should adhere to RESTful principles and return data in a consistent format (e.g., JSON).
- Endpoint paths and response codes should be well-defined for easy understanding and integration with client applications.