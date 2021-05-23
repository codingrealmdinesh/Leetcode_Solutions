def divide(self, dividend: int, divisor: int) -> int:

    # Constants.
    MAX_INT = 2147483647        # 2**31 - 1
    MIN_INT = -2147483648       # -2**31

    # Special case: overflow.
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    # We need to convert both numbers to negatives
    # for the reasons explained above.
    # Also, we count the number of negatives signs.
    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    # Count how many times the divisor has to be
    # added to get the dividend. This is the quotient.
    quotient = 0
    while dividend - divisor <= 0:
        quotient -= 1
        dividend -= divisor

    # If there was originally one negative sign, then
    # the quotient remains negative. Otherwise, switch
    # it to positive.
    return -quotient if negatives != 1 else quotient
#########
def divide(self, dividend: int, divisor: int) -> int:

    # Constants.
    MAX_INT = 2147483647        # 2**31 - 1
    MIN_INT = -2147483648       # -2**31
    HALF_MIN_INT = -1073741824  # MIN_INT // 2

    # Special case: overflow.
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    # We need to convert both numbers to negatives.
    # Also, we count the number of negatives signs.
    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    quotient = 0
    # Once the divisor is bigger than the current dividend,
    # we can't fit any more copies of the divisor into it anymore */
    while divisor >= dividend:
        # We know it'll fit at least once as divivend >= divisor.
        # Note: We use a negative powerOfTwo as it's possible we might have
        # the case divide(INT_MIN, -1). */
        powerOfTwo = -1
        value = divisor
        # Check if double the current value is too big. If not, continue doubling.
        # If it is too big, stop doubling and continue with the next step */
        while value >= HALF_MIN_INT and value + value >= dividend:
            value += value;
            powerOfTwo += powerOfTwo
        # We have been able to subtract divisor another powerOfTwo times.
        quotient += powerOfTwo
        # Remove value so far so that we can continue the process with remainder.
        dividend -= value

    # If there was originally one negative sign, then
    # the quotient remains negative. Otherwise, switch
    # it to positive.
    return -quotient if negatives != 1 else quotient
##########
def divide(self, dividend: int, divisor: int) -> int:

    # Constants.
    MAX_INT = 2147483647        # 2**31 - 1
    MIN_INT = -2147483648       # -2**31
    HALF_MIN_INT = -1073741824  # MIN_INT // 2

    # Special case: overflow.
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    # We need to convert both numbers to negatives.
    # Also, we count the number of negatives signs.
    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    doubles = []
    powersOfTwo = []

    # Nothing too exciting here, we're just making a list of doubles of 1 and
    # the divisor. This is pretty much the same as Approach 2, except we're
    # actually storing the values this time. */
    powerOfTwo = 1
    while divisor >= dividend:
        doubles.append(divisor)
        powersOfTwo.append(powerOfTwo)
        # Prevent needless overflows from occurring...
        if divisor < HALF_MIN_INT:
            break
        divisor += divisor # Double divisor
        powerOfTwo += powerOfTwo

    # Go from largest double to smallest, checking if the current double fits.
    # into the remainder of the dividend.
    quotient = 0
    for i in reversed(range(len(doubles))):
        if doubles[i] >= dividend:
            # If it does fit, add the current powerOfTwo to the quotient.
            quotient += powersOfTwo[i]
            # Update dividend to take into account the bit we've now removed.
            dividend -= doubles[i]

    # If there was originally one negative sign, then
    # the quotient remains negative. Otherwise, switch
    # it to positive.
    return quotient if negatives != 1 else -quotient
##########
def divide(self, dividend: int, divisor: int) -> int:

    # Constants.
    MAX_INT = 2147483647        # 2**31 - 1
    MIN_INT = -2147483648       # -2**31
    HALF_MIN_INT = -1073741824  # MIN_INT // 2

    # Special case: overflow.
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    # We need to convert both numbers to negatives.
    # Also, we count the number of negatives signs.
    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    # In the first loop, we simply find the largest double of divisor
    # that fits into the dividend.
    # The >= is because we're working in negatives. In essence, that
    # piece of code is checking that we're still nearer to 0 than we
    # are to INT_MIN.
    highest_double = divisor
    highest_power_of_two = -1
    while highest_double >= HALF_MIN_INT and dividend <= highest_double + highest_double:
        highest_power_of_two += highest_power_of_two
        highest_double += highest_double

    # In the second loop, we work out which powers of two fit in, by
    # halving highest_double and highest_power_of_two repeatedly.
    # We can do this using bit shifting so that we don't break the
    # rules of the question :-)
    quotient = 0
    while dividend <= divisor:
        if dividend <= highest_double:
            quotient += highest_power_of_two
            dividend -= highest_double
        # We know that these are always even, so no need to worry about the
        # annoying "bit-shift-odd-negative-number" case.
        highest_power_of_two >>= 1
        highest_double >>= 1

    # If there was originally one negative sign, then
    # the quotient remains negative. Otherwise, switch
    # it to positive.
    return quotient if negatives == 1 else -quotient
##########
def divide(self, dividend: int, divisor: int) -> int:

    # Constants.
    MAX_INT = 2147483647        # 2**31 - 1
    MIN_INT = -2147483648       # -2**31
    HALF_MIN_INT = -1073741824  # MIN_INT // 2

    # Special case: overflow.
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    # We need to convert both numbers to negatives.
    # Also, we count the number of negatives signs.
    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    # We want to find the largest doubling of the divisor in the negative 32-bit
    # integer range that could fit into the dividend.
    # Note if it would cause an overflow by being less than HALF_INT_MIN,
    # then we just stop as we know double it would not fit into INT_MIN anyway.
    max_bit = 0
    while divisor >= HALF_MIN_INT and divisor + divisor >= dividend:
        max_bit += 1
        divisor += divisor

    quotient = 0
    # We start from the biggest bit and shift our divisor to the right
    # until we can't shift it any further.
    for bit in range(max_bit, -1, -1):
        # If the divisor fits into the dividend, then we should set the current
        # bit to 1. We can do this by subtracting a 1 shifted by the appropriate
        # number of bits.
        if divisor >= dividend:
            quotient -= (1 << bit)
            # Remove the current divisor from the dividend, as we've now
            # considered this part of it.
            dividend -= divisor
        # Shift the divisor to the right so that it's in the right place
        # for the next positon we're checking at.
        divisor = (divisor + 1) >> 1


    # If there was originally one negative sign, then
    # the quotient remains negative. Otherwise, switch
    # it to positive.
    return -quotient if negatives != 1 else quotient
#############