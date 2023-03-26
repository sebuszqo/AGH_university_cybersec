from day import Day
from term_error import TermError


class Term():
    def __init__(self, day = Day.MON ,hour: int = 0, minute: int = 0 , duration = 90):
        self._day = day
        if not isinstance(self._day, Day):
            raise TermError('Wrong day type')
        self.setHour = hour
        self.setMinute = minute
        self.setDuration = duration

    # @property
    # def day(self):
    #     return self.__day 
    
    # @day.setter
    # def setDay(self, day: Day):
    #     self.__day = day

    @property
    def hour(self):
        return self._hour
    
    @hour.setter
    def setHour(self, hour:int):
        if type(hour) is int and hour >= 0 and hour <=23:
            self._hour = hour
        else:
            raise TermError('You gave wrong hour, give me <0,23>')

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def setMinute(self, minute: int):
        if isinstance(minute, int) and minute >= 0 and minute <= 59:
            self._minute = minute
        else:
             raise TermError('You gave wrong minute, give me <0,59>')

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def setDuration(self, duration: int):
        if isinstance(duration, int) and duration >= 0:
            self._duration = duration
        else:
             raise TermError('You gave wrong druation, give me <0,...>')

    # finding what day _day.value means
    def __str__(self):
        day = {      1: "Poniedziałek",
                     2: "Wtorek",
                     3: "Środa",
                     4: "Czwartek",
                     5: "Piątek",
                     6: "Sobota",
                     7: "Niedziela",
         }[self._day.value]
        return f'{day} {self._hour}:{self._minute} [{self._duration}]'
    
    def laterThan(self, termin):
        return True if termin._hour < self._hour else (True if termin._hour == self._hour and termin._minute < self._minute else False) 

    def earlierThan(self, termin):
        return False if termin._hour < self._hour else (False if termin._hour == self._hour and termin._minute < self._minute else True) 

    def equals(self, termin):
        return True if self._day == termin._day and self._hour == termin._hour and self._minute == termin._minute and self._duration == termin._duration else False

    # Overloading Functions and Operators in Python
    def __lt__(self, termin):
        return self.earlierThan(termin)

    def __le__(self, termin):
        return self.earlierThan(termin) or self.equals(termin)

    def __gt__(self, termin):
        return not self.earlierThan(termin)

    def __ge__(self, termin):
        return not self.earlierThan(termin) or self.equals(termin)

    def __eq__(self, termin):
        return self.equals(termin)

    def __sub__(self, termin):
        duration = ((self._hour + 1)- termin.hour)*60 + ((self._minute + 30) - termin.minute) + ((self._day.value - termin._day.value) * 24)*60
        # newTerm = Term(termin._day, termin.hour, termin.minute, duration)
        return Term(termin._day, termin.hour, termin.minute, duration)
    
    def getEndTime(self):
        hour_d = self._duration // 60
        min_d = self._duration % 60

        new_h = self._hour + hour_d
        new_m = self._minute + min_d

        if new_m >= 60:
            new_h += 1
            new_m -= 60
        
        return str(new_h), "0"+str(new_m) if new_m < 10 else str(new_m)

    def getStartTime(self):
        return str(self._hour), "0"+str(self._minute) if self._minute < 10 else str(self._minute)

    def getUniqueStartingHours(self):
        return (self._hour, self._minute)
    
    # never mind ...
    #DRY method -- to check if given hour minute and day is ealier or later 
    # @classmethod
    # def isTrueOrFalse(cls, termToCheck, termin):
    #     if termin._hour < termToCheck._hour:
    #         return False
    #     elif (termin._hour == termToCheck._hour and termin._minute < termToCheck._minute):
    #         return False
    #     return True

    #DRY method -- to check if given days are the same, days hours and minutes
    # @classmethod
    # def sameDay(cls, termToCheck, termin):
    #     if (termin.hour == termToCheck.hour and termin.minute == termToCheck.minute and termin.day.value == termToCheck.day.value and termin.duration == termToCheck.duration):
    #         return True
    #     return False

    #function to check is terms are ealier, gives False or True
    # def earlierThan(self, termin):
    #     # creating new instance of Term class 
    #     termToCheck = Term(self._day, self._hour, self._minute)
    #     if (Term.sameDay(termToCheck, termin)):
    #         return bool(False)
    #     result = Term.isTrueOrFalse(termToCheck,termin)
    #     return bool(result)

    #function to check is terms are later, gives False or True
    # def laterThan(self, termin):
    #     # creating new instance of Term class -- cuz I had problems with t
    #     termToCheck = Term(self._day, self._hour,self._minute)
    #     if (Term.sameDay(termToCheck,termin)):
    #         return bool(False)
    #     result = Term.isTrueOrFalse(termToCheck,termin)
    #     #using same DRY method to check F/T so in return has to be 'not'
    #     return not bool(result)


        # if termin.hour > self.hour:
        #     return False
        # elif (termin.hour == self.hour and termin.minute > self.minute):
        #     return False
        #return True
        # print(self._day.value)

    # def equals(self, termin):
    #     termToCheck = Term(self._day, self._hour, self._minute, self._duration)
    #     return bool(Term.sameDay(termToCheck,termin))
        
if __name__ == "__main__":
    term1 = Term(Day.MON, 8, 30)

    term2 = Term(Day.TUE, 9, 45, 30)
    term3 = Term(Day.TUE, 9, 45, 90)
    print("term1 < term2:", term1 < term2)   # Ma się wypisać True
    print("term1 <= term2:", term1 <= term2) # Ma się wypisać True
    print("term1 > term2:", term1 > term2)   # Ma się wypisać False
    print("term1 >= term2:", term1 >= term2) # Ma się wypisać False
    print("term2 == term2:", term2 == term2) # Ma się wypisać True
    print("term2 == term3:", term2 == term3)
    term4 = term3 - term1
    print(term4)
    # term1 = Term(Day.TUE, 9, 45)
    # print(term1)                     
    # term2 = Term(Day.WED, 10, 15)
    # print(term2)                     
    # print(term1.earlierThan(term2)); 
    # print(term1.laterThan(term2));  
    # print(term1.equals(term2)); 

        
# try:
#     term1 = Term(Day.TUE, 9, 45)
#     term2 = Term(Day.TUE, 10, 15)
# except:
#     print('Podales zle dzien')
# term1.__str__()
# print(term1.earlierThan(term2))
# print(term1.laterThan(term2))
# print(term1.equals(term2))

# klasa.earlierThan(secondclass)