
import openai
import os
import typer

# Set up the OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]


# Define a function to interact with the model
def chat_with_gpt(prompt, model):
    # Generate text based on the prompt
    completion = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
    )
    # Extract the generated text from the response
    generated_text = completion.choices[0].message
    # Return the generated text
    return generated_text


# Define the Typer app
app = typer.Typer()


# Define the chat command
@app.command()
def chat(model: str = typer.Argument("gpt-3.5-turbo")):
    """
    Start a chatbot that uses OpenAI's GPT-3 language model to generate responses based on user input.
    """
    # Print welcome message
    typer.echo("Welcome to the GPT-3.5 chatbot!")
    prompt = []
    while True:
        # Get user input
        user_input = typer.prompt("You: ")
        prompt.append({'role': 'user', 'content': user_input})
        # Generate a response using the GPT-3 model
        response = chat_with_gpt(prompt, model)
        prompt.append(response)
        # Print the generated response
        typer.echo(f"ChatGPT: {response['content']}")
