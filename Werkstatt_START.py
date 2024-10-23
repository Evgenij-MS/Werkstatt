# Import Module
import _tkinter
import io
import os
import sys
import PIL
import calendar
from tkinter import *
from tkinter import filedialog
import time
import calendar
import numpy as np
import itertools
import smtplib as email
import locale
from PIL import Image, ImageTk, ImageDraw, ImageFont
from PIL import Image, ImageTk
import scanny
from tempfile import TemporaryFile
from itertools import cycle

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from ftplib import *
import img2pdf
import imageio

import winsound
import subprocess


# Create Object
root = Tk()

#############################################################################
#     cd C:\Users\User\AppData\Local\Programs\Python\Python311\Scripts\		#
#	  cd C:\Users\malja\AppData\Roaming\Python\Python312\Scripts			#
#																			#
#																			#
#     pyinstaller --onefile D:\Python\Werkstatt_FINALLY3_2.0.py				#
#	  pyinstaller --onefile F:\Python\Werkstatt_FINALLY3_2.0.py				#
#############################################################################

from pathlib import Path
import pytesseract

path_sys = os.getcwd()  ### os.path.abspath(sys.argv[0])
print(os.getcwd())

path_ord_bilder = os.listdir(f"{path_sys}/Werkstatt_Images")  ###  Zeigt alle Dateienin Ordner
Bild_List = path_ord_bilder
Bild_List_X = IntVar()

##################################   Bild Grün Bibliothek  #######################################
Bild_Green_Bibliothek = {}
path_liste_images = os.listdir("{}/Aufträge".format(path_sys))  ###  Zeigt alle Dateienin Ordner
Liste_Images = []

for i in path_liste_images:
    path_dir_images_Auftrag = os.listdir("{}/Aufträge/{}".format(path_sys, i))
    print(i, path_dir_images_Auftrag)
    Len_Images_List = len(path_dir_images_Auftrag)
    for j in range(Len_Images_List):
        List_Img = list(path_dir_images_Auftrag[j])
        lps = List_Img[-5]
        print()
        Liste_Images.append(lps)
    Bild_Green_Bibliothek[i] = [path_dir_images_Auftrag, Liste_Images]
    Liste_Images = []

print(Bild_Green_Bibliothek)
# exit()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# path_sys = path_sys.split()
# path_system = (list(path_sys[0]))
# path_sys = path_system[0] + path_system[1]
# print(path_sys)

Len_Aufträge = IntVar()
Jahr_Monat_Tag = str(time.strftime("%d.%m."))
Monat = str(time.strftime("%m."))
Jahr_Monat = str(time.strftime("%d %m %Y"))
Jahr_Monat = Jahr_Monat.split()

print('Tag_Monat:   ', Jahr_Monat)
Mon = Jahr_Monat[1]

Kalender_Tag = IntVar()
Kalender_Tag.set(Mon)
Image_Saved = BooleanVar()
saved = False
one_on_start_1 = True
one_on_start_2 = True
one_on_start_3 = True
Arbeitsnachweis_Nr = IntVar()
Time = StringVar()
File_Import = StringVar()
Email_Adress = ''
Email_Adress_2 = ''
text = open('textdatei.txt', 'r')
n_add = text.read()
text.close()
Name_Email = ''
Name_Email_2 = ''

Bild_Green = True
Zeit_add_On = False
Heute_Var = StringVar()

scaner_counter = 0
try:
    os.remove('Arbeitsnachweis_HANSE_To_PDF.png')
except FileNotFoundError:
    pass


def pdf_from_image():
    global n_add, text
    n_add = int(n_add) + 1
    pdf_data = img2pdf.convert(r'{}\Auftrag_Image.jpg'.format(path_sys))
    with open("Arbeitsnachweis_Nr_0{}.pdf".format(n_add), "wb") as file:
        file.write(pdf_data)
        os.startfile("D:Arbeitsnachweis_Nr_0{}.pdf".format(n_add))
        time.sleep(0.5)
    os.remove('textdatei.txt')
    text = open('textdatei.txt', 'w')
    n_add = '0' + str(n_add)
    text.write(str(n_add))
    text.close()
    message('PDF-Datei ist ERSTELLT', 30)
    # Pfad zur PDF-Datei, die Sie öffnen möchten
    pdf_datei = '{}Arbeitsnachweis_Nr_0{}.pdf'.format(path_sys, n_add)
    # Öffnen der PDF-Datei mit dem Standard-PDF-Viewer des Systems
    file.close()


try:
    img_org_1 = Image.open(r'{}\Arbeitsnachweis.jpg'.format(path_sys))
except FileNotFoundError:
    pass


def pdf_from_image_2():
    pdf_data = img2pdf.convert(r'{}Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys))
    with open("Arbeitsnachweis_HANSE.pdf", "wb") as file:
        file.write(pdf_data)
    file.close()
    message('PDF-Datei ist ERSTELLT', 30)


def scanner():
    global nw, Image_Opened
    nw, = select_1.curselection()
    Aktuell, = select_1.get(nw, nw)
    if os.path.exists(r'{}Aufträge\{}'.format(path_sys, Number.get())):
        scanny.StartScan(Path=r'{}Aufträge\{}'.format(path_sys, Number.get()), ImageName='Bild_{}_{}'.format(Aktuell,
                                                                                                             bild_nr))  # 'r'{}\Aufträge\{}\bild_{}_{}.jpg'.format(path_sys, Number.get(), Auftrags_Liste_Aktuell, bild_nr))
    else:
        os.makedirs(r'{}Aufträge\{}'.format(path_sys, Number.get()))
        scanny.StartScan(Path=r'{}\Aufträge\{}'.format(path_sys, Number.get()),
                         ImageName='Bild_{}_{}'.format(Aktuell, bild_nr))
    image1 = Image.open(r'{}Aufträge\{}\Bild_{}_{}.png'.format(path_sys, Number.get(), Aktuell, bild_nr))
    image1 = image1.resize((320, 500))
    image1.save(r'{}Aufträge\{}\Bild_{}_{}.jpg'.format(path_sys, Number.get(), Aktuell, bild_nr))
    os.remove(r'{}Aufträge\{}\Bild_{}_{}.png'.format(path_sys, Number.get(), Aktuell, bild_nr))
    screen_image(bild_nr)


def scanner_2():
    scanny.StartScan(Path='{}'.format(path_sys), ImageName='Arbeitsnachweis_HANSE_To_PDF')
    dokument_2()


def scanner_3():
    try:
        os.remove(r'{}\Bild_Scan.jpg'.format(path_sys))
        os.remove(r'{}\Bild_Scan.png'.format(path_sys))
    except FileNotFoundError:
        pass
    scanny.StartScan(Path='{}'.format(path_sys), ImageName='Bild_Scan')
    image1 = Image.open(r'{}\Bild_Scan.png'.format(path_sys))
    image1.save(r'{}\Bild_Scan.jpg'.format(path_sys))
    Print()


def Print():
    img_scan = Image.open(r'{}\Bild_Scan.jpg'.format(path_sys))
    text = pytesseract.image_to_string(img_scan)
    text2 = Text(root, height=38, width=67)
    scroll = Scrollbar(root, command=text2.yview)
    text2.configure(yscrollcommand=scroll.set)
    text2.tag_configure('bold_italics', font=('Arial', 9, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 11, 'bold'))
    text2.tag_configure('color', foreground='#476042',
                        font=('Tempus Sans ITC', 9, 'bold'))
    quote = text
    text2.insert(END, quote, 'color')
    text2.insert(END, 'follow-up\n', 'follow')
    text2.place(x=1250, y=140)
    scroll.place(x=1250, y=140)

########################################################################################################################
########################################################################################################################

def E_Mail_Bestellung():
    global n_add, Number
    # Serverdaten
    smtpServer = 'smtp.gmail.com'  # "smtp.web.de"
    smtpPort = 587

    # Zugangsdaten
    username = "maljaseugen@gmail.com"
    password = "cwle qmwj lsim hosy"

    # Sender & Empfänger
    sender = "maljaseugen@gmail.com"
    reciever = Email_Adress

    # Betreff
    subject = '{}'.format(address_1.get(1.0, "end-1c"))
    body = '{}'.format(address_2.get(1.0, "end-1c"))

    body_html_1 = "<html><body>"
    body_html_2 = """<p><b>{}</b></p>
    <p>{}</p>
    <p><b>{}</b></p>
    <p>{}</p>
    <p><b>{}</b></p>
    <p>{}</p>
    <p><b>{}</b></p>
    <p>{}</p>
    <p><b>{}</b></p>
    <p>{}</p>
    <p><b>{}</b></p>
    <p>{}</p>
    <p><b>{}</b></p>
    <p>{}</p>
    <p><b>{}</b></p>
    <p>{}</p>
    <p><b>{}</b></p>
    <p>{}</p>
    <p><b>{}</b></p>
    <p>{}</p>
    """.format(str(select_2.get(0)), str(select_2.get(1)), str(select_2.get(2)), str(select_2.get(3)),
        str(select_2.get(4)), str(select_2.get(5)), str(select_2.get(6)), str(select_2.get(7)),
        str(select_2.get(8)), str(select_2.get(9)), str(select_2.get(10)), str(select_2.get(11)),
        str(select_2.get(12)), str(select_2.get(13)), str(select_2.get(14)), str(select_2.get(15)),
        str(select_2.get(16)), str(select_2.get(17)), str(select_2.get(18)), str(select_2.get(19)), str(select_2.get(20)))

    body_html_3 = """
    <div style='background-color:black'>
    <p></p>
    <p>Bitte die bestellte Waren an die Adresse von HKW Tiefstack zu liefern.</p>
    <p></p>
    <p>Senden Sie bitte das Angebot an meinen Vorgesetzten Anis Gana Hanse GM.</p>
    <p>Danke für die Mitarbeit.</p>
    <p>Mit freundlichen Grüßen</p>
    <p>Eugen Maljas</p>
    </div>
    """
    body_html_4 = "</body></html>"
    body_html = body_html_1 + body_html_2 + body_html_3 + body_html_4  # + body_html_5

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciever

    part = MIMEText(body, 'plain')
    msg.attach(part)

    html_part = MIMEText(body_html, 'html')
    msg.attach(html_part)
    message('Das email wurde erfolgreich gesendet', 30)

    # Erzeugen einer Mail Session
    smtpObj = smtplib.SMTP(smtpServer, smtpPort)
    # Debuginformationen auf der Konsole ausgeben
    smtpObj.set_debuglevel(1)
    # Wenn der Server eine Authentifizierung benötigt dann...
    smtpObj.starttls()
    smtpObj.login(username, password)

    # absenden der E-Mail
    smtpObj.sendmail(sender, reciever, msg.as_string())
    message('E-Mail wurde ERFOLGREICH versendet', 30)


def E_Mail_text_send():
    global n_add, Number
    # Serverdaten
    smtpServer = 'smtp.gmail.com'  # "smtp.web.de"
    smtpPort = 587

    # Zugangsdaten
    username = "maljaseugen@gmail.com"
    password = "cwle qmwj lsim hosy"

    # Sender & Empfänger
    sender = "maljaseugen@gmail.com"
    reciever = Email_Adress

    # Betreff
    subject = '{}'.format(address_1.get(1.0, "end-1c"))
    body = '{}'.format(address_2.get(1.0, "end-1c"))

    body_html_1 = "<html><body>"
    body_html_2 = "<p><b>{}</b></p>".format(str(select_2.get(END)))
    body_html = body_html_1 + body_html_2  # + body_html_3 + body_html_4 + body_html_5

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciever

    part = MIMEText(body, 'plain')
    msg.attach(part)

    html_part = MIMEText(body_html, 'html')
    msg.attach(html_part)
    message('Das email wurde erfolgreich gesendet', 30)

    # Erzeugen einer Mail Session
    smtpObj = smtplib.SMTP(smtpServer, smtpPort)
    # Debuginformationen auf der Konsole ausgeben
    smtpObj.set_debuglevel(1)
    # Wenn der Server eine Authentifizierung benötigt dann...
    smtpObj.starttls()
    smtpObj.login(username, password)

    # absenden der E-Mail
    smtpObj.sendmail(sender, reciever, msg.as_string())
    message('E-Mail wurde ERFOLGREICH versendet', 30)


def E_Mail_image_send():
    global n_add, Number, nw
    # Serverdaten
    smtpServer = 'smtp.gmail.com'
    smtpPort = 587

    # Zugangsdaten
    username = "maljaseugen@gmail.com"
    password = "cwle qmwj lsim hosy"

    # Sender & Empfänger
    sender = "maljaseugen@gmail.com"
    reciever = Email_Adress

    # Betreff
    subject = 'Bestellung von Material'
    body = '{}'.format(str(address_1.get(0, END)))

    body_html_1 = "<html><body>"
    body_html_2 = "<p><b>{}</b></p>".format(str(address_2.get(0, END)))

    body_html = body_html_1 + body_html_2  # + body_html_3 + body_html_4 + body_html_5

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciever

    part = MIMEText(body, 'plain')
    msg.attach(part)

    html_part = MIMEText(body_html, 'html')
    msg.attach(html_part)

    #####################################   FILE to SEND   #########################################
    nw, = select_1.curselection()
    Auftrags_Liste_Aktuell, = select_1.get(nw, nw)
    filename = r'{}\Werkstatt_Images\bild_{}_{}.jpg'.format(path_sys, Auftrags_Liste_Aktuell, bild_nr)
    file_part = MIMEBase('application', "octet-stream")
    file_part.set_payload(open(filename, "rb").read())
    encoders.encode_base64(file_part)
    file_part.add_header('Content-Disposition', 'attachment; filename="' + filename + '"')
    msg.attach(file_part)
    ################################################################################################

    # Erzeugen einer Mail Session
    smtpObj = smtplib.SMTP(smtpServer, smtpPort)
    # Debuginformationen auf der Konsole ausgeben
    smtpObj.set_debuglevel(1)
    # Wenn der Server eine Authentifizierung benötigt dann...
    smtpObj.starttls()
    smtpObj.login(username, password)

    # absenden der E-Mail
    smtpObj.sendmail(sender, reciever, msg.as_string())
    message('E-Mail wurde mit Bild versendet', 30)


def E_Mail():
    global n_add, Number
    # Serverdaten
    smtpServer = 'smtp.gmail.com'
    smtpPort = 587

    # Zugangsdaten
    username = "maljaseugen@gmail.com"
    password = "cwle qmwj lsim hosy"

    # Sender & Empfänger
    sender = "maljaseugen@gmail.com"
    reciever = Email_Adress

    # Betreff
    subject = "Moin {}!".format(Name_Email)
    body = "Hiermit folgendes steht ein Text. \n Mit einem Zeilenumbruch."

    body_html_1 = "<html><body>"
    body_html_2 = "<h1>Arbeitsnachweis</h1>"
    print(Number.get(), 'NUMBER.GET')
    body_html_3 = "<p style='color:red'>Auftragsnummer: {} </p>".format(Number.get())
    body_html_4 = "<div style='background-color:green'>Mit freundlichen Grüssen.</div>"
    body_html_5 = "</body></html>"

    body_html = body_html_1 + body_html_2 + body_html_3 + body_html_4 + body_html_5

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciever

    part = MIMEText(body, 'plain')
    msg.attach(part)

    html_part = MIMEText(body_html, 'html')
    msg.attach(html_part)

    filename = r'{}Arbeitsnachweis_Nr_{}.pdf'.format(path_sys, n_add)

    file_part = MIMEBase('application', "octet-stream")
    file_part.set_payload(open(filename, "rb").read())
    encoders.encode_base64(file_part)

    file_part.add_header('Content-Disposition', 'attachment; filename="' + filename + '"')
    msg.attach(file_part)

    # Erzeugen einer Mail Session
    smtpObj = smtplib.SMTP(smtpServer, smtpPort)
    # Debuginformationen auf der Konsole ausgeben
    smtpObj.set_debuglevel(1)
    # Wenn der Server eine Authentifizierung benötigt dann...
    smtpObj.starttls()
    smtpObj.login(username, password)

    # absenden der E-Mail
    smtpObj.sendmail(sender, reciever, msg.as_string())
    message('E-Mail wurde ERFOLGREICH versendet', 30)

    #  em040277em@gmail.com
    #  password = 'BBB0123lada9dD'
    #  okxk bjoh kbpx ocex
    #  eugen.maljas@hansegm.de
    #
    ###
    #
    #  ftp://90.186.16.117:47126
    #  Box77ineT
    #  A20d747f16
    #
    # Or connect and login as separate steps


def E_Mail_2():
    # Serverdaten
    smtpServer = 'smtp.gmail.com'
    smtpPort = 587

    # Zugangsdaten
    username = "maljaseugen@gmail.com"
    password = "cwle qmwj lsim hosy"

    # Sender & Empfänger
    sender = "maljaseugen@gmail.com"
    reciever = Email_Adress

    # Betreff
    subject = "Moin {}!".format(Name_Email)
    body = "Arbeitsnachweis in PDF."

    # body_html_1 = "<html><body>"
    # body_html_2 = "<h1>Arbeitsnachweis</h1>"
    # print(Number.get(), 'NUMBER.GET')
    # body_html_3 = "<p style='color:red'>Auftragsnummer: {} </p>".format(Number.get())
    # body_html_4 = "<div style='background-color:green'>Mit freundlichen Grüssen.</div>"
    # body_html_5 = "</body></html>"

    # body_html = body_html_1 + body_html_2 + body_html_3 + body_html_4 + body_html_5

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciever

    part = MIMEText(body, 'plain')
    msg.attach(part)

    # html_part = MIMEText(body_html, 'html')
    # msg.attach(html_part)

    filename = r'{}Arbeitsnachweis_HANSE_{}.pdf'.format(path_sys, n_add_2)

    file_part = MIMEBase('application', "octet-stream")
    file_part.set_payload(open(filename, "rb").read())
    encoders.encode_base64(file_part)

    file_part.add_header('Content-Disposition', 'attachment; filename="' + filename + '"')
    msg.attach(file_part)

    # Erzeugen einer Mail Session
    smtpObj = smtplib.SMTP(smtpServer, smtpPort)
    # Debuginformationen auf der Konsole ausgeben
    smtpObj.set_debuglevel(1)
    # Wenn der Server eine Authentifizierung benötigt dann...
    smtpObj.starttls()
    smtpObj.login(username, password)

    # absenden der E-Mail
    smtpObj.sendmail(sender, reciever, msg.as_string())
    message('E-Mail wurde ERFOLGREICH versendet', 30)

    #  em040277em@gmail.com
    #  password = 'BBB0123lada9dD'
    #  okxk bjoh kbpx ocex
    #  eugen.maljas@hansegm.de
    #
    ###  "maljaseugen@gmail.com"
    ###  "cwle qmwj lsim hosy"
    #
    #  ftp://90.186.16.117:47126
    #  Box77ineT
    #  A20d747f16
    #
    # Or connect and login as separate steps
    #
    #  Password Gmail:  cwle qmwj lsim hosy


def FTP_load():
    ftp_load = FTP()
    try:
        ftp_load.connect('90.186.164.185', 47126)
        ftp_load.login('Box77ineT', 'A20d747f16')
        ftp_load.retrlines('LIST')  # list directory contents
        ftp_load.retrbinary('RETR Werkstatt.npy', open(r'{}/Werkstatt.npy'.format(path_sys), 'wb').write)
        ftp_load.retrbinary('RETR Auto_fahrten.npy', open(r'{}/Auto_fahrten.npy'.format(path_sys), 'wb').write)
        ftp_load.retrbinary('RETR Material.npy', open(r'{}/Material.npy'.format(path_sys), 'wb').write)
        ftp_load.close()
    except TimeoutError:
        pass


def FTP_save():
    ftp_save = FTP()
    ftp_save.connect('90.186.164.185', 47126)
    ftp_save.login('Box77ineT', 'A20d747f16')
    time.sleep(1)
    with open(r'{}Werkstatt_START.py'.format(path_sys), 'rb') as image_file:
        ftp_save.storbinary(r'STOR Werkstatt_START.py', image_file)
    time.sleep(1)
    with open(r'{}Werkstatt.npy'.format(path_sys), 'rb') as image_file:
        ftp_save.storbinary(r'STOR Werkstatt.npy', image_file)
    time.sleep(1)
    with open(r'{}Auto_fahrten.npy'.format(path_sys), 'rb') as image_file:
        ftp_save.storbinary(r'STOR Auto_fahrten.npy', image_file)
    time.sleep(1)
    with open(r'{}Material.npy'.format(path_sys), 'rb') as image_file:
        ftp_save.storbinary(r'STOR Material.npy', image_file)
    time.sleep(1)
    ftp_save.close()


def FTP_DIR_SAVE():
    ftp_save = FTP()
    ftp_save.connect('90.186.164.185', 47126)
    ftp_save.login('Box77ineT', 'A20d747f16')
    ftp_save.retrlines('LIST')  # list directory contents
    ordner = os.listdir(r'{}Aufträge'.format(path_sys))  ###  Zeigt alle Dateienin Ordner
    for i in ordner:
        print(i)
        print()
        time.sleep(2)
        for bild in range(1, 8):
            message('Speichern von Ordner {}   Bild Nr.: {}'.format(i, bild), 30)

            try:
                with open(r'{}Aufträge/{}/Bild_{}_{}.jpg'.format(path_sys, i, i, bild), 'rb') as image_file:
                    ftp_save.storbinary(r'STOR CCCOMA_X64F/Aufträge/{}/'.format(i), image_file)
            except FileNotFoundError:
                pass


# FTP_DIR_SAVE()

# Set geometry
root.geometry('1920x1080')
root.attributes('-fullscreen', True)

# Information List
MATERIAL = IntVar()
DATUM = StringVar()
IMAGE_to_EMAIL = BooleanVar()
loaded = True
counter = 0
bild_nr = 1
datas = []
b1 = StringVar()
b2 = StringVar()
Kilometer = IntVar()
Set_Tag = IntVar()
Voriger_Tag = IntVar()
Bild_Aktuel = StringVar()
Letzte_KM = ''
list_s = []
Bild_Green = True
woche = IntVar()
Delete = BooleanVar()
n = 0
datas_fahr = []
fahrten = []
Counter = 0
fertig = None
# nw = []
y = 30  ###   --->   ################  Schrift Grösse Format  #################
dat_1 = []
######################   WOCHEN   #########################
woche1 = []
woche2 = []
woche3 = []
woche4 = []
woche5 = []
woche6 = []
######################  BIBLIOTHEK  #######################
Nummer = 0
Bibliothek = {}
Fahrten = {}
Wochen_Add = {}
Auftrags_Liste = int()
Auftrags_Liste_2 = int()
upload_button = StringVar()
x_size_button = IntVar()
y_size_button = IntVar()
Zeit_String = StringVar()
######################################################################
t = time.ctime()
t = t.split()
zeit = str(t[2] + '.' + t[1] + ' ' + t[4] + ' Zeit: ' + t[3])


######################################################################

def Bild_Save(bild_nr):
    global Bild_Aktuel, nw, Bild_Green, Liste_Images, Len_Images_List, Bild_Green_Bibliothek
    print(Bild_Green,'- Bild_Green ist')
    if not Bild_Green: ### Bild_Red  ###
        nw, = select_1.curselection()
        if nw:
            Auftrags_Liste_Aktuell, = select_1.get(nw, nw)
            #Auftrags_Liste_Aktuell, = select_1.get(END, END)
        try:
            image_import = Image.open(r'{}Werkstatt_Images\{}'.format(path_sys, Bild_Aktuel.get()))
            view()
            image_import.save(r'{}Aufträge\{}\Bild_{}_{}.jpg'.format(path_sys, Number.get(), Auftrags_Liste_Aktuell, bild_nr))
            message('Das Bild ist GESPEICHERT!!!', 30)
        except FileNotFoundError:
            message('Kein Auftrag für das Bild vorhanden! Bitte Auftrag wählen!', 30)
    Bild_Green_Bibliothek = {}
    path_liste_images = os.listdir("{}Aufträge".format(path_sys))  ###  Zeigt alle Dateienin Ordner
    Liste_Images = []

    for i in path_liste_images:
        path_dir_images_Auftrag = os.listdir("{}Aufträge/{}".format(path_sys, i))
        print(i, path_dir_images_Auftrag)
        Len_Images_List = len(path_dir_images_Auftrag)
        for j in range(Len_Images_List):
            List_Img = list(path_dir_images_Auftrag[j])
            lps = List_Img[-5]
            print()
            Liste_Images.append(lps)
        Bild_Green_Bibliothek[i] = [path_dir_images_Auftrag, Liste_Images]
        Liste_Images = []

    print(Bild_Green_Bibliothek)


def bild_1_import():
    Button(root, text=' BILD 1 ', font="arial 10 bold", width=15, bg='red', command=bild_1_import).place(x=1250, y=110)
    bild_nr = 1
    Bild_Save(bild_nr)
    Image_Saved.set(False)


def bild_2_import():
    Button(root, text=' BILD 2 ', font="arial 10 bold", width=15, bg='red', command=bild_2_import).place(x=1390, y=110)
    bild_nr = 2
    Bild_Save(bild_nr)
    Image_Saved.set(False)

def bild_3_import():
    Button(root, text=' BILD 3 ', font="arial 10 bold", width=15, bg='red', command=bild_3_import).place(x=1530, y=110)
    bild_nr = 3
    Bild_Save(bild_nr)
    Image_Saved.set(False)


def bild_4_import():
    Button(root, text=' BILD 4 ', font="arial 10 bold", width=15, bg='red', command=bild_4_import).place(x=1670, y=110)
    bild_nr = 4
    Bild_Save(bild_nr)
    Image_Saved.set(False)


def bild_5_import():
    Button(root, text=' BILD 5 ', font="arial 10 bold", width=15, bg='red', command=bild_5_import).place(x=1250, y=140)
    bild_nr = 5
    Bild_Save(bild_nr)
    Image_Saved.set(False)


def bild_6_import():
    Button(root, text=' BILD 6 ', font="arial 10 bold", width=15, bg='red', command=bild_6_import).place(x=1390, y=140)
    bild_nr = 6
    Bild_Save(bild_nr)
    Image_Saved.set(False)


def bild_7_import():
    Button(root, text=' BILD 7 ', font="arial 10 bold", width=15, bg='red', command=bild_7_import).place(x=1530, y=140)
    bild_nr = 7
    Bild_Save(bild_nr)
    Image_Saved.set(False)


def bild_8_import():
    Button(root, text=' BILD 8 ', font="arial 10 bold", width=15, bg='red', command=bild_8_import).place(x=1670, y=140)
    bild_nr = 8
    Bild_Save(bild_nr)
    Image_Saved.set(False)


def image_logo():
    global label_logo_1, test_logo_1
    image1 = Image.open(r'{}\hanse_gm.png'.format(path_sys))  # path_sys
    image_logo_1 = image1.resize((500, 330))
    image_logo_2 = image1.resize((400, 120))
    test_logo_1 = ImageTk.PhotoImage(image_logo_1)
    test_logo_2 = ImageTk.PhotoImage(image_logo_2)
    label_logo_1 = Label(image=test_logo_1)
    label_logo_2 = Label(image=test_logo_2)
    label_logo_1.image = test_logo_1
    label_logo_2.image = test_logo_2
    label_logo_1.place(x=1250, y=150)
    label_logo_2.place(x=30, y=550)



def zeit_out():
    t = time.ctime()
    t = t.split()
    data = str(t[2] + '.  ' + t[1] + ' ' + t[4] + '      ')
    zeit_x = t[3]
    Data_Out.config(text=data)
    # Data_Out.after(16000, zeit_out)
    Zeit_Out.config(text=zeit_x)
    Zeit_Out.after(1000, zeit_out)
    return data, zeit_x


###########################################   Material Liste Einfügen   ################################################
def einfuegen():
    global Email_Adress
    Lists = Bestellung_Liste.get()
    Lists_L = list(Lists)
    print(Lists_L)
    message(Lists_L, 30)
    if Lists_L[0] == '#':
        if Lists == '#101':
            nc, = select_2.curselection()
            select_2.delete(nc, nc)
        if Lists == '#102':
            E_Mail_text_send()
        if Lists == '#103':
            E_Mail_image_send()
        if Lists == '#104':
            image_load = Image.open(r"{}\Werkstatt_Images\Bild_Test.png".format(path_sys))
            image_load.save(r'{}\Werkstatt_Images\{}'.format(path_sys, Bild_Aktuel.get()))
            message('Das Bild ist gespeichert...', 30)
        if Lists == '#105':
            FTP_DIR_SAVE()
        if '@' in Lists_L:
            Email_Adress = Bestellung_Liste.get()
            E_Mail_Bestellung()
    else:
        if Lists:
            select_2.insert(END, Lists)
        else:
            pass
    Bestellung_Liste.set('')


########################################################################################################################

def save_file(filename):
    global dat_1, bild_nr, nw, image1
    print(bild_nr, '   ', filename)
    f = filename.split()
    print(f)
    try:
        Image_Opened = Image.open(r'{}'.format(str(filename)))  # D:\Aufträge\Wilhelmsburg\
        nw, = select_1.curselection()
        Auftrags_Liste_Aktuell, = select_1.get(nw, nw)
        message('Image mit Auftragsnummer: {}  wird GESPEICHERT'.format(str(Auftrags_Liste_Aktuell)), 20)
        Image_Opened.save(
            r'{}Aufträge\{}\Bild_{}_{}.jpg'.format(path_sys, Number.get(), Auftrags_Liste_Aktuell, bild_nr))
        image1 = Image.open(
            r'{}Aufträge\{}\Bild_{}_{}.jpg'.format(path_sys, Number.get(), Auftrags_Liste_Aktuell, bild_nr))
        x_img, y_img = image1.size
        if x_img > y_img:
            x = 500
            y = 330
            x_platz = 1270
            y_platz = 220
        else:
            x = 330
            y = 500
            x_platz = 1340
            y_platz = 200
        image1 = image1.resize((x, y))
        test_1 = ImageTk.PhotoImage(image1)
        label1 = Label(image=test_1)
        label1.image = test_1
        label1.place(x=x_platz, y=y_platz)
    except AttributeError:
        message('Keine Datei ausgewehlt', 30)


def upload_images():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("PNG", "*.png*"), ("Bild_Dateien", "*.jpg*"), ("all files", "*.*")))
    message("Datei: " + filename, 12)
    print(filename)
    save_file(filename)


