import random

a=random.randint(0,100)
b=random.randint(0,1000)
c=random.randint(0,10000)
sayac=0

level=int(input("-"*10+"\nHoşgeldiniz. Lütfen Zorluk seviyesini seçiniz.\nKolay için : 1\nOrta için : 2\nZor için : 3\n"+"-"*10+"\nSeviye :  "))
print("-"*10)

if level==1:
    while True:
        print("Ben sayıyı tuttum. Bil Bakalım ?")
        key=int(input("Tahmin : "))
        if key==a:
            sayac+=1
            print("Tebrikler. Doğru tahmin ettiniz.\nTutulan sayı: ",a,"\nToplam Deneme: ",sayac)
            break
        elif key>a:
            sayac+=1
            print("Malesef yüksek tahmin. Daha düşük bir sayı giriniz.")
        elif key<a:
            sayac+=1
            print("Malesef düşük tahmin. Daha yüksek bir sayı giriniz.")
        
elif level==2:
    while True:
        print("Ben sayıyı tuttum. Bil Bakalım ?")
        key=int(input("Tahmin : "))
        if key==b:
            sayac+=1
            print("Tebrikler. Doğru tahmin ettiniz.\nTutulan sayı: ",b,"\nToplam Deneme: ",sayac)
            break
        elif key>b:
            sayac+=1
            print("Malesef yüksek tahmin. Daha düşük bir sayı giriniz.")
        elif key<b:
            sayac+=1
            print("Malesef düşük tahmin. Daha yüksek bir sayı giriniz.")
elif level==3:
    while True:
        print("Ben sayıyı tuttum. Bil Bakalım ?")
        key=int(input("Tahmin : "))
        if key==c:
            sayac+=1
            print("Tebrikler. Doğru tahmin ettiniz.\nTutulan  sayı: ",c,"\nToplam Deneme: ",sayac)
            break
        elif key>c:
            sayac+=1
            print("Malesef yüksek tahmin. Daha düşük bir sayı giriniz.")
        elif key<c:
            sayac+=1
            print("Malesef düşük tahmin. Daha yüksek bir sayı giriniz.")
else:
    print("Lütfen yeniden deneyiniz.")

    
