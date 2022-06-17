import random

print("———– İlk Kahraman ———–")
kullanici_adi1 = input("Kullanıcı adınızı giriniz: ")
while kullanici_adi1 == "" or kullanici_adi1 == " ":            #Burada Kullanıcımız boş veya hiç bir şey girmediği zaman tekrardan bilgi istediğimiz yer.
    print("Kullanıcı adınız boşluk olamaz lütfen doldurunuz.")
    print("———– İlk Kahraman ———–")
    kullanici_adi1 = input("Kullanıcı adınızı giriniz: ")
kullanici_adi1 = kullanici_adi1[0].upper() + kullanici_adi1[1:] #Burada Kullanıcımızın girdiği isimin ilk harfini büyütüp geri kalanı aynı şekilde kullanıyoruz
print("\n———– İkinci Kahraman ———–")
kullanici_adi2 = input("Kullanıcı adınızı giriniz: ")
while kullanici_adi2 == "" or kullanici_adi2 == " ":    #Burada Kullanıcımız boş veya hiç bir şey girmediği zaman tekrardan bilgi istediğimiz yer.
    print("Kullanıcı adınız boşluk olamaz lütfen doldurunuz.")
    print("———– ikinci Kahraman ———–")
    kullanici_adi2 = input("Kullanıcı adınızı giriniz: ")
kullanici_adi2 = kullanici_adi2[0].upper() + kullanici_adi2[1:]   #Burada Kullanıcımızın girdiği isimin ilk harfini büyütüp geri kalanı aynı şekilde kullanıyoruz

while kullanici_adi1 == kullanici_adi2:    #Girilen kullanııc isimlerinin aynı olup olmadığı kontrol ediliyor eğer eşitlik varsa sürekli döngüye giriyor. Farklı bir isim girine kadar
    print(f"{kullanici_adi1} Alınmıştır lütfen farklı bir kullanıcı isimi seçiniz...")
    kullanici_adi2 = input("Kullanıcı adınızı giriniz: ")
    while kullanici_adi2 == "" or kullanici_adi2 == " ":
        print("Kullanıcı adınız boşluk olamaz lütfen doldurunuz.")
        print("———– ikinci Kahraman ———–")
        kullanici_adi2 = input("Kullanıcı adınızı giriniz: ")
    kullanici_adi2 = kullanici_adi2[0].upper() + kullanici_adi2[1:]
print(f"""\n\tOyuncular:
    1.Oyuncu:{kullanici_adi1}
    2.Oyuncu:{kullanici_adi2}
    Başarılar...    
    """)

def Oyun(Yazi_tura,can1,can2):
    if Yazi_tura=="Yazı":    #yazi tura sonucu "Yazı" gelirse buraya giriyor.
        print(f"———– {kullanici_adi1} Saldırır !! ———")
        hasar = int(input("Hasar vurmak için 1 ile 50 arasında bir sayı giriniz : "))
        while hasar>50 or hasar<1:  #Kullanıcımız burada 50 üstünde veya 1 altında bir değer girdiğinde bir daha soruyor
            print("Saldırı değeri 1 ila 50 arasında olması lazımdır!!!")
            hasar = int(input("Saldırı büyüklüğünü 1 ila 50 arasında seciniz:  "))
        basari = 100 - hasar   # Bizim başarı oranımız.
        basarisizlik = 100 - basari #Bizim başarısızlık oranımız
        e = basari*"Başarılı " #Başarılı olanların yazımı
        f = basarisizlik*"Başarısız " #Başarısız olanların yazımı
        toplam = e + f #Toplam
        t = toplam.split() #Listeye çevirdiğimiz aşama
        olasilik = random.choice(t) #Listemizden rastgele bir şekilde çekildiği yer.
        if olasilik =="Başarılı":
            print("Saldırı başarıyla gerçekleşti")
            can2 -= hasar
            if can2<0: #Burada canımız 0 dan küçük olduğunda girip canımızın - ye girmesini önlüyor
                can2=0
        if olasilik=="Başarısız":
            print("Saldırı başarısız olmuştur")
        Yazi_tura = "Tura" #Diğer oyuncuya sıra geçiyor
    else:
        print(f"———– {kullanici_adi2} Saldırır !! ———")
        hasar = int(input("Hasar vurmak için 1 ile 50 arasında bir sayı giriniz : "))
        while hasar > 50 or hasar < 1:  #Kullanıcımız burada 50 üstünde veya 1 altında bir değer girdiğinde bir daha soruyor
            print("Saldırı değeri 1 ila 50 arasında olması lazımdır!!!")
            hasar = int(input("Saldırı büyüklüğünü 1 ila 50 arasında seciniz:  "))
        basari = 100 - hasar  # Bizim başarı oranımız.
        basarisizlik = 100 - basari  #Bizim başarısızlık oranımız
        e = basari * "Başarılı "    #Başarılı olanların yazımı
        f = basarisizlik * "Başarısız "   #Başarısız olanların yazımı
        toplam = e + f  #Toplam
        t = toplam.split()  #Listeye çevirdiğimiz aşama
        olasilik = random.choice(t)  #Listemizden rastgele bir şekilde çekildiği yer.
        if olasilik == "Başarılı":
            print("Saldırı başarıyla gerçekleşti")
            can1 -= hasar
            if can1 < 0:  #Burada canımız 0 dan küçük olduğunda girip canımızın - ye girmesini önlüyor
                can1 = 0
        if olasilik == "Başarısız":
            print("Saldırı başarısız olmuştur")
        Yazi_tura = "Yazı"   #Diğer oyuncuya sıra geçiyor


    return Yazi_tura,can1,can2  #Tanımladıklarımızı çağırıyoruz
