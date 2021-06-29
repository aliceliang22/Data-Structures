#  File: Reducible.py
#  Description: HW 11
#  Student Name: Alice Liang
#  Student UT EID: axl84
#  Course Name: CS 313E
#  Unique Number: 84825
#  Date Created: 07/19/20
#  Date Last Modified: 07/20/20

# takes as input a positive integer n returns True if n is prime and False otherwise
def is_prime ( n ):

    if (n == 1):
        return False

    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

def get_max_prime(n):

    prime = 2 * n + 1
    while is_prime(prime) == False:
        prime += 1

    return prime

N = 0

# takes as input a string in lower case and the size of the hash table and returns the index the string will hash into
def hash_word (s, size):

    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# takes as input a string in lower case and the constant for double hashing and returns the step size for that string
def step_size (s, const):

    key = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        key = (key * 26 + letter)

    stepSize = const - (key % const )
    return stepSize

# takes as input a string and a hash table and enters the string in the hash table, it resolves collisions by double hashing
def insert_word (s, hash_table):

    lenWord = len(hash_table)
    hashIndex = hash_word(s, lenWord)
    w = hash_table[hashIndex]

    if len(w) == 0:
        hash_table[hashIndex] = s            
        return
        
    if w == s:
        return

    stepSize = step_size(s, N)

    while len(w) > 0:
        hashIndex += stepSize
        hashIndex = hashIndex % lenWord
        w = hash_table[hashIndex]

        if w == s:
            return

    hash_table[hashIndex] = s            

# takes as input a string and a hash table and returns True if the string is in the hash table and False otherwise
def find_word (s, hash_table):

    lenWord = len(hash_table)
    hashIndex = hash_word(s, lenWord)
    w = hash_table[hashIndex]

    if len(w) == 0:
        return False

    stepSize = step_size(s, N)

    while w != s:
        if len(w) == 0:
            return False

        hashIndex += stepSize
        hashIndex = hashIndex % lenWord
        w = hash_table[hashIndex]
 
    return True

# recursively finds if a word is reducible, if the word is reducible it enters it into the hash memo and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):

    length = len(s)
    if length == 0:
        return False

    if find_word(s, hash_memo):
        return True

    for i in range(length):
        word = s[:i] + s[i+1:]
        if find_word(word, hash_table) == True:
            insert_word(s, hash_memo)
            return True

        else:
            reduc = is_reducible(word, hash_table, hash_memo)

            if reduc == True: 
                insert_word(s, hash_memo)
                return True

    return False

# goes through a list of words and returns a list of words that have the maximum length
def get_longest_words (string_list):

    max = 0
    maxWords = []
    for i in range(len(string_list)):
        word = string_list[i]
        curr = len(word)

        if curr == max:
            maxWords.append(word)

        elif curr < max:
            continue

        elif curr > max:
            for j in range(len(maxWords)):
                maxWords.pop(0)
            maxWords.append(word)
            max = curr
    return maxWords

def main():

    # create an empty word_list
    word_list = []
    # open the file words.txt
    infile = open("words.txt", "r")

    # read words from words.txt and append to word_list
    line = infile.readline().strip()
    while line != "":
        word_list.append(line)
        line = infile.readline().strip()

    # close file words.txt
    infile.close()

    # find length of word_list
    lenWord = len(word_list)
    len2 = lenWord + lenWord

    # determine prime number N that is greater than twice the length of the word_list
    global N 
    N = get_max_prime(len2)
    
    # create an empty hash_list
    hash_list = []

    # populate the hash_list with N blank strings
    empty = ""
    for i in range(len2):
        hash_list.append(empty)

    # hash each word in word_list into hash_list
    # for collisions use double hashing 
    for i in range(lenWord):
        word = word_list[i]
        insert_word(word, hash_list)

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than 
    # 0.2 * size of word_list
    M = int(0.2 * lenWord) + 1
    while is_prime(M) == False:
        M += 1

    # populate the hash_memo with M blank strings
    hash_memo = []
    for i in range(len2):
        hash_memo.append(empty)

    # create an empty list reducible_words
    reducible_words = []

    # for each word in the word_list recursively determine if it is reducible, if it is, add it to reducible_words
    for i in range(len2):
        word = hash_list[i]

        if len(word) == 0:
            continue

        isFound = False
        for j in range(len(word)):
            if word[j] == "a" or word[j] == "i" or word[j] == "o":
                isFound = True
                break

        if isFound == True:
            insert_word(word, hash_memo)
            reducible_words.append(word)
            continue

        reduce = is_reducible(word, hash_list, hash_memo)

        if reduce == True:
            reducible_words.append(word)

    # find words of the maximum length in reducible_words
    maxReducWords = get_longest_words(reducible_words)

    # print the words of maximum length in alphabetical order
    # one word per line
    sort = sorted(maxReducWords)
    for i in range(len(sort)):
        print(sort[i])

# This line above main is for grading purposes. It will not 
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()