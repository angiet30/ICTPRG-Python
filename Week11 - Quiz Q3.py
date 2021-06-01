import re
regex = '^[A-Za-z0-9]+[\.]?[A-Za-z0-9]+[@]\w+[.]\w{2,32}$'
def main():
    email = input("Enter your email: ")
    while True:
        if(re.search(regex,email)):
            print("Valid Email")
        else:
            print("Invalid Email")
            break
    email = input("Enter your email: ")
if __name__ == '__main__':
    main()