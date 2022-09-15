import yaml

helm_d = {}

#helm template test . -n namespace > helm.txt
with open("helm.txt", 'r') as stream:
    data_loaded = yaml.load_all(stream, yaml.FullLoader)
    for item in data_loaded:
        #print(item['kind'], item['metadata']['name'])
        helm_d[(item['kind'], item['metadata']['name'])] = item

kubectl_d = {}

#kubectl get all -n namespace > kubectl.txt
with open("kubectl.txt", 'r') as stream:
    data_loaded = yaml.load_all(stream, yaml.FullLoader)
    for items in data_loaded:
        for item in items['items']:
            #print(item['kind'], item['metadata']['name'])
            kubectl_d[(item['kind'], item['metadata']['name'])] = item


#print(helm_d.keys())
#print(kubectl_d.keys())

for key in helm_d.keys():
    if key in kubectl_d.keys():
        print(key, 'yes')
        for sub_key in helm_d[key]:
            if sub_key in kubectl_d[key]:
                print(sub_key, 'yes')
            else:
                print(sub_key, 'no')
    else:
        print(key, 'no')
