from hash_table import HashTable
import re


def hashmap_repeated_word(str):
    """
    finds the first word to occur more than once in a string
    Arguments: string
    Return: string
    """
    ht = HashTable()
    new_str = re.sub('[^A-Za-z ]+', '', str).split(" ")
    for word in new_str:
        word = word.lower()
        if word and ht.contains(word):
            return word
        ht.add(word,word)



# def word_count(str):
#    counts = dict()
# words = str.split()

# for word in words:
#    if word in counts:
#    counts[word] += 1
# else :
#    counts[word] = 1

# counts_x = sorted(counts.items(), key = lambda kv: kv[1])
# #print(counts_x)
# return counts_x[-2]
