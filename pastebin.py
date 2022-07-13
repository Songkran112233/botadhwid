import requests, re

class PastebinApi():
	client = None
	def __init__(this, client):
		this.client = client

	def edit(this, id, text):
		if len(str(id).strip()) == 0:
			raise Exception("Invaild paste")
			
		paste = this.client.get("https://pastebin.com/" + str(id))
		if paste.status_code != 200:
			raise Exception("Invaild paste")

		pasteName = re.search("<h1>(.*)</h1>", paste.text).group(1)
		state = 1

		if "class=\"unlisted\"" in paste.text: state = 1
		else: state = 0

		editData = {
			"_csrf-frontend": getCSFR(this.client.get("https://pastebin.com/edit/" + str(id)).text),
			"PostForm[format]": 1,
			"PostForm[expiration]": "PREV",
			"PostForm[status]": state,
			"PostForm[folder_key]": "",
			"PostForm[folder_name]": "",
			"PostForm[is_password_enabled]": 0,
			"PostForm[is_burn]": 0,
			"PostForm[name]": pasteName,
			"PostForm[text]": str(text)
		}
		
		response = this.client.post("https://pastebin.com/edit/" + str(id), data=editData)
		if response.status_code == 302 or response.status_code == 200:
			return True
		else:
			raise Exception("Invaild response code\n" + response.text)

def login(token):
	client = requests.Session()
	client.cookies["_identity-frontend"] = token
	if "<a href=\"/signup\"><b>Sign Up</b>" in client.get("https://pastebin.com").text:
		raise Exception("Invaild Token")
	return PastebinApi(client)

def getCSFR(response):
	return re.search("<meta name=\"csrf-token\" content=\"(.*)\">", response).group(1)