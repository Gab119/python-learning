def p1():

    nums = [4,5,2,1]
    objective = 6
    for i in range(len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i] + nums[j] == objective:
                print(nums[i], nums[j])


def p2(): #Print all unique pairs (no repeats, no self-pairing).

    nums = [1,5,7,-1,5]
    target = 6
    results = []                        #or better use a set()

    for i in range(len(nums)):
        for j in range(i+1, (len(nums))):
            if nums[i] + nums[j] == target:
                pair = (nums[i], nums[j])

            #normalize pair (so (5, 1) == (1, 5))
            normalized = tuple(sorted(pair))            #the sorted pair means (1,5 is the same as 5,1) which prevents duplicates.
            if normalized not in results:
                results.append(normalized)

    print(results)

#With set:

def find_pairs():
    nums = [1, 5, 7, -1, 5]
    target = 6
    results = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = (nums[i], nums[j])
                normalized = tuple(sorted(pair))                    #sorted returns a list, lists cannot go into a set (error unhashable type), tuples can go into a set.
                results.add(normalized)                             #sets require hashable (immutable) elements.

    print(results)