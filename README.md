# Crawler do Twitter usando tweepy 4.7.0

## Como usar?
 1. Crie um arquivo chamado .env e coloque suas keys lá no seguinte formato:
    - API_KEY=XXXX
    - API_KEY_SECRET=YYYY
    - ACCESS_TOKEN=ZZZZZ
    - ACCESS_TOKEN_SECRET=WWWW 
 1. Abra o terminal
 2. conda create -n tweepy_edd
 3. conda activate tweepy_edd
 4. pip install -r requirements.txt
 5. python3 get_tweets.py --seconds X --track Nome_Da_Tag