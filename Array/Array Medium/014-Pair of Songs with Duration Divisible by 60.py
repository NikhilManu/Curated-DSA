# Time O(N) | Space O(N)

def countSongPairs(times):
    count, dic = 0, {}
    for time in times:
        first = (60 - (time % 60)) % 60
        second = time % 60
        
        if first in dic:
            count += dic[first]
            
        if second not in dic:
            dic[second] = 0
        dic[second] += 1
        
    return count


"""
Intution:

To become a vaild pair, 
we know,
    => (x + y) % 60 == 0

    => (x % 60) + (y % 60) == 0 or 60  // 60 is possible if both x and y are not divsible by 60

    => y % 60 = (60 - (x % 60))  

    since (x % 60) can be equal to zero
    so (60 - (x % 60)) == 60 is also possible
    
    therefore eqn can be changed to (60 - (x % 60)) % 60

    so final Eqn,
    y % 60 = (60 - (x % 60)) % 60


    NOTE:
        if you dont understand why we are adding %60 in the final eqn,
        it is because in the hashmap or dicitionary we are only keeping count of values from 0 --> 59
        so when (60 - (x % 60)) == 60 we have to modulo it with 60 

        TestCase: [60, 60, 60] 
"""