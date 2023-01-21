def input_str() -> int:
    """
        Fetchs valid str input from user 
    """    

    val = input()
    return val

def input_int() -> int:
    """
        Fetchs valid integer input from user 
    """    
    while True:
        try:
            val = input()
            val = int(val)
            break
        except ValueError:
            print("Please enter valid integer")

    return val

def input_float() -> int:
    """
        Fetchs valid float input from user 
    """    
    while True:
        try:
            val = input()
            val = float(val)
            break
        except ValueError:
            print("Please enter valid float")

    return val

