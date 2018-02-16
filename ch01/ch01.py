import json
import os
homedir = os.getcwd()

path = 'lib/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line)
           for line in open(path)]
print(records[0])