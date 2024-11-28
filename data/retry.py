import requests
import time
from datetime import datetime

url = 'https://fbref.com/en/comps/9/Premier-League-Stats'

# Send the request
response = requests.get(url)

# Print the status code to check if it's 429 or something else
print(f"Status code: {response.status_code}")

# Check if the status code is 429 (Too Many Requests)
if response.status_code == 429:
    retry_after = response.headers.get("Retry-After")
    
    # Print the Retry-After header value for debugging
    print(f"Retry-After header: {retry_after}")
    
    if retry_after:
        try:
            # Try to interpret Retry-After as an integer (seconds)
            wait_time = int(retry_after)
            print(f"Retry after {wait_time} seconds.")
        except ValueError:
            # If it's not an integer, assume it's a date/time string
            try:
                retry_after_time = datetime.strptime(retry_after, "%a, %d %b %Y %H:%M:%S %Z")
                wait_time = (retry_after_time - datetime.utcnow()).total_seconds()
                print(f"Retry after {wait_time} seconds (calculated from date/time).")
            except Exception as e:
                print(f"Error parsing Retry-After as date/time: {e}")
        
        # Wait for the specified time before retrying
        time.sleep(wait_time)
    else:
        print("No Retry-After header found.")
else:
    print(f"Unexpected status code: {response.status_code}")
