

import subprocess
cmd_client = 'pwd'
cmd_result = subprocess.Popen(cmd_client,shell=True, stdout=subprocess.PIPE)
cmd_result = cmd_result.stdout.read()
print(cmd_result)
print(bool(cmd_result))