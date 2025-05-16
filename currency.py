import pandas as pd
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

def to_millions_str(amount_kgs, rate):
    usd_mln = amount_kgs / rate / 1_000_000
    return f"{usd_mln:,.2f}$ млн".replace(",", " ").replace(".", ",")

def to_thousands_str(amount_kgs, rate):
    usd_ths = amount_kgs / rate / 1_000
    return f"{usd_ths:,.2f}$ тыс.".replace(",", " ").replace(".", ",")

usd_rate = get_usd_to_kgs()
