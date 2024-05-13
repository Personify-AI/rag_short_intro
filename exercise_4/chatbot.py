from openai import OpenAI
from pinecone import Pinecone

# Here we're using dotenv (pip install python-dotenv) to manage environment vars
from dotenv import load_dotenv
import os

load_dotenv()

oa = OpenAI()  # alternatively self.client = OpenAI(api_key=<<your OPENAI_API_KEY>>)
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

# In this function we will create the system message and include the relevant context
# TODO Find the system message instruction you came up with in Exercise 1
# TODO Paste it into the f""" string below,
# TODO The completed code will merge the instruction and context data
def inject_context_data(context):
    # Edit this system message
    system_message = f"""   
    
    put your system message instruction here, your data will go below
    
    {context}
    
    """

    return system_message


def respond_to_question(question):
    # TODO in exercise 3 you wrote some code to retrieve your data
    # TODO complete the line below replacing x...
    # TODO you will need to call the code you worte last time in this line
    # You could etihter do this by implementing your code within this class
    # Or calling it some other way, the choice is yours
    context_data = x_call_your_code_to_retrieve_chunks
    system_message = inject_context_data(context_data)

    # Call the OpenAI API with your systems message and question
    response = oa.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": question},
        ]
    )

    # Parse the response to an answer and return it
    return response.choices[0].message.content


# Call the chatbot to respond to a question and get the answer based on the static injected context
# Example question: If the earth is flat, why do you only see the top half of a ship

answer = respond_to_question(
    'If the earth is flat, '
    'why does only the top half of it '
    'appear when it is at a distance?')

print('Answer:', answer)
