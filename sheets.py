import streamlit as st
import gspread # Biblioteca para Google Sheets
from oauth2client.service_account import ServiceAccountCredentials # Autenticação

# Inicializa a conexão com o Google Sheets
@st.cache_resource
def init_google_sheets():
  creds_dict = st.secrets["gcp_service_account"]
  scope = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
  creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes=scope)
  client = gspread.authorize(creds)

  planilha_completa = client.open(title=st.secrets["TITLE"], folder_id=st.secrets["FOLDER_ID"])
  aba = planilha_completa.get_worksheet(0)
  return aba

# Função para adicionar linhas ao Google Sheets
def add_rows_to_sheet(tab, data_list):
    tab.append_rows(data_list)