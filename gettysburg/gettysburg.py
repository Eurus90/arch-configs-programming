__author__ = 'lorcan'

import string, httplib2


# Variables to hold file URLs
SPEECH_URL = "http://mf2.dit.ie/gettysburg.txt"
STOPWORDS_URL = "http://mf2.dit.ie/stopwords.txt"


def makeWordList(gFile, stopWords):
    """Create a list of words from the file while excluding stop words."""
    speech = [] # list of speech words: initialized to be empty
    for lineString in gFile:
        lineList = lineString.strip(
        string.whitespace).split() # split each line into a list of words and strip whitespace
        for word in lineList:
            word = word.lower() # make words lower case (we consider a word in lowercase and uppercase to be equivalent)
            word = word.strip(string.punctuation) # strip off punctuation
            if (word not in stopWords) and (word not in string.punctuation):
                # if the word is not in the stop word list, add the word to the speech list
                speech.append(word)
    return speech


def countWords(speech):
    """Create a dictionary and count the occurrences of each word.
    If a word already exists in the dictionary, add 1 to its counter
    otherwise set a counter for to to an initial value of 1"""
    counts = {}
    for word in speech:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def main():

    try:
        # The request method gives us http header information and the content as a bytes object.
        h = httplib2.Http(".cache")
        speech_headers, speech = h.request(SPEECH_URL)
        stopwords_headers, stopwords = h.request(STOPWORDS_URL)

        # We don't know what we're getting. The content-type header might give us a clue. In this example
        # I'm just going to assume that we can correctly decode utf-8 (the default). I can do this because I know that
        # the file is just a short 'plain text' speech so I know that there won't be any oddities in there. This
        # is often a bit of a gamble for, as we know, there is no such thing as 'plain text'.
        # Make a list of lines by splitting on the newline character.
        speech = speech.decode().split("\n")

        # Make a tuple of all the stop words while losing the newline character
        stopwords = tuple(stopwords.decode().strip().split(','))

        # Make word list from speech while excluding stop words
        speech = makeWordList(speech, stopwords)

        # Make a set of words from speech which automatically assures that each entry is unique
        unique = set(word for word in speech)

        # Print the results
        print("Speech Length: {}".format(len(speech)))
        print("Unique words: {}".format(len(unique)))
        print("\nWord count")

        words = countWords(speech)

        for word in words:
            print("{}: {}".format(word, words[word]), end=" ")
            print("\n")
            print("Request for {} returned status of {}.".format(SPEECH_URL, speech_headers['status']))
            print("Request for {} returned status of {}.".format(STOPWORDS_URL, stopwords_headers['status']))

    except httplib2.HttpLib2Error as e:
        print(e)


    # Run if stand-alone
if __name__ == '__main__':
    main()