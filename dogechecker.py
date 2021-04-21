import urllib.request

def requestbalance(address):
	return urlrequest('https://dogechain.info/chain/Dogecoin/q/addressbalance/'+address)
	
def urlrequest(webaddress):
	return urllib.request.urlopen(webaddress).read().decode('utf-8')

print(requestbalance(input('Dogecoin address to check: ')))
