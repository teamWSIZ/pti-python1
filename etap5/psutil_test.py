from time import sleep

import psutil

psutil.cpu_percent()

for i in range(30):
    print(psutil.cpu_percent(interval=1))  # obciążenie procesora
    print(psutil.virtual_memory().available)  # dostępna wolna pamięc
    print(psutil.virtual_memory().total)  # całkowita pamięć komputera
    print(psutil.net_io_counters())  # dane o ruchu sieciowym
    print(psutil.net_io_counters().bytes_sent)  # dane o ruchu sieciowym
    sleep(.01)