# Exercise 3 - Chunking and Upserting

## Aim

The aim of the exercise is to:
1. Familiarise yourself with chunking
2. Upsert embedded chunks from the text

The exercise is complete when you can:
- you have a Pinecone Index with your upserted chunks

## Method

### 1. Install LangChain text splitters

Install only the text splitter

    pip install -qU langchain-text-splitters


### 2. Modify the Text Splitter Code

Enter  the values for  **chunk_size** and **chunk_overlap** parameters.

You can experiment with values if you have time.
A good place to start would be 1500 and 150.


### 3. Create Your Index and Upsert

Use create_index() and upsert_chunks_from() functions to create the 
Pinecone index that will store chunks for your bot . 

Then upsert your chunks ready for your bot to use.


### 4. Query the Index

Use the retrieve_chunks() function to embed a query and get the 
closest vectors back.

How do the results look for the question:

> 'If the earth is not curved, why does only the top half of a ship when it is far away?'



