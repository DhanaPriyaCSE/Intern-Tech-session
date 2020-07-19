class Tax:
    def __init__(self,product_id,product_name,product_price,product_category):
        self.product_id=product_id
        self.product_name=product_name
        self.product_price=product_price
        self.product_category=product_category
        self.basic_tax=0
        self.additional_tax=0
        
    def find_tax(self):
        if self.product_price>500:
            basic_tax=(5/100)*self.product_price       
        else:
            basic_tax=(2/100)*self.product_price
        return(round(basic_tax,4))
        
    def finding_additional_tax(self):
        if self.product_category=='textile':
            self.additional_tax=(1/100)*self.product_price
        elif self.product_category=='dairy' and self.product_price>1000:
            self.additional_tax=(3/100)*self.product_price
        else:
            self.additional_tax=0
        return self.additional_tax

def billing_tax_of_products(*products):
    total_bill=0
    for product in products:
        total_tax_of_product=product.find_tax()+product.finding_additional_tax()
        print("Total Tax of "+product.product_name+" is "+str(total_tax_of_product))
        total_bill+=total_tax_of_product+product.product_price
    print("Total price:",total_bill)


    
kitcat=Tax(101,"Kitcat",300,"diary")
diary_milk=Tax(102,"Diary_milk",1300,"diary")
sudi=Tax(103,"Shalwar",3000,"textile")
saree=Tax(104,"Saree",450,"textile")
pomogranut=Tax(105,"Pomogranut",3000,"produce")
mango=Tax(106,"Mango",450,"produce")
cuttons=Tax(107,"Cutton",1000,"homeneeds")
glassware=Tax(108,"Glassware",300,"homeneeds")

billing_tax_of_products(kitcat,diary_milk,sudi,saree,pomogranut,mango,cuttons,glassware)

    
            
        
        
        
    
            
