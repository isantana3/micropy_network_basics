from model.led import Led
import network

class RedeWifi():
    def __init__(self, ssid : str = None, canal : str = None, seguranca : str = None, oculto : bool = None, wlan_ap : any = None, wlan_sta : any = None) -> None:
        self.ssid = ssid
        self.canal = canal
        self.seguranca = seguranca
        if oculto:
            self.visibilidade = "Oculta"
        else:
            self.visibilidade = "Visivel"
        self.senha = None
        self.wlan_ap = wlan_ap
        self.wlan_sta = wlan_sta
        self.led : Led = Led()

    def print_wifi(self) -> str:
        '''
            Retorna uma string com os dados do wifi descritos
        '''
        AUTHMODE = {0: "open", 1: "WEP", 2: "WPA-PSK", 3: "WPA2-PSK", 4: "WPA/WPA2-PSK"}
        dados_da_rede = f"Nome: {self.ssid.decode('utf-8')} \n  Canal: {self.canal} \n  Autenticacao: {AUTHMODE.get(self.seguranca, '?')} \n  Visibilidade da rede: {self.visibilidade} \n  Senha: {self.senha}"
        return dados_da_rede

    def conectar_wifi(self, ssid : str = None, senha : str = None) :
        '''
            Conecta a esp a um sinal de wifi, desde que tenha sua SSID e senha.
            O led fica piscando enquanto a esp tenta se conectar
        '''
        timeout = 0
        if not self.wlan_sta.isconnected():
            print('Conectando com a rede...')
            self.wlan_sta.active(True)
            if ssid is None and senha is None:
                sucesso = False
                resposta = f"Senha ou nome da rede não foram passados\n"
                return sucesso, resposta
            self.wlan_sta.connect(ssid, senha)
            self.led.pisca(0.2)
            while not self.wlan_sta.isconnected() and timeout < 1000:
                timeout += 1
            self.led.para_pisca()
            self.senha = senha
        if timeout < 1000:
            self.led.on()
            sucesso = True
            resposta = f"Conectado com sucesso!\nDados da rede: {self.wlan_sta.ifconfig()}"

        else:    
            sucesso = False
            resposta = f"Conexão falhou!\n"
            
        return sucesso, resposta

