#########################################################################################
#### Aveage Case Complexity  & Recurrance Relations &  Randomization in ALG  
####
#
#### Running Time of Algorithms: 

def process_array(a): 
    n = len(a)
    result = 0.0 
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i] - a[j] ==3:
                return 1
            else: 
                result = result + (a[i]-a[j])
    return result

#### Alg ust randomness 

def geometric(p):
    count = 0
    if flip(p):  ### p is the number between 0-1, return the true with prob. p and false
        return 1 + geometric(p)
    else:
        return 1
####        T(P) = 1(1-P) + (1+T(P)) * P

## W.C. is infinity 

#  why randomness
#       input ----- alg ----- output ### avg randomness the avg is less than w.c. 


#### Why random in data structure 
# 
#### Recurrences 

# def alg ( input_array):
#   if  len(input_array) <= m: 
#       alg(new_arrray_1) 
#       .....
#       alg(new_array_2) 

#>>>>> T(n) = aT(n/b) + theta( n)   # if n>m 

##############################################################################################
#### Quick Sort 
#
#      quick sort ---- divide & connque sort 
#   
#   seperate into 2 group, [1-m]  & [m+1 - n]

#### Partition ---- divide ---- choose the pivot - any thing smaller than the pivot is go left, which 
#                                                   larger than the pivot go right, not sort yet
#
#>>> Pseudo Code for Quick Sort 
#      
#   def quicksort(A)




