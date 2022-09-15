import yaml
import subprocess

list = subprocess.check_output("kubectl get all -A -o yaml", shell=True).decode("utf-8")

a = yaml.load(list)

print(a)
