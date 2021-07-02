def main():
    no1 = int(input("Enter first number"))
    no2 = int(input("Enter second number"))
    
    try:
        print("Inside try")
        ans = no1 / no2
    
    except ZeroDivisionError as obj:
        print("Divide by zero excetion ",obj)
    
    else:
        print("Inside else")
        print("Division is : ",ans)
    
    finally:
        print("Inide finally")
        print("Deallocate all the resources")
        
if __name__ == "__main__":
    main()