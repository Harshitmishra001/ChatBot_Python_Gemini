import os
import time
import pandas as pd
from gemini import Gemini
import pathlib
import textwrap
import google.generativeai as genai
import requests
# response = requests.get('https://gemini.google.com/app')
# response.cookies
# cookies = {cookie.name[i]:cookie.value[i] for i in range(len(cookie.name))}
def get_cookie_dict(url):
    response = requests.get(url)
    if hasattr(response, 'cookies'):
        cookies = dict(response.cookies)
    else:
        print("Warning: Cookies not found in response object's 'cookies' attribute.")
        cookies = {}
    return cookies
url = 'https://gemini.google.com/app'
cookie_dict = get_cookie_dict(url)
for name, value in cookie_dict.items():
    print(f"Cookie Name: {name}, Value: {value}")
# cookies = {"_ga":"GA1.1.1054790789.1712777992","SEARCH_SAMESITE":"CgQInpsB","AEC":"AQTF6HzmgCDMTFrE7NmaSe_j8OAUQstkDO4JNMRQm3qaKwWVN2fh_CheGa4","S":"billing-ui-v3","NID":"514","SID":"g.a000kAgwg-XHKQbJp6UBcagcyuH8kDbdEtjDqhr8-qjlpZSPnTADWq0OGH0OgYlPVvjEroEttQACgYKAU0SAQASFQHGX2MilWEiOdlyoAshDcJIQI621RoVAUF8yKocCapA3483bJBUwE1beOUA0076","__Secure-1PSID":"g.a000kAgwg-XHKQbJp6UBcagcyuH8kDbdEtjDqhr8-qjlpZSPnTADfbuwlBmMymqdVIOutu1wzwACgYKAfwSAQASFQHGX2Mif2A8cI-V6UeRCG0B-3bBvxoVAUF8yKp-egMMMmRfcAhyZOZdZ1rS0076","__Secure-3PSID":"g.a000kAgwg-XHKQbJp6UBcagcyuH8kDbdEtjDqhr8-qjlpZSPnTADWp6Sm3CdzQ1wNyzqg8hajgACgYKASUSAQASFQHGX2MiLBNliYN4bKa6nenPgZRQjBoVAUF8yKoNDPHdwC_WoWk29J_YlfoI0076","HSID":"AJ6p1QzltCXY0SR4H","SSID":"ArnufQqmUEDsljFMN","APISID":"x8MHNCQoGIKBhouu/Ax_slbwmhuWaW6idW","SAPISID":"69HMZ1XM95vUIqGl/AXcfU3duTK4fcAA9d","__Secure-1PAPISID":"69HMZ1XM95vUIqGl/AXcfU3duTK4fcAA9d","__Secure-3PAPISID":"69HMZ1XM95vUIqGl/AXcfU3duTK4fcAA9d","1P_JAR":"2024-05-28-06","_ga_WC57KJ50ZZ":"GS1.1.1716876712.20.1.1716877615.0.0.0","__Secure-1PSIDTS":"sidts-CjEBLwcBXFX1WDNBiXqZmaJIrMwgZaW_pBLiL7WPzkd9_QwihgQ3eI1Y5LqCxZLle5OeEAA","__Secure-3PSIDTS":"sidts-CjEBLwcBXFX1WDNBiXqZmaJIrMwgZaW_pBLiL7WPzkd9_QwihgQ3eI1Y5LqCxZLle5OeEAA","SIDCC":"AKEyXzXa3AE2vX-VhDTN40N2bajL9qO4cqBcnKll_EUyxbaJ1vSjwc-gmcg8xg0mQLL8RgSmPQ","__Secure-1PSIDCC":"AKEyXzX3FkUKEIykJ4XMjHSlTrgq392pLkSDx6yGARzvDqW6Z5zeiPHdbOqigAh7TikoEj2DP00","__Secure-3PSIDCC":"AKEyXzXjhkwmBUbf4F94I9rhbj-4hy9jgiTK138CnpTAWh7ULRZqCAj0cKsphmreMY2cWpuWRg"}
client = Gemini(cookies=cookie_dict)
genai.configure(api_key="")
text=input("Enter Your Text:\n")
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(text)
# print(response.payload)
print(response.text)