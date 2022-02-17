from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys

import os
import uuid

import rc4

#initial rc4 GUI
class rc4Screen(QMainWindow):
    def __init__(self):
        #setup rc4 screen (main screen)
        super(rc4Screen, self).__init__()
        loadUi("ui/rc4gui.ui", self)

        self.inputBut.clicked.connect(self.inputFile) #dari file
        self.processBut.clicked.connect(self.processFile) #neken tombol process
        self.saveBut.clicked.connect(self.saveFile)
        self.path = ""

    def saveFile(self):
        cipherMethod = self.inputType.currentText()

        if cipherMethod == "Plain Text":
            if self.encBut.isChecked():
                result = self.outputTB.toPlainText() 

                text_file = open("output/encrypted.txt", "w")
                text_file.write(result)
                text_file.close()

                self.outputTB.setPlainText("%s \n\nFile saved!" %result)
            else: 
                result = self.outputTB.toPlainText() 

                text_file = open("output/decrypted.txt", "w")
                text_file.write(result)
                text_file.close()

                self.outputTB.setPlainText("%s \n\nFile saved!" %result)
        else:
            result += "File already saved"        

    def inputFile(self):
        file = QtWidgets.QFileDialog.getOpenFileName()
        self.path = file[0]

        self.inputBut.setText(self.path.split('/')[-1])

    def processFile(self):
        cipherMethod = self.inputType.currentText() #text value dropdown (tipe inputan)
        result = ""
        key = self.keyInput.toPlainText()

        #get input teks/file
        if cipherMethod == "Plain Text":
            input_text = self.textInput.toPlainText() #string text

        elif cipherMethod == "Text File":
            if(self.path != ""): #ada input file
                fileName = "output/" + str(uuid.uuid4()) + os.path.splitext(self.path)[1] #output file location (optional buat detail di result)

                ext = os.path.splitext(self.path)[1]
                if(ext == ".txt"):
                    f = open(self.path)
                    input_text = f.read() #string text
                    f.close()
                else:
                    result += ""

        else: #binaryfile
            if(self.path != ""): #ada input file
                fileName = "output/" + str(uuid.uuid4()) + os.path.splitext(self.path)[1] #output file location (optional buat detail di result)
                #open file
                f = open(self.path, 'rb')
                fileByte = f.read()
                input_text = fileByte

                input_text = bytearray(input_text) #array of ascii numbers
                f.close()

                byte_array =[] 
                a = 0
                for i in input_text: #ubah jadi list
                    byte_array.append(i)
                    a = a+1
                
            else:
                result += ""

        #get method encrypt/decrypt
        if self.encBut.isChecked(): #ENKRIPSI
            if cipherMethod == "Text File":
                if (self.path != ''): #tidak kosong
                    ct = rc4.enkripsi(input_text, key)

                    text_file = open("output/encrypted.txt", "w")
                    text_file.write(ct)
                    text_file.close()

                    result += "Encrypt success!\n"
                    result += ct
                    result += "\n\nEncrypted file directory:\n"
                    result += "output/encrypted.txt"
                else: #
                    result += "Fail encrypt file! There is no input value!"           
            elif cipherMethod == "Binary File":
                ct = rc4.enkripsi(byte_array, key)
                byteResult = bytes(ct, 'utf-8')
                
                jpg_file = open("output/encrypted.jpg", "wb")
                jpg_file.write(byteResult)
                jpg_file.close()

                result += "Encrypt success!\n\n"
                result += "Encrypted file directory:\n"
                result += "output/encrypted.jpg"
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
                result += "\n\nDecrypted file directory:\n"
                result += "output/decrypted.txt"               
            elif cipherMethod == "Binary File":
                byteResult = rc4.dekripsiBin(byte_array, key)
                byteResult = bytes(byteResult, 'utf-8')
                
                jpg_file = open("output/decrypted.jpg", "wb")
                jpg_file.write(byteResult)
                jpg_file.close()

                result += "Decrypt success!\n\n"
                result += "Encrypted file directory:\n"
                result += "output/decrypted.jpg"
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