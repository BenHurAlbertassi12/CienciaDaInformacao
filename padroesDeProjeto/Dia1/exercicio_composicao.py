class Ventilador:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__tensao = tensao
        self.__ligado = False

    def cor(self):
        return self.__cor


class Batedeira:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__tensao = tensao
        self.__ligado = False

    def cor(self):
        return self.__cor


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.ventilador = None

    def comprar_ventilador(self, ventilador):
        if ventilador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= ventilador.preco
            self.ventilador = ventilador

    def comprar_batedeira(self, batedeira):
        if batedeira.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= batedeira.preco
            self.batedeira = batedeira

    def __str__(self):
        if (self.ventilador or self.batedeira):
            return f"{self.nome} - possui um novo produt."
        return f"{self.nome} - não possui um novo produto."


ventilador_branco = Ventilador("branco", potencia=250, tensao=220, preco=100)
pessoa = Pessoa("Maria", saldo_na_conta=2000)
pessoa.comprar_ventilador(ventilador_branco)


ventilador_branco = Batedeira("pink", potencia=240, tensao=110, preco=2250)
pessoa = Pessoa("Pedro", saldo_na_conta=5000)
pessoa.comprar_ventilador(ventilador_branco)

ventilador_branco = Batedeira("preta", potencia=1100, tensao=110, preco=6250)
pessoa = Pessoa("Betinho", saldo_na_conta=10000)
pessoa.comprar_ventilador(ventilador_branco)

print(pessoa)
