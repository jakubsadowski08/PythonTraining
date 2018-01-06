class Node:
    def __init__(self, nazwisko, punkty):
        self.nazwisko = nazwisko
        self.punkty = punkty
        self.previous = None
        self.next = None

class Listeczka:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def add_beggining(self, nazwisko, punkty):
        if self.head == None:
            n = Node(nazwisko, punkty)
            self.head = n
            self.tail = n
            n.next = None
            n.previous = None
            self.size = 1
        else:
            n = Node(nazwisko, punkty)
            n.next = self.head
            self.head.previous = n
            self.head = n
            self.head.previous = None
            self.size = self.size + 1


    def add_end(self, nazwisko, punkty):
        if self.tail is None:
            n = Node(nazwisko, punkty)
            self.tail = n
            self.head = n
            n.next = None
            n.previous = None
            self.size = 1
        else:
            n = Node(nazwisko, punkty)
            n.previous = self.tail
            self.tail.next = n
            self.tail = n
            self.tail.next = None
            self.size = self.size + 1


    def add_position(self, nazwisko, punkty, pozycja):
        if (self.size / 2) - pozycja >= 0:
            tmp = self.head
            x = 2
            while x != pozycja:
                tmp = tmp.next
                x = x + 1
            n = Node(nazwisko, punkty)
            n.next = tmp.next
            n.previous = tmp
            tmp.next.previous = n
            tmp.next = n


        else:
            tmp = self.tail
            x = self.size
            while x != pozycja - 1:
                tmp = tmp.previous
                x = x - 1
            n = Node(nazwisko, punkty)
            n.next = tmp.next
            n.previous = tmp
            tmp.next.previous = n
            tmp.next = n
        self.size = self.size + 1


    def printuj_beggining(self):
        n = self.head
        while n != None:
            print(n.nazwisko + str(n.punkty))
            n = n.next

    def printuj_end(self):
        n = self.tail
        while n != None:
            print(n.nazwisko + str(n.punkty))
            n = n.previous

    def delete_end(self):
        self.tail = self.tail.previous
        self.tail.next.previous = None
        self.tail.next = None

    def delete_beggining(self):
        self.head = self.head.next
        self.head.previous.next = None
        self.head.previous = None

    def znajdz(self):
        n = self.head
        max = n.punkty
        while n != None:
            if (max < n.punkty):
                max = n.punkty
            n = n.next
        return max

ll = Listeczka()
ll.add_beggining("Jakub ", 5)
ll.add_beggining("Szymon ", 15)
ll.add_end("Kamil ", 123)
ll.add_end("maciej ", 12)
ll.add_beggining("Szymon ", 15)
ll.add_position("POZYCJA ", 25, 2)
ll.add_position("POZYCJA_optymalna ", 2, 2)
ll.delete_end()
ll.delete_beggining()
ll.printuj_beggining()
print(ll.znajdz())

