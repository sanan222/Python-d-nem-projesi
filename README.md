# Python-dönem-projesi

ELK 107E Introduction to Scientific Programming dersi kapsamında term project olarak ekibimizle birlikte sunduğumuz projemizde farklı gerilimlerde olan kablolar için hesap makinesi oluşturduk. Proje sürecinde Python arayüz tasarım kütüphanesi olan PyQT5 kütüphanesi kullanıldı. Kodda benim yazdığım kısım yüksek gerilim hatları ile ilgili hesaplamalar olan kısımdı. Projenin detayları için aşağıdaki yazılara göz atabilirsiniz.

Voltage Calculation in Long Distance Communication Cables

Long-distance cables are considered to be more than 240km long. A basic version and small part of such cables can be seen from the Picture 1:
 
From the picture above, we can assume these formulas:
Voltage on the dx part:
dV=I×z×dx
Current on the dx part:
dI=V×y×dx
By finding derivatives of these figures, we can find the solutions for voltage and current. Before starting we should know the initial values. The initial conditions are x=0,I=Ir,V=Vr.
γ → spreading constant of unit length
Zc→characteristic empedance of unit length
Z → total impedance per phase
Y→total parallel admitance per phase





Writing in a matrix form we get:
  
Problem-Solving:
L=1.25 mH/km
C=7.5x10-9F/km 
R=0.2 Ω/km 
G=0 
We have 500km long cable with the values above and with total power as S=20+j12 [MVA]. 
Since the voltage between phase at load ends is desired to be 154 kV, what should be the voltage at the line head?

Solution:
  
Code Solution:
import math
import cmath
#Uzun iletim hatti modeli
L = 1.25 * (10**-3) #inductance
C = 7.5 * (10**-9) #capacitance
R = 0.2 #resistance
G = 0
length = 500 #length
S = (20 + 12j)*(10**6) #karmasik guc
gerilim = 154*(10**3) #faz arasi gerilim
#Calculation
Z = complex(R, math.pi*2*50*L)*length
print(Z)
Y = complex(0, C*2*math.pi*50)*500
print(Y)
sqrtZY = cmath.sqrt(Z*Y)
print(sqrtZY)
Zc = cmath.sqrt(Z/Y)
print(Zc)
cosh_sqrtZY = cmath.cosh(sqrtZY)
print(cosh_sqrtZY)
sinh_sqrtZY = cmath.sinh(sqrtZY)
print(sinh_sqrtZY)
V2 = complex(gerilim/math.sqrt(3), 0)
print (V2)
I2 = S/(math.sqrt(3)*gerilim) #cikis akimi
print(I2)
V1 = V2*cosh_sqrtZY + Zc*I2*sinh_sqrtZY #giris gerilimi
print(V1)


Output (Answer of the question):



![output](https://user-images.githubusercontent.com/39303015/150502227-600c7437-9f88-4446-89cd-385b8b5b677d.PNG)


Code fractions:

![code 2](https://user-images.githubusercontent.com/39303015/150502367-ada02f6e-6ae9-42f1-b933-970ccbb9fa9a.PNG)
![code 1](https://user-images.githubusercontent.com/39303015/150502371-831b8abc-970b-4933-b7d0-7e7ffc2dcbfb.PNG)
