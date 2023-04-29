import re
def check_email(email) :
    pattern=r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return True if re.match(pattern, email) else False   


e= input("Enter your email: ")
if check_email(e) :
    print("OK")
else :
    print("WRONG")