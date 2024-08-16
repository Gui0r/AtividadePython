
class Carro:
	def __init__(self, marca):
        self.__marca = marca

	def get_marca(self):
		return self.__marca
 
class Carro:
	def __init__(self, marca):
    	self.__marca = marca

	def set_marca(self, marca):
    	self.__marca = marca

class Calculadora:
	def __init__(self):
    	self._resultado = 0

	def somar(self, valor):
    	self._resultado += valor

	def subtrair(self, valor):
    	self._resultado -= valor

	def multiplicar(self, valor):
    	self._resultado *= valor

	def dividir(self, valor):
    	if valor != 0:
        	self._resultado /= valor
    	else:
        	print("Erro: Divisão por zero não é permitida.")

	def get_resultado(self):
    	return self._resultado

	def reset(self):
    	self._resultado = 0



