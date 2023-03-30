import sys
import pandas as pd
import pyqtgraph as pg
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                                QVBoxLayout, QLabel, QScrollArea)
from PyQt6.QtCore import QTimer,QSize
from PyQt6.QtGui import QIcon,QPixmap


class MainWindow1(QMainWindow):
    def __init__(self, Parent = None):
        super().__init__()

        self.setWindowTitle("KALPANA ALTITUDE GRAPH")
        
        self.setWindowIcon(QIcon(QPixmap("Add Ons\Team Kalpana Logo.png").scaled(QSize(200,200))))
        

        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

       
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setLabel('left', 'Altitude')
        self.plot_widget.setLabel('bottom', 'Time')
        layout.addWidget(self.plot_widget)


        self.df = pd.read_excel('Add Ons\Sample Data - Software Task.xlsx',usecols=['ALTITUDE'])


 
        self.time_index = 0
        self.data_index = 0


        self.timer = QTimer()
        self.timer.setInterval(1000)  
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        self.plot_widget.setLimits(xMin=-1)

    def update_plot(self):
        
        if self.data_index >= len(self.df):
            self.timer.stop()
            return

      
        x_data = range(self.data_index + 1)
        y_data = self.df['ALTITUDE'][:self.data_index+1]
        self.plot_widget.plot(x_data, y_data, clear=True)

        self.data_index += 1
        self.time_index += 1


class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KALPANA LAUNCH DATA")

        self.setWindowIcon(QIcon(QPixmap("Add Ons\Team Kalpana Logo.png").scaled(QSize(200,200))))

        self.setStyleSheet("background-image: url('Add Ons/Team Kalpana Logo background.png');")
        self.setStyleSheet("padding: 20px;")

        self.setGeometry(100, 100, 1050, 500)

        self.widget = QWidget()
        self.widget.setContentsMargins(20,20,20,20)
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.data = pd.read_excel("Add Ons\Sample Data - Software Task.xlsx")

        self.row = 0
        self.rows = []
        headers = self.data.columns.values.tolist()
        headers_connected1 = "\t".join([headers[0],headers[1]])
        headers_connected2 = "\t        ".join([headers_connected1,headers[2]])
        headers_connected3 = "\t     ".join([headers_connected2,headers[3]])
        headers_connected4 = "\t            ".join([headers_connected3,headers[4]])
        headers_connected5 = "\t           ".join([headers_connected4,headers[5]])
        headers_connected6 = "\t        ".join([headers_connected5,headers[6]])
        headers_connected7 = "\t            ".join([headers_connected6,headers[7]])
        headers_connected8 = "\t       ".join([headers_connected7,headers[8]])
        self.rows.append(headers_connected8)
        

        self.label = QLabel()
        self.label.setWordWrap(True)
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.label)
        self.layout.addWidget(self.scrollArea)


        self.timer = QTimer()
        self.timer.timeout.connect(self.displayRow)
        self.timer.start(1000)  
        
        

    def displayRow(self):

        
        if self.row < len(self.data):
            row_data = self.data.iloc[self.row]
            row_text =  "\t                   ".join([row_data[0],str(row_data[1])])
            row_text1 = "\t                    ".join([row_text,str(row_data[2])])
            row_text2 = "\t                            ".join([row_text1,str(row_data[3])])
            row_text3 = "\t                ".join([row_text2,str(row_data[4])])
            row_text4 = "\t                          ".join([row_text3,str(row_data[5])])
            row_text5 = "\t                         ".join([row_text4,str(row_data[6])])
            row_text6 = "\t              ".join([row_text5,str(row_data[7])])
            row_text7 = "\t            ".join([row_text6,str(row_data[8])])
            self.rows.append(row_text7)
            label = QLabel(row_text)
            label.setWordWrap(True)  
            
            
            self.row += 1
        else:
            self.timer.stop()


        
        self.label.setText("\n".join(self.rows))


class MainWindow3(QMainWindow):
    def __init__(self,Parent = None):
        super().__init__()

        self.setWindowTitle("KALPANA TEMPERATURE GRAPH")
        
        self.setWindowIcon(QIcon(QPixmap("Add Ons\Team Kalpana Logo.png").scaled(QSize(200,200))))
        

        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

       
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setLabel('left', 'Temperature')
        self.plot_widget.setLabel('bottom', 'Time')
        layout.addWidget(self.plot_widget)


        self.df = pd.read_excel('Add Ons\Sample Data - Software Task.xlsx',usecols=['TEMP'])


 
        self.time_index = 0
        self.data_index = 0


        self.timer = QTimer()
        self.timer.setInterval(1000)  
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        self.plot_widget.setLimits(xMin=-1)

    def update_plot(self):
        
        if self.data_index >= len(self.df):
            self.timer.stop()
            return

      
        x_data = range(self.data_index + 1)
        y_data = self.df['TEMP'][:self.data_index+1]
        self.plot_widget.plot(x_data, y_data, clear=True)

        self.data_index += 1
        self.time_index += 1


class MainWindow4(QMainWindow):
    def __init__(self,Parent = None):
        super().__init__()

        self.setWindowTitle("KALPANA VOLTAGE GRAPH")
        
        self.setWindowIcon(QIcon(QPixmap("Add Ons\Team Kalpana Logo.png").scaled(QSize(200,200))))
        

        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

       
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setLabel('left', 'Voltage')
        self.plot_widget.setLabel('bottom', 'Time')
        layout.addWidget(self.plot_widget)


        self.df = pd.read_excel('Add Ons\Sample Data - Software Task.xlsx',usecols=['VOLTAGE'])


 
        self.time_index = 0
        self.data_index = 0


        self.timer = QTimer()
        self.timer.setInterval(1000)  
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        self.plot_widget.setLimits(xMin=-1)

    def update_plot(self):
        
        if self.data_index >= len(self.df):
            self.timer.stop()
            return

      
        x_data = range(self.data_index + 1)
        y_data = self.df['VOLTAGE'][:self.data_index+1]
        self.plot_widget.plot(x_data, y_data, clear=True)

        self.data_index += 1
        self.time_index += 1



if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon("Add Ons\Team Kalpana Logo.png"))
    
    window1 = MainWindow1()
    window2 = MainWindow2()
    window3 = MainWindow3()
    window4 = MainWindow4()
    window2.show()
    window1.show()
    window3.show()
    window4.show()

    
    sys.exit(app.exec())
