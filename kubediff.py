import yaml
import subprocess

list = subprocess.check_output("kubectl get all -A -o yaml", shell=True).decode("utf-8")

parse_list = yaml.load(list)

for item in parse_list['items']:
    print(item['kind'], item['metadata']['name'])
