import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI


# We're loading env variables with dotenv
# Store your env variable in .env for PINECONE_API_KEY
load_dotenv()
oa = OpenAI()
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))



# Function to embed text, it will be used
# to change the query text to a vector
def get_embedding_for(text):

    response = oa.embeddings.create(
        model="text-embedding-3-small",
        input=text

    )

    return response.data[0].embedding



# This function queries the vector database
def query_questions(question):

    index = pc.Index('questions')

    # You should notice there are now 10 vectors there
    print(index.describe_index_stats())

    # TODO you'll have to embed the query before you query index
    # TODO complete the following line of code and replace x...
    embedding = x_call_to_embed_text

    results = index.query(
        vector=embedding,
        top_k=5,
        include_metadata=True
    )

    return results


# Call the query questions
results = query_questions('How do I get a taxi in Boston?')
print('Results response')
print(results)
