# Welcome to a Short Intro to Retrieval Augmented Generation!

## What's it all about?

We're going to be building a very simple one shot Q&A chatbot
that will help you get to grips with Retrieval Augmented Generation (RAG), 
Vector Databases, Text Embeddings and LLMs.

During the session we'll load the contents of a book into a Vector Database and construct a
Chatbot that can:

- receive a user question
- retrieve relevant content from the stored book to answer the question
- use an LLM to generate the answer based on that content.

All in 90 minutes!

It helps to be set-up before the session.

## Setup


### 1. Download this Repository

Download this repository to your device.
Open the root folder for the project in whatever IDE you usually use.


### 2. Get an Open AI Account

We'll need OpenAI to create Embeddings and complete LLM calls to generate answers.

Go to https://openai.com/api and log in or sign up.

If you sign up you'll get free credit for the API.

If you signed up sometime before, you'll just need to check you have credit available.
The next step will let you know if that's the case. If not, you might want to just put
the minimum amount of credit on your account or just collaborate with another group on the day.

See if you can successfully navigate to the Open AI Playground at:

https://platform.openai.com/playground?mode=chat. 

Can you enter a chat question in the 'User' field, press submit and get a reply?


### 2. Get an OpenAI API Key


Find your OpenAI API Key at https://platform.openai.com/api-keys. You'll likely need to create a new one
and copy the key.

We will use **dotenv** to store the keys, so edit the .env file to include 
your OPENAI_API_KEY

    OPENAI_API_KEY=<<your-api_key>>


### 3. Get a Pinecone Account and API Key

We will use Pinecone as our Vector DB.

Go to https://www.pinecone.io, set up a free account and get an API key. This will either 
be an option on set-up or go to **API KEYS** menu item on the left hand nav.

Edit the .env file to include you PINECONE_API_KEY

    PINECONE_API_KEY=<<your-api_key>>

### 4. Set up you Virtual Environment and Packages

Within the root directory, set up a Python Venv, you will need Python 3.8 or greater. 
If you are on a lower python version you will need to upgrade.
Follow these instructions to set up the Virtual Environment  or do it the way you would normally.

Run venv from the terminal

    python -m venv venv

Then, on a Mac, run the following from the terminal

    source venv/bin/activate 
    
or a PC, run the executable from a terminal

    venv/bin/activate 

Again, from the terminal, install the packages:

    pip install pinecone-client openai python-dotenv

### 5. Check it all works

Go and run the code **verify_setup.py** located in this (the root) directory.

It should all work and if it does, you are ready to start following Exercise 1
to 4 found in the directories in this project.

Enjoy!


