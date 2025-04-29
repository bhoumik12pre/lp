import re

def chatbot_response(user_input):
    user_input = user_input.lower().strip()  # Convert input to lowercase and remove leading/trailing spaces

    responses = {
        r"\b(1|hello|hi|hey)\b": "Hello! Welcome to the IFB Washing Machine Service Centre. How can I assist you today?",  # Response for greetings
        r"\b(2|how are you)\b": "I'm doing great! I'm here to help you with your IFB washing machine service needs.",  # Response for asking how the bot is
        r"\b(3|book service|schedule service|repair)\b": "Sure! Please provide your washing machine model number and preferred service date.",  # Response for booking service
        r"\b(4|installation)\b": "We provide installation support. Please share your product details and address.",  # Response for installation queries
        r"\b(5|warranty status|check warranty)\b": "Please provide your machine's serial number to check warranty status.",  # Response for warranty status
        r"\b(6|troubleshooting|problem|issue)\b": "I'm here to help! Please describe the problem you are facing with your washing machine.",  # Response for troubleshooting queries
        r"\b(7|service charges|cost)\b": "Service charges vary based on the issue. Basic inspection charges are ₹300.",  # Response for service charges
        r"\b(8|parts replacement|spare parts)\b": "We use genuine IFB spare parts. Charges depend on the part that needs replacement.",  # Response for parts replacement inquiries
        r"\b(9|service status|track request)\b": "Please share your service request number to track the status.",  # Response for service tracking
        r"\b(10|customer care|support number)\b": "You can reach our customer care at 1800-3000-5678 (toll-free).",  # Response for customer care number
        r"\b(11|working hours|timings)\b": "Our service center is open from 9 AM to 7 PM, Monday to Saturday.",  # Response for service center working hours
        r"\b(12|location|address)\b": "We are located at XYZ Plaza, Main Road, YourCity.",  # Response for location/address
        r"\b(13|feedback|complaint)\b": "We're sorry for the inconvenience. Please share your feedback or complaint, and we'll address it quickly.",  # Response for feedback or complaints
        r"\b(14|maintenance tips|care tips)\b": "Always use IFB-approved detergents, avoid overloading, and clean the filter regularly for best performance.",  # Response for maintenance tips
        r"\b(15|bye|exit)\b": "Goodbye! Thank you for contacting IFB Service Centre. 😊"  # Response for exit
    }

    for pattern, response in responses.items():  # Loop through each pattern and response
        if re.search(pattern, user_input):  # Check if the user input matches any pattern
            return response  # Return corresponding response

    return "I'm sorry, I didn't understand that. Could you please rephrase or ask about IFB washing machine service?"  # Default response for unrecognized input

# Chatbot interaction loop
print("Welcome to the IFB Washing Machine Service Centre Chatbot! Type 'exit' to end the conversation.")  # Welcome message

while True:  # Infinite loop for continuous interaction
    user_message = input("You: ")  # Get user input
    if user_message.lower() in ["bye", "exit"]:  # If user wants to exit
        print("Chatbot: Goodbye! Thank you for contacting IFB Service Centre. 😊")  # Exit message
        break  # End the loop
    response = chatbot_response(user_message)  # Get chatbot's response
    print("Chatbot:", response)  # Print the chatbot's response
