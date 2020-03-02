def create():
    #emailF is email flag pwF is Password Flag, checking whether the password's and email's format are correct
    fname = firstNamae()
    lname = lastNamae()
    email, emailF = mail()
    username = UN()
    # check(email, username)
    print("""Note: Password must be at least 8 characters and contain at least a number , 1 Lcase and Ucase character and no spaces""")
    pw, pwF = PW()

    if pwF == True and emailF == True:
        string = '{}-{}-{}-{}-{}'.format(username, pw, lname, fname, email)
        with open("accounts.txt", "a") as f:
            f.write(string)
            print('Account successfully created')

#inputs
def firstNamae():
    fname = input('Your First Name: ')
    return fname
def lastNamae():
    lname = input('Your Last Name: ')
    return lname
def mail():
    email = input('Your email address: ')
    flag = validateMail(email)
    return email, flag
def UN():
    username = input('Desired username: ')
    return username
def PW():
    pw = input('Password: ')
    pwf = validatePW(pw)
    return pw, pwf

#check whether email or username has already been used to create an account
def check(email, username):
    with open('accounts.txt', "r") as f:
        user = f.readlines()
        for line in user:
            if email in line:
                print('Email already in use')
                print('Please use another address')
                mail = mail()
                check(email, username)
            elif username in line:
                print('Username already exists')
                print('Please select another username')
                username = UN()
                check(email, username)

#check for correct format of email address
def validateMail(email):
    flag = False
    p1, p2, p3, p4 = '', '', '', ''

    if '@' in email:
        p1, p2 = email.split('@')
    else:
        flag = True

    if '.' in p2:
        p3, p4 = email.split('.')
        if p4 == '':
            flag = True
    else:
        flag = True

    if flag == True:
        print('>>>>> Invalid email address')
        mail()
    else:
         return True

#check if criteria of password have been fulfilled
def validatePW(pw):
    Lflag = pw.islower()
    Uflag = pw.isupper()
    NG = True
#NG is a flag which means No Good
    if Lflag == True or Uflag == True:
        print('>>>>>You need to use BOTH lowercase and uppercase')
        NG = False

    if ' ' in pw:
        print('>>>>>NO SPACES ALLOWED!')
        NG = False

    if (any(char.isdigit() for char in pw)):
        pass
    else:
        print('>>>>>Password must contain at least 1 digit')
        NG = False

    if NG == False:
        pw = PW()
        validatePW(pw)
    else:
        dEntry(pw)

    return True

#verification by double entry
def dEntry(pw):
#comp is a variable that will store the second entry will be used to validate the password
    comp = input('Please re-enter password')

    if comp == pw:
        print('>>>>> Password OK')
        return True

    else:
        print('Wrong second entry. Try again(1) or input new password(2)?')
        choice = input('Choice: ')

        if choice == '1':
            dEntry(pw)
        else:
            PW()


#interface
print("""1. Create an account
2. Log In""")
choice = input('Choice: ')
if choice == '1':
    create()
