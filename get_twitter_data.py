import twitter

api = twitter.Api(consumer_key='WrmwwQYAzAzPCvUcYfZfrMvlT',
                  consumer_secret='ZGchLkQrVPwEtaIhsLvxBLOxlT1T7Vq6aVWi9WtIUXFCcpHnEh',
                  access_token_key='1383129438-E8RnMQcsvG6rI82IQWrQ0HSVc0Zzc3x8DlM8PPN',
                  access_token_secret='nmzdvaq1BYDJELYmZQ1Mc5orVSnE8t8ojGhjYkbNsrw8Z')


for tw in api.GetStreamFilter(track=['python', 'javascript', 'ruby']):
    print tw
