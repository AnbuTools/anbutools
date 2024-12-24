import requests

# Define the API endpoint and API key
api_url = "http://bulksmsbd.net/api/getBalanceApi?api_key=dxL6s1sQb0J2jyusJU6l"

try:
    # Send a GET request to the API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse and print the response
        print("API Response:", response.json())
    else:
        print(f"Failed to fetch balance. Status code: {response.status_code}")
        print("Error message:", response.text)
except Exception as e:
    print(f"An error occurred: {e}")
