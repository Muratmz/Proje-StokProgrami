#---------Kütüphane Tanımlamaları#---------#
#------------------------------------------#

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AnasayfaUI import *


#-------------Ana Fonskiyonumuz------------#
#------------------------------------------#

Uygulama = QApplication(sys.argv)
anaPencere = QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(anaPencere)
anaPencere.show()



#------------Veritabanı İşlemleri----------#
#------------------------------------------#

import sqlite3
global curs
global conn
conn = sqlite3.connect('veritabani.db')
curs = conn.cursor()

sorguOlustur = ("""CREATE TABLE IF NOT EXISTS envanter(Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,                 \
 Maliyet TEXT NOT NULL,                         \
 Iscilik TEXT NOT NULL,                         \
 SatisFiyati TEXT NOT NULL,                     \
 AliciIsmi TEXT NOT NULL,                       \
 GramKarat TEXT NOT NULL,                       \
 UrunId TEXT NOT NULL,                          \
 AliciIletisim TEXT NOT NULL,                   \
 StokSayisi TEXT NOT NULL,                      \
 SatisTarihi TEXT NOT NULL,                     \
 StokDurumu TEXT NOT NULL)

""")

curs.execute(sorguOlustur)
conn.commit()



#-----------------Kayıt Ekle---------------#
#------------------------------------------#

def Ekle():

    _cmbStokdurumu = ui.cmbStokdurumu.currentText()
    _lneMaliyet = ui.lneMaliyet.text()
    _lneIscilik = ui.lneIscilik.text()
    _lneSatisFiyati = ui.lneSatisFiyati.text()
    _lneAliciAdi = ui.lneAliciAdi.text()
    _lneGramKarat = ui.lneKarat.text()
    _lneurunId = ui.lneurunId.text()
    _lneAliciIletisim = ui.lneAliciIletisim.text()
    _spbStokSayisi = ui.spbStokSayisi.text()
    _cwdSatisTarihi = ui.cwidSatisTarihi.selectedDate().toString(QtCore.Qt.ISODate)
    _lneGramKarat = ui.lneKarat.text()

    
    
    curs.execute("""INSERT INTO envanter
    (Maliyet, Iscilik, SatisFiyati, AliciIsmi, GramKarat, UrunId, AliciIletisim, StokSayisi, SatisTarihi, StokDurumu) 
    VALUES (?, ?, ?, ? , ? , ?, ?, ?, ?, ?);""",
            (_lneMaliyet, _lneIscilik, _lneSatisFiyati, _lneAliciAdi, _lneGramKarat, _lneurunId, _lneAliciIletisim, _spbStokSayisi, _cwdSatisTarihi, _cmbStokdurumu))
    conn.commit()
    Listele()
    ui.statusbar.showMessage("Kayıt ekleme işlemi başarıyla gerçekleşti", 10000)

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
            _lneMaliyet = ui.lneMaliyet.text()
            _lneIscilik = ui.lneIscilik.text()
            _lneSatisFiyati = ui.lneSatisFiyati.text()
            _lneAliciAdi = ui.lneAliciAdi.text()
            _lneKarat = ui.lneKarat.text()
            _lneurunId = ui.lneurunId.text()
            _lneAliciIletisim = ui.lneAliciIletisim.text()
            _spbStokSayisi = ui.spbStokSayisi.text()
            _cwdSatisTarihi = ui.cwidSatisTarihi.selectedDate().toString(QtCore.Qt.ISODate)

            curs.execute("UPDATE envanter SET Maliyet=?, Iscilik=?, SatisFiyati=?, AliciIsmi=?, GramKarat=?, UrunId=?, AliciIletisim=?, StokSayisi=?, SatisTarihi=?, StokDurumu=? WHERE Id=?", (_lneMaliyet, _lneIscilik, _lneSatisFiyati, _lneAliciAdi,  _lneKarat, _lneurunId, _lneAliciIletisim, _spbStokSayisi, _cwdSatisTarihi, _cmbStokdurumu, _Id))

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

    ui.tableWidget.setHorizontalHeaderLabels(('No', 'Maliyet', 'Iscilik', 'SatisFiyati', 'Alici İsmi', 'Gram Karat', 'UrunId', 'Alıcı Iletisim', 'Stok Sayisi', 'Satis Tarihi', 'Stok Durumu'))

    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    curs.execute("SELECT * FROM envanter")

    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))

    ui.lneAliciIletisim.clear()
    ui.lneKarat.clear()
    ui.lneIscilik.clear()
    ui.lneAliciAdi.clear()
    ui.lneSatisFiyati.clear()
    ui.lneurunId.clear()
  
    curs.execute("SELECT COUNT(*) FROM envanter")
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
        silinecek = secili[6].text()

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
    curs.execute("SELECT * FROM envanter WHERE AliciIsmi=? OR UrunId=?OR StokDurumu=? OR AliciIletisim=?", (aliciAdSorgu, urunIdSorgu, envanterDurumSorgu, aliciIletisimSorgu))
    conn.commit()
    ui.tableWidget.clear()

    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
            ui.tableWidget.setHorizontalHeaderLabels(('No', 'Maliyet', 'Iscilik', 'SatisFiyati', 'Alici İsmi', 'Gram Karat', 'UrunId', 'Alıcı Iletisim', 'Stok Sayisi', 'Satis Tarihi', 'Stok Durumu'))


#-------------------Doldur-----------------#
#------------------------------------------#

def Doldur():

    

    secili = ui.tableWidget.selectedItems()

    try:


        ui.lneMaliyet.setText(secili[1].text())
        ui.lneIscilik.setText(secili[2].text())
        ui.lneSatisFiyati.setText(secili[3].text())
        ui.lneAliciAdi.setText(secili[4].text())
        ui.lneKarat.setText(secili[5].text())
        
        ui.lneurunId.setText(secili[6].text())
        ui.lneAliciIletisim.setText(secili[7].text())
        ui.spbStokSayisi.setValue(int(secili[8].text()))
        yil = int(secili[9].text()[0:4])
        ay = int(secili[9].text()[5:7])
        gun=int(secili[9].text()[8:10])
    
        ui.cwidSatisTarihi.setSelectedDate(QtCore.QDate(yil, ay, gun))
    
    except IndexError:
        pass
    

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




#-----------------Sinyal Slot---------------#
#-------------------------------------------#
    
ui.btnKayitEkle.clicked.connect(Ekle)
ui.btnListele.clicked.connect(Listele)
ui.btnCikis.clicked.connect(Cikis)
ui.btnSil.clicked.connect(KayıtSil)
ui.btnAra.clicked.connect(KayıtAra)
#ui.tableWidget.itemPressed.connect(Doldur)
#ui.tableWidget.itemClicked.connect(Doldur)
ui.tableWidget.itemSelectionChanged.connect(Doldur)
ui.btnGuncelle.clicked.connect(KayitGuncelle)


sys.exit(Uygulama.exec_())