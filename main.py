#---------Kütüphane Tanımlamaları#---------#
#------------------------------------------#

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AnasayfaUI import *
from hakkimda import *
from PyQt5.QtGui import QPixmap, QIcon
import sqlite3
import time
global curs
global conn

#-------------Ana Fonskiyonumuz------------#
#------------------------------------------#

Uygulama = QApplication(sys.argv)
anaPencere = QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(anaPencere)
anaPencere.show()


#-----------Hakkımda Sayfası-------------#
#----------------------------------------#

hakkindaPencere  = QDialog()
uiHakkimda = Ui_Dialog()
uiHakkimda.setupUi(hakkindaPencere)


#------------Veritabanı İşlemleri----------#
#------------------------------------------#

import sqlite3

conn = sqlite3.connect('veritabani.db')
curs = conn.cursor()

sorguOlustur = ("""CREATE TABLE IF NOT EXISTS envanter(Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,                 \
 TasMaliyet TEXT NOT NULL,                      \
 AltinMaliyet TEXT NOT NULL,                    \
 ToplamMaliyet TEXT NOT NULL,                   \
 SatisFiyati TEXT NOT NULL,                     \
 AliciIsmi TEXT NOT NULL,                       \
 GramKarat TEXT NOT NULL,                       \
 UrunId TEXT NOT NULL,                          \
 AliciIletisim TEXT NOT NULL,                   \
 StokSayisi TEXT NOT NULL,
 GirisTarihi TEXT NOT NULL,                      \
 SatisTarihi TEXT NOT NULL,                     \
 StokDurumu TEXT NOT NULL,                      \
 Fotograf BLOB NOT NULL,                        \
 ResimYolu TEXT NOT NULL)
""")

curs.execute(sorguOlustur)
conn.commit()


#-----------------Kayıt Ekle---------------#
#------------------------------------------#

