
def tax_product(id,name,price,category):
    tax=0
    taxtile=0
    if category=='textile':
        taxtile=(1/100)*price
        
    if price>=500  :
        tax=taxtile+(5/100)*price
        if price>1000 and category=='diary':
            tax=tax+(3/100)*price
        return round(tax,4)
    else:
        tax=taxtile+(2/100)*price
        return round(tax,4)
    

sell_product=input("Enter the product id,name, price,category\n").split()
tax_details=tax_product(sell_product[0],sell_product[1],int(sell_product[2]),sell_product[3])
print("product Name:{} and Tax:{} " .format(sell_product[1],tax_details))
