#Импортируем библиотеку
import yaml

#Создаём словарь под данные, полученные через helm
helm_d = {}

#helm template test . -n namespace > helm.txt
#helm get manifest test -n namespace > helm.txt
with open("helm.txt", 'r') as stream:
    data_loaded = yaml.load_all(stream, yaml.FullLoader)
    for item in data_loaded:
        #print(item['kind'], item['metadata']['name'])
        helm_d[(item['kind'], item['metadata']['name'])] = item

#Создаём словарь под данные, полученные через kubectl
kubectl_d = {}

#kubectl get all -n namespace -o yaml > kubectl.txt
with open("kubectl.txt", 'r') as stream:
    data_loaded = yaml.load_all(stream, yaml.FullLoader)
    for items in data_loaded:
        for item in items['items']:
            #print(item['kind'], item['metadata']['name'])
            kubectl_d[(item['kind'], item['metadata']['name'])] = item


#print(helm_d.keys())
#print(kubectl_d.keys())

#Функция глубокого поиска и сравнения
def deepsearch(hl, kb):
    for key in hl:
        print(key)
        if key in kb:
            #print(key, 'yes')
            if (type(hl[key]) is dict) and (type(kb[key]) is dict):
                deepsearch(hl[key], kb[key])
            else:
                if str(hl[key]) != str(kb[key]):
                    if (type(hl[key]) is list) and (type(kb[key]) is list):
                        if (len(hl[key]) == len(kb[key])) and (len(hl[key]) == 1):
                            deepsearch(hl[key][0], kb[key][0])
                        else:
                            for el in hl[key]:
                                if type(el) is dict:
                                    print(dict(sorted(el.items())))
                                else:
                                    print(el)
                            print()
                            for el in kb[key]:
                                if type(el) is dict:
                                    print(dict(sorted(el.items())))
                                else:
                                    print(el)
                    else:
                        print(hl[key])
                        print(kb[key])
        else:
            print(key, 'no')


#Начинаем сравнение
for key in helm_d.keys():
    if key in kubectl_d.keys():
        print(key, 'yes')
        deepsearch(helm_d[key], kubectl_d[key])
        print()
    else:
        print(key, 'no')
        print()