def size_x():
    global bild_nr
    clear_pages()
    try:
        nw, = select_1.curselection()
        Auftrags_Liste_Aktuell, = select_1.get(nw, nw)
        image1 = Image.open(
            r'{}\Aufträge\{}\Bild_{}_{}.jpg'.format(path_sys, Number.get(), Auftrags_Liste_Aktuell, bild_nr))
    except NameError:
        image1 = Image.open(r"{}\Werkstatt_Images\{}".format(path_sys, Bild_Aktuel.get()))
    except FileNotFoundError:
        image1 = Image.open(r"{}\Werkstatt_Images\{}".format(path_sys, Bild_Aktuel.get()))
    except ValueError:
        image1 = Image.open(r"{}\Werkstatt_Images\{}".format(path_sys, Bild_Aktuel.get()))
    x_img, y_img = image1.size
    x = 500
    y = 330
    x_platz = 1270
    y_platz = 220
    image1 = image1.resize((x, y))

    test_1 = ImageTk.PhotoImage(image1)
    label1 = Label(image=test_1)
    label1.image = test_1
    label1.place(x=x_platz, y=y_platz)


def size_y():
    global bild_nr, Bild_Aktuel
    clear_pages()
    try:
        nw, = select_1.curselection()
        Auftrags_Liste_Aktuell, = select_1.get(nw, nw)
        image1 = Image.open(r'{}\Aufträge\{}\Bild_{}_{}.jpg'.format(path_sys, Number.get(), Auftrags_Liste_Aktuell, bild_nr))
    except NameError:
        image1 = Image.open(r"{}\Werkstatt_Images\{}".format(path_sys, Bild_Aktuel.get()))
    except FileNotFoundError:
        image1 = Image.open(r"{}\Werkstatt_Images\{}".format(path_sys, Bild_Aktuel.get()))
    except ValueError:
        image1 = Image.open(r"{}\Werkstatt_Images\{}".format(path_sys, Bild_Aktuel.get()))
    x_img, y_img = image1.size
    x = 330
    y = 500
    x_platz = 1340
    y_platz = 200
    image1 = image1.resize((x, y))
    test_1 = ImageTk.PhotoImage(image1)
    label1 = Label(image=test_1)
    label1.image = test_1
    label1.place(x=x_platz, y=y_platz)


def Image_Roter(x, y, x_platz, y_platz, angle):
    global image1, dr_x
    # image1 = image1.rotate(angle=angle)
    image1 = np.rot90(image1, k=angle)
    array = image1.astype(np.uint8)  # Convert to unsigned byte format
    image1 = Image.fromarray(array, 'RGB')  # 'L' for grayscale mode
    image1.save(r'{}\Werkstatt_Images\{}'.format(path_sys, 'Bild_Test.png'))
    # img.save(r'{}\{}'.format(path_sys, 'Bild_Test.png'))
    image1 = image1.resize((x, y))
    ##########################################################################################
    test_1 = ImageTk.PhotoImage(image1)
    label1 = Label(image=test_1)
    label1.image = test_1
    label1.place(x=x_platz, y=y_platz)


angle = 0
rotate = True
angle_set = IntVar()
angle_set.set(angle)
cycle_1_4 = [1, 2, 3, 4]
roter = cycle(cycle_1_4)


