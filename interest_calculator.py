print("""•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
    .*.*.*.* Bileşik Faiz Hesaplayıcısı, Hoş geldiniz.*.*.*.* 
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••""")

adi = input("Adınız: ")
kredi_tutari = float(input("Kredi tutarını giriniz: "))
faiz_orani = float(input("Faiz oranını giriniz(Yıllık): "))

print("          ZAMAN ARALIĞI\n")
max_yil = int(input("Yıl cinsinden kredi vadesi: "))
max_month = int(input("\nAy cinsinden kredi vadesi: "))
yineleme = int(input("\nAy cinsinden tekrarlama aralığı: "))
print("--------------------")

def duration(max_ay):                                         #Ayı yil cinsinden yazdık

    a = max_ay // 12
    b = max_ay % 12

    if max_ay >= 12:
        print('\nYıl:', a+max_yil, ",", "Ay=", b)
        return ""

    else:
        print("\nYıl=", max_yil, ",", "Ay=", max_ay)
        return ""


def money():
    print("Aylık ödeme: ", round(1), "$")

def entry():
     yil_to_ay = max_yil * 12  # Yili aya çevirdik
     yil_top_ay = yil_to_ay + max_month  # TOPLAM AY
     Toplam_faiz = (kredi_tutari / 100) * (faiz_orani / 12) * yil_top_ay
     kusurat = (Toplam_faiz + kredi_tutari) / yil_to_ay

     print(f"{adi} için Rapor")
     start = yineleme
     while start <= yil_top_ay:
         print("--------------------")
         print("-> Yıl=", start // 12, "Ay=", start % 12)
         Toplam_faiz = (kredi_tutari / 100) * (faiz_orani / 12) * start
         print("Toplam geri ödenecek tutar:", Toplam_faiz + kredi_tutari, "$")
         kusurat = (Toplam_faiz + kredi_tutari) / start

         print("Aylık ödeme: ", round(kusurat, 1), "$")
         print("--------------------")

         start += yineleme
     return " "



def full_report():
    giris = entry()
    return " "

print(full_report())