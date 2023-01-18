#coding = utf-8
try:
    import os,sys,time,requests,random,re
except ModuleNotFoundError:
    os.system('pip install requests')

logo="""
\t##     ##     #######     ########  
\t##     ##    ##     ##    ##     ## 
\t##     ##    ##     ##    ##     ## 
\t#########    ##     ##    ########  
\t##     ##    ##     ##    ##
\t##     ##    ##     ##    ##
\t##     ##     #######     ##
--------------------------------------------------
 Author: Muhammad Hamza
 Github: https://github.com/hop09
 Version: 1.1
--------------------------------------------------"""
class CheckUpdate:
    def __init__(self):
        self.update = 'https://raw.githubusercontent.com/hop09/file/main/version.txt'
        self.cv = 1.1
        self._update()


    def _update(self):
        try:
            self.server = requests.get(self.update).text
            if float(self.server) == self.cv:
                self.credentials()
            else:
                os.system('rm -rf file.py && curl -L https://raw.githubusercontent.com/hop09/file/main/file.py > file.py && python file.py')
        except requests.exceptions.ConnectionError:
            print(' No internet connection !')


    def credentials(self):
        try:
            self.cfile = open('credentials.txt','r').read()
            self.cookie,self.token = self.cfile.split('|')
        except FileNotFoundError:
            login()
        login_verify(self.cookie,self.token).check()

class login_verify:
    def __init__(self,cookie,token):
        self.cookie = cookie
        self.token = token
        self.headers = {'cookie':self.cookie}
        os.system('rm -rf .txt .temp.txt')
        self.ids = []


    def check(self):
        try:
            self.name = requests.get(f'https://b-graph.facebook.com/me?access_token={self.token}',headers=self.headers).json()['name']
            print(f' Logged in as: {self.name}')
            time.sleep(1)
            self.main()
        except KeyError:
            print(' Logged in user expired, try another !')
            os.system('rm -rf credentials.txt')


    def main(self):
        os.system('clear')
        print(logo)
        print(' [1] Mutli extract ids')
        print(' [2] Auto file extract all links')
        print(' [3] Extract from file')
        print(' [E] Exit')
        self.opt = ['1','2','3','E','e']
        self.user = input(' Select option: ')
        while self.user not in self.opt:
            print('\n Choose valid option !')
            self.user = input(' Select option: ')
        if self.user == '1':
            self.multi()
        elif self.user == '2':
            self.auto()
        elif self.user == '3':
            self.file()
        else:
            exit()


    def multi(self):
        os.system('clear')
        print(logo)
        try:
            idlimit = int(input(' How many ids do you want to add: '))
        except ValueError:
            print(' Ids limit should be in digits !')
        self.sf = input(' Save file as: ')
        self.saveids = open(self.sf,'a')
        for xd in range(idlimit):
            try:
                self.idt = input(f' Put id no.{xd+1}: ')
                self.r = requests.get(f'https://b-graph.facebook.com/v9.0/{self.idt}/friends?limit=5000&summary=true&access_token=' + self.token,headers=self.headers).json()
                for cd in self.r['data']:
                    iid = cd['id']
                    name = cd['name']
                    self.saveids.write(iid+"|"+name+"\n")
                    self.ids.append(iid)
            except KeyError:
                print(' No friends !')
            except requests.exceptions.ConnectionError:
                print(' No internet connection !')
            sys.stdout.write(f'\r Total collected ids: {len(self.ids)}\r');sys.stdout.flush()
        print(50*'-')
        input(' Press enter to back ')


    def auto(self):
        os.system('clear')
        print(logo)
        try:
            idlimit = int(input(' How many ids do you want to add: '))
        except ValueError:
            print(' Ids limit should be in digits only !')
        for xd in range(idlimit):
            self.idt = input(f' Put id no.{xd+1}: ')
            try:
                r = requests.get(f'https://b-graph.facebook.com/v9.0/{self.idt}/friends?limit=5000&summary=true&access_token=' + self.token,headers=self.headers).json()
                for xd2 in r['data']:
                    uid = xd2['id']
                    open('.txt','a').write(uid+"\n")
            except KeyError:
                print(' No friends !')
            except requests.exceptions.ConnectionError:
                print(' No internet connection !')
        print('\n Example: 100074,100084,100085 etc')
        try:
            sl = int(input('\n How many links do you want to grab: '))
        except:
            sl = 1
        for el in range(sl):
            sid = input(f' Put {el + 1} link: ')
            os.system('cat .txt | grep "' + sid + '" > .temp.txt')
        sf = input(' Put path to save file: ')
        file = open('.temp.txt', 'r').read().splitlines()
        print('')
        print(' Total ids: ' + str(len(file)))
        print(' Grabbing process has started')
        print(50 * '-')
        saveids = open(sf,'a')
        for nexd in file:
            try:
                r = requests.get(f'https://b-graph.facebook.com/v9.0/{self.idt}/friends?limit=5000&summary=true&access_token=' + self.token,headers=self.headers).json()
                for oop in r['data']:
                    iid = oop['id']
                    name = oop['name']
                    saveids.write(iid+"|"+name+"\n")
                    self.ids.append(iid)
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                print(' No internet connection !')
            sys.stdout.write(f'\r Collected ids: {len(self.ids)}');sys.stdout.flush()
        saveids.close()
        print(50*'-')
        print(f' Total ids grabbed: {len(self.ids)}')
        print(' The process has been completed')
        print(50*'-')
        input(' Press enter to back ')


    def file(self):
        count = []
        os.system('rm -rf .s.txt && clear')
        print(logo)
        try:
            self.file = input(' Put file path: ')
            if os.path.isfile(self.file):
                pass
            else:
                print(' No file found on given path !')
                os.sys.exit()
            print('\n [1] Extract newest ids')
            print(' [2] Extract oldest ids')
            print(' [3] Extract shuffle (mixed)')
            self.askType = input(' Choose ids type: ')
            if self.askType == '1':
                os.system(f'sort -r {self.file} > .s.txt')
            elif self.askType == '2':
                os.system(f'sort {self.file} > .s.txt')
            else:
                os.system(f'sort {self.file} > .s.txt')
            self.mainfile = open('.s.txt','r').read().splitlines()
        except:
            print(' Unknown error, contact author !')
        self.save = input('\n Save file as: ')
        os.system('clear')
        print(logo)
        print(f' Total ids to extract: {len(self.mainfile)}')
        print(' Grabbing process has been started')
        print(' Press ctrl c to stop')
        print(50*'-')
        self.dictt = ['\033[1;32m 0_0','\033[1;31m -_- ']
        self.ofile = open(self.save,'a')
        for usp in self.mainfile:
            try:
                waada = usp.split('|')[0]
                sys.stdout.write(f'\r {random.choice(self.dictt)} {waada} | {len(count)} \033[0;97m');sys.stdout.flush()
                self.r = requests.get(f'https://b-graph.facebook.com/v9.0/{waada}/friends?limit=5000&summary=true&access_token=' + self.token,headers=self.headers).json()
                for xd in self.r['data']:
                    self.uid = xd['id']
                    self.name = xd['name']
                    self.ofile.write(f"{self.uid}|{self.name}\n")
                    count.append(self.uid)
            #    sys.stdout.write(f'\r Total collected ids: {len(count)}');sys.stdout.flush()
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                print(' No internet connection !')
        self.ofile.close()
        print(50*'-')
        print(' The process has been completed ')
        print(f' Total id extracted: {len(count)}')
        print(50*'-')
        input(' Press enter to back ')

