class XorShift:
    """
    Xorshift random number generators, also called shift-register generators,
    are a class of pseudorandom number generators that were invented by George Marsaglia.
    They are a subset of linear-feedback shift registers (LFSRs) which allow a particularly
    efficient implementation in software without the excessive use of sparse polynomials.

    https://en.wikipedia.org/wiki/Xorshift
    """

    def __init__(self, seed):
        """
        Initialize the XorShift RNG with a non-zero seed.

        Parameters:
        seed (int): A non-zero integer to initialize the internal state.
        """
        # The seed must be non-zero; otherwise, the algorithm would produce only zeros.
        if seed == 0:
            raise ValueError("Seed must be non-zero")
        # Ensure the seed fits within 32 bits by applying a mask.
        self.state = seed & 0xFFFFFFFF

    def next(self):
        """
        Generate the next pseudorandom 32-bit unsigned integer using the Xorshift32 algorithm.

        The algorithm uses three XOR and bit shift operations with constants that are typical
        for the Xorshift32 variant: 13, 17, and 5.

        Returns:
        int: A pseudorandom 32-bit unsigned integer.
        """
        # First step: left shift the current state by 13 bits and XOR it with the current state.
        self.state ^= (self.state << 13) & 0xFFFFFFFF  # Mask to maintain 32-bit precision.
        # Second step: right shift the result by 17 bits and XOR it with the state.
        self.state ^= (self.state >> 17)
        # Third step: left shift the result by 5 bits and XOR it with the state.
        self.state ^= (self.state << 5) & 0xFFFFFFFF  # Again, mask to maintain 32-bit precision.
        # Return the new state ensuring it's a 32-bit unsigned integer.
        return self.state & 0xFFFFFFFF

    def random(self):
        """
        Convert the 32-bit integer produced by next() into a floating-point number in the range [0, 1).

        Returns:
        float: A pseudorandom float between 0 (inclusive) and 1 (exclusive).
        """
        # Divide by 2^32 to scale the integer to the range [0, 1).
        return self.next() / 4294967296.0  # = 2 ** 32



if __name__ == "__main__":

    # Create an instance of the XorShift RNG with a non-zero seed.
    rng = XorShift(seed=42)

    print("Random 32-bit integers:")
    for _ in range(5):
        print(rng.next())

    print("\nRandom floats in [0, 1):")
    for _ in range(5):
        print(rng.random())

    print(help(XorShift.__doc__))