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
    for i in ciag.split(" "):
        if i in operatory:
            sztos.zlacz(i)
        else:
            sztos.push(int(i))
    return sztos.stack[0]
operatory = ['+', '-', '*', '/']
sztos = Stack()
print(ONP("22 5 +",operatory,sztos))






