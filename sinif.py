class Exam:
    def score(self, dogru_sayisi=0, yanlis_sayisi=0):
        ogrenci_not = dogru_sayisi * 5
        return ogrenci_not

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
        return 85 / len(self.ogrenciler)


ogrenci1 = Student()
sinavlar = ogrenci1.add_exam("YKS")
ogrenci1 = Exam()
ogr_not=ogrenci1.score(17)
print(ogr_not)
print(sinavlar)
ogrenci1=Class()
ogrenci1.add_student("Alzhe01")
ort=ogrenci1.class_avg()
print(ogrenci1.ogrenciler)
