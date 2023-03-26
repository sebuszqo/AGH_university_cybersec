from typing import List
from term import Term
from lesson import Lesson
from action import Action
from action import Action


class TimetableWithoutBreaks(object):
    def __init__(self) -> None:
        self._lessons = {}
    """ Class containing a set of operations to manage the timetable """

    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        if self.busy(term):
            return False

        if full_time and term._day.value in [1,2,3,4]:
            if term._hour >= 8 and term._hour < 20:
                return True
        elif full_time and term._day.value in [5]:
            if term._hour >= 8 and term._hour < 17:
                return True
        elif not full_time and term._day.value in [5]:
            if term._hour >= 17 and term._hour < 20:
                return True
        elif not full_time and term._day.value in [6,7]:
            if term._hour >= 8 and term._hour < 20:
                return True
        return False

    def busy(self, term: Term) -> bool:
        for le in list(self._lessons.keys()):
            if le == term.__str__():
                return True
        return False

    def put(self, lesson: Lesson) -> bool:
            if self.busy(lesson._term):
                raise ValueError("Term is busy already!")
            self._lessons[lesson._term.__str__()] = lesson
            return True

    def parse(self, actions: List[str]) -> List[Action]:
        A = []
        for opt in actions:
            if opt == "d-":
                A.append(Action.DAY_EARLIER)
            elif opt == "d+":
                A.append(Action.DAY_LATER)
            elif opt == "t-":
                A.append(Action.TIME_EARLIER)
            elif opt == "t+":
                A.append(Action.TIME_LATER)
            else:
                raise ValueError(f"Translation of {opt} cannot be done!")
        return A

    def perform(self, actions: List[Action]):
        len_lessons = len(self._lessons)
        for (index, action) in enumerate(actions, start=0):
            if action == Action.DAY_EARLIER:
                # print(self.get(list(self._lessons.values())[index % len_lessons]))
                self.get(list(self._lessons.values())[index % len_lessons]).ealierDay()
                print(list(self._lessons.values())[index % len_lessons])
            elif action == Action.DAY_LATER:
                # print(self.get(list(self._lessons.values())[index % len_lessons]))
                self.get(list(self._lessons.values())[index % len_lessons]).laterDay()
                print(list(self._lessons.values())[index % len_lessons])
            elif action == Action.TIME_EARLIER:
                # print(self.get(list(self._lessons.values())[index % len_lessons]))
                self.get(list(self._lessons.values())[index % len_lessons]).ealierTime()
                print(list(self._lessons.values())[index % len_lessons])
                # print(list(self._lessons.values()[index % len_lessons]))
            elif action == Action.TIME_LATER:
                # print(self.get(list(self._lessons.values())[index % len_lessons]))
                self.get(list(self._lessons.values())[index % len_lessons]).laterTime()
                print(list(self._lessons.values())[index % len_lessons])
                # print(list(self._lessons.values()[index % len_lessons]))

    def get(self, term: Term) -> Lesson:
        for lesson in list(self._lessons.values()):
            if lesson == term:
                return lesson
        return None
