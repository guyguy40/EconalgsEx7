"""
this is a submission for question 1

submittor info:
name: Guy Wolf
I.D: 212055966
"""

class Distribution:
    def __init__(self, values):
        pass

    def f(self, x):
        pass

    def r(self, x):
        return float(x)-(float(1-self.f(x))/float(self.diff(x)))

    def diff(self, x):
        """calculates the derivative of the probability at point x using basic approximation"""
        base = self.f(x)
        h = 1
        adv = self.f(x+h)
        while adv == base:
            h += 1
            adv = self.f(x+h)
        return float(adv-base)/float(h)

class BasicDistribution(Distribution):
    def __init__(self, values):
        self.len = len(values)
        self.values = sorted(values)

    def f(self, x):
        minVal = 0
        maxVal = len(self.values)-1
        while minVal < maxVal:
            midVal = int(minVal + (maxVal - minVal)/2)
              
            #check if x is present at the middle 
            if values[midVal] == x: 
                break 
      
            #if x is greater, ignore left half 
            elif values[midVal] < x: 
                minVal = mid + 1
      
            #if x is smaller, ignore right half 
            else: 
                maxVal = midVal - 1

        if minVal >= maxVal:
            midVal = min(minVal,len(self.values)-1)

        while self.values[midVal] >= x and midVal > 0:
            midVal -= 1

        return midVal/len(self.values)

class CachedDistribution(BasicDistribution):
    def __init__(self, values):
        super().__init__(values)
        probCache = {}
        diffCache = {}

    def f(self, x):
        if x in self.probCache:
            return self.probCache[x]
        res = super().f(x)
        self.probCache[x] = res
        return res

    def diff(self, x):
        if x in self.diffCache:
            return self.diffCache[x]
        res = super().diff(x)
        self.diffCache[x] = res
        return res
