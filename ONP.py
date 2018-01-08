class Stack:
    def __init__(self):
        self.stack = []
    def push(self,a):
        self.stack.append(a)
    def pop(self):
        self.stack.pop(len(self.stack)-1)
    def wyswietl(self):
        print(self.stack)
    def zlacz(self,operator):
        x = len(self.stack)-2
        if operator =='+':
            self.stack[x] = self.stack[x] + self.stack[x + 1]
            self.pop()
        elif operator =='-':
            self.stack[x] = self.stack[x] - self.stack[x + 1]
            self.pop()
        elif operator =='*':
            self.stack[x] = self.stack[x] * self.stack[x + 1]
            self.pop()
        elif operator =='/':
            self.stack[x] = self.stack[x] / self.stack[x + 1]
            self.pop()
def ONP(ciag, operatory,sztos):
    for i in ciag:
        if i in operatory:
            sztos.zlacz(i)
        elif i ==" ":
            continue
        else:
            sztos.push(int(i))
operatory = ['+', '-', '*', '/']
sztos = Stack()
ONP("2 2 + 5 *",operatory,sztos)
print(sztos.stack)






