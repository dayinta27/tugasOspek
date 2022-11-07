print('Perhitungan waktu')
print('jml_hari')
print("| 1. Sapi Warior  : 690 hari|")
print("| 2. Sapi Mage    : 420 hari|")
print("| 3. Sapi Assasin : 530 hari|")
print("| 4. Sapi Nolep   : 330 hari|")
batas = int(input("|nBanyak input : "))
a = 1
b = 0
total = 0
waktu = 0
listValue = []
while a <= batas :
    inputValue = int(input(f"jenis sapi {a} : "))
    listValue.insert(a, inputValue) 
    a+=1
while b < batas :
    if listValue[b] == 1 :
        waktu = 690
    elif listValue[b] == 2 :
        waktu = 420
    elif listValue[b] == 3 :
        waktu = 530
    elif listValue[b] == 4 :
        waktu == 330
    total = total + waktu
    b+=1

tahun = total // 365
x = total % 365
bulan = x // 30
hari = x % 365 % 30
print(int(tahun))
print(int(bulan))
print(x)
print(int(tahun), "tahun", int(bulan), "bulan", int(hari), "hari")
