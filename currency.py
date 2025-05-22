import requests
import xml.etree.ElementTree as ET

def get_usd_to_kgs():
    url = "https://www.nbkr.kg/XML/daily.xml"
    resp = requests.get(url)
    root = ET.fromstring(resp.content)
    for cur in root.findall("Currency"):
        if cur.attrib.get("ISOCode") == "USD":
            return float(cur.find("Value").text.replace(",", "."))
    raise RuntimeError("USD курс не найден")


def format_thousands(value, currency_symbol):
    return f"{round(value / 1_000):,} тыс. {currency_symbol}".replace(",", " ")

