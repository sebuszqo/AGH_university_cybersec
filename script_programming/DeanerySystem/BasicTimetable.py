from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class Action(Enum):
    pass
##########################################################


class Lesson:
    pass
#########################################################


class Term:
    pass
##########################################################


class BasicTimetable(ABC):
    @abstractmethod
    def busy(self, term: Term) -> bool:
        pass
##########################################################

    def get(self, term: Term) -> Lesson:
        print("Wywołano metodę 'get()' zdefiniowaną w klasie 'BasicTimetable'")
##########################################################

    @abstractmethod
    def parse(self, actions: List[str]) -> List[Action]:
        pass
##########################################################

    @abstractmethod
    def perform(self, actions: List[Action]):
        pass
##########################################################

    @abstractmethod
    def put(self, lesson: Lesson) -> bool:
        pass