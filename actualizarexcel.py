import openpyxl

class editarexcel():

    def __init__(self, rutaarchivo):
        self.rutaarchivo=rutaarchivo
        # Cargar el archivo Excel
        self.excel = openpyxl.load_workbook(self.rutaarchivo)
    
    def editarcelda(self, hoja, celda, valor):
        """
        hoja:nombre de la hoja (str),
        celda:donde se va a editar (ej: A1)(str),
        valor:nuevo contenido de la celda 
        """
        #mejoraviso=tasasbinance()
        #aviso=mejoraviso.mejoraviso()
        
        # Seleccionar la hoja activa o una específica
        sheet = self.excel[hoja]  # Cambia 'Hoja1' por el nombre de tu hoja
        # Escribir en celdas específicas
        sheet[celda] = valor  # Celda A1
        
        # Guardar los cambios
        self.excel.save(self.rutaarchivo)

if __name__ == "__main__":
    # Inicializar la clase para ejecutar el script
    editarexcel()