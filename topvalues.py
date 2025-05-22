import pandas as pd

data = {
    "Банк": ["МБанк", "Айыл Банк", "Оптима Банк", "O! Банк", "Элдик Банк"],
    "Показатель": [
        "Кол-во клиентов",
        "Общие активы",
        "Наград «Лучший банк»",
        "Коэффициент ликвидности",
        "S&P Global ESG"
    ],
    "Значение": [
        "1 200 000",
        "156 млрд сом",
        "8 раз",
        "434%",
        "45 баллов"
    ],
    "Примечание": [
        "",
        "",
        "",
        "",
        "ESG S&P Global"
    ]
}

df = pd.DataFrame(data)

excel_path = "topvalues.xlsx"
df.to_excel(excel_path, index=False)

excel_path
