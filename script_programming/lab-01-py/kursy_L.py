
# proper use: python3 kursy_L.py <max_numer_of_students>

# where 'max_numer_of_students' define maximum amount of students in 1 course.

# By default there is one course 'course1' and it has only 1 person inside.

# Courses are stored by using python dictionary
# names of courses are keys 
# array contains students 

import sys

#adding my own error
class TooMuchPeople(Exception):
    pass

#adding a course
def addCorse(course):
    listOfCoursesAndStudents[course] = []
    return listOfCoursesAndStudents

#removing a course
def removeCourse(course):
    listOfCoursesAndStudents.pop(course)
    return

#adding person to course
def addPersonToCourse(name, course):
    if len(listOfCoursesAndStudents[course]) < int(sys.argv[1]):
        return listOfCoursesAndStudents[course].append(name)
    raise TooMuchPeople

#remoeing person form course
def removePersonFromCourse(name,course):
   print(listOfCoursesAndStudents[course])
   return listOfCoursesAndStudents[course].remove(name)


# main program 
if __name__ == '__main__':
#    maxNumOfStudents = sys.argv[1]
   listOfCoursesAndStudents = {'course1': ['studentA']}
   while True:
    try:
        print('\nWybierz co chcesz zrobic?\n')
        
        x = int(input('1.Zapisz osobe na kurs.\n2.Wypisz osobe z kursu.\n3.Dodaj kurs.\n4.Usun kurs.\n5.Pokaz stan kursow.'))
        if x == 1:
            numOfPeople = int(input('ile osob chcesz wpisac ? '))
            for _ in range(numOfPeople):
                name = input('Podaj imie: ')
                course = input('Podaj nazwe kursu: ')
                addPersonToCourse(name, course)
        elif x == 2:
            name = input('Podaj imie: ')
            course = input('Podaj nazwe kursu: ')
            removePersonFromCourse(name, course)
        elif x == 3:
            course = input('Podaj nazwe nowego kursu: ')
            addCorse(course)
        elif x == 4:
            course = input('Podaj nazwe kursu do usuniecia: ')
            removeCourse(course)
        elif x == 5:
            print(f'Aktualny stan wszystkich kursów: {listOfCoursesAndStudents}')
        elif x not in (1,2,3,4,5):
            print('\nDokonales zlego wyboru. Sprobuj jeszcze raz!\n')
    #handling errors 
    except EOFError:
        print('\n Koncze dzialanie programu \n')
        print(f'\nLISTA KURSOW I KURSANTOW {listOfCoursesAndStudents}')
        break
    except KeyError:
        print(' \n Podales zlą nazwe kursu  Sprobuj jeszcze raz!\n')
    except ValueError:
        print(' \n Podales zle imie osoby!  Sprobuj jeszcze raz!\n')
    except KeyboardInterrupt:
        print('\n\n Koncze dzialanie programu')
        print(f'\n LISTA KURSOW I KURSANTOW {listOfCoursesAndStudents}\n')
        break
    except TooMuchPeople:
        print('\n W tym kursie jest juz za duzo ludzi, wybierz lub stworz inny!')
            



