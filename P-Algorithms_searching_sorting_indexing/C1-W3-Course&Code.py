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
#   def quicksort(A， left, right)
#       1. x:= A[right]   # chose pivot 
#       2. p:= patition position (A, right)
#       3. quick sort( A, left, p-1)  #sort every thing from left to p-1)
#       4. quick sort(A, p+1, right)   # sort every thing from p+1 to right
#
#       >>>> BaseCase: right - left <= small number  ###
#             2 ele array just swap 
#
#####################################################################################################
####  Partitioning Scheme 
#   choose the pivot ele, do the re-arange the things #########in Place##########
## Lomuto Partition 
#   intermediate steps >>>>> Lomuto partition >>>  the array divide into 3 parts 
#   region1: [A[1], ...A[i]]   region2: [A[i+1], ......A[j-1]],   region3: A[j] .....A[j-1] %%%% A[n] is is the pivot
#
#   Begin: the netire region is unprocess, j = 1, i = 0, region 1 & region 2 is empty; 
#   For loop happen:   [A[1]....A[i] A[i+1] ..... A[j-1]A[j] ...... A[n]]  
#            Gurante:   everthing in region will < x, and the region 2 is > x;  x is the pivot
#               
#    while ( j <= n-1):  
#                      if A[j] < x: 
#                       then swap(A, i+1, j) 
#                           i = i+1
#                           j = j+1
#                       else:
#                           j = j+1
#                     swap (A, i+1, n) 
#                   return i+1

#       
#### Running time of the Lomuto Partition ====== 
#      running time = the size of the array 
#

### Get back now! 