Tekrar = "Tekrar"
while Tekrar == "Tekrar":
    can1 = 100
    can2 = 100
    Yazi_tura=random.choice(["Yazı","Tura"])
    while not(can1 < 0 and can2 < 0):  #Canlarımız "0" ın altına girdiği zaman while döngüsüne girmeyecek.

        bar1 = can1 // 2 * ("|")
        bar2 = can2 // 2 * ("|")
        print(f"""\t\t\t{kullanici_adi1}\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{kullanici_adi2}
            HP[{can1}]:{bar1} \t\tHP[{can2}]:{bar2}""")
        if can1<=0:
            print(f"""\n\t\t\t\t\t\t############### {kullanici_adi2} kazandı ############### !!""")
            break
        elif can2<=0:
            print(f"""\n\t\t\t\t\t\t############### {kullanici_adi1} kazandı ############### !!""")
            break
        Yazi_tura,can1,can2=Oyun(Yazi_tura,can1,can2) #Def içinde tanımladıklarımıza bu değerleri atıyoruz.

    print("Bir daha oynamak istiyor musunuz ?")
    Tekrar1= input("Devam etmek istiyorsanız 'Evet',Bitirmek istiyorsanız 'Hayır' yazınız: ")

    if Tekrar1 == "Evet" or Tekrar1 == "EVET" or Tekrar1 == "evet" or Tekrar1 == "Hayır" or Tekrar1== "HAYIR" or Tekrar1== "hayır": #Burada eğerki kullanıcı evet veya hayır girerse aşağı girecek oradan tekrar kontrol edip ya oyunu bitirecek ya da tekrardan başlatacak
        if Tekrar1 == "Evet" or Tekrar1 == "EVET" or Tekrar1 == "evet":
            Tekrar = "Tekrar"
        if Tekrar1 == "Hayır" or Tekrar1== "HAYIR" or Tekrar1 == "hayır":
            Tekrar = "Değil"
    else:
        while Tekrar1 != "Evet" or Tekrar1 != "EVET" or Tekrar1 != "evet" or Tekrar1 == "Hayır" or Tekrar1== "HAYIR" or Tekrar1== "hayır":#Kullanıcı farklı bir şey girdiğinde buraya girecek.Evet veya hayır girene kadar devam edicek.
            print("Bir daha oynamak istiyor musunuz ?")
            Tekrar1 = input("Devam etmek istiyorsanız 'Evet',Bitirmek istiyorsanız 'Hayır' yazınız: ")
            if Tekrar1 == "Evet" or Tekrar1 == "EVET" or Tekrar1 == "evet" or Tekrar1 == "Hayır" or Tekrar1 == "HAYIR" or Tekrar1 == "hayır":
                if Tekrar1 == "Evet" or Tekrar1 == "EVET" or Tekrar1 == "evet":
                    break
                Tekrar = "Tekrar"
                if Tekrar1 == "Hayır" or Tekrar1 == "HAYIR" or Tekrar1 == "hayır":
                    Tekrar = "Değil"
                    break

print("\nOynadığınız için teşekkür ederiz.///Yapımcılar==>Ahmet BAYRAM || Harun ÇELİK")