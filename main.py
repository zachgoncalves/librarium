import book

isWorking = True;
print('Welcome to Librarium!')

while(isWorking):
    print('This is a test')
    reply = input('Enter a command. ')

    if reply == 'stop':
        print('It is done!')
        isWorking = False
    else:
        print('Please insert a valid command \n')
