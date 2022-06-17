Kullanici_verileri={"ahmet": "İstinye123",
                    "meryem": "4444"}
urunler = []
Envanter = {"kuşkonmaz": [6, 3],
            "brokoli": [20, 7],
            "havuç": [15, 5],
            "elmalar": [25, 15],
            "muz": [19, 18],
            "meyve": [23, 5],
            "yumurta": [44, 4],
            "karışık meyve suyu": [1, 19],
            "balık çubukları": [27, 10],
            "dondurma": [0, 4],
            "elma suyu": [33, 8],
            "portakal suyu": [32, 4],
            "üzüm suyu": [21, 16]}
alis_veris2 = {"kuşkonmaz": 0,
               "brokoli": 0,
               "havuç": 0,
               "elmalar": 0,
               "muz": 0,
               "meyve": 0,
               "yumurta": 0,
               "karışık meyve suyu": 0,
               "balık çubukları": 0,
               "dondurma": 0,
               "elma suyu": 0,
               "portakal suyu": 0,
               "üzüm suyu": 0}
son = []

def tekrar():
    global urunler
    global alis_veris2
    global Envanter
    global son
    kullanici_adi = input("Kullanici adınızı giriniz: ")
    sifre = input("Şifrenizi giriniz: ")

    while list(Kullanici_verileri)[0] != kullanici_adi and list(Kullanici_verileri)[1] != kullanici_adi or\
            Kullanici_verileri[kullanici_adi]!=sifre:#Kullanıcı ismini veya şifresini yanlış girdiğinde tekrarlatıyor.
        print("Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!")
        kullanici_adi = input("Kullanici adınızı giriniz: ")
        sifre = input("Şifrenizi giriniz: ")

    print("\nBaşarıyla giriş yaptınız.")
    print(f"Hoş gelidiniz {kullanici_adi}! Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin. \n\n")
    urunler = []
    Envanter = {"kuşkonmaz": [6, 3],
                "brokoli": [20, 7],
                "havuç": [15, 5],
                "elmalar": [25, 15],
                "muz": [19, 18],
                "meyve": [23, 5],
                "yumurta": [44, 4],
                "karışık meyve suyu": [1, 19],
                "balık çubukları": [27, 10],
                "dondurma": [0, 4],
                "elma suyu": [33, 8],
                "portakal suyu": [32, 4],
                "üzüm suyu": [21, 16]}
    alis_veris2 = {"kuşkonmaz": 0,
                   "brokoli": 0,
                   "havuç": 0,
                   "elmalar": 0,
                   "muz": 0,
                   "meyve": 0,
                   "yumurta": 0,
                   "karışık meyve suyu": 0,
                   "balık çubukları": 0,
                   "dondurma": 0,
                   "elma suyu": 0,
                   "portakal suyu": 0,
                   "üzüm suyu": 0}
    son = []#SEPETİMİZDEKİ ÜRÜNLERİN LİSTESİ
    def ana():
        global urunler
        global alis_veris2
        global Envanter
        global son
        secim= int(input("Lütfen aşağıdaki hizmetlerden birini seçin:\n1-Ürün ara\n2-Sepete git\n3-Satın al\n4-Oturum "
                         "Kapat\n5-Çıkış yap\nSeçiminiz:"))#ana menü burası!

        while secim !=1 and secim !=2 and secim !=3 and secim !=4 and secim !=5:
            print("Lütfen geçerli bir menü numarası seçiniz!\n\n")
            secim= int(input("Lütfen aşağıdaki hizmetlerden birini seçin:\n1-Ürün ara\n2-Sepete git\n3-Satın al\n4-Oturum"
                             " Kapat\n5-Çıkış yap\nSeçiminiz:"))

        if secim==1:
            alis_veris = ["kuşkonmaz", "brokoli", "havuç", "elmalar", "muz", "meyve", "yumurta", "karışık meyve suyu",
                          "balık çubukları", "dondurma", "elma suyu", "portakal suyu", "üzüm suyu"]
            ne = input("Ne arıyorsunuz: ")
            while ne == " " or ne == "":
                print("Lütfen geçerli bir değer giriniz..")
                ne = input("Ne arıyorsunuz: ")
            icerenler = []#İSTEDİĞİMİZ ÜRÜNLERİN LİSTESİ
            for i in alis_veris:  #ÜRÜNLERİ ÇIKARTIP BİZİM GİRDİĞİMİZ VERİLERLE EŞLEŞİP EŞLEŞMEDİĞİNİ KONTROL EDİYORUZ.
                if ne.lower() in i:
                    icerenler.append(i)
            if len(icerenler) > 0:#İSTESİĞİMİZ ÜRÜNLERİN MİKTARI 0 DAN BÜYÜKSE BURUYA GİRİYOR.
                c = 1
                print(len(icerenler), "adet sonuç bulundu.")
                for k in icerenler:#SIRAYLA YAZDIRIYORUZ.
                    print(c, "=", k)
                    c += 1
                secenek = int(input("Hangi ürünü istiyorunuz(sayı olarak belirtin)= "))
                if secenek == 0:
                    print("Ana menüye geri dönülüyor ...")
                    return ana()
                while secenek > len(icerenler):
                    print("Lütfen aralıktaki sayıları giriniz.")
                    secenek = int(input("Hangi ürünü istiyorunuz(sayı olarak belirtin)= "))

                k = 0
                for i in range(0, len(icerenler)):
                    if secenek == i + 1:#İNDEXTEN ÇEKTİĞİMİZ İÇİN +1 OLARAK YAPIYORUZ.
                        son.append(icerenler[i])
                        break

                for i in range(0, len(son)):#SEPETİMZEDİ ÜRÜNLERİ YAZDIRMAK İÇİN KULLANIYORUZ.
                    k += 1
                miktar = int(input("Kaç tane istiyorsunuz: "))
                if miktar > Envanter[son[k-1]][0] :
                    print("Üründe yeterli stok yoktur.")
                    print("Ana Menüye Dönülüyor...")
                    import time
                    time.sleep(2)
                    return ana()
                if miktar ==0:
                    print("Ekleme yapmadınız.")
                    print("Ana Menüye Dönülüyor...")
                    import time
                    time.sleep(2)
                    return ana()

                while Envanter[son[k-1]][0] < miktar:#ENVANTERDEKİ MİKTARDAN FAZLA İSE TEKRAR SORUYORUZ.
                    miktar = int(input("Üzgünüm! Miktar sınırı aşıyor, Lütfen daha küçük bir miktarla tekrar deneyin: "))

                alis_veris2[son[k-1]] = miktar#SEPETİMZİDEKİ MİKTARI YAZDIRIYORUZ.
                urunler.append(son[k-1])

                print("Ana menüye geri dönülüyor ...")
                return ana()
        elif secim==2:
            top = 0
            sayac=1
            for tutar in urunler:#ÜRÜNLERİ FİYAT VE MİKTARLARIYLA YAZDIRIYORUZ.
                print(sayac,"-",tutar,"Fiyatı=",Envanter[tutar][1],"$ miktar=",alis_veris2[tutar],"Toplam=",
                      Envanter[tutar][1]*alis_veris2[tutar],"$")
                top +=Envanter[tutar][1]*alis_veris2[tutar]
                sayac+=1
            print(f"Güncel tutar: ${top:0.2f}")
            secenek_alt = int(input("Bir seçeneği seçiniz:\n"
                                "1- Tutarı güncelleyiniz.\n"
                                "2- Bir öğeyi kaldırın.\n"
                                "3- Satın al\n"
                                "4- Ana menüye dön.\n"
                                "Seçiminiz: "))
            if secenek_alt==1:
                guncel=int(input("Lütfen miktarını değiştireceğiniz öğeyi seçin: "))
                miktar=int(input("Lütfen yeni miktarı yazın: "))
                while Envanter[urunler[guncel-1]][0] < miktar:#ENVANTERDEKİ MİKTARDAN FAZLA İSE TEKRAR SORUYORUZ.
                    miktar = int(input("Üzgünüm! Miktar sınırı aşıyor, Lütfen daha küçük bir miktarla tekrar deneyin: "))
                alis_veris2[urunler[guncel-1]] = miktar#SEPETİMİZDEKİ MİKTARLARI GÜNCELLİYORUZ.
                sayac = 1
                top = 0
                for tutar in urunler:#ÜRÜNLERİ FİYAT VE MİKTARLARIYLA YAZDIRIYORUZ.
                    print(sayac, "-", tutar, "Fiyatı=", Envanter[tutar][1], "$ miktar=", alis_veris2[tutar], "Toplam=",
                          Envanter[tutar][1] * alis_veris2[tutar],"$")
                    top += Envanter[tutar][1] * alis_veris2[tutar]
                    sayac += 1
                print(f"Güncel tutar: ${top:0.2f}")
                return ana()

            elif secenek_alt == 2:
                item = int(input("Silmek İstediğiniz Öğenin Numarasını Seçiniz: "))
                del (urunler[item-1])#SEÇTİĞİMİZ ÜRÜNÜ SİLİYORUZ. İNDEX OLARAK SİLECEĞİMİZ İÇİN -1 YAPTIK
                sayac = 1
                top = 0
                for tutar in urunler:#ÜRÜNLERİ FİYAT VE MİKTARLARIYLA YAZDIRIYORUZ.
                    print(sayac, "-", tutar, "Fiyatı=", Envanter[tutar][1], "$ miktar=", alis_veris2[tutar], "Toplam=",
                          Envanter[tutar][1] * alis_veris2[tutar],"$")
                    top += Envanter[tutar][1] * alis_veris2[tutar]
                    sayac += 1
                print(f"Güncel tutar: ${top:0.2f}")
                secenek_alt = int(input("Bir seçeneği seçiniz:\n"
                                    "1- Tutarı güncelleyiniz.\n"
                                    "2- Bir öğeyi kaldırın.\n"
                                    "3- Satın al\n"
                                    "4- Ana menüye dön.\n"
                                    "Seçiminiz: "))

            elif secenek_alt==3:
                print("\nMakbuzunuz İşleniyor ...\n")
                import time
                time.sleep(2)#2 SN DELAY VERİYOR.
                print("******* İstinye Online Market *******")
                print("0850 283 6000 \nistinye.edu.tr")
                sayac = 1
                top = 0
                for tutar in urunler:#ÜRÜNLERİ FİYAT VE MİKTARLARIYLA YAZDIRIYORUZ.
                    print(sayac, "-", tutar, "Fiyatı=", Envanter[tutar][1], "$ miktar=", alis_veris2[tutar], "Toplam=",
                          Envanter[tutar][1] * alis_veris2[tutar],"$")
                    top += Envanter[tutar][1] * alis_veris2[tutar]
                    sayac += 1
                print(f"Güncel tutar: ${top:0.2f}")
                import datetime
                now = datetime.datetime.now()
                print(now.strftime("%d-%m-%Y %H:%M:%S"))#GÜN AY YIL SAAT VE DAKİKAYI YAZDIRIYOR.
                print("Online Marketimizi kullandığınız için teşekkür ederiz!\n\n")


                for update in urunler:
                    guncel_urun=Envanter[update][0]-alis_veris2[update]#ENVANTERDEKİ ÜRÜNLE ALDIĞIMIZ ÜRÜNÜN FARKINI ALIYORUZ
                    Envanter[update][0]=guncel_urun#ENVANTERDEKİ YENİ MİKTARI
                son = []
                urunler = []
                secenek_alt = int(input("Bir seçeneği seçiniz:\n"
                                    "1- Tutarı güncelleyiniz.\n"
                                    "2- Bir öğeyi kaldırın.\n"
                                    "3- Satın al\n"
                                    "4- Ana menüye dön.\n"
                                    "Seçiminiz: "))
            if secenek_alt==4:
                return ana()
        elif secim==3:
            print("\nMakbuzunuz İşleniyor ...\n")
            import time
            time.sleep(2)#2 SN DELAY VERİYOR.
            print("******* İstinye Online Market *******")
            print("0850 283 6000 \nistinye.edu.tr")
            sayac = 1
            top = 0
            for tutar in urunler:#ÜRÜNLERİ FİYAT VE MİKTARLARIYLA YAZDIRIYORUZ.
                print(sayac, "-", tutar, "Fiyatı=", Envanter[tutar][1], "$ miktar=", alis_veris2[tutar], "Toplam=",
                      Envanter[tutar][1] * alis_veris2[tutar],"$")
                top += Envanter[tutar][1] * alis_veris2[tutar]
                sayac += 1
            print(f"Güncel tutar: ${top:0.2f}")
            import datetime
            now = datetime.datetime.now()
            print(now.strftime("%d-%m-%Y %H:%M:%S"))#GÜN AY YIL SAAT VE DAKİKAYI YAZDIRIYOR.
            print("Online Marketimizi kullandığınız için teşekkür ederiz!\n\n")

            for update in urunler:
                guncel_urun = Envanter[update][0] - alis_veris2[update]#ENVANTERDEKİ ÜRÜNLE ALDIĞIMIZ ÜRÜNÜN FARKINI ALIYORUZ
                Envanter[update][0] = guncel_urun#ENVANTERDEKİ YENİ MİKTARI
            son = []
            urunler = []
            return ana()
        elif secim==4:
            return tekrar()
        else:
            return "Çıkış yapılıyor"


    print(ana())
print(tekrar())