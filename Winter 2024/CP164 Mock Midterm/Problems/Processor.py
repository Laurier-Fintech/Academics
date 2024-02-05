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
                Processor.py
                Word.py

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
from Word import Word
class Processor:

    def __init__(self,stack):
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
        # Your Code Here

    def insert(self, word):
        """
        -------------------------------------------------------
        Inserts a Word Object onto the Stack/Queue
        Can create AUX functions if needed.
        Use: source.insert(word)
        -------------------------------------------------------
        Parameters:
            word - a String containing a Word. No error checking needed.
        Returns:
            None
        -------------------------------------------------------
        """

        # Your Code Here

    def remove(self):
        """
        -------------------------------------------------------
        Removes/Pop and Returns an item from the Queue/Stack.
        Can create AUX functions if needed.
        Use: source.remove()
        -------------------------------------------------------
        Returns:
            output - a Word Object as a String ('_' if there is nothing to return)
        -------------------------------------------------------
        """

        # Your Code Here

    def write(self, file):
        """
        -------------------------------------------------------
        Empty's self and Writes content in correct order to a file
        Use: source.write(fileOut)
        -------------------------------------------------------
        Parameters:
            file - file Name (ex: "fileName.txt") to where Stack/Queue should be written
        Returns:
            None
        -------------------------------------------------------
        """

        # Your Code Here


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