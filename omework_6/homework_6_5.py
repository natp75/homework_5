
#Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы
# должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self,title):
        self.title = title

    def draw(self):
        print('Start drawing')


class Pen(Stationery):
    def draw(self):
        print('Start drawing with Pen')


class Pencil(Stationery):
    def draw(self):
        print('Start drawing with Pencil')


class Handle(Stationery):
    def draw(self):
        print('Start drawing with Handle')

pen = Pen("A")
pencil = Pencil("B")
handle = Handle("C")
for s in (pen, pencil, handle):
    s.draw()