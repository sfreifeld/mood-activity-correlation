import fitbit as fitbit
import requests
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_URL, TOKEN_URL
from datetime import datetime, timedelta



auth_params = {
    'client_id': CLIENT_ID,
    'response_type': 'code',
    'scope': 'activity',
    'redirect_uri': REDIRECT_URI
}

auth_request = requests.get(AUTH_URL, params=auth_params)
print(f'Go to the following URL: {auth_request.url}')




# Step 2: Exchange authorization code for access token
auth_code = input('Enter the authorization code: ')
token_data = {
    'client_id': CLIENT_ID,
    'grant_type': 'authorization_code',
    'redirect_uri': REDIRECT_URI,
    'code': auth_code
}

response = requests.post(TOKEN_URL, data=token_data, auth=(CLIENT_ID, CLIENT_SECRET))
access_token = response.json()['access_token']

print("Authorization complete. Access token obtained.")


# Step 3: Use access token to make API requests


def fetch_activity_data(access_token):
    # Use the access token to fetch activity data
    end_date = datetime.now()
    start_date = end_date - timedelta(days=6)  # last 7 days including today
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    # Corrected URL format
    period = '7d'
    activity_url = f"https://api.fitbit.com/1/user/-/activities/active-zone-minutes/date/today/{period}.json"
    headers = {'Authorization': f'Bearer {access_token}'}
    activity_response = requests.get(activity_url, headers=headers)
    return activity_response.json()

# Call the function with your token
activity_data = fetch_activity_data(access_token)
print(activity_data)

