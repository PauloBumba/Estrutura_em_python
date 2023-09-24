class Queue():
    top = -1
    Fifo = [None]*100

    def IsEmpty(self):
        if (self.top < 0):
            print("A fila está vazia")
            return True

    def Dequeu(self, inserir):
        if (self.top > len(self.Fifo)):
            print("Não podemos inserir elemento na fila, chegou ao seu limite")
            return False
        self.top += 1
        self.Fifo[self.top] = inserir
        return inserir

    def Enqueue(self):
        if (self.top < 0):
            print("A fila está vazia")
            return False
        valor = self.Fifo[0]
        for i in range(1, self.top):
            self.Fifo[i - 1] = self.Fifo[i]

        self.top-= 1

        return valor

    def Peek(self):
        if (self.top < 0):
            print("A fila está vazia")
            return False
        print(f"O primeiro elemento da fila é [{self.Fifo[0]}]")

    def Print(self):
        b = 0
        for c in range(b, self.top+1, +1):
            print(self.Fifo[c])
            
v=Queue()
v.Dequeu("paulo")
v.Dequeu("mario")
v.Dequeu("valente")


v.Print()
v.Peek()
v.Enqueue()
v.Peek()
print()
v.Print()

        
        