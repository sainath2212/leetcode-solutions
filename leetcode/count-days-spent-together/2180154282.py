class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def to_days(dates):
            m, d = map(int, dates.split("-"))
            return sum(months[:
            m-1])+d 
        
        maxi = max(to_days(arriveAlice), to_days(arriveBob))
        mini = min(to_days(leaveAlice), to_days(leaveBob))
        return max(0, mini-maxi+1)