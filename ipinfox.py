import requests

def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        data = response.json()

        print("\n🌐 IP Information:")
        print(f"🆔 IP: {data.get('ip')}")
        print(f"📍 City: {data.get('city')}")
        print(f"🌎 Country: {data.get('country')}")
        print(f"📌 Location (Lat,Long): {data.get('loc')}")
        print(f"🏢 ISP: {data.get('org')}")
        print(f"🕰️ Timezone: {data.get('timezone')}")
    except Exception as e:
        print("⚠️ Error fetching data:", e)

if __name__ == "__main__":
    target_ip = input("🔎 Enter IP address: ")
    get_ip_info(target_ip)
