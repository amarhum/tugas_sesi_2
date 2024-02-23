nilaiMtk = float(input("masukan nilai MTK : "))
nilaiEnglish = float(input("masukan nilai ENGLISH : "))
nilaiIndo = float(input("masukan nilai INDO : "))
nilaiIpa = float(input("masukan nilai IPA : "))
nilaiIps = float(input("masukan nilai IPS : "))

A = nilaiEnglish + nilaiIndo + nilaiMtk / 3
B = nilaiEnglish + nilaiIndo + nilaiMtk + nilaiIpa + nilaiIps /5

if A >= 75 :
    print ("anda lulus")
elif B >= 70 :
    print("anda lulus")
elif (nilaiMtk and nilaiEnglish)>90 :
    print("anda lulus")
else:
    print("yahhhh coba lagi")