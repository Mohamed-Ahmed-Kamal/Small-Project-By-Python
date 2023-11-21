import requests

init_currency = input("Enter an intial currency: ")
target_currency = input("Enter an target currency: ")

while True:
    try:
        amount = float(input("Enter the amount: "))
    except:
        print("The amout must be a numberic value!")
        continue

    if amount == 0:
        print("The amount must be greater than 0")
        continue
    else:
        break

url = ("https://api.apilayer.com/fixer/convert?to="
        + target_currency + "&from=" + init_currency
        + "&amount=" + str(amount))

payload = {}
headers= {
  "apikey": "8juraaxZMK8Vf8AsZMKJyKZ7LF5lpmD9"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if(status_code != 200):
    print("Sorry, there was a problem. Please try again later.")
    quit()

result = response.json()
coverted_amount = result['result']
print(f'{amount} {init_currency} = {result} {target_currency}')
