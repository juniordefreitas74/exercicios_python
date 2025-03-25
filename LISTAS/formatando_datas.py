from datetime import datetime
import locale

# Define o idioma para português do Brasil
locale.setlocale(locale.LC_TIME, "pt_BR.utf8")

data_atual = datetime.now()
data_string = '2025-03-19 20:37'

mascara_ptbr = '%A %d/%h/%Y %H:%M ' #criei uma variavel com o formato da mascara que quero apresentar
mascara_en = '%Y-%m-%d %H:%M'
print(data_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_string, mascara_en) # aqui converte string em data
print(data_convertida)


