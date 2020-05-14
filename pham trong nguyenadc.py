#1.1
<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="Dell"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2020-02-28 04:59:06 PM"/>
        <attribute name="created" value="RGVsbDtERVNLVE9QLTBMU0xBN0s7MjAyMC0wMi0yODswNDowNzoxMiBQTTsyNzIw"/>
        <attribute name="edited" value="RGVsbDtERVNLVE9QLTBMU0xBN0s7MjAyMC0wMi0yODswNDo1OTowNiBQTTsxOzI4Mzg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n" type="Integer" array="False" size=""/>
            <output expression="&quot; Nhap n:&quot;" newline="True"/>
            <input variable="n"/>
            <declare name="i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <declare name="F" type="Integer" array="True" size="n"/>
            <for variable="i" start="0" end="n-1" direction="inc" step="1">
                <if expression="i=0 or i=1">
                    <then>
                        <assign variable="F[i]" expression="1"/>
                    </then>
                    <else>
                        <assign variable="F[i]" expression="F[i-1]+F[i-2]"/>
                    </else>
                </if>
                <output expression="F[i]" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>
 39  phuong trinh bac nhat.fprg 
#1.2
<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="Luxury"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2020-03-20 09:36:36 AM"/>
        <attribute name="created" value="THV4dXJ5O0FETUlOOzIwMjAtMDMtMDI7MDM6NDY6NTQgUE07MjMwMQ=="/>
        <attribute name="edited" value="THV4dXJ5O0FETUlOOzIwMjAtMDMtMDI7MDM6NTE6MDQgUE07MTsyNDAw"/>
        <attribute name="edited" value="QuG6o28gTG9uZztERVNLVE9QLVZUTEFOUEU7MjAyMC0wMy0yMDswOTozNjozNiBBTTszOzEwOTQ4"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="a, b, x" type="Real" array="False" size=""/>
            <output expression="&quot;Nh&#7853;p a&quot;" newline="True"/>
            <input variable="a"/>
            <output expression="&quot;Nh&#7853;p b&quot;" newline="True"/>
            <input variable="b"/>
            <if expression="a=0">
                <then>
                    <output expression="&quot;Ph&#432;&#417;ng tr&#236;nh v&#244; s&#7889; nghi&#7879;m&quot;" newline="True"/>
                </then>
                <else>
                    <if expression="b=0">
                        <then>
                            <output expression="&quot;ph&#432;&#417;ng tr&#236;nh v&#244; nghi&#7879;m&quot;" newline="True"/>
                        </then>
                        <else>
                            <assign variable="x" expression="-b/a"/>
                            <output expression="&quot;Nghi&#7879;m l&#224;&quot;" newline="True"/>
                            <output expression="x" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>
 47  phuongtrinhbac2.fprg 
#1.3
<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="Dell"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2020-03-02 05:11:21 PM"/>
        <attribute name="created" value="RGVsbDtERVNLVE9QLTBMU0xBN0s7MjAyMC0wMi0yODswMzozNDozOCBQTTsyNzI3"/>
        <attribute name="edited" value="RGVsbDtERVNLVE9QLTBMU0xBN0s7MjAyMC0wMi0yODswNDowNzowOSBQTTs0OzI4Mzc="/>
        <attribute name="edited" value="THV4dXJ5O0FETUlOOzIwMjAtMDMtMDI7MDU6MTE6MjEgUE07MzsyMzk5"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="a, b, c, deltha" type="Integer" array="False" size=""/>
            <declare name="x1, x2, x" type="Real" array="False" size=""/>
            <output expression="&quot; Nhap a: &quot;" newline="True"/>
            <input variable="a"/>
            <output expression="&quot; Nhap b: &quot;" newline="True"/>
            <input variable="b"/>
            <output expression="&quot;  Nhap c &quot;" newline="True"/>
            <input variable="c"/>
            <assign variable="deltha" expression="b^2-4*a*c"/>
            <if expression="deltha&lt;0">
                <then>
                    <output expression="&quot; Phuong trinh vo nghiem &quot;" newline="True"/>
                </then>
                <else/>
            </if>
            <if expression="deltha=0">
                <then>
                    <output expression="&quot; Phuong trinh co nghiem kep &quot;" newline="True"/>
                    <assign variable="x" expression="-b/2*a"/>
                    <output expression="x" newline="True"/>
                    <breakpoint/>
                </then>
                <else/>
            </if>
            <assign variable="x1" expression="(-b-sqrt(deltha))/(2*a)"/>
            <output expression="&quot; Nghiem x1:&quot;" newline="True"/>
            <output expression="x1" newline="True"/>
            <assign variable="x2" expression="(-b+sqrt(deltha))/(2*a)"/>
            <output expression="&quot; Nghiem x2: &quot;" newline="True"/>
            <output expression="x2" newline="True"/>
        </body>
    </function>
