class Stack():
    top = -1
    pilha = [None]*100

    def IsEmpty(self):
        if (self.top < 0):
            print("A pilha está vazia")
            return True
        print(f"a pilha contém elemento {(self.top)} ")

    def Push(self, inserir):
        if (self.top > len(self.pilha)):
            print("Pilha cheia")
        self.top += 1
        self.pilha[self.top] = inserir
        return

    def Pop(self):
        if (self.top < 0):
            print("A pilha está vazia, não podemos eliminar")
            return False
        valor = self.pilha[self.top]
        self.top -= 1
        return valor

    def Peek(self):
        print(f"O topo da pilha é {self.pilha[self.top]}")

    def Print(self):
        b = -1
        for c in range(self.top, b, -1):
            print(f"Elemento da pilha [{self.pilha[c]}]")
        print()

v=Stack()
v.Push("paulo")
v.Push("mario")
v.Push("valente")
v.Push(1)

v.IsEmpty()
v.Print()
v.Peek()
