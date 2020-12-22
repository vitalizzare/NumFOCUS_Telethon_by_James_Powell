# Break down the code

from numpy.lib.stride_tricks import as_strided
from numpy import array

my_tuple = 1, 2, None, 4, None
print('An initial tuple (before mutation):', my_tuple)
print('with id =', id(my_tuple))
print('and hash =', hash(my_tuple))
original_id = id(my_tuple)
original_hash = hash(my_tuple)

# Get the memory point to stride from
memory_point = array([], dtype='uint64')

# Where in memory python places objects?
# Why a tuple is placed in memory after an array?
assert id(my_tuple) > memory_point.__array_interface__['data'][0]

offset = id(my_tuple) - memory_point.__array_interface__['data'][0]
array_from_point_to_tuple = as_strided(
    memory_point,
    strides=(1,),
    shape=(offset+1,))

# Get to the first bite of the tuple object
tuple_object_in_memory = as_strided(
    array_from_point_to_tuple[offset:], 
    strides=(8,), 
    shape=(4,))

# Get to the adress of the first item of tuple
# pass the first three 8-bytes words, which are:
#    object reference count
#    object type id
#    tuple length
tuple_items_in_memory = as_strided(
    tuple_object_in_memory[3:], 
    strides=(8,), 
    shape=(len(my_tuple),))

# write an adress of int(3) into tuple_items_in_memory[2]
# i.e. replace tuple[2], which is None, with integer 3
tuple_items_in_memory[2] = id(3)

# Do the same with 5th element of the tuple
tuple_items_in_memory[4] = id(5)

print('The tuple after mutation:', my_tuple)
print('with id:', id(my_tuple))
print(f"(id is{' not ' if original_id == id(my_tuple) else ' '}changed)")
print('and hash =', hash(my_tuple))
print(f"(hash is{' not ' if original_hash == hash(my_tuple) else ' '}changed)")

# Other 3 elements of my_tuple
assert tuple_items_in_memory[0] == id(1)
assert tuple_items_in_memory[1] == id(2)
assert tuple_items_in_memory[3] == id(4)

# The first three words of my_tuple as an object
from sys import getrefcount
assert tuple_object_in_memory[0] == getrefcount(my_tuple) - 1
assert tuple_object_in_memory[1] == id(tuple)
assert tuple_object_in_memory[2] == len(my_tuple)

del memory_point, array_from_point_to_tuple, tuple_object_in_memory, tuple_items_in_memory
