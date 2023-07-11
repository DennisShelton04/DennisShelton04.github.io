import string


def Encryption(password, n):
    u_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZABabcdefghijklmnopqrstuvwxyzab"
    encryPassword = ""
    # print(password)
    for i in password:
        if i in u_case:
            index = u_case.index(i)
            encryPassword += u_case[index+2]
        else:
            encryPassword += i
    print(encryPassword)


n = 2
password = input("Enter the password")
Encryption(password, n)
