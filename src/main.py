from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
import rc4
import codecs
import os
import uuid

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
                f = open(self.path, 'rb')
                fileByte = f.read()
                input_text = bytearray(fileByte) #array of ascii numbers
                
                # input_text =[]
                # a = 0
                # for i in byte_array:
                #     input_text.append(i)
                #     a = a+1            
                f.close()
            else:
                result += ""

        #get method encrypt/decrypt
        if self.encBut.isChecked(): #ENKRIPSI
            if cipherMethod == "Text File":
                if (ct != ''): #tidak kosong
                    ct = rc4.enkripsi(input_text, key)
                    result += "Encrypt success!\n"
                    result += ct
                    print(result)
                    text_file = open("output/encrypted.txt", "w")
                    text_file.write(ct)
                    text_file.close()
                else: #
                    result += "Fail encrypt file! There is no input value!"
            
            elif cipherMethod == "Binary File":
                byte_array =[]
                a = 0
                for i in input_text:
                    byte_array.append(i)
                    a = a+1    
                ct = rc4.enkripsi(byte_array, key)
                byteResult = bytes(ct, 'utf-8')
                #print(byte)
                result += "Encrypt success!\n"

                jpg_file = open("output/ecrypted.jpg", "wb")
                jpg_file.write(byteResult)
                jpg_file.close()
            else: #input dari keyboard
                ct = rc4.enkripsi(input_text, key)
                result += ct

        else: #decrypt method
            if cipherMethod == "Text File":
                pt = rc4.dekripsi(input_text, key)
                text_file = open("output/decrypted.txt", "w")
                text_file.write(pt)
                text_file.close()
                result += "Decrypt success!\n"
                result += pt
                
            elif cipherMethod == "Binary File":
                #ss = rc4.convertToChar(input_text)

                pt = rc4.dekripsi(input_text, key)
                byteResult = bytes(pt, 'utf-8')
                #print(byte)
                result += "yeay"

                jpg_file = open("output/decrypted.jpg", "wb")
                jpg_file.write(byteResult)
                jpg_file.close()

            else: #keyboard
                pt = rc4.dekripsi(input_text, key)
                result += pt

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