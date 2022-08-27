
from finviz.main_func import get_stock

proxies= {
    "http": "socks5://vqcsmngo:ew335afwazgd@45.146.130.123:5800",
    "https": "socks5://vqcsmngo:ew335afwazgd@45.146.130.123:5800",
}

for i in range(1000,):
    tmp_stock= get_stock('NVDA', proxies= proxies)