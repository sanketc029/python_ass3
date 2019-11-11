#second file
#here check the prime no and add it
def chkprime(arr):
    sum=0
    for num in range(len(arr)):
        # prime numbers are greater than 1
        #print(arr[num])
        if arr[num] > 1:
            for i in range(2, arr[num]):
                if (arr[num] % i) == 0:
                    break
            else:
                print(arr[num])
                sum = sum + arr[num]

    print("Addition of prime no's ",sum)