def img_rotation():
    global bild_nr, address_2, image1, angle_set, angle, select_1, nw, rotate, Nächste_Image, bild, x_platz, y_platz, x, y, roter, dr_x
    clear_pages_ima_x()
    try:
        nw, = select_1.curselection()
        Auftrags_Liste_Aktuell, = select_1.get(nw, nw)
        if Auftrags_Liste_Aktuell and Bild_Green is True:
            image1 = imageio.v2.imread(r'{}\Aufträge\{}\Bild_{}_{}.jpg'.format(path_sys, Number.get(), Auftrags_Liste_Aktuell, bild_nr))
            print('...Rotate...')
        else:
            try:
                image1 = imageio.v2.imread(r'{}\Werkstatt_Images\{}'.format(path_sys, Bild_Aktuel.get()))
            except ValueError:
                image1 = imageio.v2.imread(r'{}\Aufträge\{}\Bild_{}_{}.jpg'.format(path_sys, Number.get(), Auftrags_Liste_Aktuell, bild_nr))
    except FileNotFoundError:
        image1 = imageio.v2.imread(r'{}\Werkstatt_Images\{}'.format(path_sys, Bild_Aktuel.get()))

    except ValueError:
        image1 = imageio.v2.imread(r'{}\Werkstatt_Images\{}'.format(path_sys, Bild_Aktuel.get()))

    array = image1.astype(np.uint8)  ### Convert to unsigned byte format
    image1 = Image.fromarray(array, 'RGB')  ### 'L' for grayscale mode
    image1.save(r'{}\Werkstatt_Images\{}'.format(path_sys, 'Bild_Test.png'))
    img = Image.open(r'{}\Werkstatt_Images\{}'.format(path_sys, 'Bild_Test.png'))
    ##################################  Image Operative  #####################################
    x_img, y_img = img.size
    img.close()
    message((str(x_img) + ' x ' + str(y_img)), 30)

    if x_img > y_img:  ##############  Horizontal  ################
        dr_x = next(roter)
        ############################  Dreher 1  ###############################
        if dr_x == 1:
            x = 330
            y = 500
            x_platz = 1340
            y_platz = 200
            angle = 3
            Image_Roter(x, y, x_platz, y_platz, angle)
            print('dr_x 1')

        ############################  Dreher 2  #############################
        if dr_x == 2:
            x = 500
            y = 330
            x_platz = 1270
            y_platz = 220
            angle = 2
            Image_Roter(x, y, x_platz, y_platz, angle)
            print('dr_x 2')

        ############################  Dreher 3  ###################
        if dr_x == 3:
            x = 330
            y = 500
            x_platz = 1340
            y_platz = 200
            angle = 1
            Image_Roter(x, y, x_platz, y_platz, angle)
            print('dr_x 3')

        ############################  Dreher 4  ###################
        if dr_x == 4:
            x = 500
            y = 330
            x_platz = 1270
            y_platz = 220
            angle = 0
            Image_Roter(x, y, x_platz, y_platz, angle)
            cycle_1_4 = [1, 2, 3, 4]
            roter = cycle(cycle_1_4)
            print('dr_x 4')
        print(dr_x, '   Horizontal')

    else:  ##########  Vertikal  #############################
        dr_x = next(roter)
        ############################  Dreher 1  #############################
        if dr_x == 1:
            x = 500
            y = 330
            x_platz = 1270
            y_platz = 200
            angle = 3
            Image_Roter(x, y, x_platz, y_platz, angle)
            print('dr_x 1')

        ############################  Dreher 2  ###################
        if dr_x == 2:
            x = 330
            y = 500
            x_platz = 1340
            y_platz = 200
            angle = 2
            Image_Roter(x, y, x_platz, y_platz, angle)
            print('dr_x 2')

        ############################  Dreher 3  ###################
        if dr_x == 3:
            x = 500
            y = 330
            x_platz = 1270
            y_platz = 220
            angle = 1
            Image_Roter(x, y, x_platz, y_platz, angle)
            print('dr_x 3')

        ############################  Dreher 4  ###################
        if dr_x == 4:
            x = 330
            y = 500
            x_platz = 1340
            y_platz = 200
            angle = 0
            Image_Roter(x, y, x_platz, y_platz, angle)
            cycle_1_4 = [1, 2, 3, 4]
            roter = cycle(cycle_1_4)
            print('dr_x 4')
        print(dr_x, '    Vertikal')


def Bild_Import_Buttons_LIST():
    global bild_nr, Bild_Aktuel
    clear_pages()
    Button(root, text="  <<<BILDER>>> ", font="arial 12 bold", bg="#00C78C", width=39, command=Bilder).place(x=30, y=360)

    Button(root, text=' BILD 1 ', font="arial 10 bold", width=15, bg='yellow', command=bild_1).place(x=1250, y=110)
    Button(root, text=' BILD 2 ', font="arial 10 bold", width=15, bg='yellow', command=bild_2).place(x=1390, y=110)
    Button(root, text=' BILD 3 ', font="arial 10 bold", width=15, bg='yellow', command=bild_3).place(x=1530, y=110)
    Button(root, text=' BILD 4 ', font="arial 10 bold", width=15, bg='yellow', command=bild_4).place(x=1670, y=110)

    Button(root, text=' BILD 5 ', font="arial 10 bold", width=15, bg='yellow', command=bild_5).place(x=1250, y=140)
    Button(root, text=' BILD 6 ', font="arial 10 bold", width=15, bg='yellow', command=bild_6).place(x=1390, y=140)
    Button(root, text=' BILD 7 ', font="arial 10 bold", width=15, bg='yellow', command=bild_7).place(x=1530, y=140)
    Button(root, text=' BILD 8 ', font="arial 10 bold", width=15, bg='yellow', command=bild_8).place(x=1670, y=140)

    SCANN = Button(root, text="  <<--EINSCANNEN-->>  ", font="arial 15 bold", command=scanner, borderwidth=2, background='#FF6103')
    SCANN.place(x=1400, y=730)



Buttons_Color_1 = StringVar()
Buttons_Color_2 = StringVar()
Buttons_Color_3 = StringVar()
Buttons_Color_4 = StringVar()
Buttons_Color_5 = StringVar()
Buttons_Color_6 = StringVar()
Buttons_Color_7 = StringVar()
Buttons_Color_8 = StringVar()


def Buttons_Yellou():
    Buttons_Color_1.set('yellow')
    Buttons_Color_2.set('yellow')
    Buttons_Color_3.set('yellow')
    Buttons_Color_4.set('yellow')
    Buttons_Color_5.set('yellow')
    Buttons_Color_6.set('yellow')
    Buttons_Color_7.set('yellow')
    Buttons_Color_8.set('yellow')
    Buttons_All()


def Auftrag_On_Def():
    if '1' in Images_Red_On:
        Button(root, text=' BILD 1 ', font="arial 10 bold", width=15, bg='red', command=bild_1_import).place(x=1250, y=110)
    if '2' in Images_Red_On:
        Button(root, text=' BILD 2 ', font="arial 10 bold", width=15, bg='red', command=bild_2_import).place(x=1390, y=110)
    if '3' in Images_Red_On:
        Button(root, text=' BILD 3 ', font="arial 10 bold", width=15, bg='red', command=bild_3_import).place(x=1530, y=110)
    if '4' in Images_Red_On:
        Button(root, text=' BILD 4 ', font="arial 10 bold", width=15, bg='red', command=bild_4_import).place(x=1670, y=110)
    if '5' in Images_Red_On:
        Button(root, text=' BILD 5 ', font="arial 10 bold", width=15, bg='red', command=bild_5_import).place(x=1250, y=140)
    if '6' in Images_Red_On:
        Button(root, text=' BILD 6 ', font="arial 10 bold", width=15, bg='red', command=bild_6_import).place(x=1390, y=140)
    if '7' in Images_Red_On:
        Button(root, text=' BILD 7 ', font="arial 10 bold", width=15, bg='red', command=bild_7_import).place(x=1530, y=140)
    if '8' in Images_Red_On:
        Button(root, text=' BILD 8 ', font="arial 10 bold", width=15, bg='red', command=bild_8_import).place(x=1670, y=140)


START_X = False
Auftrag_On = []


def Red_Buttons_On():
    global Images_Red_On, Images_list, Auftrag_On, nw, Auftrags_Liste_2, START_X
    if not Bild_Green:
        try:
            nw, = select_1.curselection()
            Auftrags_Liste_2, = select_1.get(nw, nw)
            Index_Images = Bild_Green_Bibliothek[Auftrags_Liste_2]
            Images_Red_On = Index_Images[1]
            Auftrag_On.append(Auftrags_Liste_2)  ###  appand  1
            print(Auftrags_Liste_2)
            print(Auftrag_On, 'Liste von Aufträgen')
            try:
                if Auftrag_On[0] != Auftrag_On[1]:
                    Buttons_Yellou()
            except IndexError:
                Auftrag_On.append(Auftrags_Liste_2)  ###  appand  2
            if Auftrag_On[0] != Auftrag_On[1]:
                print('Ungleich...')
                Buttons_Yellou()
            if len(Auftrag_On) > 2:
                Auftrag_On.pop(0)
            print(Images_Red_On, 'red')
            print(Auftrag_On)
            Auftrag_On_Def()

            if Images_Red_On:
                Auftrag_On_Def()
            else:
                if len(Auftrag_On) > 2:
                    Auftrag_On.pop(0)
        except ValueError:
            pass
        except KeyError:
            print('Error')
        if not Bild_Green:
            root.after(1000, Red_Buttons_On)


def Buttons_All():
    global Buttons_Color_1, Buttons_Color_2, Buttons_Color_3, Buttons_Color_4
    global Buttons_Color_5, Buttons_Color_6, Buttons_Color_7, Buttons_Color_8

    Button(root, text=' BILD 1 ', font="arial 10 bold", width=15, bg=Buttons_Color_1.get(), command=bild_1_import).place(x=1250, y=110)
    Button(root, text=' BILD 2 ', font="arial 10 bold", width=15, bg=Buttons_Color_2.get(), command=bild_2_import).place(x=1390, y=110)
    Button(root, text=' BILD 3 ', font="arial 10 bold", width=15, bg=Buttons_Color_3.get(), command=bild_3_import).place(x=1530, y=110)
    Button(root, text=' BILD 4 ', font="arial 10 bold", width=15, bg=Buttons_Color_4.get(), command=bild_4_import).place(x=1670, y=110)

    Button(root, text=' BILD 5 ', font="arial 10 bold", width=15, bg=Buttons_Color_5.get(), command=bild_5_import).place(x=1250, y=140)
    Button(root, text=' BILD 6 ', font="arial 10 bold", width=15, bg=Buttons_Color_6.get(), command=bild_6_import).place(x=1390, y=140)
    Button(root, text=' BILD 7 ', font="arial 10 bold", width=15, bg=Buttons_Color_7.get(), command=bild_7_import).place(x=1530, y=140)
    Button(root, text=' BILD 8 ', font="arial 10 bold", width=15, bg=Buttons_Color_8.get(), command=bild_8_import).place(x=1670, y=140)


def Bild_Import_Buttons_Import():
    global bild_nr, Bild_Aktuel, one_on_start_3
    clear_pages()
    if Buttons_Yellou():
        pass
    else:
        Buttons_Yellou()
    if one_on_start_3:
        print('Start of the: Red_Buttons_On Defination ')
        Red_Buttons_On()
        one_on_start_3 = False
    ####################################    Def_rote_Buttons    ####################################
    Buttons_All()
    Button(root, text=' BILD >>> ', font="arial 10 bold", width=15, bg='yellow', command=bild_import_1).place(x=1670, y=730)
    Button(root, text=' <<< BILD ', font="arial 10 bold", width=15, bg='yellow', command=bild_import_2).place(x=1250, y=730)
    #####################################################################################################################################
    SCANN = Button(root, text="  <<--EINSCANNEN-->>  ", font="arial 15 bold", command=scanner, borderwidth=2, background='#FF6103')
    SCANN.place(x=1400, y=730)
    Buttons_Yellou()
    #####################################################################################################################################
    Auftrag_On = []


NEU_IMG = True
Count_Img = 0
Nächste_Image = False


def bild_import_1():  ### VORWERTS --->
    global Bild_Aktuel, Count_Img, Image_COY, NEU_IMG, Nächste_Image, roter, cycle_1_4
    Nächste_Image = True
    Count_Img += 1
    if Count_Img < 1:
        Count_Img = 0
    if NEU_IMG:
        Count_Img = 0
        NEU_IMG = False
    Image_COY = Bild_List[Count_Img]
    Bild_Import_Buttons_Import()
    Bild_Aktuel.set(Image_COY)
    message(Bild_Aktuel.get(), 25)
    Bild_View(Bild_Aktuel.get())
    cycle_1_4 = [1, 2, 3, 4]
    roter = cycle(cycle_1_4)


def bild_import_2():  ### ABWERTS --->
    global Bild_Aktuel, Count_Img, Image_COY, NEU_IMG, Nächste_Image, roter, cycle_1_4
    Nächste_Image = True
    Count_Img -= 1
    if Count_Img > len(path_ord_bilder):
        Count_Img = 0
    if NEU_IMG:
        Count_Img = 0
        NEU_IMG = False
    Image_COY = Bild_List[Count_Img]
    Bild_Import_Buttons_Import()
    Bild_Aktuel.set(Image_COY)
    Bild_View(Bild_Aktuel.get())
    message(Bild_Aktuel.get(), 25)
    cycle_1_4 = [1, 2, 3, 4]
    roter = cycle(cycle_1_4)


def Bild_View(v):
    try:
        image1 = Image.open(r'{}Werkstatt_Images\{}'.format(path_sys, v))
        x_img, y_img = image1.size
        if x_img > y_img:
            x = 500
            y = 330
            x_platz = 1270
            y_platz = 220
        else:
            x = 330
            y = 500
            x_platz = 1340
            y_platz = 200
        image1 = image1.resize((x, y))
        test_1 = ImageTk.PhotoImage(image1)
        label1 = Label(image=test_1)
        label1.image = test_1
        label1.place(x=x_platz, y=y_platz)
    except PermissionError:
        pass
    except PIL.UnidentifiedImageError:
        pass


image_paths = [r'{}Zeiger\\Bild_{}.png'.format(path_sys, r) for r in range(0, 360, 5)]


def Bilder():
    clear_buttons()
    global nw, bild_nr, grad_90, upload_B, X_ima, Y_ima, Bild_Green, one_on_start, upload_button, Bild_Aktuel, Auftrags_Liste, one_on_start_1, label_logo_1
    label_logo_1.destroy()
    print('Bild GREEN bei Bilder', Bild_Green)
    clear_pages()
    if Bild_Green == True:  #############################   Images list  ##############################
        Bild_Import_Buttons_LIST()
        Bild_Green = False
    else:  #############################   Images import  ##############################
        Button(root, text="  <<<BILDER>>> ", font="arial 12 bold", bg="red", width=39, command=Bilder).place(x=30, y=360)
        Bild_Import_Buttons_Import()
        Bild_Green = True
    ####################################################################################################################
    grad_90 = Button(root, bg='yellow', command=img_rotation)
    grad_90.place(x=1198, y=650)
    ###############################################################
    ####################  Rotierende Zeiger  ######################

    # Liste von Bildpfaden (ersetze diese mit deinen eigenen Bildern)

    images = [PhotoImage(file=image_path) for image_path in image_paths]
    images.reverse()
    image_cycle = cycle(images)

    def next_image():
        global images_cycle
        next_image_object = next(image_cycle)
        try:
            grad_90.config(image=next_image_object)
            grad_90.image = next_image_object  # Halten Sie eine Referenz auf das Bildobjekt
        except _tkinter.TclError:
            pass
        root.after(500, next_image)  # Wechsel alle 1000 Millisekunden (1 Sekunde)
    next_image()

    if upload_button.get():
        pass
    else:
        upload_button.set('-UPLOAD- Image_{}'.format(bild_nr))

    upload_B = Button(root, textvariable=upload_button, font="arial 11 bold", width=16, bg='yellow', overrelief='ridge',
                      command=upload_images)
    upload_B.place(x=1075, y=690)

    X_ima = Button(root, text='X-SIZE', font="arial 12 bold", width=6, bg='yellow', command=size_x)
    X_ima.place(x=1075, y=740)
    Y_ima = Button(root, text='Y-SIZE', font="arial 12 bold", width=6, bg='yellow', command=size_y)
    Y_ima.place(x=1158, y=740)

    # Bilder sofort sichtbar machenbeim laden
    datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
    datas_1.tolist()

    try:
        nw, = select_1.curselection()
        message('Bilder vom Auftrag: {} werden GELADEN...'.format(datas_1[nw][1]), 30)
    except ValueError:
        message('DRÜCKEN SIE  <<<--- LOAD --->>>', 30)
    return bild_nr


def screen_image(bild_nr):
    clear_pages_ima()
    global dat_1, one_on_start, image1, nw, Bild_Green
    upload_button.set('-UPLOAD- Image_{}'.format(bild_nr))
    if upload_button.get():
        pass
    else:
        upload_button.set('-UPLOAD- Image_{}'.format(1))
    try:
        nw, = select_1.curselection()
        Auftrags_Liste_Aktuell, = select_1.get(nw, nw)
        message(Auftrags_Liste_Aktuell + '  ' + str(bild_nr), 30)
    except ValueError:
        dat_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
        Auftrags_Liste_Aktuell = dat_1[0][1]
    try:
        print('Bild wird geöffnet... Bild_Green ist  ', Bild_Green)
        if Bild_Green == False:
            view()
            image1 = Image.open(r'{}\Aufträge\{}\Bild_{}_{}.jpg'.format(path_sys, Number.get(), Auftrags_Liste_Aktuell, bild_nr))
            print('Bild... : {} geöffnet'.format(bild_nr))
        else:
            if Auftrags_Liste_Aktuell:
                image1 = Image.open(r'{}\Aufträge\{}\Bild_{}_{}.jpg'.format(path_sys, Number.get(), Auftrags_Liste_Aktuell, bild_nr))
            else:
                Bilder()
        x_img, y_img = image1.size
        if x_img > y_img:
            x = 500
            y = 330
            x_platz = 1270
            y_platz = 220
        else:
            x = 330
            y = 500
            x_platz = 1340
            y_platz = 200
        image1 = image1.resize((x, y))
        test_1 = ImageTk.PhotoImage(image1)
        label1 = Label(image=test_1)
        label1.image = test_1
        label1.place(x=x_platz, y=y_platz)
    except IndexError:
        print('Das Bild wird nicht geöffnet...')
    SCANN = Button(root, text="  <<--EINSCANNEN-->>  ", font="arial 15 bold", command=scanner, borderwidth=2,
                   background='#FF6103')
    SCANN.place(x=1375, y=730)


def bild_1():
    global dat_1, bild_nr
    bild_nr = 1
    screen_image(bild_nr)
    message('Bild Nr.1', 30)


def bild_2():
    global dat_1, bild_nr
    bild_nr = 2
    screen_image(bild_nr)
    message('Bild Nr.2', 30)


def bild_3():
    global dat_1, bild_nr
    bild_nr = 3
    screen_image(bild_nr)
    message('Bild Nr.3', 30)


def bild_4():
    global dat_1, bild_nr
    bild_nr = 4
    screen_image(bild_nr)
    message('Bild Nr.4', 30)


