def list_divide(numbers,divide=2):
    count=0
    for x in numbers:
        if x % divide == 0 :
            count=count+1
        else :
            continue 
    return count    



class ListDivideException(Exception):
    pass


def test_list_divide():
        
    try:
        result=list_divide([1,2,3,4,5])
        if result!=3:
            raise ListDivideException("Test failed")
    except ListDivideException:
        print("Exception occurred: Invalid Output")    
        
def main():
    try:
        test_list_divide()
    except ListDivideException as e:
        print("Test failed: {e}")

if __name__ == "__main__":
    main()


