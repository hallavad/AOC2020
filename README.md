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

## Day 5
As with the other puzzles the key is in analyzing the data and parsing it in the right way. By realizing that the input is just a binary number where ones are replaced with B or R and zeroes replaced with F or L the algorithm becomes trivial. in A it's just about finding the highest number parsed. In B you need to find the missing number.

## Day 6
Today was a fun puzzle. Unfortunately i didn't see a good way to process the data for both the parts the way i usually do, the parsing in common is only by spliting up the groups. I could've created sets for all people in there as i do in part B but since the solution part A merges all peoples answers on to one line and then creating the set it seemed unnecessary to parse each one of them into a set and then merging them.

## Day 7
Trickiest yet. Parsing the data in to the needed values weren't that hard. However I read the question a bit fast at first so had to do a new seperate data_processing function when i realized that. The first fucntion came in to good use for part B when i needed to go through the baggage outer to inner instead of inner to outer as in part A. I'm not quite happy with my datastructure probably going to go back to it and see if i can create something different that works for both a and b simultaneously.

## Day 8
Created a couple classes to give a better representation and cleaner code. Overall a fun day, not to complex, but still a fun challenge.

## Day 9
Fun puzle to solve, made use of the solution from day 1 to solve part A, didn't help me in part B however. Not quite happy with the structure of the solution for B. I'm certain i could make it better, if only I hade the time to do it...

## Day 10
Happy about today solution, figuring out an efficient way of counting the number of choices in part b was fun and a bit challenging. Unfortunately I had an error in my initial algoritm for it and had to sit for quite a while trying to find out why I didn't get the right answer.
