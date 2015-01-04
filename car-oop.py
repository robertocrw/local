class car:
	def __init__(self,gasolina):
		     self.gasolina = gasolina
	def arrancar(self):
	     if self.gasolina > 0:
	         print('Arrancar')
	     else: 
	         print('Não liga')
	def conduzir(self):
	     if self.gasolina > 0: 
	         self.gasolina -= 1
	         print('Menos %i litros de gasolina' %(self.gasolina))
	     else:
	         print('Acabou o combustivel')

opala = car(3)
opala.arrancar()
opala.conduzir()
opala.arrancar()
opala.conduzir()
opala.arrancar()
opala.conduzir()
opala.arrancar()
opala.conduzir()	                                 	
