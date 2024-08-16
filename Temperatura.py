class Carro:
	def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

	def acelerar(self):
        print(f"O {self.modelo} está acelerando.")

	def frear(self):
        print(f"O {self.modelo} está freando.")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.acelerar()  # Saída: O Corolla está acelerando.