# Exercise 1 - The Playground

## Aim

The aim of the exercise is to get you familiar
with the Playground, which will allow you to 
experiment wth Open AI API calls without 
having to code them.

This is useful for the following:

- Lets you experiment with different instructions
to see how they affect the response
- Will let you try injecting different external data contexts 
to assess Chat GPTs ability to comprehend your data set

You've completed this assignment when you are clear about how you will construct
a **System Message** to instruct Flat Earth Bot on how to respond to user questions
and deal with contextual data.

## Method

### 1. Get an Open AI Account

Got to https://openai.com/api and log in or sign up.

If you sign up you'll get free credit for the API.

### 2. Navigate to the Playground

Navigate to the Open AI 'playground' at 
https://platform.openai.com/playground?mode=chat. 

Familiarise yourself with its operation.

For this exercise mainly play on GPT3.5, but if you have time do a comparison
to see what GPT4 is like for replies.


### 3. Constructing the System Message for Flat Earth Bot

Chatbot creators will often use the **System Message** instruction to 
inform ChatGPT what to do and how to respond to input.

The System Message is a hidden part of the conversation that ChatGPT 
will evaluate. By using this message you can have a 'clean' conversation
between the **user** and **assistant** (this is the APIs term for the LLM)

In this file **flat_earth_extract.txt**, there is an extract of a number 
of 'proofs' that are relevant for answering the question:

>"If the earth is flat, why does only the top half of a ship appear when it is at a distance?"

Use the **System Message** instruction to inform ChatGPT what 
you want it to do. Ensure that:

- You tell the bot what it is and what it is doing
- You point out where the data is that you want it to reference
- Maybe you want to give it a personality!

Paste the text data from your flat_earth_extract.txt file into the System Message and 
simulate the API call.

**IMPORTANT** - keep a note of the System Message you wrote, we will use it later.

### 4. Stretch - discuss scenarios for no relevant data

Imagine a scenario where the user answered a question the bot couldn't answer
and couldn't find relevant information for in the available datasources.

What instructions might you put in the System Message?


`


