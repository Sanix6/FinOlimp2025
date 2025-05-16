import pandas as pd
from currency import *

# Сырые данные
raw = {
    "Банк": "МБанк",
    "Активы": sum([65570887.0, 84150066.0, 90447877.0, 102257832.0]),
    "Обязательства": sum([55393644.0, 72069218.0, 76128426.0, 87063027.0]),
    "Капитал": sum([10177243.0, 12080848.0, 14319450.0, 15194805.0]),
    "Доходы": sum([1650760.0, 4343678.0, 7200912.0, 8789585.0]),
    "Расходы": sum([1185829.0, 2523597.0, 4193569.0, 6317790.0]),
    "Чистая прибыль": sum([1196144.0, 3335011.0, 5573613.0, 6448968.0]),
}

assets = raw["Активы"] / usd_rate
liabilities = raw["Обязательства"] / usd_rate
equity = raw["Капитал"] / usd_rate
income = raw["Доходы"] / usd_rate
expenses = raw["Расходы"] / usd_rate
net_income = raw["Чистая прибыль"] / usd_rate

data = {
    "Банк": raw["Банк"],
    "Активы (USD)": to_millions_str(raw["Активы"], usd_rate),
    "Обязательства (USD)": to_millions_str(raw["Обязательства"], usd_rate),
    "Капитал (USD)": to_millions_str(raw["Капитал"], usd_rate),
    "Чистая прибыль (USD)": to_thousands_str(raw["Чистая прибыль"], usd_rate),
    "Доходы (USD)": to_thousands_str(raw["Доходы"], usd_rate),
    "Расходы (USD)": to_thousands_str(raw["Расходы"], usd_rate),
    "Коэффициент ликвидности": round(equity / liabilities, 4),
    "Коэффициент рентабельности": round(net_income / equity, 4),
}

df = pd.DataFrame([data])
df.to_excel("мбанк_2024.xlsx", index=False)
