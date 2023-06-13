import requests,json
cy="\033[1;36m"
def captchakey(key,siteKey):
    url = "https://api.capmonster.cloud/createTask"
    payload = {
    "clientKey":key,
    "task":
    {
        "type":"RecaptchaV3TaskProxyless",
        "websiteURL":"https://open.spotify.com/",
        "websiteKey":siteKey,
        "minScore": 0.3,
        "pageAction": "myverify"
    }}
    key_r = requests.get(url,json=payload)
    print(f"TaskID: {key_r.json()['taskId']}")
    taski = json.loads(key_r.text)['taskId']
    while True:
        payload_r = {
            "clientKey":key,
            "taskId": taski
        }
        url = "https://api.capmonster.cloud/getTaskResult"
        r = requests.post(url,json=payload_r)
        status = json.loads(r.text)['status']
        if status == "ready":
            cap_key = json.loads(r.text)['solution']['gRecaptchaResponse']
            print(f"{cy}Captcha Solved:({cap_key[-10:]})")
            return cap_key

