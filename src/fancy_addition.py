#! /usr/bin/python3
# -*- coding: utf-8 -*-


def fancy_addition(first, second):
    total = 0
    
    for _ in range(first):
        total += 1

    for _ in range(second):
        total += 1

    return total


if __name__ == "__main__":
    print(f"3 + 2 = {fancy_addition(3, 2)}")
