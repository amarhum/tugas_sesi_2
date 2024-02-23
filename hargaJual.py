jumlahBeli = int(input("berapa kilo yang anda beli : "))
if jumlahBeli <= 2 :
    totalHarga = jumlahBeli * 20_000
elif jumlahBeli <=5 :
    totalHarga = jumlahBeli *18_000
elif jumlahBeli > 5 :
    totalHarga = jumlahBeli * 16_000

print("total yang harus di bayar Rp.",totalHarga )
