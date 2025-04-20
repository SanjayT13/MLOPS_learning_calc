from calc_func import do_addition,do_subtraction
from multiply import do_multiplication

def main() : 
    print("welcome to calculator app")
    print(""" select functions from following : \n
    1. add \n 
    2. subtract \n
    3. Multiply""")
    user_input = int(input("select the function : "))
    a = int(input("Value of A :"))
    b = int(input("Value of B :"))
    if user_input == 1 : 
        result = do_addition(a,b)
    elif user_input == 2 :
        result = do_subtraction(a,b) 
    elif user_input == 3 : 
        result = do_multiplication(a,b)
    print("result : ", result)
    return result 

if __name__ == "__main__" : 
    main()

        
