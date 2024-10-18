                        # (A)
                        
                        
  # (1) buffer_info() : The buffer_info() function is used to get the memory address and
    #   the length of the buffer that holds the array's contents return in  the tuple form.
    
  #(2) tolist() : The tolist() function is a use for converting arrays to lists.
  
  # (3) count(<value>) : The count() is used to count how many times a particular element is 
    #   present in the array. The return value will be the number returned by the count().
    
    


                        #(B)


import array

def conversion(words):
    # u : unicode string or character
    char_array = array.array('u',''.join(words).replace(" ",""))
    print(char_array)
    char_array = array.array('u', map(lambda x: x.lower(),char_array))
    print(char_array)
    # char_array = array.array('u', set(char_array))
    # print(char_array)
    char_array = array.array('u', dict.fromkeys(char_array))
    print(char_array)
    words =  ''.join(char_array)
    return  type(words),words

                     #(C)
   
   
def process_array(input_array):
    
    # Part--1 converting in absolute value using abs method
    for i in range(len(input_array)):
        if input_array[i] < 0:
            input_array[i] = abs(input_array[i])
    print(input_array)
    
    
    # Part--2 creating one new array that will be unique array
    unique_array = array.array('i', [])
    for num in input_array:
        if num not in unique_array:
            unique_array.append(num)
    print(unique_array)
    
    # Part--3 sorting the array using sorted() method 
    unique_array = sorted(unique_array)
    return  type(unique_array),unique_array

    
    
    
if __name__ == "__main__":
    
    words = input("Enter the words with a space! : ").split()
    print(conversion(words))
    arr = input("entre the number : ")
    arr = list(map(int,arr.split()))
    arr = array.array('i',arr)
    print(process_array(arr))
