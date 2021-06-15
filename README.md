# Binary-Search Algorithm

The Computer will generate a random List of 300 Integers between 1 and 1000. The user is then asked to input a random number.
The algorithm will check whether this number exists in the list or not.

The algorithm works by splitting the List in two halfs. 
If the value in the middle of the List is equals to the searched value, then the work is done. If not, the algorithm
will then compare it to the searched value.

If it is smaller, then the algorithm will take the left range of the list and repeats the process.
If it is bigger, then the algorithm will take the right range of the list and repeats the process.
Until the value is found, or the length of the sublist reaches 0. In the latter case the target is not found.


