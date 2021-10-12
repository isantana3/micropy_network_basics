import uasyncio
from machine import Pin

class Led():
    def __init__(self) -> None:
        self.p = Pin(2, Pin.OUT)
        self.pisca = False

    def on(self) -> None:
        '''
            Liga o segundo pino de led
        '''
        self.p.on()

    def off(self) -> None:
        '''
            Desliga o segundo pino de led
        '''
        self.p.off()

    async def pisca(self, intervalo : float = 0.1) -> None:
        '''
            Faz o segundo pino de led piscar
        '''
        self.pisca = True
        while self.pisca:
            self.on()
            uasyncio.sleep(intervalo)
            self.off()
            uasyncio.sleep(intervalo)

    async def para_pisca(self) -> None:
        '''
            Faz o segundo pino de led parar de piscar
        '''
        self.pisca = False
        
