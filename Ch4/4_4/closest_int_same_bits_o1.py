import sys
import random


# @include
def closest_int_same_bit_count(x):
    # NUM_UNSIGNED_BITS = 64
    BIT_MASK = 0xFFFFFFFFFFFFFFFF
    # x^=BIT_MASK
    if (x & ~(x - 1)) != 1:
        # print (x&(x-1))|((x&~(x-1))>>1)
        return (x & (x - 1)) | ((x & ~(x - 1)) >> 1)
        
    else:
        y = x ^ BIT_MASK
        
        x ^= (y & ~(y - 1)) | (y & ~(y - 1)) >> 1
        return x

    # Raise error if all bits of x are 0 or 1.
    raise ValueError('All bits are 0 or 1')
# @exclude



if __name__ == '__main__':
    print closest_int_same_bit_count(6)
    print closest_int_same_bit_count(7)
    print closest_int_same_bit_count(2)
    print closest_int_same_bit_count(32)
    print closest_int_same_bit_count(2 ** 64 - 2) == (2 ** 64) - 3
    bignumber = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(0,
                                                                   sys.maxsize)
    res = closest_int_same_bit_count(bignumber)
    print(bignumber, res)
