# Programming task 1: Finding the Most Frequent Integer in a List
# Code explanation: This program finds the integer that appears most often in a list.

def most_frequent_integer(numbers):
    # a pre-check that the list is available
    if len(numbers) == 0:
        print('the list is empty')

    # use a dictionary to store the number and the counts of the number
    counts = {}
    # set the initial most frequent number
    most_frequent = None
    # set the initial highest count
    highest_count = 0

    # read the nuber in the list one by one
    for number in numbers:

        # if the number is already in the dictionary, then increase its count by one
        if number in counts:
            counts[number] = counts[number] + 1

        # if the number is not the list, then this is its first appearance
        else:
            counts[number] = 1

        # if this number has a higher count then the highest count,
        # then this number becomes the new most frequent number
        # use > instead of >= because we need to make sure the integer that became most frequent first
        if counts[number] > highest_count:
            highest_count = counts[number]
            most_frequent = number

    return most_frequent


# Test code
def test(number):
   result = most_frequent_integer(number)
   print(f"The most frequent number is {result}")

number_1 = [1,2,3,3,3,4,4,5]
test(number_1)