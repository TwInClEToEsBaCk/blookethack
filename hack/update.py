#v2.1.1
import requests



repo = requests.get("https://raw.githubusercontent.com/thegamebegins25/blookethack/main/hack/main.py")



file = open("main.py", "r")
if file.read() != repo.text:
    print("Hack is not updated. Do you want to update? (y or n)")
    answer = input()
    if answer == "y":

        file3 = open("main.py", "rU")
        lines1 = file3.readlines()
        file3.close()

        try:
            email = lines1[5]
            password = lines1[6]
        except:
            print("No email or password. You will have to Sre-enter it.")
        print(email + password)
        file2 = open("main.py", "w")
        lines = repo.text.split("\n")
    
        lines[5] = email
        lines[6] = password
    
        file2.writelines(lines)
        file2.close()
        print("Hack updated. Please reload your python interpreter.")
        raise NameError("Quit.")

    else:
        print("Ok. Make sure to update soon for the most recent bug patches and feature updates.")
    file.close()
    



