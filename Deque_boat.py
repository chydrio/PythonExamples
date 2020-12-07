from collections import deque

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        d=deque(people)
        print(d)
        weight_current_boat=0
        boat_number=0
        while d:
            big=d.pop()
            print(big)
            weight_current_boat+=big
            while d and weight_current_boat<=limit:
                small=d.popleft()
                print(small)
                weight_current_boat+=small
                if weight_current_boat>limit:
                    d.appendleft(small)
                    print("reinsert", small)
                    print(d)
                    break
            print("boat+1")
            boat_number+=1
            weight_current_boat=0
        return boat_number


--> wrong as we should always pair big one with 1 small, good solution below
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        d=deque(people)
        weight_current_boat=0
        boat_number=0
        while d:
            big=d.pop()
            print(big)
            weight_current_boat+=big
            if d and weight_current_boat<=limit:
                small=d.popleft()
                print(small)
                weight_current_boat+=small
                if weight_current_boat>limit:
                    d.appendleft(small)
            boat_number+=1
            weight_current_boat=0
        return boat_number