def bild_5():
    global dat_1, bild_nr
    bild_nr = 5
    screen_image(bild_nr)
    message('Bild Nr.5', 30)


def bild_6():
    global dat_1, bild_nr
    bild_nr = 6
    screen_image(bild_nr)
    message('Bild Nr.6', 30)


def bild_7():
    global dat_1, bild_nr
    bild_nr = 7
    screen_image(bild_nr)
    message('Bild Nr.7', 30)
    Bilder()

def bild_8():
    global dat_1, bild_nr
    bild_nr = 8
    screen_image(bild_nr)
    message('Bild Nr.8', 30)
    Bilder()


def change():
    global Time, Zeit_add_On, Zeit_String
    datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
    datas_1.tolist()
    message(zeit_add, 30)
    if Zeit_add_On == False:
        Time.set(Zeit_String.get())
        Zeit_add_On = True
    else:
        try:
            nw, = select_1.curselection()
        except ValueError:
            nw = len(datas_1[len(datas_1) - 1])
        print(nw)
        datas_1[nw][5] = Time.get()
        print(datas_1)
        np.save(r'{}\Werkstatt.npy'.format(path_sys), datas_1)
        Zeit_add_On = False
        message('Die Zeitänderung ist durchgeführt', 30)
        Time.set(str(''))


def fertig_set():
    datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
    datas_2 = np.load(r'{}\Material.npy'.format(path_sys), allow_pickle=True)
    if checkbutton_var_4.get() == True:
        l = len(datas_1)
        for i in range(0, l):
            datas_1[i][7] = None
            select_1.itemconfig(i, bg='white')
        datas_1 = np.array(datas_1)
        datas_2 = np.array(datas_2)
        save(datas_1, datas_2)
    else:
        try:
            nw, = select_1.curselection()
            print('')
            print('')
            print('')
            print(nw)
            datas_1.tolist()
            datas_1 = list(datas_1)
            if datas_1[nw][7] == 'GREEN':
                datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
                datas_2 = np.load(r'{}\Material.npy'.format(path_sys), allow_pickle=True)
                select_1.itemconfig(nw, bg='red')
                datas_1[nw][7] = 'RED'
                datas_1 = np.array(datas_1)
                datas_2 = np.array(datas_2)
                save(datas_1, datas_2)
                print(datas_1)
                return
            if datas_1[nw][7] == 'RED':
                datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
                datas_2 = np.load(r'{}\Material.npy'.format(path_sys), allow_pickle=True)
                select_1.itemconfig(nw, bg='white')
                datas_1[nw][7] = None
                datas_1 = np.array(datas_1)
                datas_2 = np.array(datas_2)
                save(datas_1, datas_2)
            if datas_1[nw][7] == None:
                print('-GREEN-')
                datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
                datas_2 = np.load(r'{}\Material.npy'.format(path_sys), allow_pickle=True)
                select_1.itemconfig(nw, bg='green')
                datas_1[nw][7] = 'GREEN'
                datas_1 = np.array(datas_1)
                datas_2 = np.array(datas_2)
                save(datas_1, datas_2)
                print(datas_1)
        except ValueError:
            pass
    checkbutton_False_4()
    message('Der Auftrag ist fertiggestellt', 30)


def del_lists():
    global Bild_Green, Bild_Aktuel, Bestellung_Liste
    if Bild_Green and Bestellung_Liste.get() == '#106':
        message('Removing the Image...{}'.format(Bild_Aktuel.get()), 30)
        indx = Bild_List.index('{}'.format(Bild_Aktuel.get()))
        Bild_List.pop(indx)
        os.remove(r'{}/Werkstatt_Images/{}'.format(path_sys, Bild_Aktuel.get()))
        bild_import_1()
        Delete.set(False)
    else:
        select_2.delete(0, END)
        print(Bild_Green)
        message('Gelöscht...', 30)


def delete_ja():
    try:
        os.remove(r'{}\Werkstatt.npy'.format(path_sys))
        os.remove(r'{}\Material.npy'.format(path_sys))
    except FileNotFoundError:
        try:
            os.remove(r'{}\Werkstatt.npy'.format(path_sys))
            os.remove(r'{}\Material.npy'.format(path_sys))
        except FileNotFoundError:
            message('Keine Dateien vorhanden.', 30)
    message('Die Dateien wurden gelöscht!!!', 30)


def delete_all():
    JA = Button(root, text='JA', font="arial 10 bold", width=10, command=delete_ja)
    JA.place(x=1550, y=820)
    NEIN = Button(root, text='NEIN', font="arial 10 bold", width=10,
                  command=lambda: [JA.destroy(), message('Abgebrochen... Bitte warten', 30)])
    NEIN.place(x=1700, y=820)
    BREAK = Button(root, text='BREAK', font="arial 10 bold", width=20,
                   command=lambda: [JA.destroy(), NEIN.destroy(), message('Aufgeräumt... Bitte warten', 30)])
    BREAK.place(x=1580, y=860)


def save(x, y):
    x = np.array(x)
    y = np.array(y, dtype=object)
    try:
        np.save(r'{}\Werkstatt.npy'.format(path_sys), x)
        np.save(r'{}\Material.npy'.format(path_sys), y)
        np.save(r'{}\Werkstatt_KOPIE.npy'.format(path_sys), x)
        np.save(r'{}\Material_KOPIE.npy'.format(path_sys), y)
    except NotADirectoryError:
        np.save(r'{}\Werkstatt.npy'.format(path_sys), x)
        np.save(r'{}\Material.npy'.format(path_sys), y)
        np.save(r'{}\Werkstatt_KOPIE.npy'.format(path_sys), x)
        np.save(r'{}\Material_KOPIE.npy'.format(path_sys), y)

    Label(root, text='Aufträge:   {}'.format(len(dat_1)), font='arial 12 bold').place(x=475, y=115)


##########################   Add Information   ###########################
def add_save(datas_1, datas_2):
    check(1)
    checkbutton_False_1()
    global counter, list_s, select_1
    t = time.ctime()
    t = t.split()
    zeit = str(t[2] + '.' + t[1] + ' ' + t[4] + ' Zeit: ' + t[3])
    data = [Name.get(), Number.get(), Tower.get(), address_1.get(1.0, "end-1c"), address_2.get(1.0, "end-1c")]
    counter += 1
    data.append(zeit)
    data.append(counter)
    data.append(fertig)
    datas_1.append(data)
    b = len(list(select_2.get(0, END)))
    for a in range(b):  # -1
        list_s.append(select_2.get(a))
        print(a, list_s)
    datas_2.append(list_s)
    print(datas_2)

    try:
        os.mkdir(r'Aufträge\{}'.format(Number.get()))
    except FileExistsError:
        pass

    ##################################   SAVE   ##################################
    try:
        save(datas_1, datas_2)
        list_s = []
        ##########################################################################
        with open(r'{}\Werkstatt.txt'.format(path_sys), mode='w') as d:
            d.write(str(Name.get() + '   ' + Number.get() +
                        '   ' + Tower.get() +
                        '   ' + address_1.get(1.0, "end-1c")) +
                    '   ' + zeit +
                    '   ' + Bestellung_Liste.get() + '\n')
        print('Gespeichert...')
    except FileNotFoundError:
        print('Speicher gescheitert...')
        np.save(r'{}\Werkstatt.npy'.format(path_sys), datas_1)
        np.save(r'{}\Material.npy'.format(path_sys), datas_2)
        ###############################################################################
        with open(r'{}\Werkstatt.txt'.format(path_sys), mode='a') as d:
            d.write(str(Name.get() + '   ' + Number.get() +
                        '   ' + Tower.get() +
                        '   ' + address_1.get(1.0, "end-1c")) +
                    '   ' + zeit +
                    '   ' + Bestellung_Liste.get() + '\n')
    d.close()
    winsound.Beep(1400, 110)
    select_1.insert(END, Number.get())
    Name.set('')
    Number.set('')
    Tower.set('')
    address_1.delete(1.0, "end-1c")
    address_2.delete(1.0, "end-1c")
    select_2.delete(0, END)
    d_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
    d_1.tolist()
    Label(root, text='Aufträge:   {}'.format(len(dat_1)), font='arial 12 bold').place(x=475, y=115)


def add():
    try:
        datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
        datas_2 = np.load(r'{}\Material.npy'.format(path_sys), allow_pickle=True)
        print('LOADED ZUHAUSE...')
        datas_1 = datas_1.tolist()
        datas_2 = datas_2.tolist()
    except FileNotFoundError:
        try:
            datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
            datas_2 = np.load(r'{}\Material.npy'.format(path_sys), allow_pickle=True)
            print('LOADED ARBEIT...')
            datas_1 = datas_1.tolist()
            datas_2 = datas_2.tolist()
        except FileNotFoundError:
            datas_1 = []
            datas_2 = []
            pass
    if Name.get() == '' or Number.get() == '' or Tower.get() == '' or checkbutton_var_1.get() == False:
        pass
    else:
        add_save(datas_1, datas_2)
    d_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
    d_1.tolist()
    Label(root, text='Aufträge:   {}'.format(len(dat_1)), font='arial 12 bold').place(x=475, y=115)



##################################   Variable Check   ###################################
def checkbutton_True_1():
    checkbutton_var_1.set(True)


def checkbutton_True_2():
    checkbutton_var_2.set(True)
    img_2 = Image.open(r'{}\d.Auftrag.jpg'.format(path_sys))
    img_2.resize((101, 27))
    img_org_1.copy()
    img_org_1.paste(img_2, box=(750, 150))
    img_org_1.save(r'{}\Auftrag_1.jpg'.format(path_sys))
    Image_Print(img_org_1)


def checkbutton_True_3():
    checkbutton_var_3.set(True)


def checkbutton_True_4():
    checkbutton_var_4.set(True)


##########################################################################################
def checkbutton_False_1():
    checkbutton_var_1.set(False)


def checkbutton_False_2():
    global mr
    global Zelle_Plus, img_org_1
    Zelle_Plus = 1005
    mr = iter([645, 675, 705, 733, 760, 788, 815, 841, 871, 900])
    checkbutton_var_2.set(False)
    Arbeitsnachweis_ORIGINAL()
    img_org_1 = Image.open(r'{}\Arbeitsnachweis.jpg'.format(path_sys))
    img_org_1.save(r'{}\Auftrag_1.jpg'.format(path_sys))


def checkbutton_False_3():
    checkbutton_var_3.set(False)


def checkbutton_False_4():
    checkbutton_var_4.set(False)


def checkbutton_False_5():
    checkbutton_var_5.set(False)


##########################################################################################
##########################################################################################

def check(x):  # onvalue = 1  ----> DEFAULT
    checkbutton_1 = Checkbutton(root, text="-SAVE- OPTION", variable=checkbutton_var_1, onvalue=x, offvalue=x,
                                command=checkbutton_True_1, font='times 15 bold')
    checkbutton_1.place(x=633, y=705)


def check_fertig(x):  # onvalue = 1  ----> DEFAULT
    checkbutton_4 = Checkbutton(root, text="-FERTIG- OPTION", variable=checkbutton_var_4, onvalue=x, offvalue=x,
                                command=checkbutton_True_4, font='times 15 bold')
    checkbutton_4.place(x=633, y=675)


def check_delete(x):  # onvalue = 1  ----> DEFAULT
    checkbutton_3 = Checkbutton(root, text="-DELETE- OPTION", variable=checkbutton_var_3, onvalue=x, offvalue=x,
                                command=checkbutton_True_3, font='times 15 bold')
    checkbutton_3.place(x=633, y=735)


########################################################

def check_dauer_auftrag():  # onvalue = 1  ----> DEFAULT
    checkbutton_2 = Checkbutton(root, text="Dauer Auftrag", variable=checkbutton_var_2, command=checkbutton_True_2,
                                font='times 15 bold')
    checkbutton_2.place(x=1580, y=630)


###########################################################################################
#########################   DIE AUFTRAGSLISTE SCROLL  #####################################

scroll_bar_1 = Scrollbar(root, orient=VERTICAL)
select_1 = Listbox(root, yscrollcommand=scroll_bar_1.set, height=30)
scroll_bar_1.config(command=select_1.yview)
scroll_bar_1.pack(side=RIGHT, fill=Y)
select_1.place(x=470, y=140)

d_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
d_1.tolist()

Label(root, text='Aufträge:', font='arial 12 bold').place(x=475, y=115)

#########################   DIE Bestellliste SCROLL  #######################

scroll_bar_2 = Scrollbar(root, orient=VERTICAL)
select_2 = Listbox(root, yscrollcommand=scroll_bar_2.set, height=18, width=40)
scroll_bar_2.config(command=select_2.yview)
scroll_bar_2.pack(side=RIGHT, fill=Y)
select_2.place(x=940, y=340)

Material = Label(root, text='Material für den Auftrag:', font='arial 12 bold')
Material.place(x=970, y=315)

##########################  CHECK Button  ##################################
checkbutton_var_1 = BooleanVar()
checkbutton_var_2 = BooleanVar()
checkbutton_var_3 = BooleanVar()
checkbutton_var_4 = BooleanVar()
checkbutton_var_5 = BooleanVar()
check(1)
check_delete(1)
check_fertig(1)

##########################   Variable´s   ##################################
add_adress = StringVar()
Zelle_Plus_2 = 1005
Zelle_Plus = 1005
auto_add_1 = []
auto_add_2 = []
zeit_add = []
mr = iter([647, 677, 706, 734, 762, 790, 817, 841, 871, 900, 900, 900, 900, 900, 900])
mr_2 = iter([730, 759, 788, 817, 846, 875, 904, 933])


##################    LOAD    ####################
def loading():
    global DEL_LOAD, Bibliothek, dat_1, zeit_add, n1, address_1_add, address_2_add, name_add, auftrag_add, gebäude_add
    try:
        datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
        datas_2 = np.load(r'{}\Material.npy'.format(path_sys), allow_pickle=True)
        print('LOADED ZUHAUSE...')
        dat_1 = datas_1.tolist()
        dat_2 = datas_2.tolist()
    except FileNotFoundError:
        try:
            datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
            datas_2 = np.load(r'{}\Material.npy'.format(path_sys), allow_pickle=True)
            print('LOADED HIER...')
            dat_1 = datas_1.tolist()
            dat_2 = datas_2.tolist()
        except FileNotFoundError:
            pass
    try:
        Label(root, text='Aufträge:   {}'.format(len(dat_1)), font='arial 12 bold').place(x=475, y=115)
        print(dat_1)
        print(dat_2)
        global Auftrags_Liste
        for it in range(len(dat_1)):
            Auftrags_Liste = dat_1[it][1]
            print(it, Auftrags_Liste)
            #try:
            #    os.mkdir(r'Aufträge\{}'.format(Auftrags_Liste))
            #except:
            #    pass

        for n1 in range(len(dat_1)):
            name_add, auftrag_add, gebäude_add, address_1_add, address_2_add, zeit_add, counter, fertig = dat_1[n1]
            if auftrag_add in dat_1:
                pass
            else:
                select_1.insert(END, auftrag_add)
                if fertig == 'GREEN':
                    select_1.itemconfig(END, bg='green')
                elif fertig == 'RED':
                    select_1.itemconfig(END, bg='red')

        address_1.insert(float(n1), address_1_add)
        address_2.insert(float(n1), address_2_add)
        Name.set(name_add)
        Number.set(auftrag_add)
        Tower.set(gebäude_add)
        k = len(dat_2) - 1
        p = 0
        select_2.delete(0, END)
        for i in range(len(dat_2[k])):
            select_2.insert(p, dat_2[k][i])
            p += 1
        Zeit_String.set(zeit_add)
        Label(root, text=Zeit_String.get(), font="arial 10 bold", background='#00F5FF').place(x=120, y=263)

    except UnboundLocalError:
        message("Ein Fehler aufgetrettet: KEINE ERÖFFNETE DATEI !!!", 30)
        pass
    DEL_LOAD_DEF()


def DEL_LOAD_DEF():
    DEL_LOAD.destroy()
    Button(root, text="       Arne       ", font="arial 13 bold", bg='wheat', command=E_Mail_Arne).place(x=760, y=340)
    Button(root, text="   Anis Gana   ", font="arial 13 bold", bg='wheat', command=E_Mail_Anis).place(x=760, y=390)
    Button(root, text="      Eugen      ", font="arial 13 bold", bg='wheat', command=E_Mail_Eugen).place(x=760, y=440)
    Button(root, text="      Yaya       ", font="arial 13 bold", bg='wheat', command=E_Mail_Yaya).place(x=760, y=490)
    Button(root, text="      Sayid      ", font="arial 13 bold", bg='wheat', command=E_Mail_Sayid).place(x=760, y=540)
    Button(root, text=" J.Quacken-->", font="arial 13 bold", bg='orangered1', command=E_Mail_Quacken).place(x=760, y=590) #390



#############################   View Information   #################################
def view():
    global Zeit_add_On
    Zeit_add_On = False
    try:
        datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
        datas_2 = np.load(r'{}\Material.npy'.format(path_sys), allow_pickle=True)
    except FileNotFoundError:
        datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
        datas_2 = np.load(r'{}\Material.npy'.format(path_sys), allow_pickle=True)
    datas_1 = datas_1.tolist()
    datas_2 = datas_2.tolist()
    try:
        nw, = select_1.curselection()
        Name.set(str(datas_1[nw][0]))
        Number.set(str(datas_1[nw][1]))
        #####  Bestellung_Liste.set(str(datas[nw][4]))
        Tower.set(str(datas_1[nw][2]))
        address_1.delete(1.0, "end")
        address_2.delete(1.0, "end")
        address_1.insert(1.0, str(datas_1[nw][3]))
        address_2.insert(1.0, str(datas_1[nw][4]))
        k = len(datas_2[nw])
        p = 0
        select_2.delete(0, END)
        if select_2.get(0, END):
            pass
        else:
            for i in range(k):
                select_2.insert(p, datas_2[nw][i])
                p += 1
        Label(root, text=' ', font="arial 10 bold", background='#00F5FF').place(x=120, y=263)
        Label(root, text=str(datas_1[nw][5] + ' '), font="arial 10 bold", background='#00F5FF').place(x=120, y=263)
        Zeit_String.set(str(datas_1[nw][5]))
    except ValueError or IndexError:
        pass
    if select_1.getboolean(True):
        pass
    else:
        DEL_LOAD.destroy()


