import copy


class Fubbi:
    from copy import deepcopy
    """
    The Fubbi class was created by a genius. Infact, his genius was so great that humans couldn't even
    comprehend it until the future when he was long dead. His greatest invention was that of the
    Fubbi class (which can solve world peace), however, he never got a chance to finish it.
    Your job, as the briliant mind that you are is to complete his lives work, and save humanity!

    The Fubbi class works as follows:

    It takes input from a user in the form of an integer. It then looks to insert this value into ._values.
    However, it is only allowed to insert it if:
        1. There are no duplicates already
        2. The previous number, sequentaly, excists alredy in ._values.
    If either of these rules are broken, the Integer will be thrown in ._junk, to where it can be later used.
    However, Junk operates as that of a Queue (First In, First Out). Where, for every action (i.e. insert, remove) done
    to ._values, the item at the top of the ._junk stack will be removed and then used. It can only be used if it meets
    the previous conditons; if it does not it will be appended to the back of the queue, where the process will repeat.

    Example 1:
        self._values = [1,2,3]
        self._junk = [4]
        insert(5)
            self._values = [1,2,3] #No change - It did not meet conditons
            self._junk = [4,5] #Gets appended to Junk
            self._values = [1,2,3,4] #An action happened, so junk is checked and 4 is at the top, which is valid
            self._junk = [5]#Due to the prior action, 4 was removed and 5 is now at the top
        remove(2)
            self._values = [1,3,4] #The Fubbi now has a hole in it, which means 2, and 5 are now open spots.
            self._junk = [5] #Junk gets no additions
            self._values = [1,3,4,5] #An action happened, so junk is checked; 5 was valid
            self._junk = [] #Junk is now empty which means at the next action, nothing will happen to junk


    Example 2:
        Fubbi A:
            self._values = [1,2,3,5]
            self._junk = [7,9]
        Fubbi B:
            self._values = [1,3,4,6,8]
            self._junk = [3,10,9,7]
            self.union(A) #union with a into b

                self._values = [1,2,3,4,5,6,8] #The following values are inserted: [1,2,3,5]; 1,5 were succesfull
                self._junk = [3,10,9,7,1,3] #1,3 were unsuccsessfull so they are added the ._junk queue.
                self._junk = [3,10,9,7,1,3,7,9] #A's Junk = [7,9] gets appeneded regardless of values.

            self.junk_junk(4) #junk queue is roatated by 4

                3: self._junk = [10,9,7,1,3,7,9,3] #not valid in ._values so sent to back of ._junk
                10: self._junk = [9,7,1,3,7,9,3,10] #not valid in ._values so sent to back of ._junk
                9: self._junk = [7,1,3,7,9,3,10,9] #not valid in ._values so sent to back of ._junk
                7: self._junk = [1,3,7,9,3,10,9]; self._values = [1,2,3,4,5,6,7,8] #valid so added.

                return -> 1


    """


    def __init__ (self):
        self._values = []
        self._junk = []

    def junk_check (self):
        """
        Removes the front of ._junk and determines if it is allowed to be added to ._values.
        If not, it gets readded via junk_add() to the back of junk and nothing happens
        :return: None
        """

        out = deepcopy(self._junk [0])
        self.insert(out)
        return

    def junk_add (self,value):
        """
        Adds, the discarded value to the back of the ._junk Queue
        :param value: int
        :return:
        """
        self._junk.append(value)

        return

    def insert (self, value):
        """
        Inserts the value in ._values if the following conditons are met:
             1. There are no duplicates already
             2. The previous number, sequentaly, excists alredy in ._values.
        If not, junk_add() should be called.
        :param value: int
        :return: none
        """
        if value not in self._values and (value -1) in self._values:
            cheat = []
            found = False
            for val in self._values:
                if val > value and not found:
                    cheat.append(value)
                    cheat.append(val)
                    found = True
                else:
                    cheat.append(val)
            self._values = cheat
        elif len(self._values) == 0:
            self._values.append(value)
        else:
            self.junk_add(value)

        self.junk_check()
        return

    def remove (self,i):
        """
        Removes the value at position i, and returns it. If i not a valid int - make it one by subtracting the length
         from i until it is within the valid range. If the list is empty, treat i as a value to be inserted, and return None.
        :param i: int
        :return value: the value at i.
        """
        out = None
        if (self._values == 0):
            self.insert(i)
        else:
            itr = self._values [((i+1)% len(self._values)) -1]
            out = self._values [itr]
            del self._values [itr]


        self.junk_check()
        return out

    def linear_search (self,key):
        """
        Determines the position of the values which matches the key, and returns it. Return None if nothing is found.
        :param key: Int
        :return i: The positon of i.
        """
        found = False
        at = 0
        while not found or at >= len(self._values):
            if (self._values[at] == key):
                found = True
            else:
                at += 1


        return at


    def junk_junk(self,i):
        """
        Flips through the junk Queue, as many times i states, and returns the ammount of succesess
        :param i: int
        :return: how many rotations were successfull (int)
        """
        start = len(self._junk)
        for i in range(i):
            self.junk_check()
        successfull = start - len(self._junk)
        return successfull

    def export (self):
        """
        Exports itsself in a 1d text array, where the ._values come first followed by "j" and then ._junk. The values
        should be seperated by a comma, and both sides should stay in the same order.
        :return: String in desired format
        """
        string = ""
        for value in self._values:
            string += value + ","
        string += "j,"
        for junk in self._junk:
            string += junk + ","
        string.removesuffix(",")
        return string

    def overwrite (self,fubbi):
        """
        Overrite both the ._junk, and ._values with the string values using the fubbi string provided, using the
        export format as shown above in export().
        :param fubbi: A String
        :return: None
        """
        fork = fubbi.split(",")
        self._values = []
        self._junk = []
        switch = False
        
        for prong in fork:
            if switch:
                self.junk_add(prong)
            else:
                if prong == "j":
                    switch = True
                else:
                    self.insert(prong)


        return


    def union (self, Fubbi):
        """
        Will merge the given Fubbi into the current. Numbers should be imported in the same order, where:
            - ._values are inserted (if possible)
            - ._junk are automaticly merged to the end of the the current ._junk
        The paramter Fubbi's values should remain untouched at the end.
        :param Fubbi: A Fubbi Object
        :return: None
        """

        self.junk_check()
        for value in Fubbi._values:
            self.insert(value)
        for junk in Fubbi._junk:
            self._junk(value)
        return



