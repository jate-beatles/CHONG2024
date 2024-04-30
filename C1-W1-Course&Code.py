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
#####################            O      <=     ###########################
#####################            Ω      >=     ###########################
#####################            Θ       =     ###########################
#   
#####################     ∃  Tere is exist K   ###########################   
#####################           ∀  For all     ###########################
#
# The big O, Omega, Theta mean the caveat less 
# 
#
 