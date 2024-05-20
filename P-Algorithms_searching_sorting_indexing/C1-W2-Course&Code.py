
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
#### Bubble down
# 
#   the parent element is greater than the child
#   [special situation] - the root is broken
#           [Rule]      >>> the ele will swap with small child  [???????????why??????????]
#   
#### Pseudo code 
#    bubbleDown (A, j):                     # n is the length of A
#       if (left(i) > n) :               # A has no left child
#           return
#       if (left(i) and right(i) > n):        
#           if (A[i] > A[left(i)]):
#               swap(A[i], A[left(i)])
#               bubbleDown(A, left(i))

#       else                                # A has 2 child
#            if (A[left(i) < A[right(i)] ) 
#               small := left(i)
#            else: 
#               small := right(i)
#            swap (A[i], A[small])
#            bubbleDown (A, small) 
#######
##the number of the step for the worst case : theta log2(n)


################################################################################################
#### Priority Queues & Inset, heapfiy and Heapsort
#
#### Insert -----
#       insert a new ele,  in .py   --- a.append(e)
#       after inset the new e, maybe not the heap, 
#
# Pseudo Code 
#               1. Append the e to the end of heap
#               2. BubbleUp
#              overall complexity is log2(n) + 1     # 1 is the insert to end step
#
#### Deletion ----
#       cannot delete in the mid of heap, delete at he end is simple
#       1. replase with aj with an, end ele replate the delete ele
#       2. Adjust the size with n-1
#       3. Fix what broken: 
#           BubbleUp if a(n) is less than its parent,
#           BubbleDown if a(n) is greater than its children
#       
#       Complexity of deletion: 
#           1. swap        theta 1
#           2. Adjsut 
#           3. Bubble up   log2(n)

#### Find the smallest of ele in Heap 
#
#### Application  Queue called priority queue --- used in many place

#
#### Priority Queque - Data Structure 
#       FIFO  queue  -- First in First out -- Queque
#       
#### Array turn into Heap 
#       BubbleDown each ele 
#       for i = n/2 dow to 1
#           bubbleDown( A,i) 
#       #A is a Heap ----- mineap   ---------Heapify 
#       Complexity of Heapify is n
#
#
#########################################################################################
#### Hash Table 

#       Hash Funciton --- The unique key for reach 
# Opereation: 
#   1. find the key in the hastable
#   2. insert 
#   3. Delete key 

#### Insertion hash table
#    If teh hash collision [same key ]
#       how do to handle the collision 
#    >>>>1. Chaining ----- each slot associate with key list

#    >>>>> Costs of the insert  ---- Hash function that alwasy give the same key
#          aveage of the list size  ---- = n/m
#
##############################################################################################################################################################
##############################################################################################################################################################
class MinHeap:
    def __init__(self):
        self.H = [None]
 
    def size(self):
        return len(self.H)-1
    
    def __repr__(self):
        return str(self.H[1:])
        
    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] >= self.H[i//2],  f'Min heap property fails at position {i//2}, parent elt: {self.H[i//2]}, child elt: {self.H[i]}'
    
    def min_element(self):
        return self.H[1]

    ## bubble_up function at index
    ## WARNING: this function has been cut and paste for the next problem as well 
    def bubble_up(self, index):
        assert index >= 1
        if index == 1: 
            return 
        parent_index = index // 2
        if self.H[parent_index] < self.H[index]:
            return 
        else:
            self.H[parent_index], self.H[index] = self.H[index], self.H[parent_index]
            self.bubble_up(parent_index)
    
    ## bubble_down function at index
    ## WARNING: this function has been cut and paste for the next problem as well 
    def bubble_down(self, index):
        assert index >= 1 and index < len(self.H)
        lchild_index = 2 * index
        rchild_index = 2 * index + 1
        # set up the value of left child to the element at that index if valid, or else make it +Infinity
        lchild_value = self.H[lchild_index] if lchild_index < len(self.H) else float('inf')
        # set up the value of right child to the element at that index if valid, or else make it +Infinity
        rchild_value = self.H[rchild_index] if rchild_index < len(self.H) else float('inf')
        # If the value at the index is lessthan or equal to the minimum of two children, then nothing else to do
        if self.H[index] <= min(lchild_value, rchild_value):
            return 
        # Otherwise, find the index and value of the smaller of the two children.
        # A useful python trick is to compare 
        min_child_value, min_child_index = min ((lchild_value, lchild_index), (rchild_value, rchild_index))
        # Swap the current index with the least of its two children
        self.H[index], self.H[min_child_index] = self.H[min_child_index], self.H[index]
        # Bubble down on the minimum child index
        self.bubble_down(min_child_index)
        
        
    # Function: heap_insert
    # Insert elt into heap
    # Use bubble_up/bubble_down function
    def insert(self, elt):
        # your code here
        self.H.append(elt)
        self.bubble_up(len(self.H)-1)
        
    # Function: heap_delete_min
    # delete the smallest element in the heap. Use bubble_up/bubble_down
    def delete_min(self):
        # your code here
        if len(self.H) == 1: 
            return none
        min_elt = self.H[1]
        last_elt = self.H.pop()
        
        if len(self.H) > 1: 
            self.H[1] = last_elt
            self.bubble_down(1)
        return min_elt

    def extract_min(self):
        if self.size() == 0:
            return None
        min_val = self.H.A[0]
        last_val = self.H.A.pop()
        if self.size() > 0:
            self.H.A[0] = last_val
            self.H.bubble_down(0)
        return min_val
h = MinHeap()
h = h.insert(5)
print(f'\t Heap = {h}')
assert(h.min_element() == 5)
h.insert(2)
print(f'\t Heap = {h}')
assert(h.min_element() == 2)
h.insert(4)
print(f'\t Heap = {h}')
assert(h.min_element() == 2)
h.insert(-1)
print(f'\t Heap = {h}')
assert(h.min_element() == -1)
h.insert(7)
print(f'\t Heap = {h}')
























#
# %%
