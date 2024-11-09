Python ve Makine Öğrenmesi ile Hava Durumu Bazlı Nem Tahmini
Proje Açıklaması
Bu proje, tenis oyunu verisiyle hava durumu koşullarının nem üzerindeki etkisini tahmin etmek amacıyla makine öğrenmesi tekniklerini kullanır. Veriler, LabelEncoder ve OneHotEncoder ile işlendikten sonra, lineer regresyon ve OLS modelleriyle analiz edilerek nem tahminleri yapılır. Proje, veri işleme ve regresyon modelleme konularında temel bir uygulama örneğidir.

KULLANILAN YÖNTEMLER
LabelEncoder: Kategorik verileri sayısal verilere dönüştürmek için kullanılır.
OneHotEncoder: Kategorik verileri ikili vektörlere dönüştürmek için kullanılır.
Linear Regression: Nem tahmini yapmak için kullanılan temel regresyon yöntemidir.
OLS (Ordinary Least Squares): Regresyon analizinde modelin parametrelerini optimize etmek için kullanılır.

PROJE ADIMLARI
1.Veri Seti Yükleme:
Tenis oyunuyla ilgili veriler, CSV formatında bir dosyadan (tenis_hava_durumu.csv) yüklenir.

2.Veri Ön İşleme:
LabelEncoder kullanılarak kategorik sütunlar sayısal verilere dönüştürülür.
OneHotEncoder ile "outlook" (hava durumu) sütunu ikili hale getirilir.

3.Model Eğitimi ve Tahmin:
Lineer regresyon ve OLS yöntemleriyle model eğitilir.
Eğitim ve test verileri kullanılarak nem tahminleri yapılır.

4.Sonuçların Değerlendirilmesi:
OLS regresyon sonuçları ile modelin başarı durumu özetlenir.

5.Kullanım Talimatları
Proje dosyasını indirin ve veri dosyasının adını (tenis_hava_durumu.csv) doğru şekilde ayarladığınızdan emin olun.
Python dosyasını çalıştırarak modeli eğitip tahminleri elde edebilirsiniz.

Dosya Yapısı
tenis_hava_durumu.csv: Tenis oyunuyla ilgili veriler.
NemTahmini.py: Projenin Python kodu.
