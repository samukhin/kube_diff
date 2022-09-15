import yaml

with open("test.txt", 'r') as stream:
    data_loaded = yaml.load_all(stream, yaml.FullLoader)
    for i in data_loaded:
        print(i.keys())

for i in data_loaded:
    print(i)
