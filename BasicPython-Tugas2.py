import collections

ulang = True

semua_contact = []  

while(ulang == True):
    print("---Menu---")
    print("1.Daftar Kontak")
    print("2.Tambah Kontak")
    print("3.Keluar")
    userInput = int(input("Please select an option: "))

    if(userInput == 1):
        print("Daftar Kontak:")
        for i in semua_contact:
            print("Nama : ",i['name'])
            print("No Telepon : ",i['phone'])
    elif(userInput == 2):
        contact = collections.OrderedDict()
        contact['name'] = input("Enter name: ")
        contact['phone'] = input("Enter phone: ")
        semua_contact.append(contact)
    elif(userInput == 3):
        print("Program selesai, sampai jumpa!")
        break