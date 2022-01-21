from PyQt5.QtWidgets import*
from PyQt5.QtGui import  QDoubleValidator
from designerkodlari import Ui_MainWindow
import math
import cmath

class program(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        #uzunhat
        self.ui.buttonu.clicked.connect(self.hesapla)
        self.ui.u1.setValidator(QDoubleValidator())
        self.ui.u2.setValidator(QDoubleValidator())
        self.ui.u3.setValidator(QDoubleValidator())
        self.ui.u4.setValidator(QDoubleValidator())
        self.ui.u5.setValidator(QDoubleValidator())
        self.ui.u6.setValidator(QDoubleValidator())
        self.ui.u7.setValidator(QDoubleValidator())

        #orta uzunluk pi modeli
        self.ui.buttonpi.clicked.connect(self.hesapla2)
        self.ui.pi1.setValidator(QDoubleValidator())
        self.ui.pi2.setValidator(QDoubleValidator())
        self.ui.pi3.setValidator(QDoubleValidator())
        self.ui.pi4.setValidator(QDoubleValidator())
        self.ui.pi5.setValidator(QDoubleValidator())
        self.ui.pi6.setValidator(QDoubleValidator())
        self.ui.pi8.setValidator(QDoubleValidator())

        #orta uzunluk T modeli
        self.ui.buttont.clicked.connect(self.hesapla3)
        self.ui.t1.setValidator(QDoubleValidator())
        self.ui.t2.setValidator(QDoubleValidator())
        self.ui.t3.setValidator(QDoubleValidator())
        self.ui.t4.setValidator(QDoubleValidator())
        self.ui.t5.setValidator(QDoubleValidator())
        self.ui.t6.setValidator(QDoubleValidator())
        self.ui.t8.setValidator(QDoubleValidator())

    def hesapla(self):
        try:
        #inputs
            lenght =float(self.ui.u1.text())
            gerilim = float(self.ui.u2.text())
            a=float(self.ui.u3.text())
            b=float(self.ui.u4.text())
            operator=self.ui.comboBox_2.currentText()
            if operator == ('+'):
                guc=a+b*1j
            else:
                guc=a-b*1j

            L= float(self.ui.u5.text())
            R = float(self.ui.u6.text())
            G = float(self.ui.u7.text())
            C= float(self.ui.u8.text())

            if 240.0 <= lenght:

             #calculations

                Z = complex(R, math.pi * 2 * 50 * L) * lenght
                Y = complex(0, C * 2 * math.pi * 50) * 500
                sqrtZY = cmath.sqrt(Z * Y)
                Zc = cmath.sqrt(Z / Y)
                d = cmath.cosh(sqrtZY)
                e = cmath.sinh(sqrtZY)
                V2 = complex(gerilim / math.sqrt(3), 0)
                I2 = guc / (math.sqrt(3) * gerilim)  # cikis akimi
                V1 = V2 * d + Zc * I2 * e  # giris gerilimi
            #outputs
                self.ui.usonuc1.setText(str(Z))
                self.ui.usonuc2.setText(str(Y))
                self.ui.usonuc3.setText(str(d))
                self.ui.usonuc4.setText(str(e))
                self.ui.usonuc5.setText(str(I2))
                self.ui.usonuc6.setText(str(V1))
            else:
                self.ui.statusbar.showMessage(" Hat uzunluğuna 240 veya daha büyük bir değer giriniz ", 10000)
                self.ui.statusbar.setStyleSheet("color:rgb(255, 5, 5)")
        except ValueError:

            self.ui.statusbar.showMessage("Error, Invalid Inputs",10000)
            self.ui.statusbar.setStyleSheet("color:rgb(255, 5, 5)")

    def hesapla2(self):
        try:
        #inputs
            uzunluk=float(self.ui.pi1.text())
            gerilim=float(self.ui.pi2.text())
            L=float(self.ui.pi3.text())
            R=float(self.ui.pi4.text())
            C=float(self.ui.pi5.text())
            güc_faktörü=float(self.ui.pi6.text())
            yük=float(self.ui.pi8.text())
            ileri_geri=int(self.ui.combo.currentText())

            if 80<= uzunluk<=240:
        #calculations
                Z = complex(R, 2 * math.pi * 50 * L) * uzunluk
                Z1 = math.sqrt(Z.imag ** 2 + Z.real ** 2)
                Zacı = math.degrees(math.atan(Z.imag / Z.real))
                Y = complex(0, 2 * math.pi * 50 * C) * uzunluk
                A = 1 + (Y * Z / 2)
                B = Z
                C = Y + (Y ** 2 * Z) / 4
                D = A
                Vr = complex(gerilim / math.sqrt(3), 0)
                Ir = complex(yük / (math.sqrt(3) * gerilim), ileri_geri * 180 * math.acos(güc_faktörü) / math.pi)
                Iracı = Ir.imag
                cosimag = math.cos(math.radians(Ir.imag))  # cos Ir
                sinimag = math.sin(math.radians(Ir.imag))  # sin Ir
                real = Ir.real * cosimag
                imag = Ir.real * sinimag
                complexır = complex(real, imag)  # Ir complex hali
                Vs = A * Vr + B * complexır
                Is = C * Vr + D * complexır
                Vs1 = math.sqrt(Vs.imag ** 2 + Vs.real ** 2)  # Vs real part
                Vsacı = math.degrees(math.atan(Vs.imag / Vs.real))  # dereceye dönüştürülmüş hali
                Vsffreal = Vs1.real * math.sqrt(3)
                Vsffdegree = Vsacı + 30
                Is1 = math.sqrt(Is.imag ** 2 + Is.real ** 2)
                Isacı = math.degrees(math.atan(Is.imag / Is.real))
                Iseslenik = complex(Is.real, -1 * Is.imag)  # Is nin esneliği
                Ss = 3 * Vs * Iseslenik  # güç
                Ss1 = math.sqrt(Ss.imag ** 2 + Ss.real ** 2)  # real part
                Sssacı = math.degrees(math.atan(Ss.imag / Ss.real))  # açı kısmı
                ger_regulasyonu = (abs(gerilim - Vsffreal) / gerilim) * 100

        #outputs
                self.ui.pisonuc1.setText(str(Z))
                self.ui.pisonuc2.setText(str(Y))
                self.ui.pisonuc3.setText(str(A))
                self.ui.pisonuc4.setText(str( B))
                self.ui.pisonuc5.setText(str(C))
                self.ui.pisonuc6.setText(str(Vr))
                self.ui.pisonuc7.setText(str(Ir))
                self.ui.pisonuc8.setText(str(Vs))
                self.ui.pisonuc9.setText(str(Vs1)+' volt '+str(Vsacı)+ ' derece')
                self.ui.pisonuc10.setText("faz faz arası "+ str(Vsffreal)+ " volt ve " + str(Vsffdegree)+" derece")
                self.ui.pisonuc11.setText(str(Is))
                self.ui.pisonuc12.setText(str(Is1)+"amper "+str(Isacı) +"derece ")
                self.ui.pisonuc13.setText(str(Ss))
                self.ui.pisonuc14.setText("güç "+ str(Ss1)+ " volt amper "+str(Sssacı)+ " derece")
                self.ui.pisonuc15.setText("gerilim regülasyonu %"+ str(ger_regulasyonu))
            else:
                self.ui.statusbar.showMessage("hat uzunluğuna 80 ile 240 arasında bir değer giriniz ", 10000)
                self.ui.statusbar.setStyleSheet("color:rgb(255, 5, 5)")
        except ValueError:

            self.ui.statusbar.showMessage("Error, Invalid Inputs", 10000)
            self.ui.statusbar.setStyleSheet("color:rgb(255, 5, 5)")

    def hesapla3(self):
        try:
        #inputs
            uzunluk = float(self.ui.t1.text())
            gerilim = float(self.ui.t2.text())
            L = float(self.ui.t3.text())
            R = float(self.ui.t4.text())
            C = float(self.ui.t5.text())
            güc_faktörü = float(self.ui.t6.text())
            yük = float(self.ui.t8.text())
            ileri_geri = int(self.ui.combo_2.currentText())
        #calculation
            if 80 <= uzunluk <= 240:
                Z = complex(R, 2 * math.pi * 50 * L) * uzunluk
                Z1 = math.sqrt(Z.imag ** 2 + Z.real ** 2)
                Zacı = math.degrees(math.atan(Z.imag / Z.real))
                Y = complex(0, 2 * math.pi * 50 * C) * uzunluk
                A = 1 + (Y * Z / 2)
                B = Z + (Y ** 2 * Z) / 4
                C = Y
                D = A
                Vr = complex(gerilim / math.sqrt(3), 0)
                Ir = complex(yük / (math.sqrt(3) * gerilim), ileri_geri * 180 * math.acos(
                    güc_faktörü) / math.pi)  # imagınary kısmı dereceli olamaması lazım
                Iracı = Ir.imag
                cosimag = math.cos(math.radians(Ir.imag))  # cos Ir
                sinimag = math.sin(math.radians(Ir.imag))  # sin Ir
                real = Ir.real * cosimag
                imag = Ir.real * sinimag
                complexır = complex(real, imag)  # Ir complex hali
                Vs = A * Vr + B * complexır
                Is = C * Vr + D * complexır
                Vs1 = math.sqrt(Vs.imag ** 2 + Vs.real ** 2)  # Vs real part
                Vsacı = math.degrees(math.atan(Vs.imag / Vs.real))  # dereceye dönüştürülmüş hali
                Vsffreal = Vs1.real * math.sqrt(3)
                Vsffdegree = Vsacı + 30

                Is1 = math.sqrt(Is.imag ** 2 + Is.real ** 2)
                Isacı = math.degrees(math.atan(Is.imag / Is.real))
                Iseslenik = complex(Is.real, -1 * Is.imag)  # Is nin esneliği
                Ss = 3 * Vs * Iseslenik  # güç
                Ss1 = math.sqrt(Ss.imag ** 2 + Ss.real ** 2)  # real part
                Sssacı = math.degrees(math.atan(Ss.imag / Ss.real))  # açı kısmı

                ger_regulasyonu = (abs(gerilim - Vsffreal) / gerilim) * 100

        # outputs
                self.ui.tsonuc1.setText(str(Z))
                self.ui.tsonuc2.setText(str(Y))
                self.ui.tsonuc3.setText(str(A))
                self.ui.tsonuc4.setText(str(B))
                self.ui.tsonuc5.setText(str(C))
                self.ui.tsonuc6.setText(str(Vr))
                self.ui.tsonuc7.setText(str(Ir))
                self.ui.tsonuc8.setText(str(Vs))
                self.ui.tsonuc9.setText(str(Vs1) + ' volt ' + str(Vsacı) + ' derece')
                self.ui.tsonuc10.setText("faz faz arası " + str(Vsffreal) + " volt ve " + str(Vsffdegree) + " derece")
                self.ui.tsonuc11.setText(str(Is))
                self.ui.tsonuc12.setText(str(Is1) + " amper " + str(Isacı) + " derece ")
                self.ui.tsonuc13.setText(str(Ss))
                self.ui.tsonuc14.setText("güç " + str(Ss1) + " volt amper " + str(Sssacı) + " derece")
                self.ui.tsonuc15.setText("gerilim regülasyonu %" + str(ger_regulasyonu))
            else:
                self.ui.statusbar.showMessage("hat uzunluğuna 80 ile 240 arasında bir değer giriniz ", 10000)
                self.ui.statusbar.setStyleSheet("color:rgb(255, 5, 5)")
        except ValueError:

            self.ui.statusbar.showMessage("Error, Invalid Inputs", 10000)
            self.ui.statusbar.setStyleSheet("color:rgb(255, 5, 5)")


uygulama = QApplication([])
pencere = program()
pencere.show()
uygulama.exec_()