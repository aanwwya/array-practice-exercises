#1. find sum of all elements in an array 
# given an array of numbers, find the sum of all elements

# pseudocode
# initialize sum = 0
# for each number in the array:
# add the number to sum
# return the sum 

def array_sum(nums):
    s = 0 
    for n in nums:
        s+=n
    return s
print(array_sum([1,2,3,4]))  

# output= 10

#2. count how many numbers in the arr are even 
# given an array of integers, count how many numbers are even

#pseudocode
# initialize count = 0
# for each number in the array:
# if the number is even 
# increase count by 1
# return the count 

def count_even(nums):
    c = 0
    for n in nums:
        if n % 2 == 0:
            c+=1
    return c
print(count_even([1,2,3,4])) 

#output: 2

#3. find the largest element in the array
# given an array of numbers, find the largest element

#pseudocode
# set max_value = first element of the array
# for each number in the array:
# if the number is greater than max_value:
# update max_value to this number
# return max_value

def find_max(nums):
    max = nums[0]
    for n in nums:
        if n>max:
            max = n
    return max
print(find_max([10,5,30,2]))  

#output: 30

#4. count numbers greater than a given value X
# given an array and a value X, 
# count how many elements in the array are greater than X

#pseudocode 
# initialize counter = 0
# for each number in the array
# if the number is greater than X
# increase counter by 1
# return the counter

def num_greater_than_X(arr, X):
    counter = 0
    for a in arr:
        if a > X:
            counter += 1
    return counter
print(num_greater_than_X([4,1,7,3,9,6], 5))  

#ouput: 3

#5. count numbers smaller than a given val X
# given an array and a number X, 
# count how many elements in the array are less than X

#pseudocode:
# initialize counter = 0
# for each element in the array
# if the element is less than X
# increase counter by 1
# return the counter 

def count_smaller_than_X(arr, X):
    counter = 0
    for a in arr:
        if a < X:
            counter += 1
    return counter
print(count_smaller_than_X([4,1,7,9,6], 5))

# output: 2

#6. count how many times a given number appears in the array
# given an array and a target number X, 
# count how many times X appears in the array

#pseudocode:
# initialize counter = 0
# for each element in the array
# if the element equals X
# increase counter by 1
# return the counter

def count_appears(arr, X):
    counter = 0
    for a in arr:
        if a == X:
            counter += 1
    return counter
print(count_appears([2,4,2,6,2], 2))  

#output:3 

#7.find the average of all numbers in the array
#given an array of numbers, 
# calculate the average (mean) of the elements 

#pseudocode: 
# initialize total = 0
# for each number in the array:
# add the number to total
# after the loop, compute average = total / number of elements
# return the average

def avg(arr):
    total = 0
    for a in arr:
        total += a
    average = total / len(arr)
    return average
print(avg([2,4,6,8]))  

# output: 5.0

#8. find the smallest number in the array 
#given an array of numbers, find the smallest element

#pseudocode:
# assume the first element is the smallest => min_num = arr[0]
# for each element in the array
# if the element is smaller than min_num
# update min_num to that element
# after checking all elements, return min_num

def smallest_num(arr):
    min_num = arr[0]
    for a in arr:
        if a < min_num:
            min_num = a
    return min_num
print(smallest_num([4,1,7,3,9]))  

#output: 1

#9. count numbers divisible by 3
#given an array of integers , count how many numbers are divisible by 3

#pseudocode:
# start counter = 0
# for each number in the array:
# check if the number is divisible by 3
# if yes, increase counter by 1
# after checking all elements, return counter

def num_divisible_by_3(arr):
    counter = 0
    for a in arr:
        if a % 3 == 0:
            counter += 1
    return counter
print(num_divisible_by_3([3,4,6,7,9]))  

#output: 3


#10. sum of all even numbers in the array
# given an array of integers, 
# calculate the sum of all even numbers

#start sum_even = 0
# look at each number in the array
# check if the number is even 
# if yes, add the number to sum_even
# after going through the entire array, return sum_even

def sum_even_nums(arr):
    sum_even = 0
    for a in arr:
        if a % 2 == 0:
            sum_even += a
    return sum_even
print(sum_even_nums([2,3,4,5,6]))  

#ouput: 12 

#11. find the second largest number in the array
# given an array of numbers, find the second largest element

#pseudocode: 
# assume:
# largest = first element
# second_largest = second element
#
# for each number in the array:
#  if number > largest:
#  update second_largest = largest
#  update largest = number
#
#  else if number is smaller than largest
#  but bigger than second_largest:
#  update second_largest = number
#
# after checking all numbers, return second_largest

def sec_largest(arr):
    largest = arr[0]
    second = arr[1]

    for a in arr:
        if a > largest:
            second = largest
            largest = a
        elif a > second and a != largest:
            second = a
    return second
print(sec_largest([4,7,2,9,5]))  

#output: 7 

#12. count numbers divisible by 5
# given an array, count how  many numbers are divisvble by 5 

#pseudocode:
# start counter = 0
# loop through each number in the array
# check if number % 5 == 0
# if yes, increase counter by 1
# affter checking all numbers, return counter 

def d_by_5(arr):
    counter = 0
    for a in arr:
        if a % 5 == 0:
            counter += 1
    return counter

print(d_by_5([5,10,12,15,7]))  

#output: 3






























