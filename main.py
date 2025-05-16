from currency import get_usd_to_kgs_rate
from mbank import build_financial_dataframe


def main():
    try:
        rate = get_usd_to_kgs_rate()
        print(f"Курс USD/KGS: {rate}")
        df = build_financial_dataframe(rate)
        df.round(4).to_excel("mbank_2024_usd.xlsx", index=False)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
