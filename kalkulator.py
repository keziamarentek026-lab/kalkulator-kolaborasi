def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: tidak bisa membagi dengan nol!"
    return a / b

while True:
    print("\n=== KALKULATOR SEDERHANA ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

pilihan = input("Pilih operasi (1/2/3/4/5): ")

if pilihan == "5":
    print("Terima kasih, program selesai.")

if pilihan not in ["1", "2", "3", "4"]:
    print("Pilihan tidak valid!")

if pilihan == "1":
    hasil = tambah(angka1, angka2)
    print("Hasil:", hasil)
elif pilihan == "2":
    hasil = kurang(angka1, angka2)
    print("Hasil:", hasil)
elif pilihan == "3":
    hasil = kali(angka1, angka2)
    print("Hasil:", hasil)
elif pilihan == "4":
    hasil = bagi(angka1, angka2)
    print("Hasil:", hasil)