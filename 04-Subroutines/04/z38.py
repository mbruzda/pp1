import re

x="dsadSAdsadSdasdaAS"

def great(x):
    d = re.findall("[A-Z]", x)
    return d


print(great(x))
