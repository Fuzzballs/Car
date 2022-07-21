command = ""
started = False
stopped = False

while command != "quit":
    command = input(">").lower()
    if command == "start":
        if started:
            print("Already started.  No need to double start!")
        else:
            print("Car started")
            started = True
            
    elif command == "stop":
        if stopped:
            print("You might want to try turning it on genius...")
        else:
            print("Car stopped")
            stopped = True
    elif command == "help":
        print('''
        start - to start the car
        stop - to stop the car
        quit - to quit 
        ''')
    elif command == "quit":
            break
    else:
        print("Sorry dont understand what has been entered")
    
