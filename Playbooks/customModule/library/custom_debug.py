#!/bin/python

DOCUMENTATION = '''
---
module: custom_debug
short_description: Custom module example
description:
  - Print custom debug message
version_added: 0.1
author: No One
notes:
requirements:
options:
  msg:
    description: Message to be output
    required: True
'''

EXAMPLES = '''
# Example
custom_debug:
  msg: Hello World
'''

RETURN = '''
msg:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'Thu 02 Mar 2023 11:05:36 AM EST - hello world'
'''


## END ansible-doc DETAILS


try:
  import json
except ImportError:
  import simplejson as json

from ansible.module_utils.basic import AnsibleModule
import time
import sys

def main():
  module = AnsibleModule(
    argument_spec = dict(
      msg=dict(required=True, type='str')
    )
  )
  msg = module.params['msg']
  try:
    module.exit_json(changed = True, msg = "%s - %s" % (time.strftime("%c"), msg))
    #print(json.dumps({
    #  msg: "%s - %s" % (time.strftime("%c"), msg),
    #  "changed": True
    #}))
    #sys.exit(0)
  except:
    module.fail_json(msg = "Failed debugging")
    #print(json.dumps({
    #  "failed": True,
    #  "msg": "Failed debugging"
    #}))
    #sys.exit(1)

if __name__ == "__main__":
  main()