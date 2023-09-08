# Define message types
MESSAGE_TYPE_SEND = "SEND"
MESSAGE_TYPE_RECEIVED = "RECEIVED"
MESSAGE_TYPE_STOP_RECEIVING = "STOP_RECEIVING"
MESSAGE_TYPE_CONFIRMED = "CONFIRMED"

# Function to parse incoming messages
def parse_message(message):
    ## Message Format: type|to|from|message
    try:
        # Split the message using the '|' character as a delimiter
        parts = message.split('|')
        
        if len(parts) == 4:
            message_type, to, _from, message_body = parts
            # Create a dictionary with the message components
            parsed_message = {
                'type': message_type,
                'to': to,
                'from': _from,
                'message': message_body
            }
            return parsed_message
        else:
            # If the message doesn't have exactly four parts, it's invalid
            return None
    except Exception as e:
        # Handle any exceptions that may occur during parsing
        print(f"Error parsing message: {e}")
        return None


def generate_response(parsed_message):
    try:
        # Check if the parsed message has the required components
        if 'type' in parsed_message and 'to' in parsed_message and 'from' in parsed_message and 'message' in parsed_message:
            message_type = parsed_message['type']
            
            # Check the message type to determine the response
            if message_type == "SEND":
                # If it's a SEND message, generate an acknowledgment response
                response_message = f"ACK|{parsed_message['from']}|{parsed_message['to']}|Message received and acknowledged"
                
                return response_message
            else:
                # Handle other message types or responses as needed
                return "Unsupported message type"
        else:
            # If the parsed message is missing required components, return an error response
            return "Invalid message format"
    except Exception as e:
        # Handle any exceptions that may occur during response generation
        print(f"Error generating response: {e}")
        return "Error generating response"

