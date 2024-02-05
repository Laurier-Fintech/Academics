from utilities import *

# Section: What is deep copy?
a = [[1,2,3]]
b = a
a[0][0]=100
print(f'a:{a}, b:{b}')

# Initialize sample data structure
sample = SampleStructure()
# Testing append and prepend
sample.append(12)
sample.preprend(10)
sample.append(5)
print(sample)
# Testing insert
sample.insert(1,44)
print(sample)
# Testing linear search
print(sample._linear_search(12))
# Testing remove
sample.remove(44)
print(sample)
# Testing remove many
sample.append(10)
print(sample)
sample.remove_many(10)
print(sample)

# Additional sample structures for testing intersction and union
source1 = SampleStructure()
source1.append(5)
source1.append(10)
source1.append(15)
source1.append(20)


source2 = SampleStructure()
source2.append(5)
source2.append(10)
source2.append(30)
source2.append(40)