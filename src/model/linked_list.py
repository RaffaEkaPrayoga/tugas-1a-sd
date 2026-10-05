class Node:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, nim, nama):
        node_baru = Node(nim, nama)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node_baru

    def hapus(self, nim):
        current = self.head
        previous = None

        while current:
            if current.nim == nim:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                return True

            previous = current
            current = current.next

        return False

    def tampilkan(self):
        current = self.head

        while current:
            print(current.nim, "-", current.nama)
            current = current.next