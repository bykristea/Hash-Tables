# {
#     array: [],
#     hashFunctionL ()
# }

# returns an index in the array


def myHash1(key):
    return len(key) % length_of_array
    # dog--> 3
    # deterministic----non-invertible, one-way function
    # CON:
    # --output not unique


def myHash2(key):
    output_index = (len(key) * salt) % length_of_array
    return output_index

    # Pro:
    # -non-invertible
    # -pretty unique

    # CONS:
    # -not deterministic.
# key="hello"


def djb2(key):
    # some prime number
    our_salt = 5381

    # scramble each letter
    for char in key:
        hash_value = (our_salt << 5) + our_salt + char
    return hash_value

# sha256 hash function is common.
