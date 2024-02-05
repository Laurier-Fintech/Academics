from Word import Word

"""
-------------------------------------------------------
THE PROCESSOR CLASS 
-------------------------------------------------------
Author:
ID:     
Email:  
__updated__ = ""
-------------------------------------------------------

Name:           The Word Processor Problem
Created By:     Jason Van Humbeck
Package:        Laurier FinTech CP164 Mock Exam - Part 1

Task Description:
    You have been assigned the task of developing a word processor using Python with
    a focus on utilizing data structures. The data structure should be capable of interpreting
    words either as a Basic Stack or Basic Queue. Your challenge is to create modular code
    that employs the same base methods regardless of the chosen data structure. 

    Additionally, the code should handle all errors that the Word class cannot. If implemented correctly,
    the word processor should be able to transcribe the entire Interstellar Script from the provided 
    file ("interstellar.txt") and rewrite it using the Processor.write method – reversing the words 
    as a Stack and maintaining the original order as a Queue.

Requirements:

    Avoid using built-in functions such as .remove or .pop.
    Limit each function to a single return statement.
    Prohibit the use of loop breaks.
    No illegal aids.

"""


class Processor:

    def __init__(self, stack):
        """
        -------------------------------------------------------
        Initializes an empty list to be used for a Stack or Queue.
        Use: source = List()
        -------------------------------------------------------
        Parameters:
            stack - a boolean value indicating the type of list (True -> Stack; False -> Queue)
        Returns:
            a new Processor object (Processor)
        -------------------------------------------------------
        """
        self.store = []
        self.stack = stack

    def insert(self, word):
        """
        -------------------------------------------------------
        Inserts a Word Object onto the Stack/Queue
        Use: source.insert(word)

        Answer: Since we are creating a system for both Queue's and Stack's
        we need to determine a solution which will work for both. This means
        that either the remove or the insert function must change to accommodate
        both. In this example I decided to keep the insert function the same
        for simplicity - although both can be correct.
        -------------------------------------------------------
        Parameters:
            word - a String containing a Word. No error checking needed.
        Returns:
            None
        -------------------------------------------------------
        """
        self.store.append(Word(word))

    def remove(self):
        """
        -------------------------------------------------------
        Removes/Pop and Returns an item from the Queue/Stack.
        Can create AUX functions if needed.
        Use: source.remove()

        Answer: It is good practice to auxiliary functions for long
        and in this case - differing code segments.
        -------------------------------------------------------
        Returns:
            output - a Word Object as a String ('_' if there is nothing to return)
        -------------------------------------------------------
        """
        output = "_"
        if not self._is_empty():
            if self.stack:
                output = self.remove_pop()
            else:
                output = self.remove_dequeue()
        return output

    def remove_pop(self):
        """
        -------------------------------------------------------
        auxiliary function for remove
        -------------------------------------------------------
        Answer: Since we insert sequentially by time, the top of the stack
        is actually at the back of the list. To retrieve the back most item
        of a list you can use [-1]. 'del' can be used to delete the item.
        -------------------------------------------------------
        """
        keep = self.store[-1].print_out()
        del self.store[-1]
        return keep

    def remove_dequeue(self):
        """
        -------------------------------------------------------
        auxiliary function for remove
        -------------------------------------------------------
        Answer: Since we insert sequentially by time, the top of the queue
        is also at the top of the list. To retrieve the front most item
        of a list you can use [0]. 'del' can be used to delete the item.
        -------------------------------------------------------
        """
        keep = self.store[0].print_out()
        del self.store[0]
        return keep

    def write(self, file):
        """
        -------------------------------------------------------
        Empty's self and Writes content in correct order to a file
        Use: source.write(fileOut)
        Answer: Create a write-stream, and while the list is not empty
        use the previously coded remove function to remove the correct Word
        -------------------------------------------------------
        Parameters:
            file - file Name (ex: "fileName.txt") to where Stack/Queue should be written
        Returns:
            None
        -------------------------------------------------------
        """
        out = open(file, "w")
        while not self._is_empty():
            out.write(self.remove())

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================
    def _is_empty(self):
        """
        -------------------------------------------------------
        Checks if Stack/Queue is Empty
        Use: source._is_Empty()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        return len(self.store) == 0

    def write_many(self, string):
        """
        -------------------------------------------------------
        Writes string of any length to Queue/Stack.
        Should use <> to denote end of sentence. Ex: "FinTech!<>"
        Use: source.write_many(string)
        -------------------------------------------------------
        Parameters:
            string - space delimited string of words.
        Returns:
            None
        -------------------------------------------------------
        """
        split = string.split(" ")
        for word in split:
            self.insert(word)

    def remove_all(self):
        """
        -------------------------------------------------------
        Removes all items in Queue/Stack and returns it as a String
        Use: source.remove_all()
        -------------------------------------------------------
        Returns:
            string - The removed string of words in Queue/Stack
        -------------------------------------------------------
        """
        string = ""

        while not self._is_empty():
            string += str(self.remove())
        return string

    def read_file(self, name):
        """
        -------------------------------------------------------
        Reads a file inserts all elements into the Queue/Stack.
        Use: source.read_file(name)
        -------------------------------------------------------
        Parameters:
            name - Name of file to be read (ex: 'readme.txt')
        Returns:
            lines - The amount of lines in the given file.
        -------------------------------------------------------
        """
        text = open(name, "r")
        lines = 0
        for line in text:
            split = line.split(" ")
            for word in split:
                self.insert(word)
            lines += 1
        text.close()
        return lines