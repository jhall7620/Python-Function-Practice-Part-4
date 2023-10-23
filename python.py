def max_num(a, b, c):
    max = a
    if(max < b):
        max = b
    if(max < c):
        max = c
    return max

def mult_list(list):
    product = 1
    for num in list:
        product *= num
    return product

mylist = [1,2,3,4]

def factorial(num):
    if(num == 0):
        return 1
    elif(num < 0):
        return "error"
    else:
        return num*factorial(num - 1)



def pascal(length):
    def display(list):
        string = ""
        for item in list:
            string += str(item) + " "
        return string
    print(1)

    for x in range(length):
        list = []
        row = x + 1
        for i in range(row):
            list.append(int(factorial(row)/(factorial(i)*factorial(row-i))))
            
        list.append(1)
        print(display(list))

            

                
pascal(4)
        
        
        