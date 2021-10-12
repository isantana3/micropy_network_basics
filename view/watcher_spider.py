import time
from service.network_service import NetworkService
from model.esp_wifi import EspWifi
from model.rede_wifi import RedeWifi
from model.relogio import Relogio
from model.led import Led
import network
import uasyncio

import os
# from dotenv import load_dotenv, find_dotenv


# load_dotenv(find_dotenv())
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

# Nome da rede que quer se conectar
SSID = "ecologueiros"

# Senha da rede que quer se conectar
PASSWORD = "eusoufoda123"

def run():
    spider_esp : EspWifi = EspWifi()
    try:
        if spider_esp.ativar():
            if spider_esp.esta_ligado():
                print("Sensor WIFI ligado")
                networks = spider_esp.buscar()
                network_wifi : list[RedeWifi] = []
                for ssid, bssid, canal, rssi, seguranca, oculto in sorted(networks, key=lambda x: x[0]):
                    network_wifi.append(RedeWifi(ssid, canal, seguranca, oculto, spider_esp.wlan_ap, spider_esp.wlan_sta))
                ledzin : Led = Led()
                relogin : Relogio = Relogio()
                watcher_spider : NetworkService = NetworkService(spider_esp, network_wifi, ledzin, relogin)

                Wifis_perto = watcher_spider.listar_wifi()
                while True:
                    for wifi in Wifis_perto:
                        print("=============================")
                        print(wifi)
                        print("=============================\n")
                    conectado, texto = watcher_spider.conectar(str(SSID), str(PASSWORD))
                    if conectado:
                        print(texto)
                        watcher_spider.led.on()
                        watcher_spider.tempo_conectado()
                        if not spider_esp.esta_conectado():
                            print("Conexão perdida! Tendando reconexão...")
                    else:
                        print(texto)

                    time.sleep(2)
                    print("\n" * 130)

    except Exception as e:
        print(e)