def array(kal) :
    konsonan="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnopqrstvwxyz"
    vokal="AIUEOaiueo"
    jumlahvokal=""
    jumlahkonsonan=""
    for karakter in kal:
        if karakter in vokal:
            jumlahvokal+=karakter
        if karakter in konsonan:
            jumlahkonsonan+=karakter
        totalhuruf=jumlahvokal+jumlahkonsonan
    print ("Jumlah Banyaknya Huruf Vokal :")
    print (jumlahvokal)
    print ("Jumlah banyaknya huruf Konsonan :")
    print (jumlahkonsonan)
    print ("Total Huruf :")
    print (totalhuruf)
    print ("Setiap Huruf Dalam Kalimat :")
    print (kal)

#main
    print ('\nProgram Kumpulan Huruf Menjadi Sebuah Tulisan\n')
    kal=input("Masukkan Kalimat :")
    array(kal)
