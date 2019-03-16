import json
import yaml

#omment
data = {}

# function open file and set data

def getData():
    try:
        with open('sample.json', 'r') as file:
            data = json.load(file)
        return data
    except IOError:
        print("Can't open file")
        exit(0)

def writeYamlData(data):
    try:
        with open('sample.yml', 'w') as file:
            yaml.dump(data, file, default_flow_style=False,allow_unicode=True)
        return 1
    except IOError:
        print("Can't open file or file not exist")
        exit(0)


## Generate and split data. Sort buckets list

data = getData()

ppl_ages = data['ppl_ages']
buckets = data['buckets']
buckets.sort()

## init params : final_d will hold final dictionary, temp_list = list names to be added to final_d

final_d = {}
temp_list = []


for i in range(len(buckets)):

    for name,age in ppl_ages.items():
        if age < buckets[i]:
            temp_list.append(name)

# Removing already matched items

    for p in temp_list:
        if p in ppl_ages:
            del ppl_ages[p]

    #create strings for dict keys as specified

    if i==0:
        str='-%d' %buckets[i]
    else:
        str='%d-%d' %(buckets[i-1],buckets[i])

    final_d[str] = temp_list.copy()
    temp_list.clear()

# gathering remaining oldies who didnt match previous buckets
max=0
for name,age in ppl_ages.items():
    temp_list.append(name)
    if age>max:
        max=age
str='%d-%d' %(buckets[len(buckets)-1], max)
final_d[str] = temp_list.copy()

# writing Yaml

writeYamlData(final_d)
