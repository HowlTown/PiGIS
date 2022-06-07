# File: main.py
import sys

from PySide6.QtWidgets import QApplication

from ui.MainWindow import MainWindow

from PiMapObj.PiLayer import PiLayer
from PiMapObj.PiProjection import PiProjection

if __name__ == '__main__':
    '''小陈添加语句'''
    layer1 = PiLayer()
    layer2 = PiLayer()
    layer3 = PiLayer()
    proj = PiProjection()
    layer1.load("PiMapObj/图层文件/国界线.lay","PiMapObj/图层文件/图层文件坐标系统说明.txt")
    layer2.load("PiMapObj/图层文件/省级行政区.lay","PiMapObj/图层文件/图层文件坐标系统说明.txt")
    layer3.load("PiMapObj/图层文件/省会城市.lay","PiMapObj/图层文件/图层文件坐标系统说明.txt")
    at = layer2.get_attr_table()
    #print(layer2.get_attr_table())
    #print(at)
    #print(layer2.features.features[0].attributes)
    ''''''

    app = QApplication(sys.argv)

    window = MainWindow()
    '''小陈添加语句'''
    window.xiaochen_load_layers([layer1,layer2,layer3])
    ''''''
    window.show()

    sys.exit(app.exec())
