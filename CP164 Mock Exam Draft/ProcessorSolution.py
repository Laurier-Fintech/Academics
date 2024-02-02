r"""
-------------------------------------------------------
THE BIG BOOK CLASS
-------------------------------------------------------
Author: Jason Van Humbeck
ID:
Email:
__updated__ = ""
-------------------------------------------------------

Name:           The Big Book Problem
Created By:     Jason Van Humbeck
Package:        Laurier FinTech CP164 Mock Exam - Part 2
                BigBook.py

Task Description:
    The Big Book is a unique data storing system for basic set of words in the English dictionary.
    Using a base 90 number system, it can store up to 8100 words, which can all be referenced
    using two characters. This method is helpful for saving storage and hiding your text
    from those who don't have access to your dictionary. You can read or write from a file or string
    and must follow the proper string format:

        Format: All punctuation must be preceded by a '/' followed by the character.
                New lines are indicated as '/n' (not '\n').
                You can combine any combination together where instructions will be read in order. Ex: '/.n'

            Example: "My Name is Jason/.n
                      Hi/, Hello/!"

            Encoded: "al j7 -= 10/.n l)\, l*"

    It is your job to finish coding the remaining methods so the program can run, and so you can decrypt
    the secret message. Have Fun!

Requirements:
    - Avoid using built-in functions such as .remove, .pop, .index, .insert, etc.
    - Limit each function to a single return statement.
    - Prohibit the use of loop breaks.
    - No illegal aids.
"""
from copy import deepcopy
class BigBook:
    CODE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+={[}]|;:<,>.?~`"
    MAX_WORDS = 7199

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an instance of the BigBook class.
        Initializes an empty list to store words.
        Use: book = BigBook()
        -------------------------------------------------------
        Returns:
            Big Book Object
        """
        self.words = []

    def _linear_search_(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the dictionary.
        Private helper method.
        Use: index = self._linear_search(key)

        Answer: While the key is not found, and the index is not out of bounds
        check to see if the key matches the list at current index. If found,
        stop search and return index; if not, return -1
        -------------------------------------------------------
        Parameters:
            key - a partial data element (str)
        Returns:
            index - the index of key in the dictionary, -1 if key is not found (int)
        -------------------------------------------------------
        """
        found = False
        index = 0

        while not found and len(self.words) > index:
            if key == self.words[index]:
                found = True
            else:
                index += 1

        if not found:
            index = -1

        return index

    def append(self, word):
        """
        -------------------------------------------------------
        Inserts a word to the front of the dictionary (self.words).
        Ensures there are no duplicates and the dictionary length
        does not exceed self.MAX_WORDS.
        Use: self.append(word)

        Answer: Using Linear Search ensure that there are no duplicates
        and use the consant MAX_WORDS to check that the list is not filled.
        If conditions are met, use the built-in append function.
        -------------------------------------------------------
        Parameters:
            word - a string-based word
        Returns:
            None
        -------------------------------------------------------
        """
        if self._linear_search_(word) == -1 and len(self.words) < self.MAX_WORDS:
            self.words.append(word)

    def prepend(self, word):
        """
        -------------------------------------------------------
        Inserts a word to the back of the dictionary (self.words).
        Ensures there are no duplicates and the dictionary length
        does not exceed self.MAX_WORDS.
        Use: self.prepend(word)

        Answer: Check same conditions as self.append, if they are
        met, overwrite the current array with an array of word
        combined with the previous list.

            NOTE: This is the equivlant to a = [1,2,3] b = [3];
            c = b + a; c = [3,1,2,3]
        -------------------------------------------------------
        Parameters:
            word - a string-based word
        Returns:
            None
        -------------------------------------------------------
        """
        if self._linear_search_(word) == -1 and len(self.words) < self.MAX_WORDS:
            self.words = [word] + self.words

    def insert(self, i, word):
        """
        -------------------------------------------------------
        Inserts a word in the dictionary (self.words) at position i.
        Ensures there are no duplicates and the dictionary length
        does not exceed self.MAX_WORDS. All positions for i are valid -
        Negative numbers to 0, and Higher Numbers to len - 1
        Use: self.insert(i, word)

        Answer: Check same conditions as self.append, if they are
        met, determine where the operation falls. If the number is
        less than or equal to 0 -> use built-in prepend function. If
        number is greater to or equal to len(list) use built-in append
        function. If it is neither - iterate through the list, and
        insert at i. This is done by creating a new list that linearly
        re-adds each item on the list until i. Here it will add the word
        now giving it the desired location, and then adding the remaining
        words aswell. The list is then overwritten by the newly created list.

            NOTE: This is the equivilant to A = [1,2,4,5] -> (split)
            B = [1,2] C = [3,4]; D = [1,2] + [3] + [4,5]; A = D
        -------------------------------------------------------
        Parameters:
            i - the position to insert the word (int)
            word - a string-based word
        Returns:
            None
        -------------------------------------------------------
        """
        if self._linear_search_(word) == -1 and len(self.words) < self.MAX_WORDS:
            if i <= 0:
                self.prepend(word)
            elif i >= len(self.words):
                self.append(word)
            else:
                store = []
                for x in range(len(self.words)):
                    if x == i:
                        store.append(deepcopy(word))
                    store.append(deepcopy(self.words[x]))
                self.words = store

    def remove(self, word):
        """
        -------------------------------------------------------
        Removes a given word, matching 'word', and returns it.
        Returns 'None' if not found.
        Use: removed_word = self.remove(word)

        Answer: Uses Linear Search to find if there is an instance
        of the word in List (-1 if no). If it finds a match, it will
        first take a deepcopy to return, and then use 'del' to delete
        -------------------------------------------------------
        Parameters:
            word - a string-based word
        Returns:
            removed_word - the removed word
        -------------------------------------------------------
        """
        removed_word = None
        index = self._linear_search_(word)

        if index != -1:
            removed_word = deepcopy(self.words[index])
            del self.words[index]

        return removed_word

    def union(self, newBook):
        """
        -------------------------------------------------------
        Merges self and the imported BigBook into the current dictionary.
        Ensures there are no duplicates and the dictionary length does not
        exceed self.MAX_WORDS.
        Use: self.union(newBook)

        Answer: For each word in NewBook's List, appends. If code was built
        correctly, the append funcution should auto-check for duplicates
        and space.
        -------------------------------------------------------
        Parameters:
            newBook - a BigBook object
        Returns:
            None
        -------------------------------------------------------
        """
        for word in newBook.words:
            self.append(word)


    def dict_rotate(self, n):
        """
        -------------------------------------------------------
        Rotates the position of words in the dictionary,
        moving content from the front to the rear n times.
        Use: self.dict_rotate(n)

        Answer: Takes a copy of words, and then rewrites the new list
        based upon the position of the (old words + n)%len. Due to the
        modulus, there is no other math needed.

            NOTE: See A = [1,2,3] -> POS 0 @ ROATATE(100) ->
            A[(0 + 100)%3] = 1 -> = [1] -> 2
        -------------------------------------------------------
        Parameters:
            n - the number of times to rotate words (int)
        Returns:
            None
        -------------------------------------------------------
        Examples:
            source: [0, 1, 2, 3, 4], dict_rotate(source, 3), source: [3, 4, 0, 1, 2]
            source: [0, 1, 2, 3, 4], dict_rotate(source, -1), source: [4, 0, 1, 2, 3]
        -------------------------------------------------------
        """
        cheat = deepcopy(self.words)
        self.words = []
        for i in range(len(cheat)):
            self.words.append(deepcopy(cheat[(i + n) % len(cheat)]))

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================
    def write_fnTch(self, number):
        """
        -------------------------------------------------------
        Takes a decimal number and converts it to the base-90 system "fnTch."
        Use: fnTch = self.write_fnTch(number)
        -------------------------------------------------------
        Parameters:
            number - the base-10 number (int)
        Returns:
            fnTch - the base-90 number (str)
        -------------------------------------------------------
        Examples:
            8099 -> ``
            2333 -> p<
        -------------------------------------------------------
        """
        fnTch = ""
        grab = number

        if grab == 0:
            fnTch = BigBook.CODE[0]
        else:
            while grab > 0:
                fnTch = BigBook.CODE[grab % 90] + fnTch
                grab = int((grab - (grab % 90)) / 90)

        if len(fnTch) == 1:
            fnTch = '0' + fnTch

        return fnTch

    def read_fnTch(self, fnTch):
        """
        -------------------------------------------------------
        Takes a base-90 "fnTch" number and converts it to a dictionary value
        which is then returned.
        Use: word = self.read_fnTch(fnTch)
        -------------------------------------------------------
        Parameters:
            fnTch - the base-90 "fnTch" number (str)
        Returns:
            word - the corresponding word in the dictionary (str)
        -------------------------------------------------------
        Examples:
            "``" -> 8099
            "p<" -> 2333
        -------------------------------------------------------
        """
        myNum = 0
        word = ""

        for i, char in enumerate(fnTch):
            try:
                index = self.CODE.index(char)
                myNum += index * 90**(i ^ 1)
            except ValueError:
                myNum = 10000

        if not len(self.words) <= myNum:
            word = self.words[myNum]

        return word

    def _read_string(self, string, add, select):
        """
       -------------------------------------------------------
       Reads a string of data as FnTch or words and can reverse.
       Use: x = self._read_string(string, add, select)
       -------------------------------------------------------
       Parameters:
           string - the input string (str)
           add - additional character to append (str)
           select - flag for FnTch or words (bool)
       Returns:
           out - the processed string (str)
       """
        out = ""
        splt = string.split(" ")

        for word in splt:
            if select:
                lin = self._linear_search_(word)
                if lin != -1:
                    if add != " ":
                        out += self.write_fnTch(lin) + "/" + add + " "
                    else:
                        out += self.write_fnTch(lin) + add
            else:
                out += self.read_fnTch(word) + self.readExtra(add)

        return out

    def read_file(self, name, select):
        """
        -------------------------------------------------------
        Reads a file and processes its content as FnTch or words.
        Use: stream = self.read_file(name, select)
        -------------------------------------------------------
        Parameters:
            name - the name of the file (str)
            select - flag for FnTch or words (bool)
        Returns:
            stream - the processed content of the file (str)
        -------------------------------------------------------
        """
        stream = ""
        file = open(name, "r")

        for line in file:
            stream += self._read_line(line, select)

        return stream

    def _read_line(self, string, select):
        """
        -------------------------------------------------------
        Processes a line of text as FnTch or words.
        Use: stream = self._read_line(string, select)
        -------------------------------------------------------
        Parameters:
            string - the input line (str)
            select - flag for FnTch or words (bool)
        Returns:
            stream - the processed line (str)
        -------------------------------------------------------
        """
        stream = ""
        string = string.rstrip()
        split = string.split()

        for sp in split:
            extras = sp.split('/')
            if len(extras) > 1:
                stream += self._read_string(extras[0], extras[1], select)
            else:
                stream += self._read_string(extras[0], " ", select)

        return stream

    def readExtra(self, stuff):
        """
        -------------------------------------------------------
        Processes additional characters and returns the corresponding values.
        Use: out = self.readExtra(stuff)
        -------------------------------------------------------
        Parameters:
            stuff - additional characters (str)
        Returns:
            out - processed additional characters (str)
        -------------------------------------------------------
        """
        out = ""

        for stu in stuff:
            if stu == 'n':
                out += "\n"
            elif stu in ('.', ',', ';', '!'):
                out += stu + " "
            else:
                out += stu

        return out
