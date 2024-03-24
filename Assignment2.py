'''
Assignment 2
Prashanth Nallathamby
100784991
'''
# Importing required libraries
from playsound import playsound
import random

# Function to play the swap sound effect
def sound_effect():
    option = random.randint(1,3) # Generate a random number between 1 and 3 to select the type
    if option == 1:
        return playsound('1.mp3')
    elif option == 2:
        return playsound('2.mp3')
    elif  option == 3:
        return playsound('3.mp3')
    else:
        return
    
# Creates the Array based on user Input
def Create_Array():
    arr = []
    n = input("Size of Array: ")
    
    for  i in range(int(n)):
        num = int(input("Enter Number: "))
        arr.append(num)
    
    return  arr

# Split the array into single index recursively
def split_array(given_array):
    if len(given_array) <= 1:
        return given_array
        
    mid  = len(given_array)//2
    leftside =  given_array[:mid]
    rightside = given_array[mid:]
        
    leftside = split_array(leftside)
    rightside = split_array(rightside)
    
    return merge_array(leftside, rightside)
        
# Merge two sorted arrays
def merge_array(left, right):
    merged_array = []
    IndexL,IndexR = 0 , 0
    while IndexL < len(left) and IndexR < len(right):
        if left[IndexL] <= right[IndexR]:
            merged_array.append(left[IndexL])
            IndexL += 1
        else:
            merged_array.append(right[IndexR])
            IndexR += 1
        sound_effect()
    
    merged_array.extend(left[IndexL:len(left)])
    merged_array.extend(right[IndexR:len(right)])
    
    return merged_array

# Main Function
def main():
    given_array = Create_Array()
    print ("Given Array: ",given_array)
    sorted_array = split_array(given_array)
    print("Sorted Array: ",sorted_array)
    
main()