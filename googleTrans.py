import sys

from PyQt5 import uic #uic ui불러오기 위함/qt디자인에서 제작한 ui 불러는 클래스
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import googletrans #------------- 모든 모듈 준비 ---------

form_class = uic.loadUi('ui/gooUi.ui')[0]
#qt 디자이너에서 제작한 ui 불러오기

class MyGoogleTrans(QMainWindow, form_class):#두개 상속받음
    def __init__(self):#초기화자(생성자)
        super().__init__()#부모 클래스의 초기화자를 호출
        self.setupUi(self)#제작해 놓은 구글 ui 를 연결
        self.setWindowTitle('구글 번역기')#번역기 앱 타이틀
        self.setWindowIcon(QIcon('icon/goo1.png'))#번역기 앱 아이콘
        self.statusBar().showMessage('Google Trans App v1.0 copyright ⓒ W. conpany ')#상태표시줄

if __name__=='__main__':#다른곳에서 불러도 실행 안되도록 함
    app= QApplication(sys.argv)
    myApp=MyGoogleTrans()
    myApp.show()
    sys.exit(app.exec_())

    





