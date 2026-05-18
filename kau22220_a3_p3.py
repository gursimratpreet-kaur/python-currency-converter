#Author:Gursimratpreet Kaur
#Student ID:991845418
#Assignment-3 Program-3


#['European euro', 'Mexican peso', 'Norwegian krone', 'Singapore dollar', 'South African rand', 'Swedish krona', 'UK pound sterling']

#To give information about the date and how many days older are the exchange rates.
date="2025-11-10"
current_date=input("Enter today's date:(yyyy-mm-dd)")
print(f"The conversion rates are for {date}")
print(f"The data is {int(current_date[-2:])-10} days old.")

#The menu options:
menu_options=["1.List all currencies in dictionary","2.Convert an amount to CAD","3.Convert an amount from CAD","4.Quit"]

#The dictionary for currencies and conversions
currency_conversion_dict={"EUR":("European Euro", 1.6207),"MXN":("Mexican Peso", 0.07623),"NOK":("Norwegian Krone",0.1385),
"SGD":("Singapore Dollar",1.0763),"ZAR":("South African Rand",0.08170), "SEK":("Swedish Krona",0.1474),"GBP":("UK Pound Sterling",1.8476)
}

#Function-1: To convert to cad
def convert_to_cad(currency_code, amount)->float:
    if currency_code not in currency_conversion_dict.keys():
        return "Error! Code not found in dictionary"
    key=currency_conversion_dict[currency_code]
    result=amount*key[1]
    return result

#Function-1:To convert from cad
def convert_from_cad(currency_code,amount)->float:
    if currency_code not in currency_conversion_dict.keys():
        return "Error! Code not found in dictionary"
    key=currency_conversion_dict[currency_code]
    result=amount/key[1]
    return result
    
def main():
    currency_conversion_dict={"EUR":("European Euro", 0.9156),"MXN":("Mexican Peso", 0.07623),"NOK":("Norwegian Krone",0.1385),
    "SGD":("Singapore Dollar",1.0763),"ZAR":("South African Rand",0.08170), "SEK":("Swedish Krona",0.1474),"GBP":("UK Pound Sterling",1.8476)
    }
    for option in menu_options:
        print(option)
    choice=input("Make a choice: ")
    while True:
        if choice=="1":
            print(f"Dictionary: {currency_conversion_dict}")
        elif choice=="2":
            currency_code=input("Enter currency code: ")
            currency_code=currency_code.upper()
            amount=float(input("Enter the amount: "))
            print(convert_to_cad(currency_code,amount))
        elif choice=="3":
            currency_code=input("Enter currency code: ")
            currency_code=currency_code.upper()
            amount=float(input("Enter the amount: "))
            print(convert_from_cad(currency_code,amount))
        elif choice=="4":
            print("Program Complete")
            break
        else:
            print("Invalid input")
        choice=input("Make a choice:")
    
    
        
        
if __name__=="__main__":
    main()
    