class Lexer:
    def __init__(self):
        pass

    @property
    def getToken(self):
        return self.token
    
def showTable():
    file = open("example.txt", "r")
    data = file.read().split()

    reserved_words = ["for", "while", "if", "else"]
    similar_id = []
    index = len(reserved_words) - 1

    for i in data:
        if i.isnumeric():
            print(f'<token=INTEGER, integer_value={i}>')
        elif i in reserved_words:
            print(f'<token={i.upper()}>')
        elif "-" in i and "." in i:
            print(f'<token=FLOAT, float_value={i}>')
        elif '.' in i:
            print(f'<token=FLOAT, float_value={i}>')
        elif "-" in i:
            print(f'<token=INTEGER, integer_value={i}>')
        elif "&&" == i:
            print(f'<token=LOGICAL_AND>')
        elif "&" == i:
            print(f'<token=BITWISE_AND>')
        elif "||" == i:
            print(f'<token=LOGICAL_OR>')
        elif "|" == i:
            print(f'<token=BITWISE_OR>')
        elif i[0].isdigit():
            print(f'<token=ERROR, unrecognized_string="{i}">')
        else:
            # use previous index if data is in file
            if i in similar_id:
                print(f'<token=ID, index={similar_id.index(i) + 4}>')
            # use a new index
            else:
                similar_id.append(i)
                index += 1
                print(f'<token=ID, index={index}>')


    file.close()

def getLex(userinput,index,similar_id):
    print("Calling Lex")
    reserved_words = ["for", "while", "if", "else"]
    if userinput.isnumeric():
        print(f'<token=INTEGER, integer_value={userinput}>')
    elif userinput in reserved_words:
        print(f'<token={userinput.upper()}>')
    elif "-" in userinput and "." in userinput:
        print(f'<token=FLOAT, float_value={userinput}>')
    elif '.' in userinput:
        print(f'<token=FLOAT, float_value={userinput}>')
    elif "-" in userinput:
        print(f'<token=INTEGER, integer_value={userinput}>')
    elif "&&" == userinput:
        print(f'<token=LOGICAL_AND>')
    elif "&" == userinput:
        print(f'<token=BITWISE_AND>')
    elif "||" == userinput:
        print(f'<token=LOGICAL_OR>')
    elif "|" == userinput:
        print(f'<token=BITWISE_OR>')
    elif userinput[0].isdigit():
        print(f'<token=ERROR, unrecognized_string="{userinput}">')
    else:
        # use previous index if data is in file
        if userinput in similar_id:
            print(f'<token=ID, index={similar_id.index(userinput) + 4}>')

        # use a new index
        else:
            similar_id.append(userinput)
            print(f'<token=ID, index={index}>')
            return "id"
    return similar_id

count = 0
index = 4
similar_id = []

print("Welcome To The Lexical Analyser")
while(True):
    print("MENU")
    print("1- Call Lex")
    print("2- Show Symbol Table")
    print("3- Exit")
    usrinp = int(input("Please choose a command: "))

    if usrinp == 1:
        print("Calling lex...")
        #create new object
        lex = Lexer()


        while True:

            file = open("example.txt", "r")
            data = file.read().split()
            if count == len(data):
                print("No more token left")
                break
            else:
                if getLex(data[count], index, similar_id) == "id":
                    index += 1

                count += 1
                userinput = input("Call again? (y/n): ")
                if userinput == "y":
                    continue
                else:
                    break



        inpt =input("Do you want to continue with the menu? (y/n): ")
        if inpt == "y":
            continue
        else:
            print("Exiting..")
            print("Thank you")
            break
    elif usrinp == 2:
        print("Showing table...")
        lex = Lexer()
        showTable()
        inpt = input("Do you want to continue? (y/n): ")
        if inpt == "y":
            continue
        else:
            print("Exiting..")
            print("Thank you")
            break
    elif usrinp == 3:
        print("Exiting..")
        print("Thank you")
        break
    else:
        print("Not a valid command! Please try again.")