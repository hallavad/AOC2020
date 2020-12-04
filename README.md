# Advent Of Code 2020
These are my solutions to AOC2020. I also try to add a comment each day about the solution

## Day 1
Simple solution with dual loops for part a and triple loop for part b. Slightly optimized by starting the next loop one above the previous one since the earlier values has been checked with all possible values already.

The alternate solution of part a makes use of sorting the list and then excluding the values at the end until it finds the correct numbers.

## Day 2
Todays puzzle was mostly about processing the input data. Which was easily done by splitting on key characters. The difference between part a and b was minor and the only difference is that it's sovled with two different but still similar if-statements.

As a little bit more of a challenge i did an alternate solution where i mostly used iterators. While creating it i didn't find an easy way to copy the iterator after data processing so i instead combined them in to single map and reduce and separated them afterwards. This solution should be more efficient since it only goes through the whole puzzle set once for both solutions.

## Day 3
I converted  the input into a list containing True if there were a tree and false if was clear. Then it was just a matter of checking if there was a tree throughout the given slope and summing it up.

Part b was suprisingly easy and didn't add any real complexity to the problem, just a matter of using the algorithm with different parameters and then multiplying those results together.

## Day 4
Hardest puzzle as of yet. Once a again a lot of parsing of the initial input. Once the parsing was done it was just a matter of checking if the correct fields existed in a. In b a bit more tinkering was needed to both make sure that the fields existed and that they had certain values. Overall I'm happy that I managed to do it without a lot of if statements and instead made use of a dictionary containing a function. I might tinker a bit and see if i can get it to use iterator instead of looping through each passport. That would require me to change the structure somewhat and get rid of the assignment to `valid_fields`.
