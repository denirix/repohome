import requests

def convert_usd_to_byn(amount):
    url = "https://www.nbrb.by/api/exrates/rates/431?periodicity=0"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["Cur_OfficialRate"]
        converted_amount = amount * rate
        return converted_amount
    else:
        print("Ошибка при получении данных с сервера.")
        return None

if __name__ == "__main__":
    amount_usd = float(input("Введите сумму в USD: "))
    amount_byn = convert_usd_to_byn(amount_usd)
    if amount_byn is not None:
        print(f"{amount_usd} USD = {amount_byn} BYN")
