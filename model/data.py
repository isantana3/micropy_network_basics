import time
ano, mes, dia_do_mes, hora, minuto, segundo, dia_da_semana, dia_do_ano = time.localtime()
bissexto = ""
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    bissexto = "29"
else:
    bissexto = "28"
LIMITE_MES = {
      '01': '31',
      '02': bissexto,
      '03': '31',
      '04': '30',
      '05': '31',
      '06': '30',
      '07': '31',
      '08': '31',
      '09': '30',
      '10': '31',
      '11': '30',
      '12': '31'
    }

class Data():
    def __init__(self) -> None:
        self.ano, self.mes, self.dia_do_mes, self.hora, self.minuto, self.segundo, self.dia_da_semana, self.dia_do_ano = time.localtime()

    def atualizar(self):
        '''
            Atualiza o objeto Data com a data e hora mais atual
        '''
        self.ano, self.mes, self.dia_do_mes, self.hora, self.minuto, self.segundo, self.dia_da_semana, self.dia_do_ano = time.localtime()
    
    def agora(self):
        '''
            Retorna uma Tupla contendo a data e hora atua. A tupla cotém 8 inteiros retornados, sendo eles:
            ano, mês, dia do mês, hora, minuto, segundo, dia da semana e o dia do ano
        '''
        ano,mes,dia_do_mes,hora,minuto,segundo,dia_da_semana,dia_do_ano = time.localtime()
        return ano,mes,dia_do_mes,hora,minuto,segundo,dia_da_semana,dia_do_ano

    def maior_data(self, data_1, data_2 = None):
        '''
            Este método pode ser chamado através da instância de um objeto e passando uma data como parâmetro 
            ou chamando o método através da classe Data e passando 2 datas como parâmetro.
            O método compara as duas datas em questão e retorna 1, caso a primeria data seja a maior, -1 caso a 
            segunda seja a maior ou 0 caso as datas sejam iguais
        '''
        if data_2 is None:
            data_2 = data_1
            data_1 = self

        if data_1.ano > data_2.ano:
            return 1
        elif data_1.ano < data_2.ano:
            return -1
        else: 
            if data_1.mes > data_2.mes:
                return 1
            elif data_1.mes < data_2.mes:
                return -1
            else:
                if data_1.dia_do_mes > data_2.dia_do_mes:
                    return 1
                elif data_1.dia_do_mes < data_2.dia_do_mes:
                    return -1
                else:
                    if data_1.hora > data_2.hora:
                        return 1
                    elif data_1.hora < data_2.hora:
                        return -1
                    else:
                        if data_1.minuto > data_2.minuto:
                            return 1
                        elif data_1.minuto < data_2.minuto:
                            return -1
                        else:
                            if data_1.segundo > data_2.segundo:
                                return 1
                            elif data_1.segundo < data_2.segundo:
                                return -1
                            else:
                                return 0


    def add(self, nova_data):
        '''
            Faz a soma de uma data a data do objeto que chamou esse método, fazendo com que a data do objeto seja atualizada 
            para uma data futura.
        '''

        self.ano += abs(self.ano - nova_data.ano)
        self.mes += abs(self.mes - nova_data.mes)
        self.dia_do_mes += abs(self.dia_do_mes - nova_data.dia_do_mes)
        self.hora += abs(self.hora - nova_data.hora)
        self.minuto += abs(self.minuto - nova_data.minuto)
        self.segundo += abs(self.segundo - nova_data.segundo)
        self.dia_da_semana += abs(self.dia_da_semana - nova_data.dia_da_semana)
        self.dia_do_ano += abs(self.dia_do_ano - nova_data.dia_do_ano)

        if self.segundo > 59:
            self.minuto += 1
            self.segundo -= 60
        if self.minuto > 59:
            self.hora += 1
            self.minuto -= 60
        if self.hora > 23:
            self.dia_da_semana += 1
            self.dia_do_mes += 1
            self.dia_do_ano += 1
            self.hora -= 24

        if self.dia_do_mes > int(LIMITE_MES[self.mes]):
            self.dia_do_mes -= LIMITE_MES[self.mes]
            self.mes += 1

        if self.dia_da_semana > 6:
            self.dia_da_semana -= 6

        if self.mes > 12:
            self.ano += 1
            self.dia_do_ano = 0
            self.mes -= 12

    def sub(self,nova_data):
        '''
            Faz a subtração da data do objeto pela data passada por argumento, fazendo com que a data do objeto seja atualizada 
            para uma data passada.
        '''

        self.ano -= abs(self.ano - nova_data.ano)
        self.mes -= abs(self.mes - nova_data.mes)
        self.dia_do_mes -= abs(self.dia_do_mes - nova_data.dia_do_mes)
        self.hora -= abs(self.hora - nova_data.hora)
        self.minuto -= abs(self.minuto - nova_data.minuto)
        self.segundo -= abs(self.segundo - nova_data.segundo)
        self.dia_da_semana -= abs(self.dia_da_semana - nova_data.dia_da_semana)
        self.dia_do_ano -= abs(self.dia_do_ano - nova_data.dia_do_ano)

        if self.segundo < 0:
            self.minuto -= 1
            self.segundo += 60
        if self.minuto < 0:
            self.hora -= 1
            self.minuto += 60
        if self.hora >23:
            self.dia_da_semana -= 1
            self.dia_do_mes -= 1
            self.dia_do_ano -= 1
            self.hora += 24

        if self.dia_do_mes < 0:
            self.mes -= 1
            self.dia_do_mes += LIMITE_MES[self.mes]

        if self.dia_da_semana < 0:
            self.dia_da_semana += 6

        if self.mes < 0:
            self.ano -= 1
            if bissexto == "28":
                self.dia_do_ano += 365
            else:
                self.dia_do_ano += 366
            self.mes += 12

    def tempo_decorrido(self, nova_data = None):
        '''
            Recebe uma data anterior e uma data atual ou futura e retorna a diferença entre elas através de 6 parâmetros. Caso o segundo parâmetro seja uma data anterior a data do paarâmetro 1, a função retorna False
            return (int) -> Ano, mês, dia do mês, hora, minuto, segundo
            return (bool) -> False
        '''

        if nova_data == None:
            nova_data = Data()

        if self.maior_data(nova_data) == 1:
            return False

        ano = nova_data.ano - self.ano
        mes = nova_data.mes - self.mes
        dia_do_mes = nova_data.dia_do_mes - self.dia_do_mes
        hora = nova_data.hora - self.hora
        minuto = nova_data.minuto - self.minuto
        segundo = nova_data.segundo -self.segundo

        if segundo < 0:
            minuto -= 1
            segundo += 60
        if minuto < 0:
            hora -= 1
            minuto += 60
        if hora >23:
            dia_do_mes -= 1
            hora += 24

        if dia_do_mes < 0:
            mes -= 1
            dia_do_mes += LIMITE_MES[mes]

        if mes < 0:
            ano -= 1
            mes += 12

        return ano, mes, dia_do_mes, hora, minuto, segundo