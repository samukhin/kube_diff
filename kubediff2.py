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


print(helm_d.keys())
print(kubectl_d.keys())
