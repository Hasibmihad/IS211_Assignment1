''' function : list divide'''

def list_divide(numbers,divide=2):
    count=0
    for x in numbers:
        if x % divide == 0 :
            count=count+1
        else :
            continue 
    return count    



''' class : list divide exception'''

class ListDivideException(Exception):
    pass


''' function :test_list divide'''

def test_list_divide():
    
    try:
        ''' should result 2, if not ,raise exception '''
        result=list_divide([1,2,3,4,5])   
        if result !=2:
            raise ListDivideException
    except ListDivideException:
        print("Exception occurred: Invalid Output")   



    try:
        ''' should result 5, if not ,raise exception '''
        result=list_divide([2,4,6,8,10])
        if result !=5:
            raise ListDivideException
    except ListDivideException:
        print("Exception occurred: Invalid Output")  


    try:
        ''' should result 2, if not ,raise exception '''
        result=list_divide([30, 54, 63,98, 100], divide=10) 
        if result !=2:
            raise ListDivideException
    except ListDivideException:
        print("Exception occurred: Invalid Output")   



    try:
        ''' should result 0, if not ,raise exception '''
        result=list_divide([])
        if result !=0:
            raise ListDivideException
    except ListDivideException:
        print("Exception occurred: Invalid Output")  


    try:
        ''' should result 1, if not ,raise exception '''
        result=list_divide([1,2,3,4,5], 1)
        if result !=5:
            raise ListDivideException
    except ListDivideException:
        print("Exception occurred: Invalid Output")              

        
def main():
    try:
        test_list_divide()
    except ListDivideException:
        print()

if __name__ == "__main__":
    main()