#2.1
import math
a=int(input("nhap gia tri cua a"))
b=int(input("nhap gia tri cua b"))
c=int(input("nhap gia tri cua c"))
delta=b*b-4*a*c
if delta<0:
   print("phuong trinh vo nghiem")
elif delta==0:
   x=-b/2*a
   print("phuong trinh co nghiem kep: ",x)
else:
   x1=(-b+math.sqrt(delta))/(2*a)
   x2=(-b-math.sqrt(delta))/(2*a)
   print("phuong trinh co nghiem: ",x1)
   print("phuong trinh co nghiem: ",x2) /flowgorithm>
#3.3
def say_hello():
    a="hello"
    print(a)
print(say_hello())
#3.4:
n=int(input("nhap so n"))
def kiem_tra(n):
    if n%2==0:
       print("so chan")
    else:
       print("so le")
kiem_tra(n)
#3.10
import math
r=int(input("nhap ban kinh r"))
def tinh(r):
    c=2*r*math.pi;
    s=math.pi*r*r;
    print("chu vi la: ",c)
    print("dien tich la: ",s)
tinh(r)
#3.11
t=int(input("nhap lai suat"))
n=int(input("nhap so tien goc"))
k=int(input("nhap so thang gui"))
def tinh_lai(t,n,k):
    s=n;
    for i in range(0,k):
        s=s+n*t/100;
    print("so tien nhan duoc: ",s)
tinh_lai(t,n,k)
@@ -0,0 +1,5 @@
def chuyen(a):
    for i in a:
        print(i.capitalize())
a=str(input("nhap chuoi: "))
chuyen(a)
 4  baitapc3.py 
@@ -0,0 +1,4 @@


n = int(input("Nhap mot so n = "));
print("Giai thua cua", n);
#4.2
s=input('nhap chuoi: ')
for i in s:
    if i==' ':
       continue
    else:
        print(i)

#4.3
s=input('nhap chuoi: ')
print(s.upper())
#4.5
ds=input('danh sach: ').split()
print(ds)
i=len(ds)
while 1<=i:
    print(ds[i-1])
    i=i-1;
#4.6
n=input('nhap ten nguoi').split()
i=len(n)
print("ho la",n[0])
print("ten la",n[i-1])
#4.7
n=input('nhap chuoi')
for i in range(0,len(n)):
    if n[i].isdigit=='true':
        n[i]=3;
print(n)
#4.15
ds=input('danh sach: ').split()
ds.sort()
print(ds)
#4.21
value = []
items=[x for x in input("Nhập các số nhị phân: ").split(',')]
for p in items:
 intp = int(p, 2)
 if not intp%5:
 value.append(p)
print (','.join(value))
#4.22
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
 values.append(s)
print (",".join(values))
#4.23
s = input("Nhập câu của bạn: ")
d={"DIGITS":0, "LETTERS":0}
for c in s:
 if c.isdigit():
 d["DIGITS"]+=1
 elif c.isalpha():
 d["LETTERS"]+=1
 else:
 pass
print ("Số chữ cái là:", d["LETTERS"])
print ("Số chữ số là:", d["DIGITS"])
#4.24
s = input("Nhập câu của bạn: ")
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print ("Chữ hoa:", d["UPPER CASE"])
print ("Chữ thường:", d["LOWER CASE"])
#5.5
n=int(input('nhap so luong n '))
s=[]
for i in range(0,n):
    a=str(input('nhap phan tu list '))
    s.append(a)
b=max(s)
print("phan tu lon nhat",b)
print("phan tu nho nhat",min(s))
#5.6 
for i in range(0,n):
    if s[i]==b:
        print("vị trí của max là : ",i)
#6.1
class Nguoi(object):
 def getGender( self ):
 return "Unknown"

class Nam( Nguoi ):
 def getGender( self ):
 return "Nam"
class Nu( Nguoi ):
 def getGender( self ):
 return "Nữ"

aNam = Nam()
aNu= Nu()
print (aNam.getGender())
print (aNu.getGender())
#6,2
class hinhchunhat(object):
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def dien_tich(self):
        return self.a*self.b
a=int(input("nhap chieu dai: "))
b=int(input("nhap chieu rong: "))
h=hinhchunhat(a,b)
print("dien tich hinh chư nhat la: ",c.dien_tich())
#6.7:
class circle(object):
    def __init__(self, r):
        self.r=r
    def chu_vi(self):
        return self.r*2*3.14
    def dien_tich(self):
        return self.r**2*3.14
r=int(input("nhap vao ban kinh: "))
c=circle(r)
print("chu vi hinh tron la: ",c.chu_vi())
print("dien tich hinh tron la: ",c.dien_tich())print("so ngau nhien trong khoang 0,200 chia het cho 5 va 7 la: ",a)print (t)
#7.1
input_file=open('D:/a.txt','r')
for line in input file:
    l=len(line)
    s=' '
    while(l>=1):
        s=s+line[l-l]
    print(s)
input_line in k:
    

