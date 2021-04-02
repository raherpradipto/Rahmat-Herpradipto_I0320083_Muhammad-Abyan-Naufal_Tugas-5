# Program Sederhana Penyapa Pengunjung Hotel

print("Hotel Raher Castle")

# input data pengunjung
nama = str(input("Silahkan tulis nama Anda :"))
jenis_kelamin = input("Silahkan tulis jenis kelamin Anda : [L/P]")

# output ucapan selamat datang
if jenis_kelamin == "L":
    print("Selamat Datang di Raher Castle, Brother"+nama+"!")
elif jenis_kelamin == "P":
    print("Selamat Datang di Raher Castle, Sister"+nama+"!")
else:
    pass
