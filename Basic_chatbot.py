def chatbot():

    print("=============Chatbot=============")
    
    while True:
        
        user_input = input("You: ").strip().lower()

        if user_input == "hello" or user_input == "hi":
            print("chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
        
        else:
            print("Chatbot: I'm sorry, I don't understand that.")

chatbot()