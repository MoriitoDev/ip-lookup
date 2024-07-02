import os
from ipdata import ipdata

key = '76f983cd939a47ef46b7f5a1e345a2fd85ec92409cec5601e80e38de'

def print_ip_info(ip_info):
    if 'error' in ip_info:
        print(ip_info['error'])
        return

    print(f"IP Address: {ip_info.get('ip')}")
    print(f"Is EU: {ip_info.get('is_eu')}")
    print(f"City: {ip_info.get('city')}")
    print(f"Region: {ip_info.get('region')}")
    print(f"Region Code: {ip_info.get('region_code')}")
    print(f"Country: {ip_info.get('country_name')}")
    print(f"Country Code: {ip_info.get('country_code')}")
    print(f"Continent: {ip_info.get('continent_name')}")
    print(f"Continent Code: {ip_info.get('continent_code')}")
    print(f"Latitude: {ip_info.get('latitude')}")
    print(f"Longitude: {ip_info.get('longitude')}")
    print(f"ASN: {ip_info['asn'].get('asn') if ip_info.get('asn') else 'N/A'}")
    print(f"ASN Name: {ip_info['asn'].get('name') if ip_info.get('asn') else 'N/A'}")
    print(f"ASN Domain: {ip_info['asn'].get('domain') if ip_info.get('asn') else 'N/A'}")
    print(f"ASN Route: {ip_info['asn'].get('route') if ip_info.get('asn') else 'N/A'}")
    print(f"ASN Type: {ip_info['asn'].get('type') if ip_info.get('asn') else 'N/A'}")
    print(f"Postal Code: {ip_info.get('postal')}")
    print(f"Calling Code: {ip_info.get('calling_code')}")
    print(f"Flag URL: {ip_info.get('flag')}")
    print(f"Emoji Flag: {ip_info.get('emoji_flag')}")
    print(f"Emoji Unicode: {ip_info.get('emoji_unicode')}")
    print(f"Languages: {', '.join([lang['name'] for lang in ip_info.get('languages', [])])}")
    print(f"Currency Name: {ip_info['currency'].get('name') if ip_info.get('currency') else 'N/A'}")
    print(f"Currency Code: {ip_info['currency'].get('code') if ip_info.get('currency') else 'N/A'}")
    print(f"Currency Symbol: {ip_info['currency'].get('symbol') if ip_info.get('currency') else 'N/A'}")
    print(f"Currency Plural: {ip_info['currency'].get('plural') if ip_info.get('currency') else 'N/A'}")
    print(f"Timezone: {ip_info['time_zone'].get('name') if ip_info.get('time_zone') else 'N/A'}")
    print(f"Timezone Abbr: {ip_info['time_zone'].get('abbr') if ip_info.get('time_zone') else 'N/A'}")
    print(f"Timezone Offset: {ip_info['time_zone'].get('offset') if ip_info.get('time_zone') else 'N/A'}")
    print(f"Timezone DST: {ip_info['time_zone'].get('is_dst') if ip_info.get('time_zone') else 'N/A'}")
    print(f"Current Time: {ip_info['time_zone'].get('current_time') if ip_info.get('time_zone') else 'N/A'}")
    print(f"Threat Tor: {ip_info['threat'].get('is_tor') if ip_info.get('threat') else 'N/A'}")
    print(f"Threat Proxy: {ip_info['threat'].get('is_proxy') if ip_info.get('threat') else 'N/A'}")
    print(f"Threat Anonymous: {ip_info['threat'].get('is_anonymous') if ip_info.get('threat') else 'N/A'}")
    print(f"Threat Known Attacker: {ip_info['threat'].get('is_known_attacker') if ip_info.get('threat') else 'N/A'}")
    print(f"Threat Known Abuser: {ip_info['threat'].get('is_known_abuser') if ip_info.get('threat') else 'N/A'}")
    print(f"Threat: {ip_info['threat'].get('is_threat') if ip_info.get('threat') else 'N/A'}")
    print(f"Bogon: {ip_info['threat'].get('is_bogon') if ip_info.get('threat') else 'N/A'}")

def ask():
    option = input("Write the IP you want to lookup or write 'mine' to lookup your own IP: ")
    
    try:
        ipdata_instance = ipdata.IPData(key)
        
        if option.lower() == 'mine':
            external_ip = os.popen('curl -s ifconfig.me').readline().strip()
            response = ipdata_instance.lookup(external_ip)
            print_ip_info(response)
        else:
            response = ipdata_instance.lookup(option)
            print_ip_info(response)
            
    except Exception as e:
        print(f'An error occurred: {e}')

ask()