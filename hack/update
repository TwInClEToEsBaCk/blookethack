import requests

repo = requests.get("https://raw.githubusercontent.com/thegamebegins25/blookethack/main/hack/main.py")



file = open("BlooketBuy.py", "r")
if file.read() != repo.text:
    print("Hack is not updated. Updating file.")
    file2 = open("BlooketBuy.py", "w")
    lines = repo.text.split("\n")
    file2.writelines(lines)
    file2.close()
    print("Hack updated. Please reload Visual Studio on all instances. You will have to re-enter your username and password.")
file.close()

