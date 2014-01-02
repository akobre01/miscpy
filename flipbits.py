def flipbits(byte):
    """
    this is just for practice doing bit shifting in python
    pass in a byte and flip all of the bits in it
    """

    bytecopy = 0
    for i in range(8):
        if (byte >> i) & 1 == 1:
            bytecopy += 1
        bytecopy = bytecopy << 1

    return bytecopy

print(flipbits(2))
print(flipbits(flipbits(2)))
print(flipbits(flipbits(flipbits(2))))
print(flipbits(flipbits(flipbits(flipbits(2)))))
