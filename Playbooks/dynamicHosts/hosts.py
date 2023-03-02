#!/user/bin/env python

import json

# handle --list and --host args
def getCLIArgs():
  global args
  parser = argparse.ArgumentParser()
  parser.add_argument('--list', action='store_true')
  parser.add_argument('--host', action='store')
  args = parser.parse_args()

def getHosts():
  return {
    "dbs": {
      "hosts": ["vm1"],
      "vars": {
        "ansible_ssh_host": "vm1",
        "ansible_ssh_pass": "Passw0rd"
      }
    }, "web": {
      "hosts": ["vm1"],
      "vars": {
        "ansible_ssh_host": "vm2",
        "ansible_ssh_pass": "Passw0rd"
      }
    }
  }

if __name__ == "__main__":
  global args
  getCLIArgs()
  hosts = getHosts()
  if(args.list):
    print(json.dumps(hosts))
  else:
    print(json.dumps({"_meta": {"hostvars": {}}}))