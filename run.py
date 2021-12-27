import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREADS = Credentials.from_service_account_file('creds.json')
SCOPED_CREADS = CREADS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREADS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)