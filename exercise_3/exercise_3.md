# Exercise 3 - Chunking and Upserting

## Aim

The aim of the exercise is to:
1. Familiarise yourself with chunking
2. Upsert embedded chunks from the text

The exercise is complete when you can:
- you have a Pinecone Index with your upserted chunks
- you can successfully query the index to retrieve a string with excerpts

## Method

### 1. Install LangChain text splitters

Install langchain

    pip install langchain


### 2. Modify the Text Splitter Code

Open up the **load_chunks.py** file. This code will load the chunks from **flat_earth.txt**.

Enter  the values for  **chunk_size** and **chunk_overlap** parameters on line 64.

You can experiment with values if you have time.

A good place to start would be 1500 and 150.


### 3. Create Your Index and Upsert

Use create_index() and upsert_chunks_from() functions to create the 
Pinecone index that will store chunks for your bot . 

Upsert your chunks ready for your bot to use.

Remember, it takes a while for vecotrs to be indexed.


### 4. Query the Index

Let's get a sense of whether the semantic search is performing.

Open up the code **retrieve_chunks.py**.

Use the retrieve_chunks() function to embed a query and get the 
closest vectors back.

How do the results look for the question:

> 'If the earth is not curved, why does only the top half of a ship when it is far away?'

Try some other questions to see if we're getting good results.

> 'Do the press speak favourable about Flat Earth Theory? Give me examples.'
> 'Does the philosophical school of thought that pertains to a flat earth have a name?'
> 'Has the Smithsonian Institute embraced Flat Earth theory?'


Well done you've successfully got a semantic search engine to power your bot!