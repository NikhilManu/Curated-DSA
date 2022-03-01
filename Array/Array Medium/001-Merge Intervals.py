# Time O(N) | Space O(N)

def mergeIntervals(intervals):
    intervals.sort() # Sorts by the starting time
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        previous, current = res[-1], intervals[i] 

        # if current starting time is greater than the previous end time
        if current[0] > previous[1]:
            res.append(current)
        else:
            # we have to decide a end time by selecting the maximum of current and previous end time
            previous[1] = max(previous[1], current[1])
            
    return res