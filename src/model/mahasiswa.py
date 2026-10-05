class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def tampilkan(self):
        print(self.nim, "-", self.nama)