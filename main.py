from tkinter import *
from tkinter import messagebox
import cv2
# Opencv Kütüphanesini Projeme Dahil ediyorum.
import numpy as np
import io
import os
from google.cloud import vision
from google.cloud.vision import types





def resimAc(sec):
    # Dosyadan resim okumak için dosyamın yolunu seciyoruz.
    PATH="D:\windows_download\PlakaOkuma-master\Resim/" + sec +".jpg"
    img = cv2.imread(PATH)
    cv2.namedWindow("1-Orjinal Resim", cv2.WINDOW_NORMAL)
    # resm göstermek için bir pencere oluşturma
    cv2.imshow("1-Orjinal Resim", img)
    # Ekranda resim gösterme işlemi
    return img


def resimAc(sec):
    # Dosyadan resim okumak için dosyamın yolunu seciyoruz.
    PATH="D:\windows_download\PlakaOkuma-master\Resim/" + sec +".jpg"
    img = cv2.imread(PATH)
    cv2.namedWindow("1-Orjinal Resim", cv2.WINDOW_NORMAL)
    # resm göstermek için bir pencere oluşturma
    cv2.imshow("1-Orjinal Resim", img)
    # Ekranda resim gösterme işlemi
    return img


def resimAc(sec):
    # Dosyadan resim okumak için dosyamın yolunu seciyoruz.
    PATH="D:\windows_download\PlakaOkuma-master\Resim/" + sec +".jpg"
    img = cv2.imread(PATH)
    cv2.namedWindow("1-Orjinal Resim", cv2.WINDOW_NORMAL)
    # resm göstermek için bir pencere oluşturma
    cv2.imshow("1-Orjinal Resim", img)
    # Ekranda resim gösterme işlemi
    return img


def resimAc(sec):
    # Dosyadan resim okumak için dosyamın yolunu seciyoruz.
    PATH="D:\windows_download\PlakaOkuma-master\Resim/" + sec +".jpg"
    img = cv2.imread(PATH)
    cv2.namedWindow("1-Orjinal Resim", cv2.WINDOW_NORMAL)
    # resm göstermek için bir pencere oluşturma
    cv2.imshow("1-Orjinal Resim", img)
    # Ekranda resim gösterme işlemi
    return img


def resimAc(sec):
    # Dosyadan resim okumak için dosyamın yolunu seciyoruz.
    PATH="D:\windows_download\PlakaOkuma-master\Resim/" + sec +".jpg"
    img = cv2.imread(PATH)
    cv2.namedWindow("1-Orjinal Resim", cv2.WINDOW_NORMAL)
    # resm göstermek için bir pencere oluşturma
    cv2.imshow("1-Orjinal Resim", img)
    # Ekranda resim gösterme işlemi
    return img


def resimAc(sec):
    # Dosyadan resim okumak için dosyamın yolunu seciyoruz.
    PATH="D:\windows_download\PlakaOkuma-master\Resim/" + sec +".jpg"
    img = cv2.imread(PATH)
    cv2.namedWindow("1-Orjinal Resim", cv2.WINDOW_NORMAL)
    # resm göstermek için bir pencere oluşturma
    cv2.imshow("1-Orjinal Resim", img)
    # Ekranda resim gösterme işlemi
    return img


def resimAc(sec):
    # Dosyadan resim okumak için dosyamın yolunu seciyoruz.
    PATH="D:\windows_download\PlakaOkuma-master\Resim/" + sec +".jpg"
    img = cv2.imread(PATH)
    cv2.namedWindow("1-Orjinal Resim", cv2.WINDOW_NORMAL)
    # resm göstermek için bir pencere oluşturma
    cv2.imshow("1-Orjinal Resim", img)
    # Ekranda resim gösterme işlemi
    return img


def resimAc(sec):
    # Dosyadan resim okumak için dosyamın yolunu seciyoruz.
    PATH="D:\windows_download\PlakaOkuma-master\Resim/" + sec +".jpg"
    img = cv2.imread(PATH)
    cv2.namedWindow("1-Orjinal Resim", cv2.WINDOW_NORMAL)
    # resm göstermek için bir pencere oluşturma
    cv2.imshow("1-Orjinal Resim", img)
    # Ekranda resim gösterme işlemi
    return img



