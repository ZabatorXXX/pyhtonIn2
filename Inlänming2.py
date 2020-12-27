def mainMenu():
    print("1. Info for tenta")
    print("2. Text material")
    print("3. Quit")
    while True:
        try:
            selection=int(input("Enter vall: "))
            if selection==1:
             infor_for_tenta()
             break
            elif selection==2:
             list_function()
             break
            elif selection==3:
                text_material ()
                break
            else:
                print("Invalid choice. Enter 1-3")
                mainMenu()
        except ValueError:
            print("Invalid choice. Enter 1-3")
            
    exit

def infor_for_tenta():
    svar = ["[1] Linus Torvalds", "[2] Operativ systemt blev till tidigt 1990", "[3] Open sorce betyder att koden är öppen för anmällheten att kunna använda sig utav.",
            "[4] Man kan ha flera if men man skriver bara ha en else. Kan också använda elif.", "[5] Python är case sensitiv.", "[6]Svaret på frågan: Med tecknet (#) brädgård eller en multi line kommentar '''  ", "                                                                            '''  ",
            "[7] Print Working Directory."]
    for knowledge in svar:
        print(knowledge)   
    anykey=input("Enter anything to return to main menu: ")
    mainMenu()

def text_material():
    print("You ended the program")
    

def list_function():
    info = [
        "[1] Vem skapa linux?", "[2] När skapades linux?", "[3] Vad är Open source?",
        "[4] Kan man kombinera flera if else?", "[5] Är Python case sensitive?",
       "[6] Hur skapar man kommentarer I python?", "[7] Vad gör pwd kommandot?"                        ]
    for chooses in info:
        print(chooses)   
    
    choice = input("Matta in numer [1][2][3][4][5][6][7]: ")
    anwser = ''
    if choice == '1':
        anwser = "Svaret på frågan: Linus Torvalds."
    elif choice == '2':
        anwser = "Svaret på frågan: Operativ systemt blev till tidigt 1990."
    elif choice == '3':
        anwser = "Svaret på frågan: Open sorce betyder att koden är öppen för anmällheten att kunna använda sig utav."
    elif choice == '4':
        anwser = "Svaret på frågan: Man kan ha flera if men man skriver bara ha en else. Kan också använda elif."
    elif choice == '5':
        anwser = "Svaret på frågan: Python är case sensitiv."
    elif choice == '6':
        anwser ="Svaret på frågan: Med tecknet (#) brädgård eller en multi line kommentar '''  " 
        anwser +="                                                                      '''  "
    elif choice == '7':
        anwser = "Svaret på frågan: Print Working Directory."    

    else:
        print("Invalid Input", "Try number from 1 - 7")
        mainMenu()
    print(anwser)
    open('history.text', 'a+').write(choice + ' ' + anwser +  '\n') 
# main routine
mainMenu()
