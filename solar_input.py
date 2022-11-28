# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
import matplotlib.pyplot as plt

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    _, radius, color, mass, x, y, Vx, Vy = line.split()

    star.m = float(mass)
    star.R = int(radius)
    star.color = color

    star.x = float(x)
    star.y = float(y)
    star.Vx = float(Vx)
    star.Vy = float(Vy)


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    _, radius, color, mass, x, y, Vx, Vy = line.split()

    planet.m = float(mass)
    planet.R = int(radius)
    planet.color = color

    planet.x = float(x)
    planet.y = float(y)
    planet.Vx = float(Vx)
    planet.Vy = float(Vy)


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            #print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            if obj.type == 'star':
                out_file.write('Star %d %s %s %f %f %f %f \n' % (obj.R,
                                                              obj.color,
                                                              obj.m,
                                                              obj.x,
                                                              obj.y,
                                                              obj.Vx,
                                                              obj.Vy))
            else:
                out_file.write('Planet %d %s %s %f %f %f %f \n' % (obj.R,
                                                              obj.color,
                                                              obj.m,
                                                              obj.x,
                                                              obj.y,
                                                              obj.Vx,
                                                              obj.Vy))
            # FIXME: should store real values


def save_statistics(space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open("stats.txt", 'a') as out_file:
        for obj in space_objects:
            #print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            if obj.type == 'star':
                out_file.write('Star %d %s %s %f %f %f %f \n' % (obj.R,
                                                              obj.color,
                                                              obj.m,
                                                              obj.x,
                                                              obj.y,
                                                              obj.Vx,
                                                              obj.Vy))
            else:
                out_file.write('Planet %d %s %s %f %f %f %f \n' % (obj.R,
                                                              obj.color,
                                                              obj.m,
                                                              obj.x,
                                                              obj.y,
                                                              obj.Vx,
                                                              obj.Vy))
        out_file.write("\n")


def clear_statistics():
    """Функция, стирающая статистику (вызывается при новом запуске)"""
    with open("stats.txt", 'w') as out_file:
        out_file.write("")


if __name__ == "__main__":
    print("This module is not for direct call!")
