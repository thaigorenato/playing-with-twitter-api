# coding: utf-8

import json
import ast 
import pandas as pd 
import matplotlib.pyplot as plt
import re

# 1º abrir arquivo com os dados do twitter  
tweets_data = []
with open('tweet_data.txt', "r") as tweets_file:
    tweets_data = [ast.literal_eval(line) for line in tweets_file]

# 2º Ornanizando os dados num dataframe 
tweets = pd.DataFrame()
tweets['text'] = [tweet.get('text','') for tweet in tweets_data]
tweets['lang'] = [tweet.get('lang','') for tweet in tweets_data]

for tweet in tweets_data:

    try:
        if tweet['place'] != None:
            tweets['country'] = tweet.get("country", '')

    except KeyError:
        continue

# 3º vamos ver quais são os principais ediomas em que foram escritos os tweets 
tweets_by_lang = tweets['lang'].value_counts()
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Idiomas', fontsize=15)
ax.set_ylabel('Numero de tweets' , fontsize=15)
ax.set_title('Top 5', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')


# precisamos de uma função para pesquisar 
# se uma palavra 'x' aparece no texto
def word_in_text(word, text):
    '''
    Esta função verifica se a palavra word 
    existe no texto text:
    return --> False ou True
    '''
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True

    return False


# 4º Vamos acrescentar em nosso dataframe mais 
# algumas colunas que endicam as ocorrências 
# das palavras python, javascript e ruby
tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))

# 5º vamos plotar a frequência de aparição dessas palavras nos tweets
prg_langs = ['python', 'javascript', 'ruby']
tweets_by_prg_lang = [tweets['python'].value_counts()[True], tweets['javascript'].value_counts()[True], tweets['ruby'].value_counts()[True]]
x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

ax.set_ylabel('Numero de tweets', fontsize=15)
ax.set_title('Ranking: python vs. javascript vs. ruby (Dado bruto)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)


# 6º Vamos adicionar mais 2 colunas, uma para a 
# verificação da palavra programing e outra 
# para a palavra tutorial 
tweets['programming'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
tweets['tutorial'] = tweets['text'].apply(lambda tweet: word_in_text('tutorial', tweet))
tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet)\
                            or word_in_text('tutorial', tweet))


# Vamos contar quantas vezes esses dados  
# relevantes parecem para cada linguagem
tweets_by_prg_lang = [tweets[tweets['relevant'] == True]['python'].value_counts()[True], 
                      tweets[tweets['relevant'] == True]['javascript'].value_counts()[True], 
                      tweets[tweets['relevant'] == True]['ruby'].value_counts()[True]]


# Por fim, vamos plotar esses dados relevantes
x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width,alpha=1,color='g')
ax.set_ylabel('Numero de tweets', fontsize=15)
ax.set_title('Ranking: python vs. javascript vs. ruby (Dados relevantes)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)

plt.show()