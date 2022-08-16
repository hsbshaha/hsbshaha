import sys as n, random, time, webbrowser, requests, time as mm
token = input('- Enter Token :  ')
ID = input('- Enter ID :  ')
X = 1
ABC = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
klshy = 'ABCDEFGHIKLMNOPQSTVWSYZ0987654321'
Extrra = 1
while True:
    F = ''.join(random.sample(ABC, Extrra))
    G = ''.join(random.sample(klshy, Extrra))
    FF = G + F + G + G + G 
    NN = G + F + F + F + F 
    BB = F + G + G + G + F 
    CC = F + F + G + G + G 
    DD = F + F + F + F + G 
    AA = F + F + F + G + F 
    EXTRA = (FF, NN, BB, CC, DD, AA)
    user = str(''.join(random.choice(EXTRA)))
    url = f"https://t.me/{user}"
    req = requests.get(url)
    if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        print(f"'\x1b[1;32m  [   {X}   ] GOOD : {user} ")
        try:
            req = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Hi New User\n================= \n User : @{user}\n================= ")
        except NameError:
            pass

    else:
        print(f"\x1b[2;39m [  {X}  ] NoT GOOD >>  {user} ")
    X += 1
