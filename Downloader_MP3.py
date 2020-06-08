import youtube_dl
import tkinter

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)
from PyQt5.QtCore import QCoreApplication


def download_audio(video, format_='mp3', bitrate='192'):
    download_opt = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec' : format_,
            'preferredquality' : bitrate
        }]}
    with youtube_dl.YoutubeDL(download_opt) as dl:
        print(f'Downloading audio for {video}')
        dl.download([video])


class Downlodaer(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):      
        self.btn = QPushButton('Press to download', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QLineEdit(self)
        self.le.move(136, 22)
        
        self.setGeometry(300, 300, 490, 150)
        self.setWindowTitle('MP3 DOWNLOADER from YOUTUBE')
        self.show()
        
        
    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Donwload', 'Enter link from youtube:')

        if ok:
            try:
                print(text)
                download_audio(text)
                self.le.setText('Audio file in catalog!')
            except:
                self.le.setText('Link is invalid. Try again!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Downlodaer()
    sys.exit(app.exec_())