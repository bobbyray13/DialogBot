# Import required libraries
import openai
import random


# Define function to validate variability input
def validate_variability(variability):
    try:
        variability = float(variability)
        if variability < 0.01 or variability > 1.00:
            raise ValueError
        return variability
    except ValueError:
        print("Error: Variability input must be a decimal between 0.01 and 1.00.")
        exit()


# Prompt user for input
conversation_topic = input("Enter conversation topic: ")
n = int(input("Enter number of messages exchanged: "))
variability = validate_variability(input("Enter variability of conversation: "))
first_ai = input("Which AI should go first? ")
additional_context = input("Enter additional context: ")

# Set up OpenAI API key
openai.api_key = "INSERT API KEY HERE"


# Define function to generate AI response
def generate_response(prompt, temperature):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=temperature,
        max_tokens=150,
        n=1,
        stop=None,
        timeout=20,
    )
    return response.choices[0].text.strip()


# Implement AI dialogue
messages_exchanged = 0
while messages_exchanged < n:
    temperature = 0.5 + (variability * random.uniform(-0.5, 0.5))
    if first_ai == "AI1":
        prompt = "AI1: " + conversation_topic + additional_context + "\nAI2:"
        response = generate_response(prompt, temperature)
        print("AI2: " + response)
        messages_exchanged += 1
        if messages_exchanged >= n:
            break
        prompt = "AI1: " + response
        response = generate_response(prompt, temperature)
        print("AI1: " + response)
        messages_exchanged += 1
    else:
        prompt = "AI2: " + conversation_topic + additional_context + "\nAI1:"
        response = generate_response(prompt, temperature)
        print("AI1: " + response)
        messages_exchanged += 1
        if messages_exchanged >= n:
            break
        prompt = "AI2: " + response
        response = generate_response(prompt, temperature)
        print("AI2: " + response)
        messages_exchanged += 1

# End of program
print("Conversation ended.")
