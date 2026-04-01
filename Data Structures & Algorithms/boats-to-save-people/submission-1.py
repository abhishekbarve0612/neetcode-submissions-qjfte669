class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        start, end = 0, len(people) - 1
        count = 0

        while start <= end:
            takeBoth = people[start] + people[end]
            if takeBoth > limit:
                end -= 1
            else:
                start += 1
                end -= 1
            count += 1

        return count

