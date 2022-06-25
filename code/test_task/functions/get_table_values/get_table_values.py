from googleapiclient.discovery import build
from google.oauth2 import service_account


def get_table_values():
    # Ключи Sheets API
    SERVICE_ACCOUNT_FILE = 'test_task/functions/get_table_values/keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # ID spreadsheet.
    SAMPLE_SPREADSHEET_ID = '10J-A-B-RAYCQgm4ZOqUnOGVo-PBY29vZrOUI1DvULL0'
    service = build('sheets', 'v4', credentials=creds)
    # Получение данных Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range='list1!A2:D').execute()
    values = result.get('values', [])
    return values
