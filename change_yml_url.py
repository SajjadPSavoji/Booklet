import sys
import yaml

# a func to change git url to https url
def change_git_to_https(url):
  url_parts = url.split(":")
  url="".join(["https:", url_parts[-1]])
  return url[:-4]
  
# change git url to https url
file_path = sys.argv[1]
# read current yml file
with open(file_path, 'r') as stream:
    loaded = yaml.safe_load(stream)
url = loaded["repository"]["url"]
loaded["repository"]["url"] = change_git_to_https(url)
# write new yml file to path
with open(file_path, 'w') as stream:
    yaml.dump(loaded, stream)
