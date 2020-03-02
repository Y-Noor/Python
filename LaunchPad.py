
def launchPad():
    import subprocess
    import datetime
    import os
    #fetch current time
    now = datetime.datetime.now()

    #dictionary of locations that can be accessed
    dict = {
    'googlechrome' : r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    'notepad' : r'C:\Windows\system32\notepad.exe',
    'atom' : r'C:\Users\User\AppData\Local\atom\atom.exe'
    }

    try:
        #display time of entry of instruction
        inpt = input().lower()
        print(now.strftime("[%H:%M:%S]: "), end = '')
        op, target = inpt.split('-')
        if op == 'run':
            subprocess.Popen(dict[target])
        elif op == 'open':
            subprocess.Popen(target)
        elif op == 'computer':
            sys(target)

    except ValueError:
        print('Incorrect format or operation')
        launchPad()

def sys(target):
    if target == 'shutdown':
        os.system("shutdown /s /t 1")
    elif target == 'restart':
        os.system("shutdown /r /t 1")

while True:
    print('Format: operation-target')
    print()
    launchPad()
