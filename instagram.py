import requests

url = "https://instagram47.p.rapidapi.com/user_following"

querystring = {"userid":"1718924098"}

headers = {
	"X-RapidAPI-Key": "d977f8c800mshdfbacd57a494881p1fe855jsn572c74768652",
	"X-RapidAPI-Host": "instagram47.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)