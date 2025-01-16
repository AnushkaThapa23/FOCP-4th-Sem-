import json
import random
from datetime import datetime
import os

CONFIG_FILE = "chat_config.json"
AGENT_FILE = "agent_name.txt"

# Load the configuration from the JSON file
def load_config():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

# Generate and save a new agent name
def generate_agent_name():
    agent_names = ["Sunday", "Fantastic", "Apples", "Jonathan", "Clove"]
    new_name = random.choice(agent_names)
    
    # Write the new agent name to the file
    with open(AGENT_FILE, "w") as file:
        file.write(new_name)
    
    return new_name

# Load the last agent name from file, or generate a new one if it doesn't exist
def load_agent_name():
    if os.path.exists(AGENT_FILE):
        with open(AGENT_FILE, "r") as file:
            return file.read().strip()
    return generate_agent_name()

# Log conversation to a file
def log_conversation(log_file, user_name, agent_name, logs):
    with open(log_file, "a") as file:
        file.write(f"Session with {user_name}\n")
        for log in logs:
            file.write(f"{log}\n")
        file.write("\n")

# Get the current date and time
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%A, %d %B %Y, %I:%M %p")

# Main function
def chat():
    config = load_config()
    user_name = input("Hello! Welcome to Poppleton University. What's your name? ")
    agent_name = load_agent_name()  # Load last agent name
    print(f"{agent_name}: Hi {user_name}! How can I assist you today?")
    
    log_file = "chat_log.txt"
    logs = []
    message_count = 0
    
    while True:
        user_input = input(f"{user_name}: ").strip()
        logs.append(f"{user_name}: {user_input}")

        # Exit command
        if user_input.lower() in ["bye", "exit", "quit"]:
            print(f"{agent_name}: It was nice talking to you, {user_name}! Goodbye!")
            logs.append(f"{agent_name}: It was nice talking to you, {user_name}! Goodbye!")
            break

        # Date and time response
        if "date" in user_input.lower() or "time" in user_input.lower():
            current_datetime = get_current_datetime()
            response = f"The current date and time is: {current_datetime}"
        else:
            # Keywords
            response = None
            for keyword, replies in config["keywords"].items():
                if keyword in user_input.lower():
                    response = random.choice(replies)  # Randomly choose one response
                    break

            # Random response
            if response is None:
                response = random.choice(config["random_responses"])

        # Respond to the user
        print(f"{agent_name}: {response}")
        logs.append(f"{agent_name}: {response}")

        # Random disconnection
        message_count += 1
        if message_count >= 10 or random.random() < 0.05:
            print(f"{agent_name}: Oops! It seems we got disconnected. Please try again later.")
            logs.append(f"{agent_name}: Oops! It seems we got disconnected. Please try again later.")
            break

    # Log the session
    log_conversation(log_file, user_name, agent_name, logs)

    # Change agent name for the next session
    generate_agent_name()

if __name__ == "__main__":
    chat()
