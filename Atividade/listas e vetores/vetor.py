from random import randint

class Vetor:


    def tratamento(self,vetor):
        self.vetor = vetor
        for c in range(100):
            a = randint(1,10)
            vetor.append(a)

    def visualizacao(self):
    
        for c,j in enumerate(self.vetor):
            print(f" na posicçao {c} temos {j}")
    def Maior(self):
        self.vetor
        maior=vetor[0]
        menor=vetor[0]
        for a in vetor:
            if a>maior:
                maior=a
            if a<menor:
                menor=a
        print(f"menor :{menor}")
        print(f"maior :{maior}")




v = Vetor()
vetor = []
v.tratamento(vetor)
v.visualizacao()
v.Maior()
