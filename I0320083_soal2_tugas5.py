# Program Grading Nilai

# input data
nama = str(input("Silahkan tulis nama Anda :"))
nilai = float(input("Silahkan tulis nilai Anda :"))

# output nilai
if 100 >= nilai >= 85:
    print("Halo, "+nama+" ! Nilai Anda setelah dikonversi adalah A")
elif 85 > nilai >= 80:
    print("Halo, "+nama+" ! Nilai Anda setelah dikonversi adalah A-")
elif 80 > nilai >= 75:
    print("Halo, "+nama+" ! Nilai Anda setelah dikonversi adalah B+")
elif 75 > nilai >= 70:
    print("Halo, "+nama+" ! Nilai Anda setelah dikonversi adalah B")
elif 70 > nilai >= 65:
    print("Halo, "+nama+" ! Nilai Anda setelah dikonversi adalah C+")
elif 65 > nilai >= 60:
    print("Halo, "+nama+" ! Nilai Anda setelah dikonversi adalah C")
elif 60 > nilai >= 0:
    print("Halo, "+nama+" ! Nilai Anda setelah dikonversi adalah E")
else:
    print("Maaf, "+nama+" Nilai yang Anda sebutkan tidak valid untuk dikonversi")
