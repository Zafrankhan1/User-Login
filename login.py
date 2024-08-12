user_name : list[tuple[str , str]] = [("Zafran","1234") ,
                                       ("Naveed","5678") ,
                                       ( "Naeem","342") ,
                                       ( "Rafi","5679")
                                         ]

input_user :str = input("Enter user name = ")
input_password : str = input("Enter user password = ")

for row in user_name:
    user , password  = row
    
    if input_user == user and input_password == password:
        print("Valid user")
        break
else:
    print("Invalid user name or password")