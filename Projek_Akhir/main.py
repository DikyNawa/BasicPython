import smtplib
import getpass
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


while True: 
    print("Program Mengirim Email Otomatis")
    print("===============================")
    print("1.Kirim Email Biasa")
    print("2.Kirim Email Dengan Lampiran")
    print("3.Keluar")

    menu = input("Input Menu Pilihan Anda = ")

    if menu == '1':
        # create message object instance
        msg = MIMEMultipart()
        # setup the parameters of the message
        msg['From'] = input(str("Masukkan email anda : "))
        password = getpass.getpass("Masukan password email anda: ")
        msg['Subject'] = input(str("Tuliskan Subjek Email : "))
        message = input(str("Tuliskan Isi Email : "))

        #penerima email
        with open('receiver_list.txt','r') as filex:
            penerima = filex.readlines()

        j=1

        for i in range(len(penerima)):
            receiver = f"{penerima[i]}"                 
            msg['To'] = receiver
            # attach message to body
            msg.attach(MIMEText(message, 'plain'))
        
            try: 
                # create server
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(msg['From'], password)
                server.sendmail(msg['From'], receiver, msg.as_string())
                server.quit()
                print("==========================")
                print("Email " + str(j) +" berhasil terkirim!")
                print("==========================")
            except Exception as exception:
                print("Error: %s!\n\n" % exception)
            j+=1
    
    elif menu == '2':
        # create message object instance
        msg = MIMEMultipart()
        # setup the parameters of the message
        msg['From'] = input(str("Masukkan email anda : "))
        password = getpass.getpass("Masukan password email anda: ")
        #msg['To'] = input(str("Masukkan email tujuan : "))
        msg['Subject'] = input(str("Tuliskan Subjek Email : "))
        message = input(str("Tuliskan Isi Email : "))


        #penerima email
        with open('receiver_list.txt','r') as filex:
            penerima = filex.readlines()


        #lampiran
        dir = input("Path direktori dimana file anda berada (Gunakan Absolute Path) : ")
        os.chdir(dir)
        nama_file = input("Masukkan nama file beserta format  : ")
        file_attach = MIMEApplication(open(nama_file,'rb').read())
        file_attach.add_header('Content-Disposition', 'attachment', filename=nama_file)
        msg.attach(file_attach)
        
        j=1

        for i in range(len(penerima)):
            receiver = f"{penerima[i]}"                 
            msg['To'] = receiver
            # attach message to body
            msg.attach(MIMEText(message, 'plain'))


            try:          
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(msg['From'], password)
                text = msg.as_string()
                server.sendmail(msg['From'], receiver, msg.as_string())
                server.quit()
                print("Email berhasil terkirim!")
                print("========================")
            except Exception as exception:
                print("Error: %s!\n\n" % exception)

    elif menu == '3':
        print("===========================================================")
        print("Terima kasih telah menggunakan layanan ini, Sampai Jumpa!!!")
        print("===========================================================")
        break
    else:
        print("===================")
        print("Menu tidak tersedia")
        print("===================")