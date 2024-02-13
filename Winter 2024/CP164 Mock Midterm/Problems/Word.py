"""
-------------------------------------------------------
THE WORD CLASS
-------------------------------------------------------
Author: Laurier FinTech
Email:  team@wlufintech.com
__updated__ = ""
-------------------------------------------------------

Name:           The Word Processor Problem
Created By:     Jason Van Humbeck
Package:        Laurier FinTech CP164 Mock Exam - Part 1
                Processor.py
                Word.py

Description: Creates a Word object which can intake and output words.
"""

class Word():
    def __init__(self,word):
        """
        -------------------------------------------------------
        Initializes a Word Object which contains a string based word
        Use: source = Word(word)
        -------------------------------------------------------
        Parameters:
            word - a string based word
        Returns:
            a new Word object (Word)
        -------------------------------------------------------
        """
        self.word = word

    def print_out(self):
        """
        -------------------------------------------------------
        Reads self and determines how to export properly.
        The use of '<>' indicates the end of a sentence.
        The use of '\n' indicates a new line.
        -------------------------------------------------------
        Parameters:
            file - file Name (ex: "fileName.txt") to where Stack/Queue should be written
        Returns:
            None
        -------------------------------------------------------
        """
        output = self.word

        if "<>" in self.word:
            output = output.replace("<>","")
        elif "\n" not in self.word:
            output += " "
        return output
