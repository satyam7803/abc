#    Email-slicer   ##

email=input("Enter your Email: ")
username=email[:email.index("@")]
domain=email[email.index("@")+1:]
a=(f"username : {username} and domain : {domain}")
print(a)