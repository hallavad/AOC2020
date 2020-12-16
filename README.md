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

## Day 11
A bit of a challenge. Not quite happy with my solution today, would have rather solved it with networkx and a graph connecting all seats. Unfortunately pip didn't agree with me so the package didn't want to install itself. I will probably get back to this day and do a solution with a graph later.

## Day 12
Didn't have time to complete it on the day but it was a fun puzzle to solve. A quick brainteaser to then move on to day 13

## Day 13
Part A was easy but part B took a while to figure out. Quite a bit of googleing was involved until i hade (re)understood the chinese remainder theorem and implemented it in my code. The resulting code however is quite efficient which i'm happy with.

## Day 15
Figured out a good algorithm to use for todays puzzle immediately but had made a simple mistake in my data_processing, not turning the last number in to an int. I had written `d[-1]` instead of `int(d[-1])`. This resulted in my last input which was a 13 to not be handled properly. It also took quite a while to find the error since all the examples worked correctly, since i both manually antered them as ints and not strings.

Part B was however very simple since it just needed me to find a later number in the series and my code was efficient enough to do it without any changes.

## Day 16
  A fun puzzle. Had to do a different processing of the initial input than usual which was a nice change of pace. For the algorithm part it wasn't that big of a challenge. Something I have realized during the later puzzles is that it could help me do them faster if i clearly define the datastructures involved and put my algorithm down on paper first. To be clear I haven't done that yet but I have the feeling it will help work out some bugs and structure the code better from the start. Might try it tomorrow.
