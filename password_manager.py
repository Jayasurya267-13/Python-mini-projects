master_pwd: str=input("what is your master apssword? ")

def add():
    name= input("account name: ")
    pwd= input("password: ")
    with open("passwords.txt","a") as f:
        f.write(name + "|" + pwd + "\n")
    
def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user, pwd=data.split("|")
            print("Account:", user, "| Password:", pwd)

while True:
    mode=input("would you like to add a new password or view existing ones (view/add)? ").lower()
    if mode=="q":
        break
    elif mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("invalid mode")