from model.data import Data

class Relogio():
    def __init__(self) -> None:
        self.hora_inicial = Data()
        ano, mes, dia_do_mes, hora, minuto, segundo = self.hora_inicial.tempo_decorrido(self.hora_inicial)
        self.tempo_decorrido = {
            'ano' : ano,
            'mes' : mes,
            'dia' : dia_do_mes,
            'hora': hora,
            'min' : minuto,
            'sec' : segundo
        }

    def atualizar_relogio(self) -> dict:
        '''
            Atualiza o tempo decorrido desde um ponto previamente criado e retorna um dicionário com a data/hora decorrida 
            desde esse ponto.
        '''

        ano, mes, dia_do_mes, hora, minuto, segundo = self.hora_inicial.tempo_decorrido()
        self.tempo_decorrido = {
            'ano' : ano,
            'mes' : mes,
            'dia' : dia_do_mes,
            'hora': hora,
            'min' : minuto,
            'sec' : segundo
        }
        return self.tempo_decorrido

    def zerar_relogio(self) -> None:
        '''
            Zera todas as instâncias do relógio às setando para None
        '''

        self.hora_inicial = None
        self.tempo_decorrido = None

    def reinciar_relogio(self) -> None:
        '''
            Reinicia um relógio, dando a ele uma nova data de início e começando a atualizar seu tempo decorrido 
        '''
        
        self.hora_inicial = Data()
        ano, mes, dia_do_mes, hora, minuto, segundo = Data.tempo_decorrido(self.hora_inicial)
        self.tempo_decorrido = {
            'ano' : ano,
            'mes' : mes,
            'dia' : dia_do_mes,
            'hora': hora,
            'min' : minuto,
            'sec' : segundo
        }