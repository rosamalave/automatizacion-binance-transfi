import requests
import json

class tasasbinance():
    def __init__(self):
        # URL del endpoint P2P de Binance
        self.url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"

    def filtrartasas(self,moneda,comprasovendes,npaginas,nresultados_pag, montocambiobase, metodopago):
        """
            moneda=fiat= VES, COP
            montocambiobase=1000 bs o 65 mil pesos
        """
        # Configurar los parámetros de la solicitud
        self.payload = {
            "asset": "USDT",         # Activo (USDT en este caso)
            "fiat": moneda,           # Moneda fiat (Bolívares)
            "tradeType": comprasovendes,      # Tipo de operación: Comprar USDT con VES
            "page": npaginas,               # Página de resultados
            "rows": nresultados_pag,              # Número de resultados deseados
            "transAmount": montocambiobase,   # Monto específico en VES
            "payTypes": metodopago,          # Métodos de pago (vacío = todos)
            "publisherType": None    # Tipo de usuario
        }

        # Encabezados (opcional)
        self.headers = {
            "Content-Type": "application/json"
        }


    def solicitud_apip2p(self):
        # Realizar la solicitud
        self.response = requests.post(self.url, json=self.payload, headers=self.headers)
        if self.response.status_code == 200:
            print("Conexion exitosa")
            return True
        else:
             print("Error en la conexion")
             print(f"Error: {self.response.status_code} - {self.response.text}")
             return False
    
    def reporteconsola(self, moneda, filtrovalorminimo):
        # Procesar los datos
        data = self.response.json()
        ads = data['data']
        for ad in ads:
            price = ad['adv']['price']
            min_amount = ad['adv']['minSingleTransAmount']
            max_amount = ad['adv']['maxSingleTransAmount']

            # Extraer solo los `payType` de los métodos de pago
            payment_types = [method['payType'] for method in ad['adv']['tradeMethods']]
            
            if float(min_amount) >= filtrovalorminimo:
                print(f"hola{int(min_amount)}")
                print(f"Tasa: {price} {moneda}/USDT")
                print(f"Monto mínimo: {min_amount} {moneda}, Máximo: {max_amount} {moneda}")
                print("Métodos de pago (payType):")
                for pay_type in payment_types:
                        print(f"  - {pay_type}")
                print("-" * 40)

    def mejoraviso(self, filtrovalorminimo):
        """
        return
        [0]= tasa (numero str)
        [1]= metodos de pago (list)
        [2]= minimo (numero str)
        [3]= maximo (numero str)
        """
        data = self.response.json()
        ads = data['data']
        for ad in ads:
            price = ad['adv']['price']
            min_amount = ad['adv']['minSingleTransAmount']
            max_amount = ad['adv']['maxSingleTransAmount']

            # Extraer solo los `payType` de los métodos de pago
            payment_types = [method['payType'] for method in ad['adv']['tradeMethods']]
            
            if float(min_amount) >= filtrovalorminimo: #600 para bs
                mejoraviso=[price,payment_types, min_amount, max_amount]
                return mejoraviso

if __name__ == "__main__":
    # Inicializar la clase para ejecutar el script
    tasasbinance()

