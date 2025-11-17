def calculate_price_with_vat(price_str, vat_rate=20):

    price = int(price_str)
    
 

    vat_amount = price * vat_rate / 100
    

    total_price = price + vat_amount
    

    return int(total_price)


price_with_vat = calculate_price_with_vat("100")
print(price_with_vat) 
