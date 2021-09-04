from PyQt5 import uic


with open("hakkimda.py", "w", encoding="utf-8") as fout:
    uic.compileUi('hakkimda.ui', fout)