# Delete Information
def delete():
    global nw
    print(checkbutton_var_3.get())
    if checkbutton_var_3.get() == True:
        print('DELETE')
        datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
        datas_2 = np.load(r'{}\Material.npy'.format(path_sys), allow_pickle=True)
        datas_1 = datas_1.tolist()
        datas_2 = datas_2.tolist()
        try:
            print(select_1.curselection(), len(datas_1))
            nw, = select_1.curselection()
            datas_1 = list(datas_1)
            datas_2 = list(datas_2)
            datas_1.pop(nw)
            datas_2.pop(nw)
            save(datas_1, datas_2)
            #######################################################
            select_1.delete(nw)
            select_2.delete(0, END)
            #######################################################
            Name.set('')
            Number.set('')
            Tower.set('')
            Bestellung_Liste.set('')
            address_1.delete(1.0, END)
            address_2.delete(1.0, END)
        except ValueError:
            pass
        check_delete(1)
        checkbutton_False_3()
    else:
        pass
    d_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
    d_1.tolist()
    Label(root, text='Aufträge:   {}'.format(len(dat_1)), font='arial 12 bold').place(x=475, y=115)


def close():
    # FTP_save()
    sys.exit()


def reset():
    Name.set('')
    Number.set('')
    Tower.set('')
    Bestellung_Liste.set('')
    address_1.delete(1.0, 'end')
    address_2.delete(1.0, 'end')
    select_2.delete(0, END)


def clear_pages():
    frame_clear = Frame(root, background='gray94', width=650, height=700)
    frame_clear.place(x=1230, y=100)


def clear_pages_ima():
    frame_clear = Frame(root, background='gray94', width=650, height=600)
    frame_clear.place(x=1230, y=180)


def clear_pages_ima_x():
    frame_clear = Frame(root, background='gray94', width=650, height=550)
    frame_clear.place(x=1230, y=180)


def HKW_T():
    img_2 = Image.open(r'{}\HKW_T.jpg'.format(path_sys))
    img_2.resize((101, 27))
    img_org_1.copy()
    img_org_1.paste(img_2, box=(205, 250))
    img_org_1.save(r'{}\Auftrag_Image.jpg'.format(path_sys))
    Image_Print(img_org_1)


def HKW_W():
    img_2 = Image.open(r'{}\HKW_W.jpg'.format(path_sys))
    img_2.resize((101, 27))
    img_org_1.copy()
    img_org_1.paste(img_2, box=(205, 250))
    img_org_1.save(r'{}\Auftrag_Image.jpg'.format(path_sys))
    Image_Print(img_org_1)

########################################       PAGE 2   ---   DOKUMENT 2      #######################################

def auftrag_einfügen():
    img_org_1.copy()
    I1 = ImageDraw.Draw(img_org_1)
    myFont = ImageFont.truetype("arial.ttf", 20)
    # Add Text to an image
    I1.text((770, 158), str(Number.get()), font=myFont, fill=(0, 0, 0))
    img_org_1.save((r'{}\Auftrag_Image.jpg'.format(path_sys)))
    Image_Print(img_org_1)


def ort_einfügen():
    img_org_1.copy()
    I1 = ImageDraw.Draw(img_org_1)
    myFont = ImageFont.truetype("arial.ttf", 20)
    # Add Text to an image
    I1.text((135, 425), str(Tower.get()), font=myFont, fill=(0, 0, 0))
    img_org_1.save((r'{}\Auftrag_Image.jpg'.format(path_sys)))
    Image_Print(img_org_1)


def Material_Geber():
    img_org_1.copy()
    I1 = ImageDraw.Draw(img_org_1)
    myFont = ImageFont.truetype("arial.ttf", 24)
    I1.text((210, next(mr)), str(MATERIAL.get()), font=myFont, fill=(0, 0, 0))
    img_org_1.save((r'{}\Auftrag_Image.jpg'.format(path_sys)))
    Image_Print(img_org_1)


def Material_Geber_2():
    img_org_2 = Image.open(r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys))
    I1 = ImageDraw.Draw(img_org_2)
    myFont = ImageFont.truetype("arial.ttf", 24)
    I1.text((425, next(mr_2)), str(MATERIAL.get()), font=myFont, fill=(0, 0, 0))
    img_org_2.save((r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys)))
    Image_Print(img_org_2)


def Name_einfügen():
    global Zelle_Plus
    img_org_1.copy()
    I1 = ImageDraw.Draw(img_org_1)
    myFont = ImageFont.truetype("arial.ttf", 20)
    I1.text((275, Zelle_Plus), str(Name.get()), font=myFont, fill=(0, 0, 0))
    img_org_1.save((r'{}\Auftrag_Image.jpg'.format(path_sys)))
    Image_Print(img_org_1)
    pass


def Name_einfügen_2():
    global Zelle_Plus_2
    img_org_2 = Image.open(r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys))
    I1 = ImageDraw.Draw(img_org_2)
    myFont = ImageFont.truetype("arial.ttf", 20)
    I1.text((275, Zelle_Plus_2), str(Name.get()), font=myFont, fill=(0, 0, 0))
    img_org_2.save((r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys)))
    Image_Print_2(img_org_2)
    pass


def Datum_einfügen():
    global Zelle_Plus, DATUM
    img_org_1.copy()
    I1 = ImageDraw.Draw(img_org_1)
    myFont = ImageFont.truetype("arial.ttf", 20)
    if DATUM.get():
        zeit_x = DATUM.get()
    else:
        zeit_x = str(time.strftime("%d.%m."))
    I1.text((105, Zelle_Plus), str(zeit_x), font=myFont, fill=(0, 0, 0))
    img_org_1.save((r'{}\Auftrag_Image.jpg'.format(path_sys)))
    Image_Print(img_org_1)


def Datum_einfügen_2():
    global Zelle_Plus_2, DATUM
    img_org_copy = Image.open(r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys))
    I1 = ImageDraw.Draw(img_org_copy)
    myFont = ImageFont.truetype("arial.ttf", 20)
    if DATUM.get():
        zeit_x = DATUM.get()
    else:
        zeit_x = str(time.strftime("%d.%m."))
    I1.text((105, Zelle_Plus_2), str(zeit_x), font=myFont, fill=(0, 0, 0))
    img_org_copy.save((r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys)))
    Image_Print_2(img_org_copy)


def Stunden_Geber():
    img_org_1.copy()
    I1 = ImageDraw.Draw(img_org_1)
    myFont = ImageFont.truetype("arial.ttf", 24)
    I1.text((590, Zelle_Plus), A_STUNDEN.get(), font=myFont, fill=(0, 0, 0))
    img_org_1.save((r'{}\Auftrag_Image.jpg'.format(path_sys)))
    Image_Print(img_org_1)


def Stunden_Geber_2():
    img_org_3 = Image.open(r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys))
    I1 = ImageDraw.Draw(img_org_3)
    myFont = ImageFont.truetype("arial.ttf", 24)
    I1.text((590, Zelle_Plus_2), A_STUNDEN.get(), font=myFont, fill=(0, 0, 0))
    img_org_3.save((r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys)))
    Image_Print(img_org_3)


def Zelle_einfügen():
    global Zelle_Plus
    print(Zelle_Plus)
    Zelle_Plus += 27
    print(Zelle_Plus)
    return Zelle_Plus


def Zelle_einfügen_2():
    global Zelle_Plus_2
    Zelle_Plus_2 += 15
    print(Zelle_Plus_2)
    return Zelle_Plus_2


def A_einfügen():
    img_org_1.copy()
    I1 = ImageDraw.Draw(img_org_1)
    myFont = ImageFont.truetype("arial.ttf", 20)
    I1.text((105, 315), address_1.get(1.0, "end-1c"), font=myFont, fill=(0, 0, 0))
    img_org_1.save((r'{}\Auftrag_Image.jpg'.format(path_sys)))
    Image_Print(img_org_1)


def B_einfügen():
    img_org_1.copy()
    I1 = ImageDraw.Draw(img_org_1)
    myFont = ImageFont.truetype("arial.ttf", 24)
    # Add Text to an image
    I1.text((105, 481), address_2.get(1.0, "end-1c"), font=myFont, fill=(0, 0, 0))
    img_org_1.save((r'{}\Auftrag_Image.jpg'.format(path_sys)))
    Image_Print(img_org_1)


def B_einfügen_2():
    img_org_2 = Image.open(r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys))
    I1 = ImageDraw.Draw(img_org_2)
    myFont = ImageFont.truetype("arial.ttf", 24)
    list_get = address_2.get(1.0, "end-1c")
    worte = list_get.split()
    worte_pro_strophe = len(worte) // 3
    strophen = [worte[i:i + worte_pro_strophe] for i in range(0, len(worte), worte_pro_strophe)]
    f = [589, 612, 637, 661]
    next_x = iter(f)
    for i, strophe in enumerate(strophen, start=1):
        print(f"Strophe {i}: {' '.join(strophe)}")
        I1.text((180, next(next_x)), ' '.join(strophe), font=myFont, fill=(0, 0, 0))
    img_org_2.save((r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys)))
    Image_Print_2(img_org_2)


def Image_Print(x):
    img_pri = x.resize((348, 480))
    image_tk = ImageTk.PhotoImage(img_pri)
    label1 = Label(image=image_tk)
    label1.image = image_tk
    label1.place(x=1410, y=140)


def Image_Print_2(x):
    img_pri_2 = x.resize((348, 480))
    image_tk_2 = ImageTk.PhotoImage(img_pri_2)
    label2 = Label(image=image_tk_2)
    label2.image = image_tk_2
    label2.place(x=1410, y=140)


def dokument_2():
    try:
        img_org_doc = Image.open(r'{}\Arbeitsnachweis_HANSE_To_PDF.png'.format(path_sys))
        img_org_doc.save(r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys))
        img_org_doc = img_org_doc.resize((348, 480))
        test_2 = ImageTk.PhotoImage(img_org_doc)
        label2 = Label(image=test_2)
        label2.image = test_2
        label2.place(x=1410, y=140)
    except FileNotFoundError:
        pass


def Arbeitsnachweis_ORIGINAL():
    global img_org_1
    img_org_1 = Image.open(r'{}\Arbeitsnachweis.jpg'.format(path_sys))
    img_1 = img_org_1.resize((348, 480))
    image_tk_1 = ImageTk.PhotoImage(img_1)
    label1 = Label(image=image_tk_1)
    label1.image = image_tk_1
    label1.place(x=1410, y=140)


def Name_Auftragsgeber():
    img_org_1.copy()
    I1 = ImageDraw.Draw(img_org_1)
    myFont = ImageFont.truetype("arial.ttf", 24)
    # Add Text to an image
    I1.text((190, 220), NAME_X.get(), font=myFont, fill=(0, 0, 0))
    img_org_1.save((r'{}\Auftrag_Image.jpg'.format(path_sys)))
    Image_Print(img_org_1)


def Material_einfügen():
    img_org_1.copy()
    I1 = ImageDraw.Draw(img_org_1)
    myFont = ImageFont.truetype("arial.ttf", 24)
    r = iter([650, 678, 707, 735, 763, 791, 819, 846, 874, 902])
    for i in select_2.get(0, END):
        I1.text((280, next(r)), str(i), font=myFont, fill=(0, 0, 0))
        img_org_1.save((r'{}\Auftrag_Image.jpg'.format(path_sys)))
    Image_Print(img_org_1)


def Material_einfügen_2():
    img_org_22 = Image.open(r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys))
    img_org_22.copy()
    I1 = ImageDraw.Draw(img_org_22)
    myFont = ImageFont.truetype("arial.ttf", 24)
    r = iter([730, 759, 788, 818, 845, 870, 895, 920])
    for i in select_2.get(0, END):
        I1.text((495, next(r)), str(i), font=myFont, fill=(0, 0, 0))
    img_org_22.save((r'{}\Arbeitsnachweis_HANSE_To_PDF_Test.png'.format(path_sys)))
    Image_Print_2(img_org_22)


def clear_buttons():
    try:
        grad_90.destroy()
        upload_B.destroy()
        X_ima.destroy()
        Y_ima.destroy()
    except NameError:
        pass


#############################################################################
###''''''''''''''''''''''''''''   COMMAND´s  '''''''''''''''''''''''''''''###
###                               FOR PAGE 2 '''''''''''''''''''''''''''''###
#############################################################################
def comm_1():  ###  '---Wohnort'  ###
    global auto_add_1
    if len(auto_add_1) > 6:
        pass
    else:
        if Tag_Var.get() == str(time.strftime("%d.%m.")):
            zeit_x = str(time.strftime("%d.%m."))
        else:
            zeit_x = Tag_Var.get()
        text_auto = '--->   Wohnort   '
        if zeit_x in auto_add_1:
            pass
        else:
            if zeit_x == '':
                zeit_x = str(time.strftime("%d.%m."))
            auto_add_1.append(zeit_x)
        if text_auto in auto_add_1[len(auto_add_1) - 1]:
            message('Die Angaben sind vorhanden...', 30)
            pass
        else:
            auto_add_1.append(text_auto)
            message_auto(auto_add_1)


def comm_2():  ###    '---HKG_Tiefstak'    ###
    if len(auto_add_1) > 6:
        pass
    else:
        text_auto = '--->   HKW_Tiefstak   '
        if text_auto in auto_add_1[len(auto_add_1) - 1]:
            message('Die Angaben sind vorhanden...', 30)
            pass
        else:
            auto_add_1.append(text_auto)
            message_auto(auto_add_1)


def comm_3():  ###    '---Hamb.Strom_HAUS_5'   ###
    if len(auto_add_1) > 6:
        pass
    else:
        text_auto = '--->   Hamb.Strom_HAUS_5   '
        if text_auto in auto_add_1[len(auto_add_1) - 1]:
            message('Die Angaben sind vorhanden...', 30)
            pass
        else:
            auto_add_1.append(text_auto)
            message_auto(auto_add_1)


def comm_4():
    global datas_fahr
    if add_adress.get() == '#101':
        datas_fahr.pop(len(auto_add_1) - 1)
        message('Lets Date is DELETED:  {}'.format(len(auto_add_1) - 1), 30)
        np.save(r'{}\Auto_fahrten.npy'.format(path_sys), datas_fahr, allow_pickle=True)
    else:
        if len(auto_add_1) > 6:
            pass
        else:
            text_auto = add_adress.get()
            if text_auto in auto_add_1[len(auto_add_1) - 1]:
                message('Die Angaben sind vorhanden...', 30)
                pass
            else:
                auto_add_1.append('-->   {}   '.format(text_auto))
                message_auto(auto_add_1)


def heute():
    Heute_Var.set(str(time.strftime("%d.%m.")))
    message(Heute_Var.get(), 30)
    pass


def abrechen_auto():
    global auto_add_1
    auto_add_1 = []
    Message_Auto = Label(root, text='', font="arial 20 bold", bg='gray94', width=95)
    Message_Auto.place(x=55, y=925)


