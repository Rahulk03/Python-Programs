import numberss as MN
# import numberss
# from numberss import CheckEven
# from numberss import *
        
def main():
    print("Enter one number")
    value = int(input())
    
    bret = MN.CheckEven(value)

    if bret == True:
        print("{} is Even number".format(value))
    else:
        print("{} is Odd number".format(value))
        
if __name__ == "__main__":
    main()


# Camel case            checkEevn()
# Hungarian case      CheckEven()
# Student case          fun()

# iret
# fret
# lret
