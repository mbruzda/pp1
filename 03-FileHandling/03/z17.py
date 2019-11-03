import re
zdanie='To be, or not to be, that is the question'
samogloski=re.findall('[aeiouy]',zdanie)
print(len(samogloski))