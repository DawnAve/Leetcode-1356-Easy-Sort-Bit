# Leetcode-1356-Easy-Sort-Bit
A easy problem, but it requires some basic knowledge. Easy logics, but hard code for people like me who are not familiar to bits and things like that.

So there are two python files, the one with only number is my first solution. It works, but crazily slow. The second one is a improved version.
And hrer are my ideas: For the first time, I created another array to keep the number of 1 bits. And I hard coded a bubble sort, and also sort the original array when swaps are made

The second solution used the built-in sort(). It is new to learn that when a tuple is passed in to sort(), it will compare the first, when they are equal, it will keep going to the next one.
Therefore, creating a funciton that returns a tuple with (number of 1 bits, the original number), will compare the bits and then number if necessary. 
A lot to learn...
