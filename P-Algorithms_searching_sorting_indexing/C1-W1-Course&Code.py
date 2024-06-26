#####  Insertion sort algorithm 
# what is the sort meaning, give you bounch of number
################################################################################################
#### Insert sort
#       1.The elment from the input
#       2.The output must in order
#
#       Insertion sort for the small array

# Pseudo CODE for insert
#  insert (A, j) 
#  for i = j -1 down to i: 
#       if A[i] > A [i+1]: 
#           swap (A[i], A[i+1])
#       else:
#           break
#### insertion sor(A)
# for j = 1 up to n: 
#     insert (A, i)
###########################################################
#### Computation complexity of the insertion sort
# how much does it cost~!!
#   1.how much time and space(memory) to running this code
#   2. best case and worst case --best case complexity & worst complexity & aveage case 
#     >>>The Best case is when the order is already desend order
#         cost = c3(for loop) + C1 (time check the element) + C4 (break) 
#     >>>The Worst CASE:
#        (j-1)(c1 + c2[swap) + c3)   
################################################################    
# Time and Space complexity 
#       >>>> number of the operation  ----#### 1. compare the worst case & 2. avg case
#
#       x-axis as the n; y-axis
#

##########################################################################
#####################            O      <=     ########################### Asymptotic Upper Bounded
#####################            Ω      >=     ########################### Asymptotic Lower Bounded
#####################            Θ       =     ########################### Asymptotic Equal
#   
#####################     ∃  Tere is exist K   ###########################   
#####################           ∀  For all     ###########################
#
# The big O, Omega, Theta mean the caveat less ----------CAVEAT
# f = theta (g)    =====  f = O(g)  & g = O(f)
  
#
###############################################################################
#### Binary Search
#
# find the element in the list, assumen the list areading in ascending order, and return the index of the element at the index
# >>>>1. Initial the beginning of left and right, then find the mid of the list
# >>>>2. judge the element searching for is left regim or right region. 
#
########################################################################
def BinarySerchHelper ( lst, elt, left, right): 
        # 0 <= left <= right < size(lst)
        # Invariant
    if (left > right): 
        return None
    else: 
        mid = (left + right) // 2
        if lst[mid] == elt:
            return lst[mid]
        elif lst[mid] < elt:
            mid != 1
            return BinarySerchHelper(lst,elt, mid,right)
        else:
            if lst[mid] > elt: 
                mid != -1
                return BinarySerchHelper(lst, elt, mid,right)

##################################################################################
#   improve the binary search region ---- Induction 
#   >>>>> Time of bianry search ---- log2(n)  n is the list of the length
#   
#####################################################################################
#### Merge Sort Algorithm
#
####    MergeSort Pseudocode
#  def mergersort ( array, left, right) 
#   if (left >= right): 
#       return
#   if (left + 1 == right):
#       if lst[left] > lst[right]:
#           swap(lst, left, right)
#        return
#
#### Merge Procedure Correctness Argument 
#### Running of the Merge Sort 
#       >> every element get into the tmp, then comparison for each element filling, i compare with j
#### Cost of each level is n of the array size, n * # level of array, is the ########  n * log2(n)

#  https://colab.research.google.com/drive/1wjnh0bRUZtH7OVi3Hmbm56BkDq-q-We5?usp=sharing         
#
#### pitfall and logarithms 
#
# the constant of the exponent cannot get rid of
# in asympotic function,  the n of the constant cannot ge get rid off it
#
#   2^ n  is O 3^n; since 3^n = 2^(log2(3)n)
#
#### Asymptomatic Notation
#


        