def login():
    os.system('clear')
    print(logo)
    print(' [1] Login with cookie')
    print(' [2] Help')
    user = input(' Select option: ')
    if user == '1':
        loginM().main()
    elif user == 'H' or user == '2':
        print(' No help available hehehehe :)')
    else:
        exit()
class loginM:
    def __init__(self):
        self.session = requests.Session()
        self.url = 'https://web.facebook.com/adsmanager/manage'
        self.actUrl = 'https://web.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'
        self.ua = 'Mozilla/5.0 (Linux; Android 12; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
        
        
    def main(self):
        os.system('clear')
        print(logo)
        self.cookie = input(' Paste cookie here: ')
        try:
            self.content = self.session.get(self.url,cookies={'cookie':self.cookie}).text
            self.act = re.findall('act=(.*?)&nav_source',self.content)
            if self.act == 0:
                print('\n cannot parse provided cookie, may be the account is enrolled in a checkpoint !')
                exit()
            else:
                for xd in self.act:
                    self.generate_url = self.session.get(f"{self.actUrl}".format(xd),cookies={'cookie':self.cookie}).text
                    self.accessToken = re.search('(EAAB\w+)',self.generate_url).group(1)
                    if 'EAAB' in self.accessToken:
                        open('credentials.txt','a').write(self.cookie+'|'+self.accessToken)
                    else:
                        print('\n cannot find access token, internal script error !')
                        exit()
                print(' Logged in successfully !')
                time.sleep(1)
                checkUpdate()
        except AttributeError:
            print('\n invalid cookie format !')
CheckUpdate()