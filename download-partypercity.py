import urllib
import ssl
import simplejson
from tqdm import tqdm

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for http_obj in urllib.urlopen("https://pemilu2019.kpu.go.id/static/json/hr/dprri.json", context=ctx):
	all_dapil = simplejson.loads(http_obj.decode("utf-8"))

for http_obj in urllib.urlopen("https://pemilu2019.kpu.go.id/static/json/wilayah/0.json", context=ctx):
	all_wilayah = simplejson.loads(http_obj.decode("utf-8"))

for http_obj in urllib.urlopen("https://pemilu2019.kpu.go.id/static/json/partai.json", context=ctx):
	party = simplejson.loads(http_obj.decode("utf-8"))
	f = open("result/party.txt", "w")
	f.write(simplejson.dumps(party))
	f.close()

all_wilayah.pop("-99")

for dapil in tqdm(all_dapil.get("table").keys()):
	for province_key, province_value in all_wilayah.items():
		if int(dapil) in province_value.get("dapil"):
			wilayah_key = province_key
			province_name = province_value.get("nama")
	for http_obj in urllib.urlopen("https://pemilu2019.kpu.go.id/static/json/wilayah/" + wilayah_key + ".json", context=ctx):
		some_city = simplejson.loads(http_obj.decode("utf-8"))
	for http_obj in urllib.urlopen("https://pemilu2019.kpu.go.id/static/json/hr/dprri/" + dapil + ".json", context=ctx):
		all_city = simplejson.loads(http_obj.decode("utf-8"))
		for city in all_city.get("table"):
			if(city != "-99"):
				for http_obj in urllib.urlopen("https://pemilu2019.kpu.go.id/static/json/hr/dprri/" + dapil + "/" + city + ".json", context=ctx):
					votes = simplejson.loads(http_obj.decode("utf-8")).get("chart")
				name = some_city[city].get("nama")
				result = {
					"name" : name,
					"votes" : votes
				}
				f = open("result/" + province_name + ".txt", "a")
				f.write(simplejson.dumps(result) + ",")
				f.close()