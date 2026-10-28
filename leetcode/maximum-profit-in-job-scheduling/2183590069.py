class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [job[0] for job in jobs]
        n = len(jobs)
        d = {}
        def recur(i):
            if i==n:return 0 
            if i in d:return d[i]
            s, e, p = jobs[i]
            nextt = bisect_left(starts, e)
            t = p+recur(nextt)
            nt = recur(i+1)
            d[i] = max(t, nt)
            return d[i]
        return recur(0)
