# NUVEM IP Locator v1.0
# Made for Termux by ChatGPT

import requests
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_ip_info(ip=""):
    if ip.strip() == "":
        ip = "check"  # Will use your public IP
    url = f"https://ipwho.is/{ip}"
    try:
        res = requests.get(url, timeout=5)
        data = res.json()

        if data.get("success", False):
            print(f"\n📍 NUVEM IP LOCATOR RESULT")
            print("-" * 40)
            print(f"🔹 IP Address     : {data['ip']}")
            print(f"🌍 Country        : {data['country']}")
            print(f"🏙️  Region         : {data['region']}")
            print(f"🏘️  City           : {data['city']}")
            print(f"📮 Postal Code    : {data['postal']}")
            print(f"📡 Latitude       : {data['latitude']}")
            print(f"📡 Longitude      : {data['longitude']}")
            print(f"🕐 Timezone       : {data['timezone']['id']}")
            print(f"📶 Connection Type: {data['type']}")
            print(f"🌐 ISP/WiFi       : {data['connection']['isp']}")
            print(f"🏢 Organization   : {data['connection']['org']}")
            print("-" * 40)
        else:
            print(f"[!] Error: {data.get('message', 'Unable to get info.')}")
    except Exception as e:
        print(f"[!] Request failed: {e}")

def main():
    clear()
    print("🌩️  NUVEM IP LOCATOR")
    print("==============================")
    ip = input("Enter IP address (leave blank for your own): ")
    get_ip_info(ip)

if __name__ == "__main__":
    main()