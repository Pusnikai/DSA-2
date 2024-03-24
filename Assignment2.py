'''
Assignment 2
Prashanth Nallathamby
100784991
'''
from playsound import playsound

def Create_Array():
    arr = []
    n = input("Size of Array: ")
    
    for  i in range(int(n)):
        num = int(input("Enter Number: "))
        arr.append(num)
    
    return  arr

def merge_sort(given_array):
    if len(given_array) >= 1:
        print(given_array)
        mid  = len(given_array)//2
        leftside =  given_array[:mid]
        rightside = given_array[mid:]
        
        merge_sort(leftside)
        merge_sort(rightside)    
        
        
        
        
def main():
    given_array = Create_Array()
    merge_sort(given_array)
    
main()