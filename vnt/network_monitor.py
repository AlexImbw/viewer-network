import psutil
from time import sleep

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