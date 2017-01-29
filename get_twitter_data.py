import twitter
import os

# Para obter suas chaves de acesso, crie uma conta
# de desenvolvedor no twitter no seguinte link:
# https://dev.twitter.com/


consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token_key= os.environ['access_token_key']
access_token_secret = os.environ['access_token_secret']

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)


for tw in api.GetStreamFilter(track=['python', 'javascript', 'ruby']):
    print tw
