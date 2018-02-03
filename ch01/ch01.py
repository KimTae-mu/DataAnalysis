import json
import os
homedir = os.getcwd()

path = 'usagov_bitly_data2012-03-16-1331923249.txt'
'''大解放发生的奇偶发爱妃我免费电视'''
records = [json.loads(line)
           for line in open(path)]
print(records[0])