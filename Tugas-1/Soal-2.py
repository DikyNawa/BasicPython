from cmath import pi


phi = 22/7
r = int(input("Masukkan jari-jari lingkaran : "))
luas_lingkaran = phi * r * r

print("Luas lingkaran dengan jari-jari " + str(r) + " cm adalah " + "{:.2f}".format(luas_lingkaran) + " cm\u00b2")