import re   # Import regex module for matching patterns

# Dictionary: regex patterns → response type
pattren = {
    r"hello|hi|hey": "greeting",
    r"What is your name\??": "name_query",
    r"How are you\??": "status_query",
    r"bye|goodbye": "farewell"
}

print("Chatbot: Hello! I am your chatbot. How can I assist you today? (Type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower().strip() == 'exit':   # User types exit → end program
        print("Chatbot: Goodbye! Have a great day!")
        break

    matched = False   # Keeps track if any pattern matched
    for pattern, response in pattren.items():   # Check input against all patterns
        if re.search(pattern, user_input, re.IGNORECASE):   # Case-insensitive match
            matched = True
            if response == "greeting":
                print("Chatbot: Heyy! How can I help you?")
            elif response == "name_query":
                print("Chatbot: I am a simple chatbot created to assist you.")
            elif response == "status_query":
                print("Chatbot: I'm just a program, but thanks for asking!")
            elif response == "farewell":
                print("Chatbot: Goodbye! Have a great day!")
                break   # End loop on farewell
            break

    if not matched:   # If nothing matched
        print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")
