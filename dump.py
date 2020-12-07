"""
We are building a word processor and we would like to implement a "word-wrap" functionality.
Given a list of words followed by a maximum number of characters in a line, return a collection of strings where each string element represents a line that contains as many words as possible, with the words in each line being concatenated with a single '-' (representing a space, but easier to see for testing). The length of each string must not exceed the maximum character length per line.
Your function should take in the maximum characters per line and return a data structure representing all lines in the indicated max length.
Note: built-in functions like Python textwrap module should not be used as solutions to this problem.

Examples:

words1 = [ "The", "day", "began", "as", "still", "as", "the",
          "night", "abruptly", "lighted", "with", "brilliant",
          "flame" ]

wrapLines(words1, 13) ... "wrap words1 to line length 13" =>

  [ "The-day-began",
    "as-still-as",
    "the-night",
    "abruptly",
    "lighted-with",
    "brilliant",
    "flame" ]

wrapLines(words1, 20) ... "wrap words1 to line length 20" =>

  [ "The-day-began-as",
    "still-as-the-night",
    "abruptly-lighted",
    "with-brilliant-flame" ]

words2 = [ "Hello" ]

wrapLines(words2, 5) ... "wrap words2 to line length 5" =>

  [ "Hello" ]

words3 = [ "Hello", "world" ]

wrapLines(words3, 5) ... "wrap words3 to line length 5" =>

  [ "Hello",
  "world" ]

words4 = ["Well", "Hello", "world" ]

wrapLines(words4, 5) ... "wrap words4 to line length 5" =>

  [ "Well",
  "Hello",
  "world" ]

n = number of words OR total characters


"""

def wrap(arr_string, max_number):
    res= []
    line=""
    i=0

    if len(arr_string)==1:
        res.append(arr_string[0])


    while i<len(arr_string):
        word=arr_string[i]
        temp=line
        line+=word+"-"
        print(line,len(line[:-1]))
        if (len(line[:-1]))==13:
            res.append(line[:-1])
            print("adding a line ==13",line[:-1])
            line=""
            i+=1
        elif (len(line[:-1]))<13:
            print(line,len(line[:-1]))
            i+=1
            if i==len(arr_string)-1:
                res.append(line[:-1])
        else:
            line=temp
            res.append(line[:-1])
            print("adding a line",line[:-1])
            line=""
            if i==len(arr_string)-1:
                res.append(word)

    print(res)
    return res



words1 = ["The","day","began","as","still","as","the","night","abruptly","lighted","with","brilliant","flame"]
test_words1_width1 = 13
test_words1_width2 = 20

words2 = ["Hello"]
test_words2_width1 = 5

words3 = ["Hello", "world"]
test_words3_width1 = 5

words4 = ["Well", "Hello", "world"]
test_words4_width1 = 5


wrap(words3, test_words2_width1)
