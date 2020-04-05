# coding=utf-8
"""Solves the ANARC05B problem in SPOJ."""

while True:
    FIRST = list(map(int, input().split()))
    if FIRST[0] == 0:
        break
    SECOND = list(map(int, input().split()))
    LEN_FIRST = FIRST[0]
    LEN_SECOND = SECOND[0]
    FIRST[0] = SECOND[0] = 0
    ITER_FIRST = ITER_SECOND = 1

    def inc_first():
        """Increments the sum of FIRST and also its iterator."""
        global ITER_FIRST
        FIRST[ITER_FIRST] += FIRST[ITER_FIRST - 1]
        ITER_FIRST += 1

    def inc_second():
        """Increments the sum of SECOND and also its iterator."""
        global ITER_SECOND
        SECOND[ITER_SECOND] += SECOND[ITER_SECOND - 1]
        ITER_SECOND += 1

    while ITER_FIRST <= LEN_FIRST or ITER_SECOND <= LEN_SECOND:
        if ITER_FIRST > LEN_FIRST:
            inc_second()
        elif ITER_SECOND > LEN_SECOND:
            inc_first()
        elif FIRST[ITER_FIRST] < SECOND[ITER_SECOND]:
            inc_first()
        elif FIRST[ITER_FIRST] > SECOND[ITER_SECOND]:
            inc_second()
        else:
            inc_first()
            inc_second()
            FIRST[ITER_FIRST - 1] = SECOND[ITER_SECOND - 1] = max(
                FIRST[ITER_FIRST - 1], SECOND[ITER_SECOND - 1],
            )
    print(max(FIRST[LEN_FIRST], SECOND[LEN_SECOND]))
