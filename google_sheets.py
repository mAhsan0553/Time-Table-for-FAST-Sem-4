import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# Google Sheets API Setup
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
CREDS_FILE = '../time-table-project-450013-c42c82494be7.json'

def get_google_sheets_data(sheet_url):
    # Prefer Streamlit secrets in cloud deployments; fallback to local JSON for local runs.
    if "gcp_service_account" in st.secrets:
        creds = ServiceAccountCredentials.from_json_keyfile_dict(
            dict(st.secrets["gcp_service_account"]), SCOPES
        )
    else:
        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPES)
    client = gspread.authorize(creds)
    return client.open_by_url(sheet_url)
