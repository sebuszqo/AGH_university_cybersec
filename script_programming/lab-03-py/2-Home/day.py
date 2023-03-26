from enum import Enum


class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    def difference(self, day):
        dif = day.value - self.value    
        return dif + 7 if dif <= -4 else (dif - 7 if dif >= 4 else dif)
        
def nthDayFrom(n, day):
    val = day.value + n
    return Day(val + 7) if val <= 0 else (Day(val - 7) if val >= 8 else Day(val))