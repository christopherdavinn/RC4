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
        cipherMethod = self.inputType.currentText() #baca dropdownnya
        result = ""
        key = self.keyInput.toPlainText()

        #get input teks/file
        if cipherMethod == "Plain Text":
            input_text = self.textInput.toPlainText() #string text

        elif cipherMethod == "Text File":
            if(self.path != ""): #ada input file
                ext = os.path.splitext(self.path)[1]
                if(ext == ".txt"):
                    f = open(self.path)
                    input_text = f.read() #string text
                    f.close()
                else:
                    result += ""

        else: #binaryfile
            if(self.path != ""): #ada input file
                directory = os.path.dirname(os.path.realpath(__file__))
                fileName = "output/" + str(uuid.uuid4()) + os.path.splitext(self.path)[1]
                filePath = os.path.join(directory, fileName)
                #open file
                f = open(filePath, 'rb')
                fileByte = f.read()
                input_text = bytearray(fileByte) #array of ascii numbers
                f.close()
            else:
                result += ""

        #get method encrypt/decrypt
        if self.encBut.isChecked(): #ENKRIPSI
            ct = rc4.enkripsi(input_text, key)
            result += ct

            if cipherMethod == "Text File":
                #perlu di save ke textfile kan??
                text_file = open("ecnrypted.txt", "w")
                text_file.write(result)
                text_file.close()
            elif cipherMethod == "Binary File":
                f = open(filePath, 'wb')
                f.write(result)
                f.close()

        else: #decrypt method
            pt = rc4.dekripsi(input_text, key)
            result += pt

            if cipherMethod == "Text File":
                #perlu di save ke textfile kan??
                text_file = open("decrypted.txt", "w")
                text_file.write(result)
                text_file.close()
            elif cipherMethod == "Binary File":
                f = open(filePath, 'wb')
                f.write(result)
                f.close()

        #nampilin output di tb
        self.outputTB.setPlainText(result)

#main program
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