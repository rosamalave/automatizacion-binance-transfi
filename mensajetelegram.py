import openpyxl
from telegram import Bot
import os
import asyncio

class bottelegram():

    def __init__(self, rutacreds):
        if 'GITHUB_ACTIONS' in os.environ:
            # Si está en GitHub Actions, usamos las variables de entorno
            self.token, self.chat_id = self.leer_credenciales_desde_github()
        else:
            # Si está en la PC local, usamos el archivo Excel
            self.token, self.chat_id = self.leer_credenciales_desde_excel(rutacreds)

    # Función para leer las credenciales desde un archivo Excel local
    def leer_credenciales_desde_excel(self,ruta_archivo):
        # Cargar el archivo Excel
        wb = openpyxl.load_workbook(ruta_archivo)
        sheet = wb.active
        # Leer el token desde la celda A1 y el chat_id desde la celda A2
        token = sheet['A1'].value
        chat_id = sheet['A2'].value
        return token, int(chat_id)

    # Función para leer un mensaje desde el archivo Excel
    def leer_mensaje_desde_excel(self,ruta_archivo):
        # Cargar el archivo Excel
        wb = openpyxl.load_workbook(ruta_archivo)
        sheet = wb['Hoja1']
        # Leer el mensaje (ejemplo: A3 es la celda que contiene el mensaje)
        mensaje = sheet['A1'].value
        return mensaje

    # Función para obtener las credenciales de GitHub Secrets (en caso de estar en GitHub Actions)
    def leer_credenciales_desde_github(self):
        token = os.getenv('TELEGRAM_BOT_TOKEN')  # GitHub Secret
        chat_id = os.getenv('TELEGRAM_CHAT_ID')  # GitHub Secret
        return token, int(chat_id)

    # Función para enviar el mensaje automáticamente
    async def enviar_mensaje_automatico(self,mensaje,rutamensajeexcel):
        # Crear una instancia del bot
        print (f"token: {self.token}")
        self.bot = Bot(token=self.token)
        
        # Leer el mensaje desde Excel
        #mensaje = leer_mensaje_desde_excel("rutamensajeexcel") 'tasas-transfi.xlsx'

        # Enviar el mensaje al chat de Telegram
        await self.bot.send_message(chat_id=self.chat_id, text=mensaje)
