import urllib.request

try:
    nome_site = str(input('Digite a URL do site: '))
    site = urllib.request.urlopen('http://' + nome_site)
except:
    print(f'O site http://{nome_site} não está acessível no momento.')
else:
    print(f'Consegui acessar o site http://{nome_site} com sucesso.')
    #print(site.read())