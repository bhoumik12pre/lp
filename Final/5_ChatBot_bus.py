import re

def chatbot_response(user_input):
    user_input = user_input.lower().strip()  # Convert user input to lowercase and remove extra spaces

    responses = {
        r"\b(1|hello|hi|hey)\b": "Hello! Welcome to RedBus. How can I assist you today?",  # Response for greetings
        r"\b(2|how are you)\b": "I'm doing great! I'm here to help you book your bus tickets.",  # Response for asking chatbot's status
        r"\b(3|book ticket|bus booking|book bus)\b": "Sure! Please provide your departure and destination cities.",  # Response for ticket booking
        r"\b(4|cancel ticket|cancellation)\b": "You can cancel your ticket from 'My Bookings' section. Need help with it?",  # Response for ticket cancellation
        r"\b(5|refund status|refund)\b": "Refunds are processed within 5-7 working days after cancellation.",  # Response for refund status
        r"\b(6|available buses|search buses)\b": "Please provide your source, destination, and date of journey.",  # Response for bus search
        r"\b(7|ticket price|fare)\b": "Ticket prices vary by route and bus type. Please specify your route.",  # Response for ticket prices
        r"\b(8|offers|discounts)\b": "We have exciting discounts! Use code 'BUS10' to get 10% off on your first booking.",  # Response for offers
        r"\b(9|payment options|payment methods)\b": "We accept UPI, credit/debit cards, net banking, and wallets.",  # Response for payment options
        r"\b(10|bus timings|departure time)\b": "Please tell me the route so I can share available timings.",  # Response for bus timings
        r"\b(11|customer care|support)\b": "You can contact our customer care at 1800-123-1234.",  # Response for customer support
        r"\b(12|track bus|live location)\b": "Tracking is available 1 hour before the scheduled departure.",  # Response for bus tracking
        r"\b(13|luggage policy|baggage)\b": "Most buses allow up to 15kg of luggage per passenger.",  # Response for luggage policy
        r"\b(14|sleeper bus|ac bus|non ac bus)\b": "Yes, we have AC, Non-AC, Sleeper, and Semi-Sleeper buses. Please specify your preference!",  # Response for bus types
        r"\b(15|rating|reviews)\b": "You can check bus ratings and customer reviews before booking.",  # Response for bus reviews
        r"\b(16|reschedule ticket|change journey)\b": "Some buses allow rescheduling. Would you like me to check for your ticket?",  # Response for rescheduling tickets
        r"\b(17|popular routes)\b": "Popular routes include Mumbai-Pune, Bangalore-Chennai, Delhi-Jaipur, and more!",  # Response for popular routes
        r"\b(18|bus operator|travel agency)\b": "We partner with top bus operators like VRL, SRS, KSRTC, and more.",  # Response for bus operators
        r"\b(19|bye|exit)\b": "Goodbye! Safe travels! 🚌"  # Response for exit
    }

    for pattern, response in responses.items():  # Loop through all patterns and responses
        if re.search(pattern, user_input):  # Check if user input matches any pattern
            return response  # Return matching response

    return "I'm sorry, I couldn't understand that. Could you please rephrase or ask something about RedBus services?"  # Default response for unrecognized input

# Chatbot interaction loop
print("Welcome to the RedBus Chatbot! Type 'exit' to end the conversation.")  # Greeting message

while True:  # Infinite loop for continuous chatbot interaction
    user_message = input("You: ")  # Get user input
    if user_message.lower() in ["bye", "exit"]:  # Check if user wants to exit
        print("Chatbot: Goodbye! Safe travels! ")  # Exit message
        break  # Exit the loop
    response = chatbot_response(user_message)  # Get chatbot's response
    print("Chatbot:", response)  # Print chatbot's response
