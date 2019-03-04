year=int(input("Masukkan Tahun untuk mengetahui kabisat atau tidak:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("Tahun tersebut Kabisat!")
else:
    print("Tahun Tersebut Bukan Kabisat!")

