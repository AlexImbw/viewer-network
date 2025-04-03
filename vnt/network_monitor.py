import psutil
from time import sleep
import requests


def monitor():
    dados_rede_inicial = psutil.net_io_counters()
    downloads_inicial = dados_rede_inicial.bytes_recv
    upload_inicial = dados_rede_inicial.bytes_sent

    sleep(1)

    dados_rede_final = psutil.net_io_counters()
    downloads_final = dados_rede_final.bytes_recv
    upload_final = dados_rede_final.bytes_sent

    MegabytesD = downloads_final - downloads_inicial
    MegabytesU = upload_final - upload_inicial

    Mbps_D = (MegabytesD / 1048576) * 8
    Mbps_U = (MegabytesU / 1048576) * 8

    print(f"Download:{Mbps_D:.2f} Mb/s")
    print(f"upload: {Mbps_U:.2f} Mb/s")

def obter_ip_publico():
    try:
        resposta = requests.get('https://api.ipify.org')
        if resposta.status_code == 200:
            return resposta.text
        else:
            print(f"Erro ao obter endereço público: {resposta.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Erro ao conectar ao serviço de IP: {e}")
        return None

ip_publico = obter_ip_publico()
if ip_publico: 
    print(f"Endereço IP Público: {ip_publico}")
else:
    print("Não foi possível obter o endereço de IP público.")
