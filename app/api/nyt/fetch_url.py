import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

NYT_API_KEY = os.getenv("NYT_API_KEY")
NYT_AUTH_KEY = os.getenv("NYT_AUTH_KEY")
period = 1
base_url = f"https://api.nytimes.com/svc/mostpopular/v2/viewed/{period}.json"

# Parameters for the request
params = {
    "api-key": NYT_API_KEY
}

try:
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

    data = response.json()
    if data.get("status") == "OK":
        results = data.get("results", [])
        if results:
            print(f"--- Top {len(results)} Most Popular Articles (Last {period} days) ---")
            for article in results:
                url = article.get("url")
                title = article.get("title") # Optionally get the title as well
                if url:
                    print(f"Title: {title}\nURL: {url}\n")
        else:
            print("No articles found in the response.")
    else:
        print(f"API request failed with status: {data.get('status')}")
        if data.get('fault'):
            print(f"Fault message: {data['fault']['faultstring']}")


except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # e.g., 401 Client Error: Unauthorized
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}") # e.g., DNS failure, refused connection
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred during the request: {req_err}")
except json.JSONDecodeError:
    print("Failed to decode JSON response.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
