

import subprocess
cmd_client = 'pwd'



import sys
import os


with open('data_send/put.txt','r') as rf:
    for i in rf:
        print(len(i))
        i += i
    print(len(i))