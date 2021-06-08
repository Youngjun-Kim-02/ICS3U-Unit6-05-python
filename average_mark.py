#!/usr/bin/env python3

# Created by: Youngjun Kim
# Created on: June 2021
# This program uses an list


def main():
    # this function uses a list

    marks = []
    each_mark = None
    total = 0

    # input
    print("Please enter 1 mark at a time. Enter -1 to end.")

    each_mark = input("What is your mark? (as %): ")
    marks.append(each_mark)
    while each_mark != "-1":
        each_mark = input("What is your mark? (as %): ")
        marks.append(each_mark)

    marks.pop()  # remove the "-1" that was added
    print("")

    for counter in range(0, len(marks)):
        total += int(marks.pop())

    average = total / (counter + 1)
    print("The average is {0}".format(average))


if __name__ == "__main__":
    main()
