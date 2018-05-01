def max_subarray(A):
   maxSoFar = A[0]
   maxEndingHere = A[0]

   for a in A[1:len(A)]:
     maxEndingHere = max(maxEndingHere+a, a)
     maxSoFar = max(maxSoFar, maxEndingHere)

   return maxSoFar

if __name__ == '__main__':

    response = max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(response)
    # print
    # maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    # print
    # maxSubArray([0, 0, 0, 0])
    # print
    # maxSubArray([0, 0, 0, 0])