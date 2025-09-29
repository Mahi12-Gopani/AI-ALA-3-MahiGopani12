def chatbot():
    print("Hello! I am a professional Python chatbot. Type 'exit' anytime to quit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Chatbot: Thank you for chatting! Goodbye.")
            break
        
        # Greetings
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm fully operational! How about you?")
        
        elif "your name" in user_input:
            print("Chatbot: I am called the Python Professional Chatbot.")
        
        # Help info
        elif "help" in user_input:
            print("Chatbot: You can ask me about Python programming, tech concepts, general knowledge, or even quiz questions.")
        
        # Python specific questions
        elif "python" in user_input and ("work" in user_input or "how" in user_input):
            print("Chatbot: Python works by interpreting code line-by-line using the Python interpreter, allowing dynamic typing and rapid development.")
        
        elif "python" in user_input and ("advantages" in user_input or "benefits" in user_input):
            print("Chatbot: Python advantages include simplicity, readability, vast libraries, cross-platform compatibility, and strong community support.")
        
        elif "python" in user_input and ("uses" in user_input or "applications" in user_input):
            print("Chatbot: Python is used in web development, data science, automation, artificial intelligence, scientific computing, and more.")
        
        elif "python" in user_input and ("version" in user_input or "latest" in user_input):
            print("Chatbot: As of now, Python 3.11 is the latest stable version offering improved speed and enhanced typing features.")
        
        # Programming and tech questions
        elif "what is a variable" in user_input:
            print("Chatbot: A variable is a storage location identified by a name that holds data which can be changed during program execution.")
        
        elif "what is a function" in user_input:
            print("Chatbot: A function is a block of reusable code that performs a specific task and can be called as needed.")
        
        elif "what is object oriented programming" in user_input:
            print("Chatbot: Object-Oriented Programming (OOP) is a paradigm where data and functions are bundled into objects, promoting modularity and reuse.")
        
        elif "what is artificial intelligence" in user_input:
            print("Chatbot: Artificial Intelligence is a field of computer science focused on creating systems capable of performing tasks that usually require human intelligence.")
        
        elif "what is machine learning" in user_input:
            print("Chatbot: Machine Learning is a subset of AI where systems learn patterns from data to make predictions or decisions without being explicitly programmed.")
        
        elif "what is data science" in user_input:
            print("Chatbot: Data Science is an interdisciplinary field that uses algorithms, statistics, and technology to extract insights from structured and unstructured data.")
        
        # General knowledge / quiz style
        elif "capital of france" in user_input:
            print("Chatbot: The capital of France is Paris.")
        
        elif "who is the president of the united states" in user_input:
            print("Chatbot: The current president of the United States is Joe Biden.")
        
        elif "who discovered gravity" in user_input:
            print("Chatbot: Sir Isaac Newton is credited with discovering the law of gravity.")
        
        elif "what is the speed of light" in user_input:
            print("Chatbot: The speed of light in vacuum is approximately 299,792 kilometers per second.")
        
        else:
            print("Chatbot: Sorry, I didn't quite catch that. Can you please ask something else or rephrase?")
            
if __name__ == "__main__":
    chatbot()
