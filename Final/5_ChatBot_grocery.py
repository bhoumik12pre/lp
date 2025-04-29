import re

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase

    responses = {
        r"\b(1|hello|hi|hey)\b": " Hello! Welcome to our grocery store. How can I help you today?",  # Greeting response
        r"\b(2|how are you)\b": "I'm just a bot, but I'm here to assist you with groceries!",  # Response for how are you
        r"\b(3|order status|track order)\b": "Please provide your order ID to check the status.",  # Response for order tracking
        r"\b(4|shipping time|delivery time)\b": "We offer same-day delivery and standard shipping (3-5 business days).",  # Response for shipping time
        r"\b(5|return policy)\b": "You can return items within 7 days if unopened. Would you like help with a return?",  # Response for return policy
        r"\b(6|thank you|thanks)\b": " You're welcome! Let me know if you need anything else.",  # Response for thanking
        r"\b(7|price|cost)\b": "Please specify the product name to check its price.",  # Response for asking price
        r"\b(8|milk)\b": "Milk is 30rs per liter.",  # Response for milk price
        r"\b(9|eggs)\b": "A dozen eggs cost 80rs.",  # Response for egg price
        r"\b(10|rice)\b": "Rice is 50rs per kg.",  # Response for rice price
        r"\b(11|vegetables|veggies)\b": "We have fresh vegetables available. What are you looking for?",  # Response for vegetables
        r"\b(12|fruits)\b": "We have apples, bananas, and oranges in stock. Which one do you need?",  # Response for fruits
        r"\b(13|snacks)\b": "We have chips, biscuits, and chocolates available.",  # Response for snacks
        r"\b(14|beverages|drinks)\b": "We have soft drinks, juices, and bottled water. What would you like?",  # Response for beverages
        r"\b(15|buy|order)\b": "You can place an order on our website or visit our store.",  # Response for buying items
        r"\b(16|payment methods)\b": "We accept cash, credit/debit cards, and UPI payments.",  # Response for payment methods
        r"\b(17|store hours|timing)\b": "Our store is open from 8 AM to 10 PM every day.",  # Response for store hours
        r"\b(18|location|address)\b": "We are located at XYZ Market, Main Street, City.",  # Response for location/address
        r"\b(19|bye|exit)\b": "Goodbye! Happy shopping! 🛍"  # Response for exit
    }

    for pattern, response in responses.items():  # Loop through each pattern and response
        if re.search(pattern, user_input):  # Check if the user input matches any pattern
            return response  # Return corresponding response

    return "I am sorry, I didn't understand that. Can you rephrase or ask about a specific grocery item?"  # Default response for unrecognized input

# Chatbot interaction loop
print("Welcome to our Grocery Chatbot! Type 'exit' to end the conversation.")  # Welcome message

while True:  # Infinite loop for continuous interaction
    user_message = input("You: ")  # Get user input
    if user_message.lower() in ["bye", "exit"]:  # If user wants to exit
        print("Chatbot: Goodbye! Happy shopping! 🛍")  # Exit message
        break  # End the loop
    response = chatbot_response(user_message)  # Get chatbot's response
    print("Chatbot:", response)  # Print the chatbot's response
