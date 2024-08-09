from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def get_token_prices():
    val = b_combobox.get()
    code = combobox.get()
    if code and val:

        try:

            prices = cg.get_price(ids=code,
                                  vs_currencies=val)

            rez = prices[code][val]
            mb.showinfo("Курс обмена", f"Курс за 1 {code} {rez} {val} ")

        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Необходимо выбрать элемент из списка!")


def update_b_label(event):
    code = b_combobox.get()
    name = destination_currency[code]
    b_label.config(text=name)


def update_label(event):
    code = combobox.get()
    name = crypto_currency[code]
    label.config(text=name)


crypto_currency = {
    'bitcoin': 'BTC Биткоин',
    'ethereum': 'ETH Эфириум',
    'tether': 'USDT Tether',
    'monero': 'XMR Monero',
    'solana': 'SOL Solana',
    'dogecoin': 'DOGE Dogecoin',
    'bitdao': 'BIT bitDAO',
    'cardano': 'ADA Кардано',
    'toshi': 'TOSHI',
    'tron': 'TRX Tron',
    'kaspa': 'KAS Каспа'
}


destination_currency = {
    'usd': 'Американский доллар',
    'rub': 'Российский рубль',
    'eur': 'Евро',
    'cny': 'Китайский юань',
    'gbp': 'Британский фунт стерлингов',
    'jpy': 'Японская йена',
    'chf': 'Швейцарский франк',
    'aed': 'Дирхам ОАЭ',
    'cad': 'Канадский доллар',
    'aud': 'Австралийский доллар'
}

window = Tk()
window.title("Курсы обмена криптовалют")
window.geometry("400x300")

Label(text="Денежная валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(destination_currency.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind('<<ComboboxSelected>>', update_b_label)
b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Криптовалюта").pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(crypto_currency.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind('<<ComboboxSelected>>', update_label)

label = ttk.Label()
label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=get_token_prices).pack(padx=10, pady=10)

window.mainloop()