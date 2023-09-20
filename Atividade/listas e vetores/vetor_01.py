import numpy as np
class Num:
    def Tratamento(self, vetor):
        self.vetor = vetor
        self.vetor = np.arange(0, 100, 20)
        return self.vetor
    
    def Soma(self, soma):
        self.soma
        for c in self.vetor:
            self.soma += c
        return self.soma
    
    def Media(self):
        a = len(self.vetor)
        media = self.soma / a
        return media

b = Num()
vetor = ()
soma = 0
Print("==============================================================")
vetor = b.Tratamento(vetor)
soma = b.Soma(soma)
media = b.Media()
print("Vetor:", vetor)
print("Soma:", soma)
print("Média:", media)
