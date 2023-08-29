def list_divide(numbers,divide=2):
    count=0
    for x in numbers:
        if x % divide == 0 :
            count=count+1
        else :
            continue 
    return count                  