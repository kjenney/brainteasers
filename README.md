# Calculate a Brain Teaser

A Python script to calculate Brain Teasers

Limited to 5 clues

Example:

```
682 1 digit is right and in it's place
614 1 digit is right in the wrong place
206 two digits are right both in the wrong place
738 all digits are wrong
380 1 digit is right in wrong place
```

How to run it with the Script:

Each clue is processed as a list. The elements are:
  - the number defined in the clue
  - how many digits to compare
  - whether the digits are valid or invalid
  - whether the placement is correct, incorrect, or none

```
python tease.py \
    -c 681 1 valid correct \
    -c 614 1 valid incorrect \
    -c 206 2 valid incorrect \
    -c 738 3 invalid none \
    -c 380 1 valid incorrect
```

## Order of Operations

1. Put clues into a list of lists
2. Process each clue and return a set
3. Compare the first set with the rest to get the answer
