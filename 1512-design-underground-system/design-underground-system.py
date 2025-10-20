class UndergroundSystem(object):

    def __init__(self):
        self.checkintime = {}
        self.totaltime = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkintime[id] = (stationName,t)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        (startstationName, time) = self.checkintime.pop(id)

        totaltime = t - time

        if (startstationName, stationName) not in self.totaltime:
            self.totaltime[(startstationName, stationName)] = [0,0]

        self.totaltime[(startstationName, stationName)][0] += totaltime
        self.totaltime[(startstationName, stationName)][1] += 1


    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """

        return float(self.totaltime[(startStation, endStation)][0]) / self.totaltime[(startStation, endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)