from nsetools import Nse
nse = Nse()

q = nse.get_quote('tcs') # it's ok to use both upper or lower case for codes.
print(q)