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

    def calcular_mensaje(self):
        # Seleccionar la hoja de trabajo donde están los valores
        hoja = self.excel['tasas']  # Cambia 'Hoja1' por el nombre de la hoja que estás usando
        
        # Leer los valores de las celdas
        bsausdt = float(hoja['N10'].value)
        usdtacop = float(hoja['O10'].value)
        copausdt = float(hoja['N12'].value)
        usdtabs = float(hoja['O12'].value)
        promediotasa=(hoja['B10'].value)
        porcentajeganancia=(hoja['F10'].value)
        print("Prueba de promedio tasa: ", promediotasa)
        print("Prueba de promedio tasa: ", porcentajeganancia)
        # Realizar los cálculos necesarios
        valor_bsausdt = 1000.00 / bsausdt
        print(f"1000 bs a usdt= {valor_bsausdt}")
        valor_usdtacop = valor_bsausdt * usdtacop
        print(f"{valor_bsausdt} a pesos = {valor_bsausdt*usdtacop}")
        valor_copausdt = valor_usdtacop / copausdt
        print(f"{valor_usdtacop} pesos a usdt = {valor_copausdt}")
        valor_usdtabs = valor_copausdt * usdtabs
        print(f"{valor_copausdt} usdt a bs = {valor_usdtabs}")

        # Generar el mensaje con los valores calculados
        mensaje = (
            "Conversión del día 💰\n"
            "✅ Dólar paralelo: 68\n\n"
            "Binance\n"
            f"✅ 1000 Bs = {round(valor_bsausdt, 2)} = {round(valor_usdtacop, 2)} pesos\n"
            f"✅ {round(valor_usdtacop, 2)} pesos = {round(valor_copausdt, 2)} = {round(valor_usdtabs, 2)} Bs\n\n"
            "Promedio competencia\n"
            f"✅ Tasa pesos: {round(20, 2)}\n"
            f"✅ Tasa Bs: {round(20, 2)}\n"
            f"✅ % Ganancia: {round(20, 2)}%"
        )

        # Mostrar el mensaje en la celda A1 de otra hoja, por ejemplo, 'Mensaje'
        hoja_destino = self.excel['Hoja1']  # Cambia 'Mensaje' por el nombre de la hoja donde quieres guardar el mensaje
        hoja_destino['A1'] = mensaje

        # Guardar los cambios en el archivo
        self.excel.save(self.rutaarchivo)
        return mensaje

if __name__ == "__main__":
    # Inicializar la clase para ejecutar el script
    editarexcel()