import csv, os, secrets, string
 
symbols = string.punctuation
dictionary = []

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'CSV','dictionary.csv'), mode='r', encoding='utf-8-sig') as infile:
    reader = csv.reader(infile)
    for word in reader:
         if 3 < len(word[0]) < 6 and word[0] != '#NAME?' and word[0] not in dictionary:
            dictionary.append(word[0])

def screen_clear():
   # for mac and linux (here, os.name is 'posix')
   if os.name == 'posix':
      os.system('clear')
   else:
      # for windows platfrom
      os.system('cls')

def PasswordGen(length):
    pw = ''

    while len(pw) < length:
        
        pw = pw + secrets.choice(dictionary).capitalize()
        
        if len(pw) > length-3:
            pw = ''
        elif len(pw) > length-5:
            pw = pw + ('!' * (length-len(pw)))

    pw = pw[:pw.find('!')]

    while len(pw) < length-1:
        num = secrets.randbelow(10)
        if str(num) not in pw:
            pw = pw + str(num)

    return pw + secrets.choice(symbols)

def loop_or_close():
    check = True

    # Error handling
    while check:
        question = str(input('Again? (Y/N): ')).upper()
        
        if not question.isalpha():
            print('\nInvalid input. Please type a letter.')
        elif question not in ['Y', 'N']:
            print(question)
            print('\nInvalid input. Please type \'Y\' or \'N\'.')
        else:
            check = False

    if question == 'Y':
        screen_clear()
        length = int(input('Enter desired password length: '))
        print(PasswordGen(length))
    elif question == 'N':
        exit()


screen_clear()
    
length = int(input('Enter desired password length: '))
    
print(PasswordGen(length))

while 1>0:
    loop_or_close()
