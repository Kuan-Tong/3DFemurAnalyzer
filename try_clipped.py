from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import vtk
# from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import numpy as np
from natsort import natsorted
import cv2

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200,800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.gridlayout = QtWidgets.QGridLayout(self.centralwidget)                  #网格布局类
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.vtkWidget = QVTKRenderWindowInteractor(self.centralwidget)
        self.textEdit = QTextEdit()
        self.gridlayout.addWidget(self.vtkWidget, 0, 0, 100, 100)

        self.gridlayout.addWidget(self.textEdit, 0, 100, 100, 30)

        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        # self.actionSave = QtWidgets.QAction(MainWindow)
        # self.actionSave.setObjectName("actionSave")
        # self.actionSave_As = QtWidgets.QAction(MainWindow)
        # self.actionSave_As.setObjectName("actionSave_As")

        self.actionOpen.triggered.connect(self.open)
        # self.actionSave_As.triggered.connect(self.save_as)

        # self.actionExit = QtWidgets.QAction(MainWindow)
        # self.actionExit.setObjectName("actionExit")
        # self.actionUndo = QtWidgets.QAction(MainWindow)
        # self.actionUndo.setObjectName("actionUndo")
        self.buttonDown = QtWidgets.QPushButton("Save")
        self.gridlayout.addWidget(self.buttonDown, 100, 50, 1, 1)         #网格布局类
        self.buttonDown1 = QtWidgets.QPushButton("Save_Clipped")
        self.gridlayout.addWidget(self.buttonDown1, 100, 55, 1, 1)  # 网格布局类
        # self.gridlayout.addWidget(self.buttonDown, 0,  Qt.AlignBottom )           # 水平布局类
        self.number = 0
        self.buttonDown.clicked.connect(self.about)
        self.buttonDown1.clicked.connect(self.save_clipped)
        self.menuFile.addAction(self.actionOpen)
        # self.menuFile.addAction(self.actionSave)
        # self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        # self.menuFile.addAction(self.actionExit)
        # self.menuEdit.addAction(self.actionUndo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        # self.setGeometry(400, 400, 300, 260)
        # self.checkBox1 = QCheckBox("&Checkbox 1")
        # self.checkBox2 = QCheckBox("&Checkbox 2")
        # self.checkBox2.setChecked(True)
        # self.tristateBox = QCheckBox("Tri-&state button")
        # self.tristateBox.setTristate(True)
        # self.tristateBox.setCheckState(Qt.PartiallyChecked)

        # self.lcd = QTextBrowser()
        # self.lcd.setFixedHeight(190)
        # self.lcd.setFont(QFont("Microsoft YaHei", 20))
        # self.lcd.setText(self.getCheckBoxStatus())

        # mainLayout = QVBoxLayout()
        # mainLayout.addWidget(groupBox)
        # mainLayout.addWidget(self.lcd)
        # self.setLayout(mainLayout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def getCheckBoxStatus(self):
    #     status = self.checkBox1.text()+":  "+ str(self.checkBox1.checkState()) +"\n" +self.checkBox2.text()+":  "+ str(self.checkBox2.checkState()) \
    #              +"\n"+self.tristateBox.text()+":  "+ str(self.tristateBox.checkState())
    #     return status

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clip_model"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        # self.actionSave.setText(_translate("MainWindow", "Save"))
        # self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        # self.actionExit.setText(_translate("MainWindow", "Exit"))
        # self.actionUndo.setText(_translate("MainWindow", "Undo"))

    # def save_as(self):
    #     self.save_path = QFileDialog.getExistingDirectory(self, "choose folder", "C:/")
    #     print(self.save_path)
    #     self.save_as_path()
    #
    # def save_as_path(self):

        # file_path = QFileDialog.getSaveFileName(self, "save file", "./")
        # print('zxy nice!!!')

    def save_clipped(self):
        self.save_path = QFileDialog.getExistingDirectory(self, "choose folder", r"D:\123")
        self.femur_seg(self.data_path, self.save_path, self.PlaneNormal1, self.PlaneOrigin1, self.PlaneNormal2,
                       self.PlaneOrigin2, self.PlaneNormal3, self.PlaneOrigin3)
        self.textEdit.append("save clipped")

    def about(self):
        # insertHtml(str)插入文本是将文本插入到光标处
        # append(str)追加文本是将文本追加到文本末尾
        # print(self.textEdit.toPlainText())

        self.number = self.number + 1
        # self.textEdit.append("save data")


        self.save()

    def save(self):
        if self.number == 1:
            # self.PlaneNormal = self.textEdit.toPlainText().split('\n')[0].split('=')[1].split('(')[1].split(')')[0]
            #
            # # print(type(PlaneNormal))
            # # print(np.array(PlaneNormal))
            # self.PlaneNormal = self.PlaneNormal.split(',')
            self.PlaneNormal1 = self.PlaneNormal
            self.PlaneOrigin1 = self.PlaneOrigin
            self.textEdit.append("save data")
            # print(type(PlaneNormal))
            # print(self.PlaneNormal)
            # self.PlaneOrigin = self.textEdit.toPlainText().split('\n')[1].split('=')[1].split('(')[1].split(')')[0]
            # self.PlaneOrigin = self.PlaneOrigin.split(',')
            # print(self.PlaneOrigin)
        elif self.number == 2:
            self.PlaneNormal2 = self.PlaneNormal
            self.PlaneOrigin2 = self.PlaneOrigin
            self.textEdit.append("save data")
            # self.PlaneNormal1 = self.textEdit.toPlainText().split('\n')[0].split('=')[1].split('(')[1].split(')')[0]
            # self.PlaneNormal1 = self.PlaneNormal1.split(',')
            # # print(self.PlaneNormal1)
            # # print('PlaneNormal1='+self.PlaneNormal1)
            # self.PlaneOrigin1 = self.textEdit.toPlainText().split('\n')[1].split('=')[1].split('(')[1].split(')')[0]
            # # print('PlaneOrigin1='+self.PlaneOrigin1)
            # self.PlaneOrigin1 = self.PlaneOrigin1.split(',')
        elif self.number == 3:
            self.PlaneNormal3 = self.PlaneNormal
            self.PlaneOrigin3= self.PlaneOrigin
            self.textEdit.append("save data")
            # self.PlaneNormal2 = self.textEdit.toPlainText().split('\n')[0].split('=')[1].split('(')[1].split(')')[0]
            # # print('PlaneNormal2='+self.PlaneNormal2)
            # self.PlaneNormal2 = self.PlaneNormal2.split(',')
            # self.PlaneOrigin2 = self.textEdit.toPlainText().split('\n')[1].split('=')[1].split('(')[1].split(')')[0]
            # # print('PlaneOrigin2='+self.PlaneOrigin2)
            # self.PlaneOrigin2 = self.PlaneOrigin2.split(',')
        elif self.number >= 4:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', 'Three planes have been selected!')
            msg_box.exec_()
            # if self.number == 4:
        #     self.femur_seg(self.data_path, self.save_path, self.PlaneNormal1, self.PlaneOrigin1, self.PlaneNormal2, self.PlaneOrigin2, self.PlaneNormal3, self.PlaneOrigin3)

    def get_image_data(self,img_dir, i):
        test_data = []
        test_list = natsorted([img_dir + '/' + s for s in os.listdir(img_dir)])
        # print(len(test_list))
        for test in test_list:
            # print(test+'\n')
            img = cv2.imread(test,i)
            ret, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            # cv2.imwrite(pic_path+str(i)+".png",binary)
            test_data.append(binary)
        test = np.array(test_data)
        # print(test.shape)
        return test

    def make_dir(self,save_path):
        if not os.path.isdir(save_path):
            os.makedirs(save_path)

    def femur_seg(self,img_path, save_path, normal, point, normal1, point1, normal2, point2):
        # 输入的npy格式是一般是（x,y,z）,我们要将其转换为(y,x,z)
        data = self.get_image_data(img_path, 0)
        print(data.shape)
        data = data.transpose((2, 1, 0))
        print(data.shape)
        point_index = np.zeros((data.shape[0], data.shape[1], data.shape[2], 3))
        mask_head = np.zeros(data.shape)
        mask_head_tmp = np.zeros(data.shape)
        mask_neck = np.zeros(data.shape)
        mask_tro = np.zeros(data.shape)
        a11 = np.zeros((data.shape[0], data.shape[1], data.shape[2], 3))
        # 建立坐标矩阵，大小为[x * y * z * 3]
        for i in range(0, data.shape[0]):
            point_index[i, :, :, 0] = i
        for j in range(0, data.shape[1]):
            point_index[:, j, :, 1] = j
        for k in range(0, data.shape[2]):
            point_index[:, :, k, 2] = k
        # 判断点在法向量的哪个方向，大于0在上方，小于0在下方
        #####################################
        # get FH
        point_index_tmp = point_index.copy()
        point_index_tmp = (point_index_tmp - point) @ np.array(normal)
        plane1_index = np.where(point_index_tmp < 0)
        plane1_index_tmp = np.where(point_index_tmp > 0)
        plane1_index = np.array(plane1_index)
        plane1_index_tmp = np.array(plane1_index_tmp)
        mask_head_tmp[plane1_index_tmp[0, :], data.shape[1] - plane1_index_tmp[1, :] - 1, plane1_index_tmp[2, :]] = 1
        mask_head[plane1_index[0, :], data.shape[1] - plane1_index[1, :] - 1, plane1_index[2, :]] = 1
        head_result = mask_head * data
        head_result = head_result.transpose(2, 1, 0)
        ######################################
        # get FN
        point_index_tmp = point_index.copy()
        point_index_tmp = (point_index_tmp - point1) @ np.array(normal1)
        plane2_index = np.where(point_index_tmp < 0)
        plane2_index = np.array(plane2_index)
        mask_neck[plane2_index[0, :], data.shape[1] - plane2_index[1, :] - 1, plane2_index[2, :]] = 1
        neck_result = mask_neck * data * mask_head_tmp
        neck_result = neck_result.transpose(2, 1, 0)
        ######################################
        # get tro
        # point_index_tmp = point_index.copy()
        # point_index_tmp = (point_index_tmp - point2) @ np.array(normal2)
        # plane3_index = np.where(point_index_tmp < 0)
        # plane3_index = np.array(plane3_index)
        # mask_tro[plane3_index[0, :], data.shape[1] - plane3_index[1, :] - 1, plane3_index[2, :]] = 1
        # tro_result = mask_tro * data * mask_head_tmp
        # tro_result = tro_result.transpose(2, 1, 0)
        ######################################
        # save results
        self.make_dir(save_path + '/head')
        self.make_dir(save_path + '/neck')
        # self.make_dir(save_path + '/tro')
        for k in range(0, data.shape[2]):
            cv2.imwrite(save_path + '/head/' + str(k) + ".png", head_result[k, :, :])
            cv2.imwrite(save_path + '/neck/' + str(k) + ".png", neck_result[k, :, :])
            # cv2.imwrite(save_path + '/tro/' + str(k) + ".png", tro_result[k, :, :])
    def test(self):
        print("hahahaha")

    def open(self):
        directory = QFileDialog.getExistingDirectory(self, "choose folder", "./")+'/'

        self.data_path = directory
        print(directory)

        self.Reader.SetDataExtent(0, 512, 0, 512, 0, len(os.listdir(self.data_path)) - 1)
        self.Reader.SetFilePrefix(self.data_path)
        self.Reader.SetFilePattern("%s%d.png")
        self.Reader.SetDataSpacing(1,1,1)  # Volume Pixel
        self.Reader.Update()

        self.skinExtractor = vtk.vtkContourFilter()
        self.skinExtractor.SetInputConnection(self.Reader.GetOutputPort())
        self.skinExtractor.SetValue(0, 1)
        self.skinExtractor.ComputeGradientsOn()
        self.skinExtractor.ComputeScalarsOn()
        self.smooth = vtk.vtkSmoothPolyDataFilter()
        self.smooth.SetInputConnection(self.skinExtractor.GetOutputPort())
        self.smooth.SetNumberOfIterations(700)

        self.skinNormals = vtk.vtkPolyDataNormals()
        self.skinNormals.SetInputConnection(self.smooth.GetOutputPort())
        self.skinNormals.SetFeatureAngle(50)

        self.skinStripper = vtk.vtkStripper()
        self.skinStripper.SetInputConnection(self.skinNormals.GetOutputPort())

        self.skinMapper = vtk.vtkPolyDataMapper()
        self.skinMapper.SetInputConnection(self.skinStripper.GetOutputPort())
        self.skinMapper.ScalarVisibilityOff()

        self.skin = vtk.vtkActor()
        self.skin.GetProperty().SetDiffuseColor(1, .19, .15)
        self.skin.SetMapper(self.skinMapper)

        # 定义一个图像边界控件
        self.outlineData = vtk.vtkOutlineFilter()
        self.outlineData.SetInputConnection(self.Reader.GetOutputPort())

        self.mapOutline = vtk.vtkPolyDataMapper()
        self.mapOutline.SetInputConnection(self.outlineData.GetOutputPort())

        self.outline = vtk.vtkActor()
        self.outline.SetMapper(self.mapOutline)
        self.outline.GetProperty().SetColor(0, 0, 0)

        self.aCamera = vtk.vtkCamera()
        self.aCamera.SetViewUp(0, 0, -1)
        self.aCamera.SetPosition(0, 1, 0)
        self.aCamera.ComputeViewPlaneNormal()
        self.aCamera.Azimuth(30.0)
        self.aCamera.Elevation(30.0)
        self.aCamera.Dolly(1.5)
        self.arender.AddActor(self.outline)
        self.arender.AddActor(self.skin)

        self.arender.SetActiveCamera(self.aCamera)
        self.arender.ResetCamera()
        self.arender.SetBackground(.2, .3, .4)
        self.arender.ResetCameraClippingRange()

        # self.renWin.SetSize(1000, 700)
        self.style = vtk.vtkInteractorStyleTrackballCamera()
        self.iren.SetInteractorStyle(self.style)

        # 定义切割器
        global cliper
        self.cliper = vtk.vtkClipPolyData()
        self.cliper.SetInputData(self.skinStripper.GetOutput())
        # 定义平面隐函数
        self.implicitPlaneWidget = vtk.vtkImplicitPlaneWidget()
        self.implicitPlaneWidget.SetInteractor(self.iren)
        self.implicitPlaneWidget.SetPlaceFactor(1.25)
        self.implicitPlaneWidget.SetInputData(self.skinStripper.GetOutput())
        self.implicitPlaneWidget.PlaceWidget()
        self.implicitPlaneWidget.AddObserver("EndInteractionEvent", self.execute)
        self.implicitPlaneWidget.On()
        global coneSkinActor
        self.coneSkinActor = vtk.vtkActor()
        self.coneSkinActor.SetMapper(self.skinMapper)

        self.coneSkinActor.RotateZ(90)
        self.rRenderer.AddActor(self.coneSkinActor)

        self.iren.Initialize()
        self.iren.Start()

    def init_vtk(self):
        self.arender = vtk.vtkRenderer()
        self.arender.SetViewport(0, 0.0, 0.5, 1.0)
        self.vtkWidget.GetRenderWindow().AddRenderer(self.arender)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        self.Reader = vtk.vtkPNGReader()
        self.Reader.SetNumberOfScalarComponents(1)
        self.Reader.GetOutput().GetOrigin()
        self.Reader.SetDataByteOrderToLittleEndian()
        self.Reader.SetFileDimensionality(3)

        self.arender.SetBackground(.2, .3, .4)
        self.arender.ResetCameraClippingRange()

        self.rRenderer = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.rRenderer)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        self.rRenderer.SetBackground(0.2, 0.3, 0.5)
        self.rRenderer.SetViewport(0.5, 0.0, 1.0, 1.0)

    global planeNew
    def execute(self, pWidget, ev):
        if pWidget:
            # print(pWidget.GetClassName(), "Event Id:", ev)
            self.planeNew = vtk.vtkPlane()
            # 获得pWidget中的平面，将平面值赋值planeNew
            pWidget.GetPlane(self.planeNew)
            # cliper将裁剪器cliper的平面设置为planeNew
            self.cliper.SetClipFunction(self.planeNew)
            self.planeNew.GetNormal()
            self.cliper.Update()
            # 将裁减后的模型传递给另一个窗口
            self.clipedData = vtk.vtkPolyData()
            self.clipedData.DeepCopy(self.cliper.GetOutput())

            self.coneMapper = vtk.vtkPolyDataMapper()
            self.coneMapper.SetInputData(self.clipedData)
            self.coneMapper.ScalarVisibilityOff()
            self.coneSkinActor.SetMapper(self.coneMapper)
            self.PlaneNormal = np.array(self.planeNew.GetNormal())
            self.PlaneOrigin = np.array(self.planeNew.GetOrigin())
            self.textEdit.setPlainText("PlaneNormal=" + str(self.planeNew.GetNormal())
                                        + '\n'
                                        + "PlaneOrigin=" + str(self.planeNew.GetOrigin()))
            # self.textEdit.append

            # PlaneNormal = self.planeNew.GetNormal()
            # PlaneOrigin = self.planeNew.GetOrigin()
            # print("Plane Normal = " + str(self.planeNew.GetNormal()))
            # print("Plane Origin = " + str(self.planeNew.GetOrigin()))

class SimpleView(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.init_vtk()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = SimpleView()
    window.show()

    sys.exit(app.exec_())
