import os
import json
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials

# Autenticación con Google Drive API
class conexiondrive():
    def __init__(self, idfiledrive, nombrearchivodrive, rutaarchivolocal):
        SCOPES = ['https://www.googleapis.com/auth/drive']

        # Verificar si el script se está ejecutando en un GitHub Action
        if os.environ.get("GITHUB_ACTIONS") == "true":
            # Cargar las credenciales desde la variable de entorno
            google_credentials_json = os.environ.get("GOOGLE_CREDENTIALS")
            creds = Credentials.from_service_account_info(json.loads(google_credentials_json), scopes=SCOPES)
        else:
            # Ruta local a las credenciales
            rutacred = 'R:/Respaldo/singular-hash-437514-p9-9bc09e62582b.json'
            creds = Credentials.from_service_account_file(rutacred, scopes=SCOPES)

        self.drive_service = build('drive', 'v3', credentials=creds)
        self.nombrearchivodrive = nombrearchivodrive
        self.file_id = idfiledrive  # ID del archivo de Google Drive (se obtiene de la URL del archivo en Drive)
        self.local_file_path = rutaarchivolocal  # Ruta al archivo local que quieres subir

    def sincronizararchivo(self):
        # Subir y reemplazar el archivo existente
        file_metadata = {'name': self.nombrearchivodrive}  # Nombre del archivo en Drive 
        media = MediaFileUpload(self.local_file_path, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        updated_file = self.drive_service.files().update(
            fileId=self.file_id,
            media_body=media,
            fields='id'
        ).execute()

        print(f"Archivo actualizado con éxito. ID: {updated_file['id']}")