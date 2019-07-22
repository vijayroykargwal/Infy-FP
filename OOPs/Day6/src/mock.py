#OOPR-Assgn-203
'''
Created on Mar 24, 2019

@author: vijay.pal01
'''

class Mart:
    item_name_list=["Chocolate","Perfume","Bouquet","Apparel"]
    item_price_list=[200,400,150,300]
    item_quantity_list=[10,20,30,40]

    def find_price_per_item(self,item_name):
        if item_name in Mart.item_name_list:
            index = Mart.item_name_list.index(item_name)
            return Mart.item_price_list[index]
        return -1



class OnlineMart(Mart):
    def __init__(self,order):
        self.__online_discount_percentage=None
        self.__order=order

    def identify_online_discount(self):
        if self.__order.get_payment_mode()=='Prepaid':
            self.__online_discount_percentage=5
        elif self.__order.get_payment_mode()=='COD':
            self.__online_discount_percentage=2
        else:
            self.__online_discount_percentage=-1

    def get_order(self):
        return self.__order

    #To trainee
    def find_price_per_item(self,item_name):
        initial_price_per_item=super().find_price_per_item(item_name)
        if(initial_price_per_item==-1):
            price_per_item=-1
        else:
            self.identify_online_discount()
            if(self.__online_discount_percentage==-1):
                price_per_item=-1
            else:
                discount = (self.__online_discount_percentage/100)*initial_price_per_item
                price_per_item=initial_price_per_item-discount
        return price_per_item
        pass #Remove pass and write your code here

    #To trainee
    def check_item_availability(self):
        ns=super().item_name_list
        no=self.get_order().get_item_name()
        qs = super().item_quantity_list
        qo=self.get_order().get_quantity_required()
        for i in range(0,len(ns)):
            if(ns[i]==no):
                if(qs[i]>=qo):
                    qs[i]=qs[i]-qo
        
        return qo               

         #Remove pass and write your code here

    #To trainee
    def ship_order(self):
        quantity = self.check_item_availability()
        price_per_item = self.find_price_per_item(self.__order.get_item_name())
        if(quantity==-1 or price_per_item==-1):
            order_price = -1
            self.__order.set_tracking_id("NA")
        else:
            self.__order.set_order_price(quantity*price_per_item)
            self.__order.generate_tracking_id()
         #Remove pass and write your code here

class Order():
    __counter=1000
    def __init__(self,item_name,quantity_required,payment_mode):
        self.__tracking_id=None
        self.__item_name=item_name
        self.__quantity_required=quantity_required
        self.__payment_mode=payment_mode
        self.__order_price=None

    def get_tracking_id(self):
        return self.__tracking_id

    def set_tracking_id(self,tracking_id):
        self.__tracking_id = tracking_id

    def get_item_name(self):
        return self.__item_name

    def get_quantity_required(self):
        return self.__quantity_required

    def get_payment_mode(self):
        return self.__payment_mode

    def get_order_price(self):
        return self.__order_price

    def set_order_price(self,order_price):
        self.__order_price=order_price

    #To trainee
    def generate_tracking_id(self):
        self.__tracking_id="TR"+str(Order.__counter)
        Order.__counter+=1
     #Remove pass and write your code here

#You may modify the below code for testing
order_obj=Order('Bouquet',20,'Prepaid')
online_mart_object=OnlineMart(order_obj)
online_mart_object.ship_order()
print('Tracking ID :',online_mart_object.get_order().get_tracking_id())
print('Order Price :',online_mart_object.get_order().get_order_price())