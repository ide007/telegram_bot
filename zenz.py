import json

stop_list = []

with open('stopwords.txt', encoding='utf-8') as s:
    for i in s:
        word = i.lower().split(' ')
        if word != '':
            stop_list.append(word)

with open('stop_list.json', 'w', encoding='utf-8') as e:
    json.dump(*stop_list, e)
