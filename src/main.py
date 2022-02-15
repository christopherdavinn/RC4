from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
import rc4

#initial rc4 GUI
class rc4Screen(QMainWindow):
    def __init__(self):
        #setup rc4 screen (main screen)
        super(rc4Screen, self).__init__()
        loadUi("ui/rc4gui.ui", self)

        self.inputBut.clicked.connect(self.inputFile) #dari file
        self.processBut.clicked.connect(self.processFile) #neken tombol process

        self.path = ""

    def inputFile(self):
        file = QtWidgets.QFileDialog.getOpenFileName()
        self.path = file[0]

        self.inputBut.setText(self.path.split('/')[-1])

    def processFile(self):
        #baca dari dropdown
        cipherMethod = self.inputType.currentText() #baca dropdownnya
        result = ""
        key = self.keyInput.toPlainText()

        #encrypt code
        if self.encBut.isChecked(): #baca dari radiobutton
            if cipherMethod == "Plain Text":
                pt = self.textInput.toPlainText() #str
                ct = rc4.enkripsi(pt, key)
                result += ct

            elif cipherMethod == "Text File":
                if(self.path != ""): #ada file txtnya
                    ext = os.path.splitext(self.path)[1]
                    if(ext == ".txt"):
                        f = open(self.path)
                        pt = f.read() #str
                    else:
                        result += ""

            else: #binaryfile
                if(self.path != ""):
                    directory = os.path.dirname(os.path.realpath(__file__))
                    fileName = "output/" + str(uuid.uuid4()) + os.path.splitext(self.path)[1]
                    filePath = os.path.join(directory, fileName)
                    #open file
                    f = open(filePath, 'rb')
                    fileByte = f.read()
                    pt = bytearray(fileByte) #ubah jadi byte
                    #pt = enumerate(filedata)
                else:
                    result += ""

            #proceed

        #decrypt code
        else: #baca dari radiobutton
            if cipherMethod == "Plain Text":
                ct = self.textInput.toPlainText() #str
                pt = rc4.dekripsi(ct, key)
                result += pt

        #nampilin output di tb
        self.outputTB.setPlainText(result)




#main prog
app = QApplication(sys.argv)
main = rc4Screen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main)
widget.setFixedWidth(1000)
widget.setFixedHeight(850)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")