import httpx,random,json,Capmonster,requests
import threading,os,names

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

capmonsterCaptchaKey = "efc0ca32f4ade040d9780586d60742f3"
password = "(Pakistan99)"

def generateDOB():
    year = str(random.randint(1985,2001))
    month = str(random.randint(1, 12))
    day = str(random.randint(1,28))
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    return year + '-' + month + '-' + day
def Generate_email(name:str):
    email = name.replace(' ',str(random.randint(100,999)))
    email+=random.choice(['@gmail.com','@hotmail.com','@outlook.com'])
    return email.lower()


class BOT():    
    def event(self,payload):
        res = self.session.post('https://www.spotify.com/api/growth-events/wwwanalyticsnonauth',json=payload)
        self.session.cookies.update(res.cookies)
    def pre_actions(self):
        res = self.session.get('https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email={}'.format(self.email))
        # print(res.text)
        self.event({"category":"check-email-availability","action":"check-email-availability","label":"1"})
    
    def create_account(self):
        self.event({"action":"attempt","category":"signup","context":"","label":"adaptive_email","tags":{"action":"attempt","category":"signup","type":"adaptive_email"}})
        json_data = {
            'account_details': {
                'birthdate': generateDOB(),
                'consent_flags': {
                    'eula_agreed': True,
                    'send_email': True,
                    'third_party_email': True,
                },
                'display_name': self.name,
                'email_and_password_identifier': {
                    'email': self.email,
                    'password': self.password,
                },
                'gender': 1,
            },
            'callback_uri': 'https://www.spotify.com/signup/challenge?locale=it',
            'client_info': {
                'api_key': 'a1e486e2729f46d6bb368d6b2bcda326',
                'app_version': 'v2',
                'capabilities': [
                    1,
                ],
                'installation_id': self.install_id,
                'platform': 'www',
            },
            'tracking': {
                'creation_flow': '',
                'creation_point': 'spotify.com',
                'referrer': '',
            },
        }

        response = self.session.post('https://spclient.wg.spotify.com/signup/public/v2/account/create', json=json_data)
        self.event({"action":"success","category":"signup","context":"","label":"adaptive_email","tags":{"action":"success","category":"signup","type":"adaptive_email"}})
        self.session.cookies.update(response.cookies)
        if response.status_code == 200:
            print(f"{gr}Account_Generator: {self.email}:{self.password}")
            with open('SpotifyAcounts.txt','a',encoding='UTF-8',errors='ignore') as f:
                f.write(f"{self.email}:{self.password}\n")
            return response.json()['success']['login_token']
        else:
            print(response.text)
            print(f"{re}[!] Error: Creating Account")
            return None
    def cookies(self):
        res = self.session.get("https://www.spotify.com/it/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F")
        self.session.cookies.update(res.cookies)
        try:self.install_id = res.cookies['sp_t']
        except Exception as e:print(e)
    def Captcha_success(self):
        self.session.headers.update({'referer': 'https://www.spotify.com/pk-en/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F',})
        json_data = {'action': 'website/signup/success','token': Capmonster.captchakey(capmonsterCaptchaKey,'6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39'),}
        response = self.session.post('https://www.spotify.com/api/signup/recaptcha/assess',json=json_data)
        self.session.cookies.update(response.cookies)
        print(f"{gr}Authenticated:{self.email}")
    def Authenticate(self,token):
        self.session.headers.update({"content-type": "application/x-www-form-urlencoded"})
        res = self.session.post('https://www.spotify.com/api/signup/authenticate',data={"splot":token})
        self.event({"category":"authentication","action":"splot_authentication_success"})

        pass
    def run(self):
        # self.gen_email_password()
        self.name = names.get_full_name()
        self.email = Generate_email(self.name)
        self.cookies()
        self.pre_actions()
        token = self.create_account()
        if token is None:
            return 0 
        self.Captcha_success()
        if not token is None:
            self.Authenticate(token)
    def __init__(self,proxies) -> None:
        PROXY = random.choice(proxies)
        self.password = password
        if not PROXY is None: self.session = httpx.Client(proxies="http://{}".format(PROXY))
        else: self.session = httpx.Client()
        self.session.headers.update({'authority': 'spclient.wg.spotify.com','accept': '*/*','accept-language': 'en-GB,en;q=0.9','cache-control': 'no-cache','origin': 'https://www.spotify.com','pragma': 'no-cache','referer': 'https://www.spotify.com/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',})
        

def reading_proxies():
    try: proxies = open('proxies.txt').read().strip().splitlines()
    except: proxies = []
    if not len(proxies):
        proxies = [None]
    return proxies

def banner():
    if os.name is "nt": os.system('cls')
    else: os.system('clear')
    print(f'''
    {re}╔═╗╔═╗╔═╗{gr}╔╦╗╦╔═╗╦ ╦
    {re}╚═╗╠═╝║ ║ {gr}║ ║╠╣ ╚╦╝
    {re}╚═╝╩  ╚═╝ {gr}╩ ╩╚   ╩ 
    ''')

def Main():
    while True:
        try:
            client = BOT(reading_proxies())
            client.run()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    banner()
    no_thread = int(input(f"{cy}[?] No of Thread: "))
    for i in range(no_thread):
        threading.Thread(target=Main).start()