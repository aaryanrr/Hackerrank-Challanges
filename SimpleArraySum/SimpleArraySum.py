#!/usr/bin/python3

import os


def simpleArraySum(ar: list) -> int:
    # Write your code here
    return int(sum(ar))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
