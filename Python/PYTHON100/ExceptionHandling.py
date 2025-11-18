def devide(dividend,divisor):
    try :
       result =  dividend/divisor
    except ZeroDivisionError:
        print("Cannot divide to zero")
    except Exception as e:
        print("any other error ",e)
    else:
        return result
    

print(devide(10,0))
        
