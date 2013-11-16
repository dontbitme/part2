# -*- coding: utf-8 -*-
class Lodowka(object):
    
    def __init__(self):
        self.products = []
        self.temperature = None
        self.status = False  

    def add_product(self, product):
        for i in self.products:
            if i.nazwa != product.nazwa:
                self.products.append(product)
            else:
                i.waga = i.waga + product.waga
                
                
            
        
        
    def delete_product(self, product_name):
        print 'deleting... %s' %product_name
        for i in self.products:
            if i.nazwa == product_name:
                self.products.remove(i)
            else:
                print 'Nie ma takiego produktu..'
           
            
    def show_products(self):
        print "------ PRODUCTS ------"
        for product in self.products:
            print '- ', product.nazwa, product.cena, product.waga, product.data_waznosci
        print "----------------------"
        
    def turn_on(self):
        self.status = True
    
    def turn_off(self):
        self.status = False
    
    def show_status(self):
        return self.status
        
    def set_temp(self, temp):
        self.temperature = temp
    
    def show_temperature(self):
        return self.temperature
    
    def total_price(self):
        hajs = 0
        for x in self.products:
            hajs += x.cena
        print hajs    
        
        
    def take_out(self, product):
        for a in self.products:
            if a.nazwa == product:
                self.products.remove(a)
                print "Product " + a.nazwa +" was taken out..."
            else:
                print "Nie ma takiego produktu."
    
    def najczestszy_produkt(self):
        lis=[]
        for s in self.products:
            self.products.index(s.nazwa)        #NIE ZROBIŁEM


            
        
            
            


class Produkt(object):
    def __init__(self, nazwa, cena, waga, data_waznosci):
        self.nazwa = nazwa
        self.cena = cena
        self.waga = waga
        self.data_waznosci = data_waznosci
        

p = Produkt('banan', 3, 0.5, '01.03.2013')


l = Lodowka()
l.add_product(p)
l.show_products()





