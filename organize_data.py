import json
import pandas as pd 
import matplotlib.pyplot as plt
import ast 

tweets_data = []

tweets_file = open('teste.txt', "r")

for line in tweets_file:
    dic_string = json.dumps(line)
    json_acceptable_string = dic_string.replace("'", "\"")
    tweet = json.loads(json_acceptable_string)
    tweets_data.append(tweet)





'''
for line in tweets_file:
    dic_string = json.dumps(line)
    json_acceptable_string = dic_string.replace("'", "\"")
    tweet = json.loads(json_acceptable_string)
    tweets_data.append(tweet)'''
    
''' 
s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
json_acceptable_string = line.replace("'", "\"")
d = json.loads(json_acceptable_string)
'''