class contasalario:
    def __init__(self,cliente, numeroconta, saldo):
        self.__cliente = cliente
        self.__numeroconta = numeroconta
        self.__saldo = saldo
    def mostrarsaldo(self,quantia):
        print("Saldo anterior:", self._contasalario__saldo)

class contacorrente(contasalario):
    def __init__(self,cliente, numeroconta, saldo):
        super().__init__(cliente, numeroconta, saldo)
    def transferir(self,quantia):
        print("Saldo anterior:", self._contasalario__saldo)
        self._contasalario__saldo -= quantia
        print("Novo saldo:", self._contasalario__saldo)

    
conta1 = contasalario("maycon", 10238590358, 7000)
conta2 = contacorrente("cris", 490582905682, 5000)
# print(conta1.__cliente)
# print(conta1.numero)
# print(conta1.saldo)
# print(conta2.cliente)
# print(conta2.numero)
# print(conta2.saldo)

conta2.transferir(100)