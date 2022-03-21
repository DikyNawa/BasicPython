ujian_teori = int(input("Berapa nilai ujian teori? "))
ujian_praktek = int(input("Berapa nilai ujian praktek? "))

if ujian_teori >=70 and ujian_praktek >= 70:
    print("Selamat, anda lulus!")
elif ujian_teori >=70 and ujian_praktek < 70:
    print("Anda harus mengulang ujian praktek")
elif ujian_teori < 70 and ujian_praktek >= 70:
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")

