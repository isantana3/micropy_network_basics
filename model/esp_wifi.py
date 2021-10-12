import network

class EspWifi():
    def __init__(self) -> None:
        self.wlan_ap = network.WLAN(network.AP_IF)
        self.wlan_sta = network.WLAN(network.STA_IF)

    def esta_ligado(self) -> bool:
        '''
            Retorna True caso o sensor de wifi da esp esteja ligado, e False caso contrário
        '''
        return self.wlan_sta.active()
   
    def esta_conectado(self) -> bool:
        '''
            Retorna True caso a esp esteja conectada a um wifi, e False caso contrário
        '''
        return self.wlan_sta.isconnected()

    def ativar(self) -> bool:
        '''
            Ativa o sensor de wifi da esp e retorna True em caso de sucesso, e False caso contrário 
        '''
        return self.wlan_sta.active(True)

    def desativar(self) -> bool:
        '''
            Desativa o sensor de wifi da esp e retorna True em caso de sucesso, e False caso contrário 
        '''
        return self.wlan_sta.active(False)

    def buscar(self):
        '''
            Busca sinais de wifi próximos e os retorna 
        '''
        return self.wlan_sta.scan()