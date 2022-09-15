import yaml

#helm template test . -n namespace > helm.txt
with open("helm.txt", 'r') as stream:
    data_loaded = yaml.load_all(stream, yaml.FullLoader)
    for i in data_loaded:
        print(i['kind'], i['metadata']['name'])

print()

#kubectl get all -n namespace > kubectl.txt
with open("kubectl.txt", 'r') as stream:
    data_loaded = yaml.load_all(stream, yaml.FullLoader)
    for i in data_loaded:
        for j in i['items']:
            print(j['kind'], j['metadata']['name'])
