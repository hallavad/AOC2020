# Advent Of Code 2020
These are my solutions to AOC2020. I also try to add a comment each day with my thoughts about the solution

## Day 1
Simple solution with dual loops for part a and triple loop for part b.
Slightly optimized by starting the next loop one above the previous one since the earlier values has been checked with all possible values already.

The alternate solution of part a makes use of sorting the list and then excluding the values at the end until it finds the correct numbers.

## Day 2
Todays puzzle was mostly about processing the input data. Which was easily done by splitting on key characters. The difference between part a and b was minor and the only difference is that it's sovled with two different but still similar if-statements.

As a little bit more of a challenge i did an alternate solution where i mostly used iterators. While creating it i didn't find an easy way to copy the iterator after data processing so i instead combined them in to single map and reduce and separated them afterwards. This solution should be more efficient since it only goes through the whole puzzle set once for both solutions and to process the data.
