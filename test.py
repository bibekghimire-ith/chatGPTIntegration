# Importing the necessary libraries
import requests
import json

# Setting the base URL
base_url = "https://api.chatgpt.com/v3/"

# Function to send a message
def send_message(message, session_id):
    """
    Sends a message to ChatGPT and returns the response.
    
    Parameters:
    message (str): The message to be sent.
    session_id (str): The session ID associated with the conversation.
    
    Returns:
    response (dict): The response from ChatGPT.
    """
    
    # Creating the request URL
    url = base_url + "message"
    
    # Setting the request headers
    headers = {
        "Content-Type": "application/json"
    }
    
    # Setting the request payload
    payload = {
        "message": message,
        "session_id": session_id
    }
    
    # Sending the request
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # Returning the response
    return response.json()

# Function to create a new session
def create_session():
    """
    Creates a new session and returns the session ID.
    
    Returns:
    session_id (str): The session ID associated with the new session.
    """
    
    # Creating the request URL
    url = base_url + "session"
    
    # Sending the request
    response = requests.post(url)
    print(response)
    
    # Returning the session ID
    return response.json()["session_id"]

session = create_session()