__author__ = 'Guilherme Noronha'
__contact__ = 'https://www.linkedin.com/in/noronha2001/'

import json
import os
import time
from tweepy import Stream
from decouple import config
from datetime import datetime
import argparse

global out

# Modificando a classe Stream pra gravar os tweets num arquivo
class MyListener(Stream):
    def on_data(self, raw_data):
        out.write(json.dumps(json.loads(raw_data)) + "\n")
        return super().on_data(raw_data)

if __name__ == '__main__':

    # Carrega parametros da linha de comando
    CLI = argparse.ArgumentParser()
    CLI.add_argument('--seconds', type=int)
    CLI.add_argument('--track', type=str, default=[])
    args = CLI.parse_args()

    # Carregando as Keys do arquivo .env
    API_KEY=config('API_KEY')
    API_KEY_SECRET=config('API_KEY_SECRET')
    ACCESS_TOKEN=config('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET=config('ACCESS_TOKEN_SECRET')

    # Criando pasta que vai receber os tweets e os arquivos txt
    os.makedirs('data', exist_ok=True)
    now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    out = open(f'data/tweets-{now}.txt', 'w', encoding='UTF-8')
    # Executando o Listener pra obter tweets da Ucrânia por 5 segundos.s
    stream = MyListener(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream.filter(track=args.track, threaded=True)
    time.sleep(args.seconds)
    stream.disconnect()