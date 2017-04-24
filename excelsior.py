import requests
from random import getrandbits

def entries(amount):
    print("Welcome to Andrew's ExcelsiorMilano raffle bot LMFAO!")
    for i in range(0, amount):
        session = requests.session()
        url = "https://www.excelsiormilano.com/module/antcontactcustom/sendmail"
        email = 'taeyspam+{}@gmail.com'.format(getrandbits(40)) ## CHANGE taeyspam to your EMAIL PRE FIX!!!
        data = {
                    "first_name": "Ande", ## Ande to your first name
                    "last_name": "Lee", ## Lee to your last name
                    "birth": "1990-01-25", ## 1990-01-25 to your/any birthday
                    "mail": email, ## Don't change this
                    "number": "3101111234", #ENTER PHONE HERE
                    "size": "10", # ENTER SIZE 3-12
                    "country": "United States", # ENTER COUNTRY
                    "state": "CA", #ENTER STATE (abreviated)
                    "city": "San Diego",  # ENTER CITY
                    "zip": "92122", # ENTER ZIP CODE
                    "street": "8730 Costa Verde Blvd", # ENTER STREET
                }
        response = session.post(url, data)
        print('{} out of {} entered with email: {}.'.format(i, amount, email))
if __name__ == '__main__':
    entries(1000)
