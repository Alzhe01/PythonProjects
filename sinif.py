class Exam:
    def __init__(self, dogru_sayisi,yanlis_sayisi):
        self.dogru_sayisi=dogru_sayisi
        self.yanlis_sayisi=yanlis_sayisi
    def score(self):
        return self.dogru_sayisi*100/(self.dogru_sayisi+self.yanlis_sayisi)
class Student:
    def __init__(self,ogrenci_adi):
        self.ogrenci_adi=ogrenci_adi
        self.sınavlar = []
    def add_exam(self,nt):
        self.nt = nt
        self.sınavlar.append(self.nt.score())
    def avg_score(self):
        return sum(self.sınavlar)/len(self.sınavlar)
class Class:
    def __init__(self):
        self.ogrenci_liste = []
        self.notlar =[]
    def add_student(self,isim):
        self.isim = isim
        self.ogrenci_liste.append(self.isim.ogrenci_adi)
        self.notlar.append(self.isim.avg_score())
    def class_avg(self):
        return sum(self.notlar)/len(self.ogrenci_liste)
