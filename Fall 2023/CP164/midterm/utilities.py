from copy import deepcopy

class SampleStructure:
    def __init__(self):
        self._values = []
        return
    
    def preprend(self, value):
        prev = deepcopy(self._values)
        add = []
        add.append(deepcopy(value))
        self._values = add + prev
        return
    
    def append(self, value):
        self._values.append(deepcopy(value))
        return
    
    def insert(self, i, value):
        if (i<=0):
            self.preprend(value)
        elif (i>=len(self._values)):
            self.append(self._values)
        else:
            prev = deepcopy(self._values)
            for x,_ in enumerate(self._values):
                if (x==i):
                    self._values[x] = deepcopy(value)
                elif(x>i):
                    self._values[x] = prev[x-1]
            self.append(prev[x])
        return

    def _linear_search(self, key):
        i = -1
        for x,value in enumerate(self._values):
            if value==key:
                i=x
                break
        return i 
    
    def remove(self, key):
        value = None
        at = self._linear_search(key)
        if (at!=-1):
            value = deepcopy(self._values[at])
            del self._values[at]
        return value
    
    def remove_many(self, key):
        cheat = deepcopy(self._values)  # Creating a deep copy of the list
        i = 0  # Initialize the index
        length = len(cheat)  # Get the initial length of the cheat list
        while i < length:
            if cheat[i] == key:  # If the value matches the key
                del cheat[i]  # Remove the value from the cheat list
                length -= 1  # Decrease the length since an element is removed
            else:
                i += 1  # Move to the next index if no element is removed
        self._values = cheat  # Update self._values with the modified cheat list
        return
    
    def intersection(self, source1, source2):
        cheat = []
        for val in self._values:
            if (val in source1.values()) and (val in source2.values()) and not (val in cheat):
                cheat.append(val)
        self._values = cheat
        return 
    
    def union(self, source1, source2):
        cheat = []
        for val in (source1.values() + source2.values()):
            if val not in cheat:
                cheat.append(val)
        self._values = cheat
        return
    
    def values(self): return deepcopy(self._values)

    def __str__(self):
        return ', '.join(str(value) for value in self._values)