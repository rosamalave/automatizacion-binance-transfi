from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials

# Autenticación con Google Drive API
class actualizandoarchivodrive():
    def __init__(self):
        SCOPES = ['https://www.googleapis.com/auth/drive']
        creds = Credentials.from_service_account_file('R:/Respaldo/singular-hash-437514-p9-9bc09e62582b.json', scopes=SCOPES)
        drive_service = build('drive', 'v3', credentials=creds)

        # ID del archivo de Google Drive (se obtiene de la URL del archivo en Drive)
        file_id = '1wcsIICT1KjWlhKQnSNJZn09AqCrtiT6g'

        # Ruta al archivo local que quieres subir
        local_file_path = 'R:/Respaldo/Rosa/TRABAJO/transfihermanos/automatizacion/automatizacion-binance-transfi/tasas-transfi.xlsx'

        # Subir y reemplazar el archivo existente
        file_metadata = {'name': 'tasas-transfi.xlsx'}  # Nombre del archivo en Drive
        media = MediaFileUpload(local_file_path, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        updated_file = drive_service.files().update(
            fileId=file_id,
            media_body=media,
            fields='id'
        ).execute()

        print(f"Archivo actualizado con éxito. ID: {updated_file['id']}")
