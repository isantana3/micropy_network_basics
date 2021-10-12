from model.esp_wifi import EspWifi
from model.data import Data
import uasyncio
import time
from model.rede_wifi import RedeWifi
from model.relogio import Relogio
from model.led import Led
import network

class NetworkService():
    def __init__(self, esp : EspWifi, wifi : list[RedeWifi], led : Led, relogio : Relogio) -> None:
        self.esp : EspWifi = esp
        self.wifis : list[RedeWifi] = wifi
        self.led : Led = led
        self.relogio : Relogio = relogio

    def listar_wifi(self) -> list[str]:
        '''
            Retorna uma lista com todos os wifis no alcance da esp 
        '''
        lista_de_wifis = []
        for wf in self.wifis:
            lista_de_wifis.append(wf.print_wifi())

        return lista_de_wifis

    def tempo_conectado(self):
        '''
            Calcula há quanto tempo o esp está conectado.O tempo é dado em:
            Anos/meses/dias horas:minutos:segundos
        '''
        while True:
            if (self.esp.esta_conectado()):
                tempo_decorrido : dict = self.relogio.atualizar_relogio()
                string_saida = str(tempo_decorrido['ano']) + "/" +\
                                str(tempo_decorrido['mes']) + "/" +\
                                str(tempo_decorrido['dia']) + " " +\
                                str(tempo_decorrido['hora']) +":" +\
                                str(tempo_decorrido['min']) + ":" +\
                                str(tempo_decorrido['sec'])
                        
                print(f"| Tempo conectado: {string_saida}")
                time.sleep(0.9)
            else:
                break
        self.led.off()

    def conectar(self, ssid : str , senha : str):
        '''
            Recebe um SSID e senha e tenta se conectar ao wifi, retornando uma tupla composta com um bool indicando 
            sucesso ou falaha na conexão e uma string com a mensagem de erro ou de sucesso
        '''
        if not self.esp.esta_ligado():
            self.esp.ativar()

        for wifi in self.wifis:
            if ssid == wifi.ssid:
                break

        try:
            resposta, texto = wifi.conectar_wifi(ssid, senha)
            if resposta:
                self.relogio.reinciar_relogio()
            return resposta, texto
            

        except Exception as e:
            print(e)

