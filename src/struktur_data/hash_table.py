class HashTable:
    def __init__(self):
        self.data = {}

    def tambah(self, nim, nama):
        self.data[nim] = nama

    def cari(self, nim):
        return self.data.get(nim)

    def tampilkan(self):
        print(self.data)