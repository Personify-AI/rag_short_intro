import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI

# you need to do a pip install of LangChain, you can just use the text splitter
# pip install -qU langchain-text-splitters
from langchain.text_splitter import RecursiveCharacterTextSplitter


load_dotenv()

oa = OpenAI()
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
index_name = 'proofs'

# We'll use this to embed the question for query
def embed_chunk(text):

    response = oa.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )

    print(response)

    embedding = response.data[0].embedding

    return embedding


# This will be used to retrieve chunks from Pinecone
# Default chunks to retrieve is 5
def retrieve_chunks(query, no_of_chunks=5):

    # The query is embedded before querying Pinecone
    embedding = embed_chunk(query)

    index = pc.Index(index_name)

    response = index.query(
        vector= embedding,
        top_k=no_of_chunks,
        include_metadata=True
    )

    retrieved_chunks = ""

    for match in response['matches']:

        retrieved_chunks += "________________________________\n"
        retrieved_chunks += "EXCERPT\n"
        retrieved_chunks += "-------\n"
        retrieved_chunks += match['metadata']['chunk'] + '\n'

    return retrieved_chunks



# TODO have a go at some experimental queries
# are the results relevant?
chunks = retrieve_chunks('If the earth is not curved, why can only the top half of a ship be seen at a distance?')
print(chunks)






