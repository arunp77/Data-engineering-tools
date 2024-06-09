# Indexing in Elasticsearch and SQL database
Let's break down the concept of an index in Elasticsearch and compare it to a relational SQL database with a practical example.

### Elasticsearch Index vs. SQL Database

In Elasticsearch, an index is analogous to a database in a relational SQL system. Each index contains a collection of documents (similar to rows in SQL) that share common characteristics and are logically related. 

### Example Scenario

Imagine you are building an application that deals with managing articles and users. In a relational SQL database, you would typically create separate tables for articles and users. In Elasticsearch, you would create separate indexes for each type of data.

### Relational SQL Database

1. **Database**: `my_app`
   - **Table 1**: `users`
     - Columns: `id`, `name`, `email`, `age`
   - **Table 2**: `articles`
     - Columns: `id`, `title`, `body`, `author_id`, `published_date`

#### SQL Table Structure

- `users` table:

| id  | name  | email          | age |
|-----|-------|----------------|-----|
| 1   | John  | john@example.com | 30  |
| 2   | Alice | alice@example.com | 25  |

- `articles` table:

| id  | title                  | body             | author_id | published_date |
|-----|------------------------|------------------|-----------|----------------|
| 1   | Elasticsearch Basics   | Introduction to ES | 1         | 2023-01-15     |
| 2   | Advanced Elasticsearch | Deep dive into ES | 2         | 2023-02-20     |

### Elasticsearch Index

In Elasticsearch, we create separate indexes for `users` and `articles`. Each index will contain documents (similar to rows in SQL) with relevant fields.

#### 1. Creating Indexes

```bash
# Creating an index for users
PUT /users
{
  "mappings": {
    "properties": {
      "id": { "type": "integer" },
      "name": { "type": "text" },
      "email": { "type": "text" },
      "age": { "type": "integer" }
    }
  }
}

# Creating an index for articles
PUT /articles
{
  "mappings": {
    "properties": {
      "id": { "type": "integer" },
      "title": { "type": "text" },
      "body": { "type": "text" },
      "author_id": { "type": "integer" },
      "published_date": { "type": "date" }
    }
  }
}
```

#### 2. Indexing Documents

```bash
# Indexing a user document
POST /users/_doc/1
{
  "id": 1,
  "name": "John",
  "email": "john@example.com",
  "age": 30
}

POST /users/_doc/2
{
  "id": 2,
  "name": "Alice",
  "email": "alice@example.com",
  "age": 25
}

# Indexing an article document
POST /articles/_doc/1
{
  "id": 1,
  "title": "Elasticsearch Basics",
  "body": "Introduction to ES",
  "author_id": 1,
  "published_date": "2023-01-15"
}

POST /articles/_doc/2
{
  "id": 2,
  "title": "Advanced Elasticsearch",
  "body": "Deep dive into ES",
  "author_id": 2,
  "published_date": "2023-02-20"
}
```

#### 3. Querying the Data

**Search for articles with the word "Elasticsearch" in the title:**

```bash
GET /articles/_search
{
  "query": {
    "match": {
      "title": "Elasticsearch"
    }
  }
}
```

**Search for users with the name "John":**

```bash
GET /users/_search
{
  "query": {
    "match": {
      "name": "John"
    }
  }
}
```

### Summary

- **Elasticsearch Index**: An index in Elasticsearch is a collection of documents that are logically related and share common characteristics. It can store as many documents as needed, similar to how a database contains multiple tables in an RDBMS.
  
- **Relational SQL Database**: A database in an RDBMS consists of multiple tables with predefined schemas. Each table contains rows with data.

In this example, we have created two indexes in Elasticsearch (`users` and `articles`) to store user and article data, respectively. Each document within these indexes can be queried and managed independently, providing flexibility and powerful search capabilities inherent to Elasticsearch. This setup mirrors having separate tables for users and articles in a traditional SQL database but offers more advanced search and analytics features.