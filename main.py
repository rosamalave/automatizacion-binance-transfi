#.venv\Scripts\activate
import os
from tasasbinance import tasasbinance
from actualizarexcel import editarexcel
from actualizardrive import conexiondrive

class Automatizacion:

    def __init__(self):
        self.tasasbinance = tasasbinance()
        if os.getenv("GITHUB_ACTIONS") == "true":
            # Ruta para GitHub Actions
            rutalocalexcel = 'tasas-transfi.xlsx'
        else:
            # Ruta local en tu máquina
            rutalocalexcel = 'R:/Respaldo/Rosa/TRABAJO/transfihermanos/automatizacion/automatizacion-binance-transfi/tasas-transfi.xlsx'
        
        rutalocalexcel='R:/Respaldo/Rosa/TRABAJO/transfihermanos/automatizacion/automatizacion-binance-transfi/tasas-transfi.xlsx'
        self.editarexcel = editarexcel(rutalocalexcel)
        self.drive=conexiondrive('1wcsIICT1KjWlhKQnSNJZn09AqCrtiT6g','tasas-transfi.xlsx', rutalocalexcel)
        self.hoja='Hoja1'
        #self.drive.sincronizararchivo()
        
    def cop_usdt(self):
        precio=self.calculotasa('COP','BUY',1,10,65000, [], 10000)
        if precio:
            self.editarexcel.editarcelda(self.hoja,'N12',float(precio))
    def usdt_cop(self):
        precio=self.calculotasa('COP','SELL',1,10,65000, [], 10000)
        if precio:
            self.editarexcel.editarcelda(self.hoja,'O10',float(precio))
    def bs_usdt(self):
        precio=self.calculotasa('VES','BUY',5,10,1000, ['Banesco', 'PagoMovil'], 600)
        if precio:
            self.editarexcel.editarcelda(self.hoja,'N10',float(precio))
    def usdt_bs(self):
        precio=self.calculotasa('VES','SELL',5,10,1000, ['Banesco', 'PagoMovil'], 600)
        if precio:
            self.editarexcel.editarcelda(self.hoja,'O12',float(precio))

    def calculotasa(self, moneda, compraovende, npagina, nresultspag, montobase, metodopago, basefiltro):
        self.tasasbinance.filtrartasas(moneda, compraovende, npagina, nresultspag, montobase, metodopago)
        if self.tasasbinance.solicitud_apip2p():
            data = self.tasasbinance.mejoraviso(basefiltro)

            if data:
                self.tasasbinance.reporteconsola(moneda,basefiltro)
                print(f"moneda: {moneda} cambio: {compraovende}")
                precio = data[0]
                return precio
            else:
                self.tasasbinance.reporteconsola(moneda,0)
                print(f"moneda: {moneda} cambio: {compraovende} No se pudo calcular la tasa. O si imprime algo antes es porque no pasa el filtro")
                return False
        else:
            print("Error en la solicitud de datos a la API.")
            return False
        
if __name__ == "__main__":
    # Inicializar la clase para ejecutar el script
    automatizacion = Automatizacion()
    automatizacion.cop_usdt()
    automatizacion.usdt_cop()
    automatizacion.bs_usdt()
    automatizacion.usdt_bs()
    automatizacion.drive.sincronizararchivo()
