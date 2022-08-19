from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from mainWindow import Ui_MainWindow
from pptx import Presentation
from datetime import datetime
import PIL
from PIL import ImageGrab, Image
import pyautogui

#아직 구현하지 못한 것.
# 1. clean code

class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

    def make_ppt(self):
        try:
            title = self.titleEdit.text()
            inform = self.informEdit.toPlainText()
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S\n")
            current_text = current_time + inform
            img_path = self.imgLabel.text()

            # 본인의 base가 될 ppt 를 지정하여서 slide에 있는 shape를 지정해주고 그 shape 의 type에 맞게 데이터를 넣어주면 된다.
            prs = Presentation('base.pptx')
            main_slide = prs.slides[0]

            shape_list = main_slide.shapes
            shape_index = {}
            for i, shape in enumerate(shape_list):
                shape_index[shape.name] = i

            # 제목
            title_select = shape_list[shape_index['title_box']].text_frame
            title_select.text = title

            # 사진
            img_select = shape_list[shape_index["img_box"]]
            img_select.insert_picture(img_path)

            # inform
            text_select = shape_list[shape_index['text_box']].text_frame
            text_select.text = current_text
            
            # 파일 저장 양식
            output = now.strftime("%Y-%m-%d %H_%M_%S") + '.pptx'
            prs.save(output)
            QMessageBox.about(self, "About", "Work Done!")
            QApplication.closeAllWindows()
        # 예외 처리
        except FileNotFoundError:
            QMessageBox.warning(self, "Error!", "There is no image File.\n Please select image file or capture screen.")
        except PIL.UnidentifiedImageError:
            QMessageBox.warning(self, "Error!", "You selected wrong type of file.\n File type is must be image.")

    def capture_screen(self):
        pyautogui.hotkey('win', 'shift', 's')

    def upload_func(self):
        try:
            img_file = QFileDialog.getOpenFileName(self, filter="PNG (*.png);; JPEG (*.jpg *.jpeg);; All files (*.*)")
            self.imgLabel.setText(img_file[0])
        except IndexError:
            pass

    def get_img(self):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H_%M_%S")
        img_name = current_time + '.png'
        # get image from clipboard
        img = ImageGrab.grabclipboard()
        img.save(img_name, 'PNG')
        self.imgLabel.setText(img_name)
        # resize image
        im = Image.open(img_name)
        im = im.resize((644, 400))
        im = im.convert('RGB')
        im.save(img_name, 'PNG')

app = QApplication()
win = mainWindow()
win.show()
app.exec()