def auto_save():
    fahrten = []
    global auto_add_1, Fahrten, datas_fahr, Kilometer, Letzte_KM, Jahr_Monat_Tag, saved
    try:
        fahrten_load = np.load(r'{}\Auto_fahrten.npy'.format(path_sys), allow_pickle=True)
        datas_fahr = fahrten_load.tolist()
    except FileNotFoundError:
        message('Die Datei ist nicht gefunden', 30)
        exit()
    try:
        datas_fahr_len = datas_fahr[len(datas_fahr) - 1]
    except IndexError:
        datas_fahr_len = 0
    ##########################################    KILOMETER   #######################################################

    if Tag_Var.get() == str(time.strftime("%d.%m.")):
        letzte_datum = [key for key in Fahrten]
        HR = len(letzte_datum) - 1
        KM = letzte_datum[HR]
        Letzte_KM = Fahrten[KM]
        Letzte_KM = Letzte_KM[6]
        print('Heute:     ', Letzte_KM)
        if auto_add_1[1] == '--->   Wohnort   ' and auto_add_1[2] == '--->   HKW_Tiefstak   ' and auto_add_1[
            3] == '--->   Wohnort   ':
            Letzte_KM = int(Letzte_KM) + 20
        if auto_add_1[1] == '--->   Wohnort   ' and auto_add_1[2] == '--->   Hamb.Strom_HAUS_5   ' and auto_add_1[
            3] == '--->   HKW_Tiefstak   ' and auto_add_1[4] == '--->   Wohnort   ':
            Letzte_KM = Letzte_KM + 26
        if Kilometer.get() > 0:
            Letzte_KM = int(Letzte_KM) + int(Kilometer.get())
            print('Rechnen: Letzte Kilometer   ', Letzte_KM)

        if len(auto_add_1) == 4:
            auto_add_1.append('')
            auto_add_1.append('')
        if len(auto_add_1) == 5:
            auto_add_1.append('')

        auto_add_1.append(str('   ' + str(Letzte_KM)))
        for i in datas_fahr:
            fahrten.append(i)
        fahrten.append(auto_add_1)
        datas_fahr = fahrten

        np.save(r'{}\Auto_fahrten.npy'.format(path_sys), datas_fahr, allow_pickle=True)
        np.save(r'{}\Auto_fahrten_KOPIE.npy'.format(path_sys), datas_fahr, allow_pickle=True)
        saved = True
    else:  ##########  Letzer Fahrt  ##########
        KM = "{}{}.{}.".format('0', str(Voriger_Tag.get()), str(Kalender_Tag.get()))
        print(KM)
        try:
            print(Fahrten)
            Letzte_KM = Fahrten[KM]
        except KeyError:
            KM = "{}{}.{}.".format('0', str(Voriger_Tag.get() - 2), str(Kalender_Tag.get()))
            try:
                Letzte_KM = Fahrten[KM]
            except KeyError:
                KM = "{}.{}.".format(str(Voriger_Tag.get()), str(Kalender_Tag.get()))
                try:
                    Letzte_KM = Fahrten[KM]
                except KeyError:
                    KM = "{}.{}.".format(str(Voriger_Tag.get() - 2), str(Kalender_Tag.get()))
                    try:
                        Letzte_KM = Fahrten[KM]
                    except KeyError:
                        letzte_datum = [key for key in Fahrten]
                        HR = len(letzte_datum) - 1
                        KM = letzte_datum[HR]
                        Letzte_KM = Fahrten[KM]
    print(Letzte_KM, '     ######################### KM #############################', KM)
    #################################################################################################################
    if saved == True:
        pass
    else:
        if auto_add_1[0] == datas_fahr[len(datas_fahr) - 1][0]:  ### ==  <--geändert
            if auto_add_1[1] == '--->   Wohnort   ' and auto_add_1[2] == '--->   HKW_Tiefstak   ' and auto_add_1[
                3] == '--->   Wohnort   ':
                print(Letzte_KM)
                Letzte_KM = int(Letzte_KM[6]) + 20
            if auto_add_1[1] == '--->   Wohnort   ' and auto_add_1[2] == '--->   Hamb.Strom_HAUS_5   ' and auto_add_1[
                3] == '--->   HKW_Tiefstak   ' and auto_add_1[4] == '--->   Wohnort   ':
                Letzte_KM = Letzte_KM + 26
            if Kilometer.get() > 0:
                Letzte_KM = int(Letzte_KM) + int(Kilometer.get())

            ################################  Andere Wege  #####################################

            ####################################################################################
            if len(auto_add_1) == 4:
                auto_add_1.append('')
                auto_add_1.append('')
            if len(auto_add_1) == 5:
                auto_add_1.append('')

            auto_add_1.append(str('   ' + str(Letzte_KM)))

            for i in datas_fahr:
                fahrten.append(i)
            A1 = auto_add_1[0]
            n = 0
            for i in fahrten:
                if A1 in i[0]:
                    print('Adress for Insert    ', n)
                    K2 = n
                    fahrten.pop(K2)
                n += 1
            print('########## _fahrten        ', fahrten)
            fahrten.insert(K2, auto_add_1)
            datas_fahr = fahrten
            print('########## _auto_add_1     ', auto_add_1)
            print('########## _fahrten        ', fahrten)
            if saved == True:
                pass
            else:
                np.save(r'{}\Auto_fahrten.npy'.format(path_sys), datas_fahr, allow_pickle=True)
                np.save(r'{}\Auto_fahrten_KOPIE.npy'.format(path_sys), datas_fahr, allow_pickle=True)
        else:
            fahrten = []
            if auto_add_1[1] == '--->   Wohnort   ' and auto_add_1[2] == '--->   HKW_Tiefstak   ' and auto_add_1[
                3] == '--->   Wohnort   ':
                print(Letzte_KM)
                Letzte_KM = Letzte_KM[6]
                Letzte_KM = int(Letzte_KM) + 20
                print('YES')
            if auto_add_1[1] == '--->   Wohnort   ' and auto_add_1[2] == '--->   Hamb.Strom_HAUS_5   ' and auto_add_1[
                3] == '--->   HKW_Tiefstak   ' and auto_add_1[4] == '--->   Wohnort   ':
                Letzte_KM = Letzte_KM + 26
            if Kilometer.get() > 0:
                Letzte_KM = int(Letzte_KM[6]) + int(Kilometer.get())
            ################################  Andere Wege  #####################################

            ####################################################################################
            if len(auto_add_1) == 4:
                auto_add_1.append('')
                auto_add_1.append('')
            if len(auto_add_1) == 5:
                auto_add_1.append('')

            auto_add_1.append(str('   ' + str(Letzte_KM)))
            for i in datas_fahr:
                fahrten.append(i)
            fahrten.append(auto_add_1)
            datas_fahr = fahrten
            if saved == True:
                pass
            else:
                np.save(r'{}\Auto_fahrten.npy'.format(path_sys), datas_fahr, allow_pickle=True)
                np.save(r'{}\Auto_fahrten_KOPIE.npy'.format(path_sys), datas_fahr, allow_pickle=True)
    auto_add_1 = []
    page_3()
    print(datas_fahr)
    saved == False


###################################   E-MAIL´s   #######################################

def E_Mail_Arne():
    global Email_Adress, Name_Email
    Name_Email = 'Arne'
    Email_Adress = 'Arne.Schimnick@hansegm.de'
    message('E-Mail an:  Arne Schimnick', 30)
    return


def E_Mail_Quacken():
    global Email_Adress, Name_Email
    Bestellung_Liste.set('J.Quacken@hiplo.de')
    message('Bestellung an:  Jutta Quacken', 30)
    return


def E_Mail_Eugen():
    global Email_Adress, Name_Email
    Name_Email = 'Eugen'
    Email_Adress = 'maljaseugen@gmail.com'
    message('E-Mail an:   Eugen Maljas', 30)
    return


def E_Mail_Anis():
    global Email_Adress, Name_Email
    Name_Email = 'Anis'
    Email_Adress = 'Anis.Gana@hansegm.de'
    message('E-Mail an:  Anis Gana', 30)
    return


def E_Mail_Yaya():
    global Email_Adress, Name_Email
    Name_Email = 'Yaya Diallo'
    Email_Adress = 'yayadiallo3@yahoo.de'
    message('E-Mail an:  Yaya Diallo', 30)
    return


def E_Mail_Sayid():
    global Email_Adress, Name_Email
    Name_Email = 'Sayid Hoosen'
    Email_Adress = 'sayid.doone@hotmail.com'
    message('E-Mail an:  Sayid Huseen', 30)
    return


def Buttons_Page_3():
    global b1, b2, Jahr_Monat, L1, alfa
    Kalendar_Set = []
    for x_mon in range(-1, 34):
        if x_mon < 1 or x_mon > 31:
            Kalendar_Set.append('')
        else:
            Kalendar_Set.append(str(x_mon))

    print('Jahr_Monat    ', Jahr_Monat)
    kalenderblatt = calendar.LocaleTextCalendar(calendar.MONDAY)
    ausgabe = kalenderblatt.formatmonth(int(Jahr_Monat[2]), Kalender_Tag.get())
    print(ausgabe)

    woche_set = ausgabe.split(' ')
    try:
        auto_fahrten = np.load(r'{}\Auto_fahrten.npy'.format(path_sys), allow_pickle=True)
        message('LADEN von Fahrten... ist ABGESCHLOSSEN', 30)
        auto_fahrten = np.array(auto_fahrten).tolist()
        for n in range(len(auto_fahrten)):
            Fahrten[auto_fahrten[n][0]] = auto_fahrten[n]

    except FileNotFoundError:
        message('Keine Datei gefunden...', 30)

    woche_add = []
    for i in woche_set:
        ln = i.split()
        woche_add.append(ln)
    print('Woche_Add   ', woche_add)
    ########################################### AI - TO HELP #################################################
    N = 0
    for i in woche_add:
        if i == ['So']:
            L1 = N
        N += 1
    ###########################################################################
    ###########################################################################
    woche_f = woche_add[L1 + 1: L1 + 20]
    ###########################################################################
    ###########################################################################
    #################################  ALFA  ##################################
    alfa = []
    for k in woche_add[L1 + 1:]:
        if len(k) > 1:
            a = k[0]
            b = k[1]
            alfa.append([a])
            alfa.append([b])
        else:
            if k == []:
                pass
            else:
                alfa.append(k)
    print('<<<Alfa>>>:   :', alfa)
    #############################################################################
    #
    # Zuerst kommt: Darf man nicht! Um zu Überleben ...
    # Zum Überleben atmen - darf man !
    #############################################################################
    Monat_M_1 = woche_add[L1 + 1: L1 + 20]

    W1 = [[], [], [], [], [], [], ['1'], [], ['2'], [], ['3'], [], ['4'], [], ['5'], ['6'], [], ['7'],
          []]  ###  Mittwoch : FEBRUAR, MÄRZ
    W2 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['1']]  ###  Sonntag  : JANUAR
    W3 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['1'], [], ['2'], ['3']]  ###  Samstag  : APRIL
    W4 = [['1'], [], ['2'], [], ['3'], [], ['4'], [], ['5'], [], ['6'], [], ['7'], ['8'], [], ['9'], ['10'], ['11'],
          ['12']]  ###  Monntag  : MAI
    W5 = [[], [], [], [], [], [], [], [], [], ['1'], [], ['2'], [], ['3'], [], ['4'], ['5'], [],
          ['6']]  ###  Donnerstag : JUNI
    W6 = [[], [], [], ['1'], [], ['2'], [], ['3'], [], ['4'], [], ['5'], [], ['6'], ['7'], [], ['8'], [],
          ['9']]  ###  Dienstag   : AUGUST
    W7 = [[], [], [], [], [], [], [], [], [], [], [], [], ['1'], [], ['2'], [], ['3'], ['4'],
          []]  ###  Freitag    : SEPTEMBER

    global woche1, woche2, woche3, woche4, woche5, woche6, woche, Tag
    if Monat_M_1 == W1:
        print('Woche 1')
        woche.set(1)

    if Monat_M_1 == W2:
        print('Woche 2')
        woche.set(2)

    if Monat_M_1 == W3:
        print('Woche 3')
        woche.set(3)

    if Monat_M_1 == W4:
        print('Woche 4')
        woche.set(4)

    if Monat_M_1 == W5:
        print('Woche 5')
        woche.set(5)

    if Monat_M_1 == W6:
        print('Woche 6')
        woche.set(6)

    if Monat_M_1 == W7:
        print('Woche 7')
        woche.set(7)

    ##############################################################
    def conter_list(x):
        global alfa
        for i in range(0, x):
            alfa.insert(0, [])
        print('PRINT LEN ALFA:   ', len(alfa))
        len_x = 37 - len(alfa)
        for i in range(0, len_x):
            alfa.append([])
        return alfa

    if woche.get() == 1:
        x = 2
        alfa = conter_list(x)
    if woche.get() == 2:
        x = 6
        alfa = conter_list(x)
    if woche.get() == 3:
        x = 5
        alfa = conter_list(x)
    if woche.get() == 4:
        len_x = 37 - len(alfa)
        for i in range(0, len_x):
            alfa.append([])
    if woche.get() == 5:
        x = 3
        alfa = conter_list(x)
    if woche.get() == 6:
        x = 1
        alfa = conter_list(x)
    if woche.get() == 7:
        x = 4
        alfa = conter_list(x)

    ##############################################################
    Wochen_Add[1] = alfa[0:  6]
    Wochen_Add[2] = alfa[7: 13]
    Wochen_Add[3] = alfa[14: 20]
    Wochen_Add[4] = alfa[21: 27]
    Wochen_Add[5] = alfa[28: 32]
    Wochen_Add[6] = alfa[35: 39]

    woche1 = alfa[0:  7]
    woche2 = alfa[7: 14]
    woche3 = alfa[14: 21]
    woche4 = alfa[21: 28]
    woche5 = alfa[28: 35]
    woche6 = alfa[35: 37]

    for i in range(1, 37):
        try:
            Wochen_Add[i] = alfa[i - 1]
        except IndexError:
            print(i)
            Wochen_Add[i] = alfa[i]
    print(Wochen_Add)

    ####################################################################################################################
    print(Wochen_Add)
    ####################################################################################################################
    Jahr_Monat = str(time.strftime("%d %m %Y"))
    print('Jahr_Monat    ', Jahr_Monat.split())
    Jahr_Monat = Jahr_Monat.split()
    if int(Jahr_Monat[0]) >= 10:
        Tag = Jahr_Monat[0]
    else:
        Tag = list(Jahr_Monat[0])
        Tag = Tag[1]

    b1.set('white')
    if woche1[0] == [int(Tag)]:
        b1.set('aqua')
    W_100 = Button(root, text=woche1[0], font="arial 10 bold", width=4, command=Kalendar_1, background=b1.get())
    W_100.place(x=1250, y=380)
    b1.set('white')
    if woche1[1] == [Tag]:
        b1.set('aqua')
    W_101 = Button(root, text=woche1[1], font="arial 10 bold", width=4, command=Kalendar_2, background=b1.get())
    W_101.place(x=1323, y=380)
    b1.set('white')
    if woche1[2] == [Tag]:
        b1.set('aqua')
    W_102 = Button(root, text=woche1[2], font="arial 10 bold", width=4, command=Kalendar_3, background=b1.get())
    W_102.place(x=1400, y=380)
    b1.set('white')
    if woche1[3] == [Tag]:
        b1.set('aqua')
    W_103 = Button(root, text=woche1[3], font="arial 10 bold", width=4, command=Kalendar_4, background=b1.get())
    W_103.place(x=1477, y=380)
    b1.set('white')
    if woche1[4] == [Tag]:
        b1.set('aqua')
    W_104 = Button(root, text=woche1[4], font="arial 10 bold", width=4, command=Kalendar_5,
                   background=b1.get())  #################
    W_104.place(x=1550, y=380)
    b1.set('white')
    if woche1[5] == [Tag]:
        b1.set('red')
    else:
        b1.set('#F08080')
    W_105 = Button(root, text=woche1[5], font="arial 10 bold", width=4, command=Kalendar_6, background=b1.get())
    W_105.place(x=1620, y=380)
    b1.set('white')
    if woche1[6] == [Tag]:
        b1.set('red')
    else:
        b1.set('#F08080')
    W_106 = Button(root, text=woche1[6], font="arial 10 bold", width=4, command=Kalendar_7, background=b1.get())
    W_106.place(x=1690, y=380)
    b1.set('white')
    if woche2[0] == [Tag]:
        b1.set('aqua')
    W_107 = Button(root, text=woche2[0], font="arial 10 bold", width=4, command=Kalendar_8, background=b1.get(), )
    W_107.place(x=1250, y=430)
    b1.set('white')
    if woche2[1] == [Tag]:
        b1.set('aqua')
    W_108 = Button(root, text=woche2[1], font="arial 10 bold", width=4, command=Kalendar_9, background=b1.get())
    W_108.place(x=1323, y=430)
    b1.set('white')
    if woche2[2] == [Tag]:
        b1.set('aqua')
    W_109 = Button(root, text=woche2[2], font="arial 10 bold", width=4, command=Kalendar_10, background=b1.get())
    W_109.place(x=1400, y=430)
    b1.set('white')
    if woche2[3] == [Tag]:
        b1.set('aqua')
    W_110 = Button(root, text=woche2[3], font="arial 10 bold", width=4, command=Kalendar_11, background=b1.get())
    W_110.place(x=1477, y=430)
    b1.set('white')
    if woche2[4] == [Tag]:
        b1.set('aqua')
    W_111 = Button(root, text=woche2[4], font="arial 10 bold", width=4, command=Kalendar_12, background=b1.get())
    W_111.place(x=1550, y=430)
    b1.set('white')
    if woche2[5] == [Tag]:
        b1.set('red')
    else:
        b1.set('#F08080')
    W_112 = Button(root, text=woche2[5], font="arial 10 bold", width=4, command=Kalendar_13, background=b1.get())
    W_112.place(x=1620, y=430)
    b1.set('white')
    if woche2[6] == [Tag]:
        b1.set('red')
    else:
        b1.set('#F08080')
    W_113 = Button(root, text=woche2[6], font="arial 10 bold", width=4, command=Kalendar_14, background=b1.get())
    W_113.place(x=1690, y=430)
    b1.set('white')
    if woche3[0] == [Tag]:
        b1.set('aqua')
    W_114 = Button(root, text=woche3[0], font="arial 10 bold", width=4, command=Kalendar_15, background=b1.get())
    W_114.place(x=1250, y=480)
    b1.set('white')
    if woche3[1] == [Tag]:
        b1.set('aqua')
    W_115 = Button(root, text=woche3[1], font="arial 10 bold", width=4, command=Kalendar_16, background=b1.get())
    W_115.place(x=1323, y=480)
    b1.set('white')
    if woche3[2] == [Tag]:
        b1.set('aqua')
    W_116 = Button(root, text=woche3[2], font="arial 10 bold", width=4, command=Kalendar_17, background=b1.get())
    W_116.place(x=1400, y=480)
    b1.set('white')
    if woche3[3] == [Tag]:
        b1.set('aqua')
    W_117 = Button(root, text=woche3[3], font="arial 10 bold", width=4, command=Kalendar_18, background=b1.get())
    W_117.place(x=1477, y=480)
    b1.set('white')
    if woche3[4] == [Tag]:
        b1.set('aqua')
    W_118 = Button(root, text=woche3[4], font="arial 10 bold", width=4, command=Kalendar_19, background=b1.get())
    W_118.place(x=1550, y=480)
    b1.set('white')
    if woche3[5] == [Tag]:
        b1.set('red')
    else:
        b1.set('#F08080')
    W_119 = Button(root, text=woche3[5], font="arial 10 bold", width=4, command=Kalendar_20, background=b1.get())
    W_119.place(x=1620, y=480)
    b1.set('white')
    if woche3[6] == [Tag]:
        b1.set('red')
    else:
        b1.set('#F08080')
    W_120 = Button(root, text=woche3[6], font="arial 10 bold", width=4, command=Kalendar_21, background=b1.get())
    W_120.place(x=1690, y=480)
    b1.set('white')
    if woche4[0] == [Tag]:
        b1.set('aqua')
    W_121 = Button(root, text=woche4[0], font="arial 10 bold", width=4, command=Kalendar_22, background=b1.get())
    W_121.place(x=1250, y=530)
    b1.set('white')
    if woche4[1] == [Tag]:
        b1.set('aqua')
    W_122 = Button(root, text=woche4[1], font="arial 10 bold", width=4, command=Kalendar_23, background=b1.get())
    W_122.place(x=1323, y=530)
    b1.set('white')
    if woche4[2] == [Tag]:
        b1.set('aqua')
    W_123 = Button(root, text=woche4[2], font="arial 10 bold", width=4, command=Kalendar_24, background=b1.get())
    W_123.place(x=1400, y=530)
    b1.set('white')
    if woche4[3] == [Tag]:
        b1.set('aqua')
    W_124 = Button(root, text=woche4[3], font="arial 10 bold", width=4, command=Kalendar_25, background=b1.get())
    W_124.place(x=1477, y=530)
    b1.set('white')
    if woche4[4] == [Tag]:
        b1.set('aqua')
    W_125 = Button(root, text=woche4[4], font="arial 10 bold", width=4, command=Kalendar_26, background=b1.get())
    W_125.place(x=1550, y=530)
    b1.set('white')
    if woche4[5] == [Tag]:
        b1.set('red')
    else:
        b1.set('#F08080')
    W_126 = Button(root, text=woche4[5], font="arial 10 bold", width=4, command=Kalendar_27, background=b1.get())
    W_126.place(x=1620, y=530)
    b1.set('white')
    if woche4[6] == [Tag]:
        b1.set('red')
    else:
        b1.set('#F08080')
    W_127 = Button(root, text=woche4[6], font="arial 10 bold", width=4, command=Kalendar_28, background=b1.get())
    W_127.place(x=1690, y=530)
    b1.set('white')
    if woche5[0] == [Tag]:
        b1.set('aqua')
    W_128 = Button(root, text=woche5[0], font="arial 10 bold", width=4, command=Kalendar_29, background=b1.get())
    W_128.place(x=1250, y=580)
    b1.set('white')
    if woche5[1] == [Tag]:
        b1.set('aqua')
    W_129 = Button(root, text=woche5[1], font="arial 10 bold", width=4, command=Kalendar_30, background=b1.get())
    W_129.place(x=1323, y=580)
    b1.set('white')
    if woche5[2] == [Tag]:
        b1.set('aqua')
    W_130 = Button(root, text=woche5[2], font="arial 10 bold", width=4, command=Kalendar_31, background=b1.get())
    W_130.place(x=1400, y=580)
    b1.set('white')
    if woche5[3] == [Tag]:
        b1.set('aqua')
    W_131 = Button(root, text=woche5[3], font="arial 10 bold", width=4, command=Kalendar_32, background=b1.get())
    W_131.place(x=1477, y=580)
    b1.set('white')
    if woche5[4] == [Tag]:
        b1.set('aqua')
    W_132 = Button(root, text=woche5[4], font="arial 10 bold", width=4, command=Kalendar_33, background=b1.get())
    W_132.place(x=1550, y=580)
    if woche5[5]:
        b1.set('white')
        if woche5[5] == [Tag]:
            b1.set('red')
        else:
            b1.set('#F08080')
        W_133 = Button(root, text=woche5[5], font="arial 10 bold", width=4, command=Kalendar_34, background=b1.get())
        W_133.place(x=1620, y=580)
        b1.set('white')
        if woche5[6] == [Tag]:
            b1.set('red')
        else:
            b1.set('#F08080')
        W_134 = Button(root, text=woche5[6], font="arial 10 bold", width=4, command=Kalendar_35, background=b1.get())
        W_134.place(x=1690, y=580)
        b1.set('white')
    print(alfa[34])
    if alfa[34] == ['29']:
        if woche6[0] == [Tag]:
            b1.set('aqua')
        W_135 = Button(root, text=woche6[0], font="arial 10 bold", width=4, command=Kalendar_36,
                       background=b1.get())
        W_135.place(x=1250, y=630)
        b1.set('white')
        if woche6[1] == [Tag]:
            b1.set('aqua')
        W_136 = Button(root, text=woche6[1], font="arial 10 bold", width=4, command=Kalendar_37,
                       background=b1.get())
        W_136.place(x=1323, y=630)


