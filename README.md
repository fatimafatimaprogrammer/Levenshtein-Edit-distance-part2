# Levenshtein-Edit-distance-part2
modify the above written program in such a way that it takes two text files containing
single- line and lowercase English sentences named as reference.txt and hypothesis.txt,
and outputs the file result.txt containing Levenshtein distance of these two files as below.
The distance should be word level and not character level.

**********reference.txt***************
this is some text and we would like to see if it has been identified correctly by speech recognition 
system
***************************************
**********hypothesis.txt*************
this is a text and we would like to check what has been identified by the speech recognition
***************************************
*********result.txt******************* 
Levenshtein distance is 7
Insertions 1
Deletions 3
Substitutions 3
***************************************
Hint:-
In this case we can treat words as characters in previous case, right?