def Ekle():

    _cmbStokdurumu = ui.cmbStokdurumu.currentText()
    _lneTasMaliyet = ui.lneTasMaliyet.text()
    _lneAltinMaliyet = ui.lneAltinMaliyet.text()
    _lneToplamMaliyet = ui.lneToplamMaliyet.text()
    _lneSatisFiyati = ui.lneSatisFiyati.text()
    _lneAliciAdi = ui.lneAliciAdi.text()
    _lneGramKarat = ui.lneKarat.text()
    _lneurunId = ui.lneurunId.text()
    _lneAliciIletisim = ui.lneAliciIletisim.text()
    _spbStokSayisi = ui.spbStokSayisi.text()
    _cwdSatisTarihi = ui.cwidSatisTarihi.selectedDate().toString(QtCore.Qt.ISODate)
    _cwdGirisTarihi = ui.cwidGirisTarihi.selectedDate().toString(QtCore.Qt.ISODate)
    _lneGramKarat = ui.lneKarat.text()
    _lneResimYolu = ui.lneResimYolu.text()
    _lneResimYoluforShow = ui.lneResimYolu.text()

    image = BinaryCeviri(_lneResimYolu)

    #if(ui.cmbStokdurumu.currentText()=='Satıldı'):
        #ui.lneAliciAdi.setEnabled()
        #ui.lneAliciIletisim.setEnabled()
        #_lneAliciAdi = ui.lneAliciAdi.text()
        #_lneAliciIletisim = ui.lneAliciIletisim.text()


    
    curs.execute("""INSERT INTO envanter
    (TasMaliyet, AltinMaliyet, ToplamMaliyet, SatisFiyati, AliciIsmi, GramKarat, UrunId, AliciIletisim, StokSayisi, GirisTarihi, SatisTarihi, StokDurumu, Fotograf, ResimYolu) 
    VALUES (?, ?, ?, ? , ? , ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
            (_lneTasMaliyet, _lneAltinMaliyet,_lneToplamMaliyet, _lneSatisFiyati, _lneAliciAdi, _lneGramKarat, _lneurunId, _lneAliciIletisim, _spbStokSayisi,_cwdGirisTarihi, _cwdSatisTarihi, _cmbStokdurumu, image, _lneResimYoluforShow))
    conn.commit()
    Listele()
    ui.statusbar.showMessage("Kayıt ekleme işlemi başarıyla gerçekleşti", 10000)

#---------------Urun Kontrol---------------#
#------------------------------------------#   

def UrunKontrol():
# Bu fonksiyon eklenen ürünün satılan bir ürün mü yoksa bekleyen bir ürün mü olduguna karar verir ve ona göre işlem yapar


    if(ui.cmbStokdurumu.currentText()=='Satıldı'):
        ui.lneAliciAdi.setEnabled(True)
        ui.lneAliciIletisim.setEnabled(True)
        ui.cwidSatisTarihi.setEnabled(True)
    
    elif(ui.cmbStokdurumu.currentText()=='Envanterde Var'):

        ui.lneAliciAdi.setDisabled(True)
        ui.lneAliciIletisim.setDisabled(True)
        ui.cwidSatisTarihi.setDisabled(True)


#--------------Envanter'e Ekleme Modu---------#
#---------------------------------------------#

def EnvanterMod():

    ui.lneAliciAdi.setDisabled(True)
    ui.lneAliciIletisim.setDisabled(True)
    ui.cwidSatisTarihi.setDisabled(True)

    ui.cmbStokdurumu.setCurrentText("Envanterde Var")

#--------------Satış  Modu--------------------#
#---------------------------------------------#

def SatisMod():

    ui.lneAliciIletisim.setEnabled(True)
    ui.lneAliciAdi.setEnabled(True)
    ui.cwidSatisTarihi.setEnabled(True)

    ui.cmbStokdurumu.setCurrentText("Satıldı")

#---------------Kayıt Güncelle-------------#
#------------------------------------------#

def KayitGuncelle():

    cevap=QMessageBox.question(anaPencere,"Kayıt Güncelle","Kaydı güncellemek istediğinize emin misiniz ?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        try:

            secili1 = ui.tableWidget.selectedItems()
            _Id = int(secili1[0].text())
            _cmbStokdurumu = ui.cmbStokdurumu.currentText()
            _lnetTasMaliyet = ui.lneTasMaliyet.text()
            _lneAltınMaliyet = ui.lneAltinMaliyet.text()
            _lneToplamMaliyet = ui.lneToplamMaliyet.text()
            _lneSatisFiyati = ui.lneSatisFiyati.text()
            _lneAliciAdi = ui.lneAliciAdi.text()
            _lneKarat = ui.lneKarat.text()
            _lneurunId = ui.lneurunId.text()
            _lneAliciIletisim = ui.lneAliciIletisim.text()
            _spbStokSayisi = ui.spbStokSayisi.text()
            _cwdSatisTarihi = ui.cwidSatisTarihi.selectedDate().toString(QtCore.Qt.ISODate)
            _cwdGirisTarihi = ui.cwidGirisTarihi.selectedDate().toString(QtCore.Qt.ISODate)

            _lneResimYolunew = ui.lneResimYolu.text()

            #------------ResimGuncelleme-----------#
            
            imagenew = BinaryCeviri(_lneResimYolunew)

            curs.execute("UPDATE envanter SET TasMaliyet=?, AltinMaliyet=?, ToplamMaliyet=?, SatisFiyati=?, AliciIsmi=?, GramKarat=?, UrunId=?, AliciIletisim=?, StokSayisi=?, GirisTarihi=?, SatisTarihi=?, StokDurumu=?,Fotograf=?, ResimYolu=? WHERE Id=?", (_lnetTasMaliyet, _lneAltınMaliyet, _lneToplamMaliyet, _lneSatisFiyati, _lneAliciAdi,  _lneKarat, _lneurunId, _lneAliciIletisim, _spbStokSayisi, _cwdGirisTarihi, _cwdSatisTarihi, _cmbStokdurumu, imagenew, _lneResimYolunew, _Id))

            conn.commit()

            Listele()


        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata meydana geldi"+str(Hata))
    else:
        ui.statusbar.showMessage("Güncelleme iptal edildi", 10000)


#-------------------Listele----------------#
#------------------------------------------#

def Listele():

    ui.tableWidget.clear()

    ui.tableWidget.setHorizontalHeaderLabels(('No', 'Tas Maliyet', 'Altın Maliyet', 'Toplam Maliyet', 'SatisFiyati', 'Alici İsmi', 'Gram Karat', 'UrunId', 'Alıcı Iletisim', 'Stok Sayisi','Giris Tarihi', 'Satis Tarihi', 'Stok Durumu', 'Fotograf', 'ResimYolu'))

    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    curs.execute("SELECT * FROM envanter")

    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            it = QTableWidgetItem()
            if sutunIndeks == 13:
                pixmap = QPixmap()
                pixmap.loadFromData(sutunVeri)
                it.setIcon(QIcon(pixmap))
                
                ui.tableWidget.setItem(satirIndeks,sutunIndeks, it)
            else:

                ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))

    ui.lneResimYolu.clear()
    ui.lneTasMaliyet.clear()
    ui.lneAltinMaliyet.clear()
    ui.lneToplamMaliyet.clear()
    ui.lneAliciIletisim.clear()
    ui.lneKarat.clear()
    ui.lneAliciAdi.clear()
    ui.lneSatisFiyati.clear()
    ui.lneurunId.clear()
    curs.execute("SELECT COUNT(*) FROM envanter WHERE StokDurumu=?", ('Envanterde Var',))  # Envanterde Var olan ürünlerin sayısını verir.
    kayitSayisi = curs.fetchone()
    ui.lblUrunsayisi.setText(str(kayitSayisi[0]))
   


Listele()

#-------------------KayıtSil------------------#
#---------------------------------------------#

def KayıtSil():
    cevap=QMessageBox.question(anaPencere,"Kayıt Sil","Kaydı silmek istediğinize emin misiniz ?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        secili = ui.tableWidget.selectedItems()
        silinecek = secili[7].text()

        try:
            curs.execute("DELETE FROM envanter WHERE UrunId='%s'" %(silinecek))
            conn.commit()
            Listele()
            ui.statusbar.showMessage("Kayıt silme başarıyla gerçekleşti", 10000)
        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir haya ile karşılaşıldı"+str(Hata))
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi....", 10000)


#-------------------KayıtAra------------------#
#---------------------------------------------#


def KayıtAra():


    aliciAdSorgu = ui.lneAliciAdi.text()
    urunIdSorgu = ui.lneurunId.text()
    envanterDurumSorgu = ui.cmbStokdurumu.currentText()
    aliciIletisimSorgu = ui.lneAliciIletisim.text()


    if(envanterDurumSorgu  == 'Envanterde Var'):
        curs.execute("SELECT * FROM envanter WHERE (StokDurumu=? AND UrunId=?)",(envanterDurumSorgu, urunIdSorgu))
        conn.commit()
    elif(envanterDurumSorgu  == 'Satıldı'):

        curs.execute("SELECT * FROM envanter WHERE(StokDurumu=? AND AliciIsmi=?) OR (AliciIletisim=? AND StokDurumu=?)", (envanterDurumSorgu, aliciAdSorgu, aliciIletisimSorgu, envanterDurumSorgu))
        conn.commit()
    
    ui.tableWidget.clear()

    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):

            it = QTableWidgetItem()
            if sutunIndeks == 13:
                #13. sütun fotoğraf içerdiği için yani string tabanlı olmadığından bu çevrim işlemini yapmamız gerekiyor.
                pixmap = QPixmap()
                pixmap.loadFromData(sutunVeri)
                it.setIcon(QIcon(pixmap))
                
                ui.tableWidget.setItem(satirIndeks,sutunIndeks, it)
            else:

                ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))


           
            ui.tableWidget.setHorizontalHeaderLabels(('No', 'Tas Maliyet', 'Altin Maliyet','Toplam Maliyet', 'SatisFiyati', 'Alici İsmi', 'Gram Karat', 'UrunId', 'Alıcı Iletisim', 'Stok Sayisi','Giris Tarihi' 'Satis Tarihi', 'Stok Durumu', 'Fotograf', 'ResimYolu'))




#------------------BinaryCeviri(SQlite Database için)-----------------#
#---------------------------------------------------------------------#

def BinaryCeviri(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

#-------------------ResimYoluBul------------------#
#-------------------------------------------------#

def ResimYoluBul():
    #Resimlerin büyük halini kullanıcıya gösterebilmek için gerekli fonksiyon

    fname = QFileDialog.getOpenFileName(caption='Open File',directory= 'C:/Users/MONSTERHAN/Desktop', filter="Images (*.png *.jpg *gif)")
    ui.lneResimYolu.setText(fname[0])
    

#-------------------ResimEkle------------------#
#----------------------------------------------#


def ResimEkle():
    # SQlite3 veritabanına resimler binary tabanlı geçebildiği için bu özel fonksiyonda resimleri binary tabanlı yapmak zorundayız.

    conn = sqlite3.connect('veritabani.db')
    curs = conn.cursor()


    sorgu = """ INSERT INTO envanter
                                  (Fotograf) VALUES (?)"""
    
    #secili = ui.tableWidget.selectedItems() # Secili item
    resimyolu = ui.lneResimYolu.text()
    
    photo = BinaryCeviri(resimyolu)

    curs.execute(sorgu, (photo,))

    conn.commit()

#-------------------ResimGoster------------------#
#------------------------------------------------#

def ResmiGoster():
    
    from PIL import Image

    resimYolu = ui.lneResimYolu.text() 

    secili = ui.tableWidget.selectedItems()

    item = secili[14].text()

    img = Image.open(item)

    img.show()


#-------------------Doldur (Yardımcı Fonksiyon)-----------------#
#---------------------------------------------------------------#

def Doldur():
    # UI üzerinde seçili olan verinin bilgileriyle kutucukları doldurur.

    secili = ui.tableWidget.selectedItems()

    try:


        ui.lneTasMaliyet.setText(secili[1].text())
        ui.lneAltinMaliyet.setText(secili[2].text())
        ui.lneToplamMaliyet.setText(secili[3].text())
        ui.lneSatisFiyati.setText(secili[4].text())
        ui.lneAliciAdi.setText(secili[5].text())
        ui.lneKarat.setText(secili[6].text())
        
        ui.lneurunId.setText(secili[7].text())
        ui.lneAliciIletisim.setText(secili[8].text())
        ui.spbStokSayisi.setValue(int(secili[9].text()))

        yilGiris = int(secili[10].text()[0:4])
        ayGiris = int(secili[10].text()[5:7])
        gunGiris = int(secili[10].text()[8:10])

        yilSatis = int(secili[11].text()[0:4])
        aySatis = int(secili[11].text()[5:7])
        gunSatis =int(secili[11].text()[8:10])

        ui.cmbStokdurumu.setCurrentText(secili[12].text())

        ui.lneResimYolu.setText(secili[14].text())
    
        ui.cwidSatisTarihi.setSelectedDate(QtCore.QDate(yilSatis, aySatis, gunSatis))
        ui.cwidGirisTarihi.setSelectedDate(QtCore.QDate(yilGiris, ayGiris, gunGiris))
    
    except IndexError:
        pass


#-------------------Temizle------------------#
#--------------------------------------------#

def Temizle():

    ui.lneResimYolu.clear()
    ui.lneTasMaliyet.clear()
    ui.lneAltinMaliyet.clear()
    ui.lneToplamMaliyet.clear()
    ui.lneAliciIletisim.clear()
    ui.lneKarat.clear()
    ui.lneAliciAdi.clear()
    ui.lneSatisFiyati.clear()
    ui.lneurunId.clear()
    ui.cmbStokdurumu.setCurrentText("-----------")
    ui.spbStokSayisi.setValue(0)

#-------------------Butun Urunleri Listele------------------#
#-----------------------------------------------------------#

def ButunUrunler():

    curs.execute("SELECT * FROM envanter WHERE StokDurumu=?", ("Envanterde Var",))

    conn.commit()
    ui.tableWidget.clear()

    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):

            it = QTableWidgetItem()
            if sutunIndeks == 13:
                pixmap = QPixmap()
                pixmap.loadFromData(sutunVeri)
                it.setIcon(QIcon(pixmap))
                
                ui.tableWidget.setItem(satirIndeks,sutunIndeks, it)
            else:

                ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))


           
            ui.tableWidget.setHorizontalHeaderLabels(('No', 'Tas Maliyet', 'Altin Maliyet','Toplam Maliyet', 'SatisFiyati', 'Alici İsmi', 'Gram Karat', 'UrunId', 'Alıcı Iletisim', 'Stok Sayisi','Giris Tarihi', 'Satis Tarihi', 'Stok Durumu', 'Fotograf', 'ResimYolu'))

#-------------------Satilan Urunleri Listele------------------#
#-------------------------------------------------------------#

def SatilanUrunler():
    curs.execute("SELECT * FROM envanter WHERE StokDurumu=?", ("Satıldı",))

    conn.commit()
    ui.tableWidget.clear()

    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):

            it = QTableWidgetItem()
            if sutunIndeks == 13:
                pixmap = QPixmap()
                pixmap.loadFromData(sutunVeri)
                it.setIcon(QIcon(pixmap))
                
                ui.tableWidget.setItem(satirIndeks,sutunIndeks, it)
            else:

                ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))


           
            ui.tableWidget.setHorizontalHeaderLabels(('No', 'Tas Maliyet', 'Altin Maliyet','Toplam Maliyet', 'SatisFiyati', 'Alici İsmi', 'Gram Karat', 'UrunId', 'Alıcı Iletisim', 'Stok Sayisi','Giris Tarihi', 'Satis Tarihi', 'Stok Durumu', 'Fotograf', 'ResimYolu'))

#-------------------Çıkış------------------#
#------------------------------------------#
 
def Cikis():
    cevap=QMessageBox.question(anaPencere,"ÇIKIŞ","Programdan çıkmak istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        conn.close()
        sys.exit(Uygulama.exec_())
    else:
        anaPencere.show()

#----------------------HAKKINDA-----------------------------#
#---------------------------------------------------------#
def Hakkinda():
    hakkindaPencere.show()


ui.hakkimda.triggered.connect(Hakkinda)

#-----------------Sinyal Slot---------------#
#-------------------------------------------#
    
ui.btnKayitEkle.clicked.connect(Ekle)
ui.btnListele.clicked.connect(Listele)
ui.btnCikis.clicked.connect(Cikis)
ui.btnSil.clicked.connect(KayıtSil)
ui.btnAra.clicked.connect(KayıtAra)
ui.tableWidget.itemSelectionChanged.connect(Doldur)
ui.btnGuncelle.clicked.connect(KayitGuncelle)
ui.btnResmiGoster.clicked.connect(ResmiGoster)
ui.btnResimYolu.clicked.connect(ResimYoluBul)
ui.btnTemizle.clicked.connect(Temizle)
ui.btnSatilanUrunler.clicked.connect(SatilanUrunler)
ui.btnUrunlerinHepsi.clicked.connect(ButunUrunler)
ui.btnEnvanterMod.clicked.connect(EnvanterMod)
ui.btnSatisMod.clicked.connect(SatisMod)

ui.cmbStokdurumu.currentTextChanged.connect(UrunKontrol)


sys.exit(Uygulama.exec_())