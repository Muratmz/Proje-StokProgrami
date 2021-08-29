from PyQt5 import uic


with open("AnasayfaUI.py", "w", encoding="utf-8") as fout:
    uic.compileUi('Anasayfa.ui', fout)
