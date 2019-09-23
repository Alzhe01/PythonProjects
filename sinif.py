class Exam:
    notlar = [52,69]
    def score(self, dogru_sayisi=0, yanlis_sayisi=0):
        ogrenci_not = dogru_sayisi * 5
        self.notlar.append(ogrenci_not)
        return self.notlar

class Student:
    ogrenci_adi = ""
    sinavlar = ["TYT" , "AYT"]

    def add_exam(self, yenisinav=""):
        self.sinavlar.append(yenisinav)
        print(yenisinav + " adında yeni sınav eklendi")
        return self.sinavlar

    def avg_score(self):
        return self.sinavlar / len(self.sinavlar)


class Class:
    ogrenciler = ["Deneme" , "THT"]

    def add_student(self, yeniogrenci=""):
        self.ogrenciler.append(yeniogrenci)
        print(yeniogrenci + " adlı öğrenci eklendi")

    def class_avg(self):
        self.ortalama=0
        for i in range(1,len(ogr_not)):
            self.ortalama += ogr_not[i]
        return self.ortalama / len(self.ogrenciler)


ogrenci1 = Exam()
ogr_not=ogrenci1.score(17)
ogrenci1 = Student()
sinav = ogrenci1.add_exam("YKS")
ogrenci1=Class()
ogrenci1.add_student("Alzhe01")
ort=ogrenci1.class_avg()
print(ogr_not)
print(sinav)
print(ort)
print(ogrenci1.ogrenciler)
