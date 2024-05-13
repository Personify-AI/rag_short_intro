# Exercise 2 - Pinecone and Embeddings

## Aim

The aim of the exercise is to:
1. Get you set up with Pinecone
2. Do your first embeddings
3. Gain familiarity with querying the index with embeddings

The exercise is complete when you can:
- embed the question 'How do I get a taxi in Boston?'
- retrieve the most similar questions from Pinecone

## Method

### 1. Set up A Virtual Environment

You've likely created a new directory for this project, and it'll have the exercises in it.

Within the root directory, set up a Python Venv, you will need Python 3.8 or greater. 
Follow these instructions or do it the way you would normally

    python -m venv venv

Then, on a Mac

    source venv/bin/activate 
    
or a PC

    venv/bin/activate 

### 1. Set Up OpenAI API Key (for using Embeddings API)

Find you OpenAI API Key at https://platform.openai.com/api-keys

We will use **dotenv** to store the keys, so edit the .env file to include 
your OPENAI_API_KEY

    OPENAI_API_KEY=<<your-api_key>>

Install openai and python-dotenv:

    pip install openai python-dotenv


### 1. Set up Pinecone

Go to https://www.pinecone.io, set up a free account and get an API key. This will either 
be an option on set-up or go to **API KEYS** menu item on the left hand nav.

Edit the .env file to include you PINECONE_API_KEY

    PINECONE_API_KEY=<<your-api_key>>

Install pinecone-client

    pip install pinecone-client



### 2. Get Familiar with Embedding

Open the **load_embeddings.py** file in this directory.

In this exercise you will be embedding and loading the **questions** on line 22.

The 'Embeddings' guide for OpenAI is https://platform.openai.com/docs/guides/embeddings.

Use the  get_embedding_for('your text to embed') function to 
practice embedding some sample text:

    'How do I get a taxi in Boston?'

Check the raw output from the OpenAI call.

The raw response from OpenAI will be printed on the screen.

What do you see?


### 3. Create Index, Embed the Data and Upsert

Use the create_index() and load_questions() functions to get the
questions data loaded into the index. You will need to uncomment the calls on 
lines 113 and 114.

You will need to alter the create_index query to include the correct 
dimension that is required for an OpenAI call to the **text-embedding-3-small** 
embeddings model.

Once the records are loaded, we print index statistics at the end of the process , 
what do you notice?

Go to the index in the project console in Pinecone. Is your data there yet?


### 4. Query the Index

Your data should now be indexed, it takes a short while for the index to catch up after load.

Now we're going to query it, to find the closest match.

Open the **query_embeddings.py** code.

Use the query_questions() function to embed a query and get the closest vectors back.

You will need to complete the code on line 39 to ensure you embed the question
before using that embedding to query the database.


### 5. Stretch Activity - Only Return Most Relevant Results

How would you augment the use of the top_k parameter with logic to 

a. Only return results if they were relevant
b. If there were lots of relevant results, to just return the ones that are the best




