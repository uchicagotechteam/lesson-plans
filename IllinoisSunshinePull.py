import requests
import json

def main():
	url = 'https://www.illinoissunshine.org/api/committees/'
	response = requests.get(url)
	
	print(response.json()['objects'][0]["id"])
	
	#for committee in response.json()['objects']:
	#	print(committee["id"])
		
	print len(response.json()["objects"])
	
	url2 = 'https://www.illinoissunshine.org/api/receipts/?committee_id=2887&amount__ge=10000'
	response2 = requests.get(url2)
	
	print(response2.json())
	

def get_committee_by_id(id, amount):
	base_url = 'https://www.illinoissunshine.org/api/receipts/?committee_id='
	base_url += str(id) + '&' + 'amount__ge=' + str(amount)
	response = requests.get(base_url)
	print(response.json())
	
	
def get_all_receipts(id):
	base_url = 'https://www.illinoissunshine.org/api/receipts/?committee_id='
	base_url += str(id)
	response = requests.get(base_url)
	#response.json()['objects'][0]['receipts']
	rlist = response.json()['objects'][0]['receipts']
	rtotal_amount = 0
	numdonations = 0
	for receipt in rlist:
		rtotal_amount += receipt['amount']
		numdonations += 1
	
	dic = {}
	dic["volume"] = rtotal_amount
	dic["count"] = numdonations
	return dic

def ask_name(name):
	base_url = 'https://www.illinoissunshine.org/api/committee/?'
	name = name.replace(' ', '%20')
	base_url += 'refer_name__like=' + name
	response = requests.get(base_url)
	c_id = response.json()['objects'][0]['id']
	print (get_all_receipts(c_id))
	
	
if __name__ == '__main__':
	main()