################################   PAGE 1   #################################
def page_1():
    IMAGE_to_EMAIL.set(False)
    clear_buttons()
    clear_pages()
    global select_1
    try:
        datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
        datas_1 = datas_1.tolist()
    except FileNotFoundError:
        datas_1 = ['']

    message(' AKTUELLE AUFGABEN ', 30)
    AKT = Label(root, text='                    AKTUELL                        ', font="arial 25 bold")
    AKT.place(x=1230, y=100)
    # Label(root, text='GEBÄUDE', font="arial 16 bold", bg='yellow').place(x=1400, y=100)
    # Label(root, text='BESCHREIBUNG', font="arial 16 bold", bg='yellow').place(x=1600, y=100)

    i = 0
    ds = []
    abc_size = 15
    for i_list in datas_1:
        if i_list[7] == 'GREEN':
            pass
        else:
            ds.append(i_list)
    for ip in range(200, 700, 70):
        try:
            name_x = ds[i][1]
            gebau = ds[i][2]
            beschr = ds[i][3]

            A = Label(root, text=name_x, font="arial 15 bold", bg='yellow')
            A.place(x=1230, y=ip)
            gebau_list = list(gebau)
            print(gebau_list)
            if len(gebau_list) > 9:
                abc_size = 13
            else:
                abc_size = 15
            B = Label(root, text=gebau, font="arial {} bold".format(abc_size), bg='#FFE4C4')
            B.place(x=1450, y=ip)
            if len(beschr) > 22:
                abc_size = 13
            else:
                abc_size = 15
            C = Label(root, text=beschr, font="arial {} bold".format(abc_size), bg='#CD661D')
            C.place(x=1600, y=ip)
            i += 1
        except IndexError:
            pass


################################   PAGE 1   #################################
def page_2():
    IMAGE_to_EMAIL.set(False)
    global checkbutton_var_2, img_org_1
    clear_pages()
    clear_buttons()
    check_dauer_auftrag()
    message('Senden und PDF Erstellen', 30)
    AKT = Label(root, text='                                                                 ', font="arial 25 bold")
    AKT.place(x=1230, y=100)

    Arbeitsnachweis_ORIGINAL()  ####  Load  ####

    Button(root, text="   ABBRECHEN   ", font="arial 12 bold", bg='yellow', command=checkbutton_False_2).place(x=1585,
                                                                                                               y=670)
    Button(root, text="   ERSTELLEN <<-PDF->>   ", font="arial 12 bold", bg='yellow', command=pdf_from_image).place(
        x=1585, y=710)
    Button(root, text="   SENDEN <<-PDF->>   ", font="arial 15 bold", bg='aqua', command=E_Mail).place(x=1585, y=752)

    Button(root, text=" AUFTR._EINFÜGEN ", font="arial 10 bold", command=auftrag_einfügen, background='#E9967A').place(
        x=1230, y=140)
    Button(root, text="      A-ARBEITEN   ", font="arial 10 bold", command=A_einfügen, background='#E9967A').place(
        x=1230, y=240)
    Button(root, text="      B-ARBEITEN   ", font="arial 10 bold", command=B_einfügen, background='#E9967A').place(
        x=1230, y=320)
    Button(root, text="     +MATERIAL+   ", font="arial 10 bold", command=Material_einfügen,
           background='#DFFF00').place(x=1230, y=360)

    Button(root, text="   ORT EINFÜGEN  ", font="arial 10 bold", command=ort_einfügen, background='#DFFF00').place(
        x=1230, y=280)
    Button(root, text="   NAME EINFÜGEN   ", font="arial 10 bold", command=Name_einfügen, background='#A4D3EE').place(
        x=1230, y=510)
    Button(root, text="  DATUM EINFÜGEN  ", font="arial 10 bold", command=Datum_einfügen, background='#A4D3EE').place(
        x=1230, y=470)
    Button(root, text="   NÄCHSTE ZELLE    ", font="arial 10 bold", command=Zelle_einfügen, background='#A4D3EE').place(
        x=1230, y=600)

    Button(root, text=" HKW TIEFSTACK ", font="arial 7 bold", command=HKW_T, background='#DFFF00').place(
        x=1230, y=650)
    Button(root, text="   HKW WEDEL   ", font="arial 7 bold", command=HKW_W, background='#DFFF00').place(
        x=1330, y=650)

    frame_auftr_name = Frame()
    frame_auftr_name.place(x=1230, y=200)
    Entry(frame_auftr_name, textvariable=NAME_X, font="arial 10 bold", width=15, background='#FFDAB9').pack()
    Button(root, text=">", font="arial 10 bold", command=Name_Auftragsgeber, background='#E3A869').place(x=1349, y=197)

    frame_stunden = Frame()
    frame_stunden.place(x=1230, y=550)
    Entry(frame_stunden, textvariable=A_STUNDEN, font="arial 10 bold", width=15, background='#FFDAB9').pack()
    Button(root, text=">", font="arial 10 bold", command=Stunden_Geber, background='#E3A869').place(x=1349, y=547)

    frame_material = Frame()
    frame_material.place(x=1230, y=400)
    Entry(frame_material, textvariable=MATERIAL, font="arial 10 bold", width=15, background='#FFDAB9').pack()
    Button(root, text=">", font="arial 10 bold", command=Material_Geber, background='#E3A869').place(x=1349, y=397)

    frame_datum = Frame()
    frame_datum.place(x=1230, y=440)
    Entry(frame_datum, textvariable=DATUM, font="arial 10 bold", width=15, background='#FFDAB9').pack()

    n_add = open('textdatei.txt', 'r')
    n_add_read_file = n_add.read()
    message(n_add_read_file, 30)
    img_org_1.copy()
    I1 = ImageDraw.Draw(img_org_1)
    myFont = ImageFont.truetype("arial.ttf", 24)
    # Add Text to an image
    I1.text((375, 119), str(n_add_read_file), font=myFont, fill=(0, 0, 0))
    img_org_1.save((r'{}\Auftrag_Image.jpg'.format(path_sys)))
    Image_Print(img_org_1)
    n_add.close()


################################   PAGE 3   #################################
def page_3():
    clear_buttons()
    IMAGE_to_EMAIL.set(False)
    global datas_fahr, Kilometer
    message('<<<  Autofahrten  >>>   ', 30)
    clear_pages()
    messageVar = (Message(root))
    messageVar.place(x=1230, y=300, height=370, width=550)
    messageVar.config(bg='lightgreen', font="times 20 bold", width=200)
    global auto_add_1, auto_add_2, add_adress
    Button(root, text="      Wohnort       ", font="arial 10 bold", command=comm_1).place(x=1230, y=140)
    Button(root, text="    HKW Tiefstak   ", font="arial 10 bold", command=comm_2).place(x=1360, y=140)
    Button(root, text=" Hamb.Strom HAUS 5  ", font="arial 10 bold", command=comm_3).place(x=1492, y=140)
    Button(root, text="Heute", font="arial 10 bold", command=heute, width=17, background='#FF6103').place(
        x=1230, y=250)
    Button(root, text=" Adresse Eingabe", font="arial 10 bold", command=comm_4).place(x=1400, y=200)
    Button(root, text=" ALLES SPEICHERN", font="arial 10 bold", command=auto_save, width=30).place(x=1400, y=250)
    Button(root, text=" ABBRECHEN", font="arial 10 bold", command=abrechen_auto, width=11, background='#CD2626').place(
        x=1675, y=140)

    frame4_1 = Frame()
    frame4_1.place(x=1235, y=205)
    Entry(frame4_1, textvariable=add_adress, width=25).pack()

    frame4_2 = Frame()
    frame4_2.place(x=1550, y=205)
    Entry(frame4_2, textvariable=Kilometer, width=16).pack()

    print('{}Auto_fahrten.npy'.format(path_sys))
    ##############################################   MONATE  ###########################################################

    Button(root, text=" Januar", font="arial 8 bold", command=Monat_1, width=15, borderwidth=4,
           background='#00CDCD').place(x=1230, y=680)
    Button(root, text=" Februar", font="arial 8 bold", command=Monat_2, width=15, borderwidth=4,
           background='#00CDCD').place(x=1375, y=680)
    Button(root, text=" März", font="arial 8 bold", command=Monat_3, width=15, borderwidth=4,
           background='#00CDCD').place(x=1520, y=680)
    Button(root, text=" April", font="arial 8 bold", command=Monat_4, width=15, borderwidth=4,
           background='#00CDCD').place(x=1655, y=680)
    Button(root, text=" Mai", font="arial 8 bold", command=Monat_5, width=15, borderwidth=4,
           background='#ADFF2F').place(x=1230, y=720)
    Button(root, text=" Juni", font="arial 8 bold", command=Monat_6, width=15, borderwidth=4,
           background='#ADFF2F').place(x=1375, y=720)
    Button(root, text=" July", font="arial 8 bold", command=Monat_7, width=15, borderwidth=4,
           background='#ADFF2F').place(x=1520, y=720)
    Button(root, text=" August", font="arial 8 bold", command=Monat_8, width=15, borderwidth=4,
           background='#ADFF2F').place(x=1655, y=720)
    Button(root, text=" September", font="arial 8 bold", command=Monat_9, width=15, borderwidth=4,
           background='#EEEE00').place(x=1230, y=760)
    Button(root, text=" Oktober", font="arial 8 bold", command=Monat_10, width=15, borderwidth=4,
           background='#EEEE00').place(x=1375, y=760)
    Button(root, text=" November", font="arial 8 bold", command=Monat_11, width=15, borderwidth=4,
           background='#EEEE00').place(x=1520, y=760)
    Button(root, text=" Dezember", font="arial 8 bold", command=Monat_12, width=15, borderwidth=4,
           background='#EEEE00').place(x=1655, y=760)

    ####################################################################################################################

    try:
        fahrten_load = np.load(r'{}Auto_fahrten.npy'.format(path_sys))
        datas_fahr = fahrten_load.tolist()
        Woche = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
        it = [1245, 1313, 1389, 1461, 1549, 1612, 1685]
        itr = iter(it)
        ##################################   WOCHEN TAGE   ##########################################
        for wch in Woche:
            Label(root, text=wch, font="arial 10 bold", bg='yellow').place(x=next(itr), y=320)

        datas_fahr_len = datas_fahr[len(datas_fahr) - 1]
        Label(root, text='KM: {} '.format(datas_fahr[len(datas_fahr) - 1][len(datas_fahr_len) - 1]),
              font="arial 12 bold", bg='yellow').place(x=1675, y=200)
        Letzte_KM = str(datas_fahr[len(datas_fahr) - 1][len(datas_fahr_len) - 1])
        print(Letzte_KM)


    except FileNotFoundError:
        message('Kein File gefunden', 30)

    Buttons_Page_3()

    monat = Kalender_Tag.get()
    locale.setlocale(locale.LC_ALL, 'de_DE')
    Monat_Name = calendar.month_name[monat]
    Label(root, text=Monat_Name, font="arial 15 bold", bg='#00FFFF').place(x=1677, y=250)


#########################################################################################################
#############################################   DOKUMENT 2   ################################################
def page_4():
    global img_org_2
    IMAGE_to_EMAIL.set(False)
    clear_pages()
    clear_buttons()
    message('Senden und PDF Erstellen', 30)
    AKT = Label(root, text='                                                                 ', font="arial 25 bold")
    AKT.place(x=1230, y=100)

    SCANN = Button(root, text="  <<--EINSCANNEN-->>  ", font="arial 18 bold", command=scanner_2, borderwidth=2,
                   background='#FF6103')
    SCANN.place(x=1230, y=696)

    Button(root, text="   ABBRECHEN   ", font="arial 12 bold", bg='yellow', command=dokument_2).place(x=1585,
                                                                                                      y=670)
    Button(root, text="   ERSTELLEN <<-PDF->>   ", font="arial 12 bold", bg='yellow', command=pdf_from_image_2).place(
        x=1585, y=710)
    Button(root, text="   SENDEN <<-PDF->>   ", font="arial 15 bold", bg='aqua', command=E_Mail).place(x=1585, y=752)

    Button(root, text="      A-ARBEITEN   ", font="arial 10 bold", command=B_einfügen_2, background='#E9967A').place(
        x=1230, y=320)
    Button(root, text="     +MATERIAL+   ", font="arial 10 bold", command=Material_einfügen_2,
           background='#DFFF00').place(x=1230, y=360)

    Button(root, text="   NAME EINFÜGEN   ", font="arial 10 bold", command=Name_einfügen_2, background='#A4D3EE').place(
        x=1230, y=510)
    Button(root, text="  DATUM EINFÜGEN  ", font="arial 10 bold", command=Datum_einfügen_2, background='#A4D3EE').place(
        x=1230, y=470)
    Button(root, text="   NÄCHSTE ZELLE    ", font="arial 10 bold", command=Zelle_einfügen_2,
           background='#A4D3EE').place(
        x=1230, y=600)

    frame_stunden = Frame()                 ##########   Stunden   ##########
    frame_stunden.place(x=1230, y=550)
    Entry(frame_stunden, textvariable=A_STUNDEN, font="arial 10 bold", width=15, background='#FFDAB9').pack()
    Button(root, text=">", font="arial 10 bold", command=Stunden_Geber_2, background='#E3A869').place(x=1349, y=547)

    frame_material = Frame()                ##########   Material   ##########
    frame_material.place(x=1230, y=400)
    Entry(frame_material, textvariable=MATERIAL, font="arial 10 bold", width=15, background='#FFDAB9').pack()
    Button(root, text=">", font="arial 10 bold", command=Material_Geber_2, background='#E3A869').place(x=1349, y=397)

    frame_datum = Frame()                   ##########   DATUM   ##########
    frame_datum.place(x=1230, y=440)
    Entry(frame_datum, textvariable=DATUM, font="arial 10 bold", width=15, background='#FFDAB9').pack()


