import yaml

with open('worthRange.yml', 'r') as file:
    docs = yaml.safe_load_all(file)
    
    for doc in docs:
        for block in doc:
            print(block+":")
            print("  Max: " + str(doc[block]['max']))
            print("  Min: " + str(doc[block]['min']))
