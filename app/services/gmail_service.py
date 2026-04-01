from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None

    # Load existing token
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If no valid creds → login flow
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        # Save token for future
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service
def read_latest_email():
    service = get_gmail_service()

    results = service.users().messages().list(
        userId='me', maxResults=1
    ).execute()

    messages = results.get('messages', [])

    if not messages:
        return "No messages found"

    msg = service.users().messages().get(
        userId='me',
        id=messages[0]['id']
    ).execute()

    snippet = msg.get('snippet', '')
    return snippet