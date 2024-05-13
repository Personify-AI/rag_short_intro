import os
from dotenv import load_dotenv

# TODO Make sure you...
# pip install pinecone-client
from pinecone import Pinecone, ServerlessSpec

# TODO Make sure you...
# pip install openai
from openai import OpenAI


# We're loading env variables with dotenv
# Store your env variable in .env for
# PINECONE_API_KEY
# OPENAI_API_KEY

# This loads all the env variables defined in your .env file
# TODO pip install python-dotenv
load_dotenv()

print('Checking OpenAI Connectivity....')
# This call works becasue you OPENAI_API_KEY has been loaded
# Openai fetches it from the env variable unless you explicitly define an api key in the call
oa = OpenAI() # could be OpenAI(api_key=os.getenv('OPENAI_API_KEY')

response = oa.embeddings.create(
    input="Check embedding this works",
    model="text-embedding-3-small"
)

print("OpenAI Check complete")

print('Checking Pinecone Connectivity....')

pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

pc.create_index(
    name="test",
    dimension=1536,
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)
index = pc.Index("test")
print(index.describe_index_stats())
pc.delete_index("test")
print("Pinecone check comeplete, you're ready to go")