# RGB uzayından Gri seviyeli resme dönüş işlemi
def griyecevir(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.namedWindow("2-Griye Donusturme İslemi", cv2.WINDOW_NORMAL)
    # Pencre Oluştur
    cv2.imshow("2-Griye Donusturme İslemi", img_gray)
    # Resmi Göster
    return img_gray


# 2. Gauss Filtreleme , Medyan ortalama ile aynı işi yapan fonk.
## gürültü azaltıcı yumuşatma işlemi
# Her pikselin yoğunluğunu, yakındaki piksellerin yoğunluk ortalamasının ağırlıklı ortalaması ile değiştirir
# Diğer üç filtre kenarları pürüzsüz hale getirirken sesleri kaldırır, ancak bu filtre, kenar #koruyarak görüntünün gürültüyü azaltabilir.

def gurultuAzalt(img_gray):
    gurultuazalt = cv2.bilateralFilter(img_gray, 9, 75, 75)
    cv2.namedWindow("3-Gürültü Temizleme islemi", cv2.WINDOW_NORMAL)
    cv2.imshow("3-Gürültü Temizleme islemi", gurultuazalt)
    return gurultuazalt


# Daha iyi sonuç elde etmek için histogram eşitleme işlemi yapıyoruz
def histogramEsitleme(gurultuazalt):
    histogram_e = cv2.equalizeHist(gurultuazalt)
    cv2.namedWindow("4-Histogram esitleme islemi", cv2.WINDOW_NORMAL)
    cv2.imshow("4-Histogram esitleme islemi", histogram_e)
    return histogram_e


# Açma İşlemi(Opening):
# Aşındırma ile küçük parçalar yok edildikten sonra dilation ile görüntü tekrar genişletilerek küçük parçaların kaybolması sağlanır.
# gürültülerin etkisi azaltılır.
def morfolojikIslem(h_esitleme):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    morfolojikresim = cv2.morphologyEx(h_esitleme, cv2.MORPH_OPEN, kernel, iterations=15)
    cv2.namedWindow("5-Morfolojik acilim", cv2.WINDOW_NORMAL)
    cv2.imshow("5-Morfolojik acilim", morfolojikresim)
    return morfolojikresim


# Resim üzerinde düzensiz bölümleri dengelemek.
# veya iki resim arasındaki değişiklikleri saptamak için görüntü çıkarma kullanılır.(Image subtraction).
def goruntuCikarma(h_esitleme, morfolojik_resim):
    # Görüntü çıkarma (Morph görüntüsünü histogram eşitlenmiş görüntüsünden çıkarmak)
    gcikarilmisresim = cv2.subtract(h_esitleme, morfolojik_resim)
    cv2.namedWindow("6-Goruntu cikarma", cv2.WINDOW_NORMAL)
    cv2.imshow("6-Goruntu cikarma", gcikarilmisresim)
    return gcikarilmisresim


#   görüntüdeki her pikseli siyah bir piksel ile değiştirir; Formul var ona göre yapıyor
# görüntü yoğunluğu bu sabitten büyükse beyaz bir piksel
def goruntuEsikle(goruntucikarma):
    ret, goruntuesikle = cv2.threshold(goruntucikarma, 0, 255, cv2.THRESH_OTSU)
    cv2.namedWindow("7-Goruntu Esikleme", cv2.WINDOW_NORMAL)
    cv2.imshow("7-Goruntu Esikleme", goruntuesikle)
    return goruntuesikle


# Görüntünün kenarlarını algılamak için canny edge kullandım
def cannyEdge(goruntuesikleme):
    canny_goruntu = cv2.Canny(goruntuesikleme, 250, 255)
    cv2.namedWindow("8-Canny Edge", cv2.WINDOW_NORMAL)
    cv2.imshow("8-Canny Edge", canny_goruntu)
    canny_goruntu = cv2.convertScaleAbs(canny_goruntu)
    return canny_goruntu


# Dilatasyon operatörü, girdi olarak iki veri alanını alır.
# Birincisi dilate edilecek olan resimdir. İkincisi, yapılandırma unsuru cekirdek
# Dilate, Büyümek, Genişletmek
def genisletmeIslemi(cannedge_goruntu):
    # Kenarları güçlendirmek için genleşme
    cekirdek = np.ones((3, 3), np.uint8)
    # Genişletme için çekirdek oluşturma
    gen_goruntu = cv2.dilate(cannedge_goruntu, cekirdek, iterations=1)
    cv2.namedWindow("9-Genisletme", cv2.WINDOW_NORMAL)
    cv2.imshow("9-Genisletme", gen_goruntu)
    return gen_goruntu


def konturIslemi(img, gen_goruntu):
    # Kenarlara dayanan resimdeki Konturları Bulma
    contours, hierarchy = cv2.findContours(gen_goruntu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    # Rakamları alana göre sıralama, böylece sayı plakası ilk 10 konturda olacak
    screenCnt = None
    # kontur dng işlemi
    for c in contours:
        # yaklaşık çizgi belirliyoruz
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.06 * peri, True)  # % 6 hata ile yaklaşıklık
        # Yaklaşık konturuzun dört noktası varsa, o zaman
        # ----Plakamızı yaklaşık olarak bulduğumuzu varsayabiliriz.

        if len(approx) == 4:  # Konturu 4 köşeli olarak seçiyoruz
            screenCnt = approx
            break

    final = cv2.drawContours(img, [screenCnt], -1, (9, 236, 255), 3)  # KARENİN RENGİ VE ÇİZİMİ
    # Seçilen konturun orijinal resimde çizilmesi
    cv2.namedWindow("10-Konturlu Goruntu", cv2.WINDOW_NORMAL)
    cv2.imshow("10-Konturlu Goruntu", final)
    return screenCnt


##Belirnenen alan dışında kalan yerleri maskeleme
def maskelemeIslemi(img_gray, img, screenCnt):
    # Numara plakası dışındaki kısmı maskeleme
    mask = np.zeros(img_gray.shape, np.uint8)
    yeni_goruntu = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
    yeni_goruntu = cv2.bitwise_and(img, img, mask=mask)
    cv2.namedWindow("11-Plaka", cv2.WINDOW_NORMAL)
    cv2.imshow("11-Plaka", yeni_goruntu)
    # Maskelenen görüntüyü Yeni klasörüne kaydetme
    #cv2.imwrite("Yeni/" + str('a') + ".jpg", yeni_goruntu)
    return yeni_goruntu


def plakayaz():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "apikey.json"
    client = vision.ImageAnnotatorClient()
    # Yeni klasörüne kaydedilen a.jpg resmini işleme sokup plakayı yazdırma
    file_name = os.path.join(os.path.dirname(__file__), "Yeni/a.jpg")

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response2 = client.text_detection(image=image)
    texts = response2.text_annotations
    sayac = 0
    # for text in texts:
    #     sayac=sayac+1
    #     if(sayac==1):
    #         main.etiket["text"] = text.description
    #         print(text.description)
    #         break

def plakaIyilestir(yeni_goruntu):
    # Daha fazla işlem için numara plakasını geliştirmek için histogram eşitleme
    y, cr, cb = cv2.split(cv2.cvtColor(yeni_goruntu, cv2.COLOR_RGB2YCrCb))
    # Görüntüyü YCrCb modeline dönüştürme ve 3 kanalı bölme
    y = cv2.equalizeHist(y)
    # Histogram eşitleme uygulama
    son_resim = cv2.cvtColor(cv2.merge([y, cr, cb]), cv2.COLOR_YCrCb2RGB)
    # 3 kanalı birleştirme
    #cv2.namedWindow("Gelismis_plaka_no", cv2.WINDOW_NORMAL)
    #cv2.imshow("Gelismis_plaka_no", son_resim)
    cv2.imwrite("Yeni/" + str('a') + ".jpg", son_resim)
    return son_resim

def goruntu():

    try:

        sec= yazi.get()

        if(sec!=""): #Seçilen dosya adı null değilse
            img=resimAc(sec)  #Resim Açma İşlemi
            img_gray=griyecevir(img)  #griye cevirme fonk
            gurultuazalt=gurultuAzalt(img_gray) #Gurultu azaltma fonksiyonu
            h_esitleme=histogramEsitleme(gurultuazalt) #Histogram Eşitleme
            morfolojik_resim=morfolojikIslem(h_esitleme) #Morfolojik islem
            goruntucikarma=goruntuCikarma(h_esitleme,morfolojik_resim) #Goruntu Çıkarma İşlemi
            goruntuesikleme=goruntuEsikle(goruntucikarma)  ##Goruntu Eşikleme İşlemi
            cannedge_goruntu=cannyEdge(goruntuesikleme)     #Canny_Edge İşlemi
            gen_goruntu=genisletmeIslemi(cannedge_goruntu)  #Dilated (Genişletme İşlemi)
            screenCnt=konturIslemi(img,gen_goruntu)                   #Kontur İşlemi
            yeni_goruntu=maskelemeIslemi(img_gray,img,screenCnt)    #Maskeleme İşlemi
            iyilesmisGoruntu=plakaIyilestir(yeni_goruntu)   #Maskelenmiş görüntü üzerinde işlemler.
            plakayaz()
            plakayazdef()

            cv2.waitKey()  # Bir tuşa basarsan pencereyi kapatır.
    except :
        print("Lütfen Resim adını kontrol ediniz...")
        print("Unexpected error:", sys.exc_info()[0])

def plakayazdef():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "apikey.json"
    client = vision.ImageAnnotatorClient()
    #Yeni klasörüne kaydedilen a.jpg resmini işleme sokup plakayı yazdırma
    file_name = os.path.join(os.path.dirname(__file__), "Yeni/a.jpg")

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response2 = client.text_detection(image=image)
    texts = response2.text_annotations
    sayac=0
    for text in texts:
        sayac=sayac+1
        if(sayac==1):
            str = text.description.split('\n')[0]
            messagebox.showinfo("Resimdeki Plaka", str)
            break


pencere = Tk()
pencere.title("Plaka Tanıma Sistemi")
pencere.geometry("450x200+350+40")

yazi = Entry()
yazi.pack()

buton = Button(text="Plaka Oku", command=goruntu)
buton.pack()

yazi2= Label(text="Resimdeki Plaka")
yazi2.pack()

etiket = Label(text="")
etiket.pack()

mainloop()
