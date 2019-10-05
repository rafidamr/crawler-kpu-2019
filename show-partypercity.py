import simplejson
import operator

while(1):
	query = raw_input("Province Name: ").upper()
	jsonparty = open("result/party.txt", "r").read()
	jsonvote = open("result/" + query + ".txt", "r").read()
	jsonvote = jsonvote[:len(jsonvote) - 1]

	province = simplejson.loads('[' + jsonvote + ']')
	parties = simplejson.loads(jsonparty)

	for city in province:
		name = city.get("name")
		votes = city.get("votes")
		if(votes != None):
			sorted_v = sorted(votes.items(), key=operator.itemgetter(1), reverse=1)
			party = parties.get(sorted_v[0][0]).get("nama")
			count = sorted_v[0][1]
		else:
			party = None
			count = None
		print(name, party, count)
	print("\n")