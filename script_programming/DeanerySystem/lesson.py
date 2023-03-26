from term import Term
from day import Day
from typing import List


class LessonError(Exception):
    pass

class Lesson(object):
    def __init__(self, timetable, term: Term, name: str, teacherName: str, year: int, fullTime: bool= True ):
        self._timeTable = timetable
        self.setTerm = term
        self.setName = name 
        self.setTeacherName = teacherName
        self.setYear = year
        self.setFullTime = fullTime

    @property
    def term(self):
        return self._term
    
    @term.setter
    def setTerm(self, term):
        if type(term) != Term:
            raise LessonError('Wrong type of term')
        self._term = term
    
    @property
    def name(self):
        return self._name

    @name.setter
    def setName(self, name):
        if not isinstance(name, str):
            raise LessonError('Wrong type of Lesson name!')
        self._name = name

    @property
    def teacherName(self):
        return self._teacherName

    @teacherName.setter
    def setTeacherName(self, teacherName):
        if not isinstance(teacherName, str):
            raise LessonError('Wrong type of Teacher name!')
        self._teacherName = teacherName

    @property
    def year(self):
        return self._year
    
    @year.setter
    def setYear(self, year):
        if isinstance(year, int):
            self._year = year
        else:
            raise LessonError('Wrong type of year')

    @property        
    def fullTime(self):
        return self._fullTime
    
    @fullTime.setter
    def setFullTime(self, fullTime):
        if ((self._term._day.value in [1,2,3,4] and self._term.hour <= 20) or (self._term._day.value == 5 and self._term.hour < 17)) and self._term.hour >= 8:
            self._fullTime = True
        else:
            self._fullTime = False

    # def typeOfStudies(self):
    #     if ((self._term._day.value in [1,2,3,4] and self._term.hour <= 20) or (self._term._day.value == 5 and self._term.hour < 17)) and self._term.hour >= 8:
    #         return True
    #     else:
    #         return False
        
    # sprawdzam juz przesuniety w tyl lub w przod dzien
    # sprawdzam ten przesuniety dzien / godzine majac wiadomosc czy nalezy to do studiow stacjonarnych lub niestacjonranych
    # dzieki temu moge ocenic czy przesunieta juz data nalezy do przedzialu czasu ktory odpowiada jej 'rodzajowi' studiow
    # nie moze byc <= np. 20 bo 20:40 wtedy tez zostanie zaliczona
    # def can_be_transferred_to(self,term: Term, full_time: bool) -> bool:
    #     if full_time and term._day.value in [1,2,3,4]:
    #         if term._hour >= 8 and term._hour < 20:
    #             return True
    #     elif full_time and term._day.value in [5]:
    #         if term._hour >= 8 and term._hour < 17:
    #             return True
    #     elif not full_time and term._day.value in [5]:
    #         if term._hour >= 17 and term._hour < 20:
    #             return True
    #     elif not full_time and term._day.value in [6,7]:
    #         if term._hour >= 8 and term._hour < 20:
    #             return True
    #     return False
    
    #self._timetable  - odwolanie do klasy TimeTable - ktora posiada funkcje sprawdzajaca mozliwosc wykonania dzialania
    def ealierDay(self) -> bool:
        new_day = Day(7 if self._term._day.value - 1 == 0 else self._term._day.value - 1)
        new_term = Term(new_day, self._term._hour, self._term._minute, self._term._duration)
        # wystarczy sprawdzenie czy nowy termin spelnia warunki dla studiow stacjonarnych lub niestacjonarnych w zaleznosci ktore wybralismy
        # true - stacjonarne false - niestacjonarne
        if self._timeTable.can_be_transferred_to(new_term, self._fullTime):
            self._term = new_term
            return True
        else:
            return False
        

    def laterDay(self) -> bool:
        new_day = Day(1 if self._term._day.value + 1 == 8 else self._term._day.value + 1)
        new_term = Term(new_day, self._term._hour, self._term._minute, self._term._duration)
        if self._timeTable.can_be_transferred_to(new_term, self._fullTime):
            self._term = new_term
            return True
        else:
            return False

    # method to use DRY methodology
    def setDurationTime(self) -> List[int]:
        hoursToChange = self._term._duration // 60
        minutesToChange = self._term._duration % 60
        return [hoursToChange, minutesToChange]

    def laterTime(self) -> bool:
        # hoursToChange = self.term.duration // 60
        # # minutesToChange = self.term.duration - 60 * hoursToChange
        # minutesToChange = self.term.duration % 60
        arrayOfTime = self.setDurationTime()
        new_hour = self._term._hour + arrayOfTime[0]
        new_minutes = self._term._minute + arrayOfTime[1]

        if new_minutes >= 60:
            new_hour += 1
            new_minutes -= 60 

        new_term = Term(self._term._day, new_hour, new_minutes, self._term._duration)
        if self._timeTable.can_be_transferred_to(new_term, self._fullTime):
            self._term = new_term
            return True
        else:
            return False

    def ealierTime(self) -> bool:
        # from timeTable import Time
        # hoursToChange = self.term.duration // 60
        # # minutesToChange = self.term.duration - 60 * hoursToChange
        # minutesToChange = self.term.duration % 60
        arrayOfTime = self.setDurationTime()
        new_hour = self._term._hour - arrayOfTime[0]
        new_minutes = self._term._minute - arrayOfTime[1]

        if new_minutes < 0:
            new_hour -=1
            new_minutes += 60 

        new_term = Term(self._term._day, new_hour, new_minutes, self._term._duration)
        if self._timeTable.can_be_transferred_to(new_term, self._fullTime):
            self._term = new_term
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'{"-"*50}\n{self._name} ({self._term}) \n{self._year} rok studiów {"stacjonarnych" if self._fullTime else "niestacjonarnych"} \nProwadzący: {self._teacherName}\n{"-"*50}'

if __name__ == "__main__":
    # some manual tests before unitests
    from timeTableWithoutBreaks import TimetableWithoutBreaks
    table = TimetableWithoutBreaks()
    actions = ["t+", "d-", "t+", "d-"]
    act = table.parse(actions)
    print(act)

    # lesson1 = Lesson(table, Term(Day.THU, 12, 40), "Projektowe", "Krzyszot Dominikowski", 2)
    # lesson2 = Lesson(table, Term(Day.FRI, 11, 40), "Skryptowe", "Krzyszot Michail", 2)
    lesson1 = Lesson(table, Term(Day.TUE, 9, 40), "Kryptografia", "Krzyszot Rzecki", 2)
    lesson2 = Lesson(table, Term(Day.SUN, 19, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
    
    table.put(lesson1)
    table.put(lesson2)

    # print(table._lessons)
    table.perform(act)
    # print(table._lessons)
    # lesson1.laterDay()
    # lesson1.laterDay()
    print(table._lessons)
   
    # lesson.earlierTime()
    # term2 = Term(Day.FRI, 9, 45, 30)
    # termafter = Lesson(term2, 'name', 'name', 2, False)
    # print(termafter)
    # print(termafter.term._day.value)
    # print(termafter.laterDay())
    # print(termafter.term._day.value)