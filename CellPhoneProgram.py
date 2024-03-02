import CellPhoneClass as cc
def main () :
    my_phone = cc. CellPhone ('Apple', 'iPhone 15', 1099)
    my_phone.set_retail_price (999)
    print (f"The phone manufacturer is {my_phone.get_manufact()}")
    print(f"The phone model is {my_phone.get_model()}")
    print(f"The phone retail price is ${my_phone.get_retail_price()}")
main ()