def page_5():
    IMAGE_to_EMAIL.set(False)
    clear_buttons()
    clear_pages()
    global select_1
    try:
        datas_1 = np.load(r'{}\Werkstatt.npy'.format(path_sys), allow_pickle=True)
        datas_1 = datas_1.tolist()
    except FileNotFoundError:
        datas_1 = ['']

    message(' AKTUELLE AUFGABEN ', 30)
    AKT = Label(root, text='                    AKTUELL                        ', font="arial 25 bold")
    AKT.place(x=1230, y=100)
    # Label(root, text='GEBÄUDE', font="arial 16 bold", bg='yellow').place(x=1400, y=100)
    # Label(root, text='BESCHREIBUNG', font="arial 16 bold", bg='yellow').place(x=1600, y=100)

    i = 0
    ds = []
    abc_size = 15
    for i_list in datas_1:
        if i_list[7] == 'GREEN':
            pass
        else:
            ds.append(i_list)
    for ip in range(200, 700, 70):
        try:
            name_x = ds[i][1]
            gebau = ds[i][2]
            beschr = ds[i][3]

            A = Label(root, text=name_x, font="arial 15 bold", bg='yellow')
            A.place(x=1230, y=ip)
            gebau_list = list(gebau)
            print(gebau_list)
            if len(gebau_list) > 9:
                abc_size = 13
            else:
                abc_size = 15
            B = Label(root, text=gebau, font="arial {} bold".format(abc_size), bg='#FFE4C4')
            B.place(x=1450, y=ip)
            if len(beschr) > 22:
                abc_size = 13
            else:
                abc_size = 15
            C = Label(root, text=beschr, font="arial {} bold".format(abc_size), bg='#CD661D')
            C.place(x=1600, y=ip)
            i += 1
        except IndexError:
            pass


#########################################################################################################
#########################################################################################################
def Sayid():
    Name.set('Sayid')
    print()


def Yaya():
    Name.set('Yaya Diallo')
    print()


def Eugen():
    Name.set('Eugen Maljas')
    print()


###############################  NOTIZEN   ##################################


########################  Add Buttons, Label, ListBox   ######################
Name = StringVar()
Number = StringVar()
Tower = StringVar()
NAME_X = StringVar()
A_STUNDEN = StringVar()
Bestellung_Liste = StringVar()
IMAGE_to_EMAIL.set(False)

auftrag = Label(root, text="Autrag: ", font="arial 12 bold", bg='yellow').place(x=30, y=140)
name = Label(root, text="Name:   ", font="arial 12 bold", bg='yellow').place(x=30, y=180)
datum = Label(root, text="Datum: ", font="arial 12 bold", bg='yellow').place(x=30, y=260)
gebaude = Label(root, text="Gebäude: ", font="arial 12 bold", bg='yellow').place(x=30, y=220)

copyright = Label(root, text="Copyright© Eugen Maljas ", font="arial 12 bold", bg='yellow').place(x=50, y=1040)

#####################   Zeit   #######################
Data_Out = Label(root, font="arial 40 bold")
Data_Out.place(x=60, y=710)
Zeit_Out = Label(root, font="arial 70 bold")
Zeit_Out.place(x=40, y=410)

#####################  Auftrag  ######################
frame = Frame()
frame.place(x=120, y=143)
Entry(frame, textvariable=Number, width=25).pack()

#####################   Name   #######################
frame1 = Frame()
frame1.place(x=120, y=183)
Entry(frame1, textvariable=Name, width=25).pack()

#####################  Beantragte Arbeiten   #################
frame2 = Frame()
frame2.place(x=640, y=115)
Label(frame2, text='Beantragte Arbeiten:', font='arial 12 bold').pack()
address_1 = Text(frame2, width=30, height=7)
address_1.pack()

#####################  Ausgeführte Arbeiten   #################
frame21 = Frame()
frame21.place(x=940, y=115)
Label(frame21, text='Ausgeführte Arbeiten:', font='arial 12 bold').pack()
address_2 = Text(frame21, width=30, height=10)
address_2.pack()

#####################   Bestelliste   #######################
frame3 = Frame()
frame3.place(x=940, y=650)
Entry(frame3, textvariable=Bestellung_Liste, width=40).pack()

#####################  Gebäude  ######################
frame4 = Frame()
frame4.place(x=120, y=223)
Entry(frame4, textvariable=Tower, width=25).pack()

#############################################################
frame5 = Frame()
frame5.place(x=120, y=307)
Entry(frame5, textvariable=Time, width=27).pack()
Button(root, text="Zeit EINFÜGEN", font="arial 11 bold", bg="#EED8AE", command=change, width=12).place(x=310, y=300)

#####################   Message  #####################
messageVar = Message(root, text='WILLKOMMEN !!!')
messageVar.place(x=50, y=800, height=100, width=1820)
messageVar.config(bg='lightgreen', font="times 30 bold", width=1000)

Button(root, text="  SPEICHERN ", font="arial 12 bold", bg="green", command=add, width=11).place(x=310, y=140)
Button(root, text="       VIEW         ", font="arial 12 bold", command=view, width=11).place(x=310, y=180)
Button(root, text="       NEU          ", font="arial 12 bold", command=reset, width=11).place(x=310, y=220)

Button(root, text="  LÖSCHEN    ", font="arial 12 bold", bg='yellow', command=delete).place(x=470, y=680)
Button(root, text="      FERTIG     ", font="arial 12 bold", bg='#228B22', command=fertig_set).place(x=470, y=730)

#############################  Entry_List  ###############################
Button(root, text="  EINFÜGEN   ", font="arial 12 bold", bg='yellow', command=einfuegen).place(x=940, y=690)
##########################################################################

Button(root, text="   LÖSCHEN   ", font="arial 12 bold", bg='red', command=del_lists).place(x=940, y=740)
Button(root, text="  <<<BILDER>>> ", font="arial 12 bold", bg="#00C78C", width=39, command=Bilder).place(x=30, y=360)

Button(root, text=' Sayid ', font="arial 14 bold", command=Sayid).place(x=640, y=340)
Button(root, text='Eugen', font="arial 14 bold", command=Eugen).place(x=640, y=390)
Button(root, text=' Yaya ', font="arial 14 bold", command=Yaya).place(x=640, y=440)

DEL_LOAD = Button(root, text=' LOAD ', font="arial 32 bold", command=loading, background='aqua')
DEL_LOAD.place(x=735, y=340)
SCAN_to_TEXT = Button(root, text=' SCAN ', font="arial 14 bold", command=scanner_3, background='aqua')
SCAN_to_TEXT.place(x=640, y=585)

Button(root, text=' SCHLIESSEN ', font="arial 15 bold", bg='yellow', command=close).place(x=1720, y=950)
Button(root, text=' SAVE to FTP ', font="arial 15 bold", bg='yellow', command=FTP_save).place(x=1720, y=1000)

Button(root, text=' AKTUELLE AUFGABEN ', font="arial 14 bold", bg='lightgreen', command=page_1, width=46).place(x=30,
                                                                                                                y=50)
Button(root, text=' DOKUMENT 1 ', font="arial 14 bold", bg='lightgreen', command=page_2, width=25).place(x=605, y=50)
Button(root, text=' DOKUMENT 2 ', font="arial 14 bold", bg='lightgreen', command=page_4, width=25).place(x=927, y=50)
Button(root, text=' AUTO FAHRTEN NACHWEIS ', font="arial 14 bold", bg='lightgreen', command=page_3, width=45).place(
    x=1250, y=50)

Tag_Var = StringVar()
Tag_Var.set(str(time.strftime("%d.%m.")))


def Kalendar_1():
    Set_Tag.set(woche1[0][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[1]
    addition = str(0) + str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_2():
    Set_Tag.set(woche1[1][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[2]
    addition = str(0) + str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_3():
    global Kalender_Tag
    Set_Tag.set(woche1[2][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[3]
    addition = str(0) + str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_4():
    Set_Tag.set(woche1[3][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[4]
    addition = str(0) + str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_5():
    Set_Tag.set(woche1[4][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[5]
    addition = str(0) + str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_6():
    Set_Tag.set(woche1[5][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[6]
    addition = str(0) + str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_7():
    Set_Tag.set(woche1[6][0])
    Voriger_Tag.set(Set_Tag.get())
    YES = Wochen_Add[7]
    addition = str(0) + str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(Tag_Fahrt))


def Kalendar_8():
    Set_Tag.set(woche2[0][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[8]
    addition = str(0) + str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_9():
    Set_Tag.set(woche2[1][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[9]
    addition = str(0) + str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_10():
    Set_Tag.set(woche2[2][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[10]
    addition = str(0) + str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_11():
    Set_Tag.set(woche2[3][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[11]
    addition = str(0) + str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_12():
    Set_Tag.set(woche2[4][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[12]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_13():
    Set_Tag.set(woche2[5][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[13]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_14():
    Set_Tag.set(woche2[6][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[14]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_15():
    Set_Tag.set(woche3[0][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[15]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_16():
    Set_Tag.set(woche3[1][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[16]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_17():
    Set_Tag.set(woche3[2][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[17]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_18():
    Set_Tag.set(woche3[3][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[18]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_19():
    Set_Tag.set(woche3[4][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[19]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_20():
    Set_Tag.set(woche3[5][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[20]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_21():
    Set_Tag.set(woche3[6][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[21]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_22():
    Set_Tag.set(woche4[0][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[22]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_23():
    Set_Tag.set(woche4[1][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[23]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_24():
    Set_Tag.set(woche4[2][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[24]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_25():
    Set_Tag.set(woche4[3][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[25]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_26():
    Set_Tag.set(woche4[4][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[26]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_27():
    Set_Tag.set(woche4[5][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[27]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_28():
    Set_Tag.set(woche4[6][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[28]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_29():
    Set_Tag.set(woche5[0][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[29]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_30():
    Set_Tag.set(woche5[1][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[30]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_31():
    Set_Tag.set(woche5[2][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[31]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_32():
    Set_Tag.set(woche5[3][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[32]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_33():
    Set_Tag.set(woche5[4][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[33]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_34():
    Set_Tag.set(woche5[5][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[34]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_35():
    Set_Tag.set(woche5[6][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[35]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_36():
    Set_Tag.set(woche6[0][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[36]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Kalendar_37():
    Set_Tag.set(woche6[1][0])
    Voriger_Tag.set(Set_Tag.get() - 1)
    YES = Wochen_Add[37]
    addition = str((YES[0])) + str('.') + str(Kalender_Tag.get()) + str('.')
    Tag_Var.set(addition)
    try:
        Tag_Fahrt = Fahrten[addition]
    except KeyError:
        Tag_Fahrt = 'Wochenende)!!!'
    string_auto = ''
    for i in Tag_Fahrt:
        string_auto = string_auto + '' + str(i) + ''
    message_auto('{}'.format(string_auto))


def Monat_1():
    Kalender_Tag.set(1)
    page_3()


def Monat_2():
    Kalender_Tag.set(2)
    page_3()


def Monat_3():
    Kalender_Tag.set(3)
    page_3()


def Monat_4():
    Kalender_Tag.set(4)
    page_3()


def Monat_5():
    Kalender_Tag.set(5)
    page_3()


def Monat_6():
    Kalender_Tag.set(6)
    page_3()


def Monat_7():
    Kalender_Tag.set(7)
    page_3()


def Monat_8():
    Kalender_Tag.set(8)
    page_3()


def Monat_9():
    Kalender_Tag.set(9)
    page_3()


def Monat_10():
    Kalender_Tag.set(10)
    page_3()


def Monat_11():
    Kalender_Tag.set(11)
    page_3()


def Monat_12():
    Kalender_Tag.set(12)
    page_3()


def delete_message():
    messageVar = Message(root, text='')
    messageVar.place(x=50, y=800, height=100, width=1820)
    messageVar.config(bg='lightgreen', font="times 30 bold", width=1000)


def message(x, y):
    #########################     BESCHRIFTUNG      #######################
    ourMessage = x
    messageVar = Message(root, text=ourMessage)
    messageVar.place(x=50, y=800, height=100, width=1820)
    messageVar.config(bg='lightgreen', font="times {} bold".format(y), width=1000)
    messageVar.after(7000, delete_message)


def message_auto(auto_add_1):
    #########################     AUTO FARTEN --SAVE--     #######################
    global datas_fahr
    Message_Auto = Label(root, text='    ', font="arial 20 bold", bg='gray94', width=95)
    Message_Auto.place(x=55, y=925)
    string_auto = ''
    for i in auto_add_1:
        string_auto = string_auto + '' + str(i) + ''

    Message_Auto = Label(root, text=string_auto, font="arial 20 bold", bg='yellow')
    Message_Auto.place(x=75, y=925)

    print(auto_add_1)  # messageVar.place(x=1230, y=300, height=80, width=542)


TR_Bool = True
strofen_liste = [
    "#101 --- wird zum Löschen aus der Materialliste               "
    "#102 --- E-Mails senden ohne Bild-Datei                       "
    "#103 --- E-Mails senden mit Bild-Anhang                       "
    "#104 --- Speichern von bearbeiteten Bildern                   "
    "#105 --- Speichern Ordner mit Bildern                         "
    "#106 --- wird zum Löschen den Bildern                         "
]


def update_strofe():
    global TR_Bool, current_x, canvas, displayed_text, strofe_index, strofen_liste, speed
    if TR_Bool == True:
        speed = -3
        canvas = Canvas(root, width=1620, height=50, bg='#FFD39B')
        canvas.place(x=50, y=970)
        strofe_index = 0
        # gesamt_zeichenanzahl = sum(len(strophe) for strophe in strofen_liste)
        displayed_text = canvas.create_text(canvas.winfo_width(), 25, anchor='w', text=strofen_liste[strofe_index],
                                            font="arial 20 bold", fill="#000000")
        current_x = abs(canvas.bbox(displayed_text)[2])  # canvas.winfo_width() + 4000

    TR_Bool = False
    if current_x > -canvas.bbox(displayed_text)[2]:  # Überprüfen Sie, ob der Text vollständig sichtbar ist
        canvas.move(displayed_text, -3, 0)
        current_x -= 3
        speed = -3
    else:
        alpha = canvas.itemcget(displayed_text, "fill")  # Holen Sie sich die aktuelle Farbe
        if alpha.startswith("#"):
            alpha = alpha[1:]  # Entfernen Sie das "#" am Anfang
        alpha = int(alpha, 16)  # Konvertieren Sie den Hexadezimalwert in eine Dezimalzahl
        if alpha > 0:
            alpha -= 1
            alpha_hex = format(alpha, "02x")  # Konvertieren Sie den Alpha-Wert zurück in Hexadezimal
            color = f"#000000{alpha_hex}"  # Setzen Sie die Textfarbe mit neuem Alpha-Wert
            canvas.itemconfig(displayed_text, fill=color)
            root.after(20, update_strofe)
        else:
            # Strophe ist vollständig verschwunden, aktualisiere die Strophe und setze die Position zurück
            strofe_index = (strofe_index + 1) % len(strofen_liste)
            canvas.itemconfig(displayed_text, text=strofen_liste[strofe_index],
                              fill="#000000")  # Zurücksetzen der Textfarbe
            canvas.coords(displayed_text, canvas.winfo_width(), 25)  # Setzen Sie die Anfangsposition auf der rechten Seite
            current_x = abs(canvas.bbox(displayed_text)[2])
    root.after(50, update_strofe)


def add_note():
    global strofen_liste, speed, canvas, strofe_index
    user_text = address_1.get(1.0, "end-1c")
    if user_text:
        # Benutzertext als neue Strophe zur Strophenliste hinzufügen
        strofen_liste.append(user_text)
        # Starte die Animation mit der neuen Strophenliste
        strofe_index = len(strofen_liste) - 1
        canvas.itemconfig(displayed_text, text=strofen_liste[strofe_index], fill="#000000")
        canvas.coords(displayed_text, canvas.winfo_width(), 25)
    speed = -3
    update_strofe()


####################################    OPEN AI   ######################################
import openai


def chat_with_gpt(api_key, chat_history, user_input):
    openai.api_key = api_key

    # Füge die Nutzer-Eingabe zur Chat-Historie hinzu
    chat_history += '\nUser: ' + user_input

    # GPT antwortet
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=chat_history,
        temperature=0.7,
        max_tokens=150
    )

    # Extrahiere und zeige die GPT-Antwort
    gpt_response = response.choices[0].text.strip()
    print("GPT:", gpt_response)
    message(gpt_response, 30)

    # Füge die GPT-Antwort zur Chat-Historie hinzu
    chat_history += '\nGPT: ' + gpt_response
    return chat_history, gpt_response


def start_chat():
    api_key = 'sk-0000'
    chat_history = ""

    # Nutzer-Eingabe
    user_input = address_1.get(1.0, "end-1c")

    # GPT antwortet und aktualisiert die Chat-Historie
    chat_history, _ = chat_with_gpt(api_key, chat_history, user_input)


#########################  NOTIZEN  ###########################
Button(root, text="NOTIZEN", font="arial 12 bold", bg="#FFB90F", width=23, command=start_chat).place(x=642, y=274)  # add_note

update_strofe()
image_logo()
#FTP_load()
zeit_out()
root.mainloop()
