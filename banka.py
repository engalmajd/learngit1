"""
ad soyad = Nisa Nur Yılmaz
numara = 20227170240
"""


class Hesap: 
    isim:str = ''
    soyisim:str = ''
    bas_bakiyesi:int = 0
    harcanan_miktar:int=0
    yatirilan_miktar:int=0
    
    """Hesap ve harcama bilgilerini tutan sınıf"""

    def __init__(self,ad,soyad,baslangic_bakiyesi) -> None:
      
        self.isim = ad
        self.soyisim = soyad
        self.bas_bakiyesi = baslangic_bakiyesi
        self.hareket = []
        self.aciklama = []

        """Hesap Constructor
        Args:
            ad (str): kişi adı
            soyad (str): kişi soyadı
            baslangic_bakiyesi (str): hesap açılış bakiyesi
        """ 

    @property
    def ad(self):
        return f'{self.ad[:3]}*'
        """ad property getter

        Returns:
            str: adın ilk üç harfi ve 3 yıldız
            örnek: Ayş***
        """ 
    @ad.setter
    def ad(self,value):
        self.isim = value
        """ad setter

        Args:
            value (str): kişi adı
        """ 
    @property
    def soyad(self):
        return f'{self.soyad[:3]}*'
        """soyad setter

        Returns:
            str: soyadın ilk üç harfi ve 3 yıldız
            örnek: Yıl***
        """ 
    @soyad.setter
    def soyad(self,value):
        self.soyisim = value
        """soyad setter

        Args:
            value (str): kişi soyadı
        """ 
    @property
    def bakiye(self):
        return self.bas_bakiyesi + self.yatirilan_miktar - self.harcanan_miktar
        """bakiye property

        Returns:
            float: kişi bakiyesi
        """ 
    @bakiye.setter
    def bakiye(self,value):

        if self.bas_bakiyesi != value :
            raise AttributeError("Bakiye değiştirilemez!")
        """bakiye setter

        Args:
            value (float): bakiye property si read-only dir

        Raises:
            AttributeError: Bakiye değiştirilemez!
        """ 

    def __hareket_ekle(self,aciklama,miktar):

        self.hareket.append(miktar)
        self.aciklama.append(aciklama)

        """hareket ekle methodu

        Args:
            aciklama (str): hareket açıklaması
            miktar (float): miktar 
        """ 

    def yatir(self,value):

        if value <= 0:
            raise AttributeError("Yatırılan miktar 0'dan büyük olmalıdır!")
        
        self.yatirilan_miktar += value

        self.__hareket_ekle("Para Yatırma" , value)
                
        """para yatirma methodu

        Args:
            value (float): yatan miktar
        miktar negatif olursa aşağıdaki hata gerçekleşmelidir.

        Raises:
            AttributeError: Yatırılan miktar 0'dan büyük olmalıdır!
        """ 

    def harca(self,aciklama,miktar):
        if miktar <= 0:
            raise AttributeError("Harcanan Miktar 0'dan büyük olmalıdır!")
        
        elif miktar > self.bakiye:
            raise AttributeError("Bakiye yetersiz!")

        self.harcanan_miktar+=miktar
        self.__hareket_ekle(aciklama,-miktar)

        """harcama methodu

        Args:
            aciklama (str): harcama açıklaması
            miktar (float): miktar

            miktar negatif olursa aşağıdaki hata gerçekleşir
        Raises:
            AttributeError: Harcanan miktar 0'dan büyük olmalıdır!
        
            miktar bakiyeden büyük olursa aşağıdaki hata gerçekleşir
        Raises:
            AttributeError: Bakiye yetersiz!
        """ 

    def dokum(self):
        print("-"*20)
        print(f'{self.ad},{self.soyad}')
        print(f"*Başlangıç bakiyesi,{self._baslangic_bakiyesi}")
        for k in range (len(self.hareket)):
            print(f"*{self.aciklama[k]},{self.hareket[k]}")
        print(f"Hesap Bakiyesi:{self.bakiye}")
        print("-"*20)

        """hesap dokumu methodu 
        önce ------ yazar 20 çizgi
        sonra kişinin adı ve soyadı yazar
        sonra tüm hareketler alt alta yazılır
        sonra hesap bakiyesi yazılır
        sonra ------ yazar 20 çizgi
        
        """ 
