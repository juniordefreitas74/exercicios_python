#pip install pytz

# UTC significa Tempo Universal Coordenado (Coordinated Universal Time). 
# É o principal padrão de tempo pelo qual o mundo regula os relógios e o tempo.
# Ele é usado como referência para definir fusos horários ao redor do mundo. 
# O Brasil, por exemplo, tem diferentes fusos horários em relação ao UTC:

import pytz
from datetime import datetime

data = datetime.now(pytz.timezone('Europe/Oslo'))
print(data)
