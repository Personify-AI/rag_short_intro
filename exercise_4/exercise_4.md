# Exercise 4 - Augment Data and Generate an Answer

## Aim

The aim of the exercise is to:

1. Augment the retrieved chunk data with an instruction to the Chatbot
2. Call the OpenAI Chat Completions interface and get great answers

The exercise is complete when your bot can answer a targeted 
question referencing the content from the book.

## Method

### 1. Construct Your System Message

Open up **chatbot.py**.

On line 19 you will see an f string that
will combine a system message instruction with the extracted data
you'll want to augment as context.

Remember you did Exercise 1 - what System Message instruction did you write 
in the Playground. You can use that here.


### 2. Retrieve Chunks

Look at the **respond_to_question()** function. 

The first line of this (line 36) needs modifying so that you can call
some code to retrieve your relevant chunks for the users question.

Alter this line of code to call code you wrote in **exercise_3**. You could 
either import it and call the function or copy and paste the functions in to the chatbot code.


### 3. Ask your Bot Questions

Call the bot and get it to answer questions. Here are some examples:

Start with our constant question we've been using:

> 'If the earth is not curved, why does only the top half of a ship when the ship is far away?'

But why not try these:

> 'Do the press speak favourable about Flat Earth Theory? Give me examples.'
> 'Does the philosophical school of thought that pertains to a flat earth have a name?'
> 'Has the Smithsonian Institute embraced Flat Earth theory?'

How did your bot do?

### 4. Stretch - How many tokens

Edit the code a print the raw response from the OpenAI API.

How many tokens did your call use. How much did it cost?

https://openai.com/api/pricing/ might help.

How much would it cost using GPT4?

### 4. Stretch - Designing for Multiple Turns of Conversation

If you had to re-design this to cope with multiple steps / turns of conversations
what are some of the design considerations?