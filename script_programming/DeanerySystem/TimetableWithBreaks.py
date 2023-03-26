from break1 import Break
from typing import List
from term import Term

class TimetableWithBreaks():
    skipBreaks: bool = True
    def __init__(self, breaks: List[Break]):
        super().__init__()
        self._breaks = breaks
    
    @property
    def breaks(self):
        return self._breaks

    @breaks.setter
    def setBreaks(self, value):
        self._breaks.append(value)

    def onBreak(self, term: Term):
        start_t = (int(term.getStartTime()[0]), int(term.getStartTime()[1]))
        end_t = (int(term.getEndTime()[0]), int(term.getEndTime()[1]))

        for br in self._breaks:
            start_b = (int(br.getStartTime()[0]), int(br.getStartTime()[1]))
            end_b = (int(br.getEndTime()[0]), int(br.getEndTime()[1]))
            if end_b > start_t and start_t > start_b:
                return True, br.duration

            if end_t > start_b and end_b > end_t:
                return True, br.duration

            if start_t == start_b and end_t > end_b:
                return True, br.duration

            if end_b == end_t and start_b > start_t:
                return True, br.duration

            if start_t < start_b and end_t > end_b:
                return True, br.duration

        return False
    
    def busy(self, term: Term) -> bool:
        start_t = (int(term.getStartTime()[0]), int(term.getStartTime()[1]))
        end_t = (int(term.getEndTime()[0]), int(term.getEndTime()[1]))

        for lessson in list(self._lessons.values()):
            if term._day == lessson.term._day:

                start_l = (int(lessson.term.getStartTime()[0]), int(lessson.term.getStartTime()[1]))
                end_l = (int(lessson.term.getEndTime()[0]), int(lessson.term.getEndTime()[1]))

                if start_t > start_l and start_t < end_l:
                    return True
                if end_t > start_l and end_t < end_l:
                    return True
                if start_t == start_l:
                    return True
                if start_t < start_l and end_t > end_l:
                    return True
                if start_t > start_l and end_t < end_l:
                    return True
                if end_t == end_l:
                    return True

        return False

    def __str__(self):
        tabl = f'{"": <12}{"Poniedziałek": <12}{"*Wtorek": <12}{"*Środa": <12}{"*Czwartek": <12}{"*Piątek": <12}{"*Sobota": <12}{"*Niedziela": <12}\n'      
        tabl += f'{"": <12}{"*"*85}\n'
        
        times = []
        for lesson in list(self._lessons.values()):
            times.append(lesson.term)
        for br in self._breaks:
            times.append(br)
        times = sorted(times, key=lambda x: x.getUniqueStartingHours())

        to_display = [[f'{"*": <12}' for x in range(8)] for y in range(len(times))]

        prev_hour = []

        count = 0
        
        for i in range(len(times)):
            if [times[i].hour, times[i].minute, times[i].duration] != prev_hour:
                prev_hour = [times[i].hour, times[i].minute, times[i].duration]

                end_hour, end_min = times[i].getEndTime()
                start_hour, start_min = times[i].getStartTime()

                start = f'{start_hour}:{start_min}'
                end = f'{end_hour}:{end_min}'
                
                to_display[i-count][0] = f'{start+"-"+end: <12}'

                if type(times[i]) == Break:
                    # to_display[i-count][0] = f'{"Przerwa": <12}'
                    for j in range(7):
                        to_display[i-count][j+1] = f'{"-"*12}'
                
                if type(times[i]) == Term:
                    for lesson in list(self._lessons.values()):
                        if lesson.term.hour == times[i].hour and lesson.term.minute == times[i].minute and lesson.term.duration == times[i].duration:
                            day = lesson.term.day.value
                            to_display[i - count][day] = f'{"*"+lesson.name: <12}'
            else:
                count += 1

        for i in range(len(to_display) - count):
            for j in range(len(to_display[i])):
                tabl += f'{to_display[i][j]}'
            tabl += f'*\n{" ": <12}'
            tabl += f'{"*"*85}\n'

        return tabl