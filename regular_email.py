import re


def email_checking(email_in):
    spliter = email.split("@")
    if len(spliter) != 2:
        return False
    username = spliter[0]
    hostname = spliter[1]

    user_patt = '^[a-zA-Z0-9!# %&`*+-/=?^_{|}~][a-zA-Z0-9!# %&`*+-/=?^_{|}~.]*\.[a-zA-Z0-9!# %&`*+-/=?^_{|}~]*$|^[a-zA-Z0-9!# %&`*+-/=?^_{|}~]+$'
    res1 = re.fullmatch(user_patt, username)
    #print("ВывоД: ", res1)

    host_patt = '^[a-zA-Z0-9][a-zA-Z0-9-]{1,62}(\.[a-zA-Z0-9-]{1,63})*[a-zA-Z0-9]$'
    res2 = re.fullmatch(host_patt, hostname)
    #print("ВывоД: ", res2)

    if res2 != None and res1 != None:
        return True
    else:
        return False


email = "use#rn.ame@7-dosrg.asg-sd.dsrg"
print(f"{email} прошёл проверку с отметкой: {email_checking(email)}  ")
print("Введите мыло:")
email=input()
print(f"{email} прошёл проверку с отметкой: {email_checking(email)}  ")