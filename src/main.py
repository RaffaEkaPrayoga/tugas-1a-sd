from input.data_mahasiswa import data_mahasiswa
from model.linked_list import LinkedList
from struktur_data.stack import Stack
from struktur_data.queue import Queue
from struktur_data.hash_table import HashTable


# 1. ARRAY / LIST
print("=== DATA MAHASISWA (ARRAY/LIST) ===")
for mahasiswa in data_mahasiswa:
    mahasiswa.tampilkan()

# 2. LINKED LIST
daftar_dinamis = LinkedList()

daftar_dinamis.tambah("12550110330", "Siti")
daftar_dinamis.tambah("12550110331", "Doni")

print("\n=== DATA DINAMIS (LINKED LIST) ===")
daftar_dinamis.tampilkan()

print("\nMenghapus mahasiswa dengan NIM 12550110330...")
daftar_dinamis.hapus("12550110330")
daftar_dinamis.tampilkan()


# 3. STACK - UNDO
undo_stack = Stack()

undo_stack.push("Menambahkan data Raffa")
undo_stack.push("Mengubah data Andi")
undo_stack.push("Menghapus data Budi")

print("\n=== FITUR UNDO (STACK) ===")
print("Aktivitas terakhir:", undo_stack.peek())

aktivitas_terakhir = undo_stack.pop()

print("Undo dilakukan:", aktivitas_terakhir)
print("Sisa aktivitas:", end=" ")
undo_stack.tampilkan()


# 4. QUEUE - ANTREAN
antrian = Queue()

antrian.enqueue("Raffa")
antrian.enqueue("Andi")
antrian.enqueue("Budi")

print("\n=== ANTREAN MAHASISWA (QUEUE) ===")
print("Antrean:", end=" ")
antrian.tampilkan()

mahasiswa_diproses = antrian.dequeue()

print("Mahasiswa yang diproses:", mahasiswa_diproses)
print("Sisa antrean:", end=" ")
antrian.tampilkan()


# 5. HASH TABLE
data_mahasiswa = HashTable()

data_mahasiswa.tambah("12550110327", "Raffa")
data_mahasiswa.tambah("12550110328", "Andi")
data_mahasiswa.tambah("12550110329", "Budi")

print("\n=== PENCARIAN MAHASISWA (HASH TABLE) ===")

nim_dicari = "12550110327"

hasil = data_mahasiswa.cari(nim_dicari)

if hasil:
    print("Data ditemukan:", hasil)
else:
    print("Data mahasiswa tidak ditemukan.")