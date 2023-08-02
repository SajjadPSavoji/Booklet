import sys
import yaml

# get file path, field and value from argv
file_path = sys.argv[1]
field     = sys.argv[2]
value     = sys.argv[3]

# read current yml file
with open(file_path, 'r') as stream:
    loaded = yaml.safe_load(stream)
  
# parse filed by . (eg a.b -> [a, b])
field_list = list(field.split("."))

# make a nested dict(or update it)
last_d = loaded
for i in range(len(field_list) - 1):
  if not field_list[i] in last_d:
    last_d[field_list[i]] = {}
  last_d = last_d[field_list[i]]
  
# set value in nested dict
last_d[field_list[-1]] = value

# write new yml file to path
with open(file_path, 'w') as stream:
    yaml.dump(loaded, stream)
