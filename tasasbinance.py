import requests
import json

# URL del endpoint P2P de Binance
url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"

# Configurar los parámetros de la solicitud
payload = {
    "asset": "USDT",         # Activo (USDT en este caso)
    "fiat": "VES",           # Moneda fiat (Bolívares)
    "tradeType": "BUY",      # Tipo de operación: Comprar USDT con VES
    "page": 5,               # Página de resultados
    "rows": 10,              # Número de resultados deseados
    "transAmount": "1000",   # Monto específico en VES
    "payTypes": ["PagoMovil", "Banesco"],          # Métodos de pago (vacío = todos)
    "publisherType": None    # Tipo de usuario
}

# Encabezados (opcional)
headers = {
    "Content-Type": "application/json"
}

# Realizar la solicitud
response = requests.post(url, json=payload, headers=headers)

# Procesar los datos
if response.status_code == 200:
    data = response.json()
    ads = data['data']
    for ad in ads:
        price = ad['adv']['price']
        min_amount = ad['adv']['minSingleTransAmount']
        max_amount = ad['adv']['maxSingleTransAmount']

        # Extraer solo los `payType` de los métodos de pago
        payment_types = [method['payType'] for method in ad['adv']['tradeMethods']]
        
        if int(min_amount) >= 600:
            print(f"Tasa: {price} VES/USDT")
            print(f"Monto mínimo: {min_amount} VES, Máximo: {max_amount} VES")
            print("Métodos de pago (payType):")
            for pay_type in payment_types:
                    print(f"  - {pay_type}")
            print("-" * 40)
else:
    print(f"Error: {response.status_code} - {response.text}")
