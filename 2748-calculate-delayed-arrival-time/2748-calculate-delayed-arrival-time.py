class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        t = arrivalTime + delayedTime
        if  t >= 24:
            return t%24
        return t
        