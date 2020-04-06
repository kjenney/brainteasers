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

Each clue is processed as a comma-separated-value string. The elements are:
  - the number defined in the clue
  - how many digits to compare
  - whether the digits are valid or invalid
  - whether the placement is correct, incorrect, or none

```
python tease.py \
    --first 681,1,valid,correct \
    --second 614,1,valid,incorrect \
    --third 206,2,valid,incorrect \
    --fourth 738,3,invalid,none \
    --fifth 380,1,valid,incorrect
```
