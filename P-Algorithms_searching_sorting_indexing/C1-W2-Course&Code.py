
#########################################################################################################
#########################################################################################################
# Data Strucuture: The Dynamic Array 
#
#   > insert data
#   > Delete data
#   > Modify data
#

#### Dynamic Arrays
# append the element to the end, space to grow at the end, the W.C. should as theta n of the n list
#
#### Dictionary Data Structure 
#### Hash table - quickly to lookup a value of certain key
#
##################################################################################################
#### Heaps, Min / Max - Heaps 
#   Abstract Data Type ---  adt
#   Min Heap  & Max Heap 

#   A: [ 3, 4, 5, 7, 6, 18, 14, 9] 
#>>>>>>>>>for the element i, the left child is 2i & 2i + 1 is the right child
#>>>>>>>>>for i is the parent of 2i & (2i +1)
#   A[i] has no parent which is the root 
#   Heap is a special binary tree laid out on array
#
#### Min heap property - 
#      > Every A[i] <= A[2i] is left child
#      >       A[i] <= A[2i+1] is right child
#      > 
#     1.> Every parent is less than & equal to its children 
#### Max Heap ---- the parent node > child
#    Depth of the heap

#### Heap operation
#>>>>       inset ele into the heap
#>>>>       deleting ele from the heap

#### Heap Primitive: Bubble up & Bubble down
     
###########################################################################################
#### Pseudo Code for bubble up
#     bubble up (A,j)
#       if j <= 1: 
#           RETURN
#       else: 
#         if A[j] < A[j//2]: 
#           swap(A[j], A[j//2])
#           bubbleup(A, j//2)
#       return
####   the number of the bubble up is hte depth of the heap
#   depth = log2(n)

##########################################################################################
#### bubble down
#
#
#
#