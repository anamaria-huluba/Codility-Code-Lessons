# A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

# Count the minimal number of jumps that the small frog must perform to reach its target.

# Write a function:

# def solution(X, Y, D)

# that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

# For example, given:

#   X = 10
#   Y = 85
#   D = 30
# the function should return 3, because the frog will be positioned as follows:

# after the first jump, at position 10 + 30 = 40
# after the second jump, at position 10 + 30 + 30 = 70
# after the third jump, at position 10 + 30 + 30 + 30 = 100
# Write an efficient algorithm for the following assumptions:

# X, Y and D are integers within the range [1..1,000,000,000];
# X ≤ Y.

# solution 1
def solution(X,Y,D):
    float_d = (Y-X)/D
    int_d = (Y-X)//D
    if float_d- int_d == 0: 
        return int_d
    else: 
        return int_d + 1

# solution 2
def solution(X, Y, D):
    v = (Y - X) // D
    if X + (v * D) >= Y:
        return v
    else:
        return v + 1

# an edge case where if from position X the frog makes V jumps of distance D each (so X+v*D) ... and still didn't reach the other side hence X+v*D<Y, so we must add one more step therefore we return v+1

# solution 3
import math 

def solution(X, Y, D):
    k = math.ceil((Y-X)/D)
    return k