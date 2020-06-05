# Use words.txt as the file name
while True:
    fname = input('Enter file name:')
    if fname == 'exit':
        print('\nSee you!.')
        quit()
    try:
        fh = open(fname)
        break
    except:
        print('\nFile does not exist, write "exit" or try again.')
        import time
        time.sleep(0.2)
        continue
for line in fh:
    print(line.upper().rstrip())
