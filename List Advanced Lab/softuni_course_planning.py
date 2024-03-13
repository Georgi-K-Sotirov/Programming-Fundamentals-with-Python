def add(lesson):
    if lesson not in list_of_lessons:
        list_of_lessons.append(lesson)


def insert(lesson, index):
    if lesson not in list_of_lessons:
        list_of_lessons.insert(index, lesson)


def remove(lesson):
    if lesson in list_of_lessons:
        list_of_lessons.remove(lesson)

    if f"{lesson}-Exercise" in list_of_lessons:
        list_of_lessons.remove(f"{lesson}-Exercise")


def swap(lesson1, lesson2):
    if lesson1 in list_of_lessons and lesson2 in list_of_lessons:
        lesson1_index = list_of_lessons.index(lesson1)
        lesson2_index = list_of_lessons.index(lesson2)
        list_of_lessons[lesson1_index], list_of_lessons[lesson2_index] = \
            list_of_lessons[lesson2_index], list_of_lessons[lesson1_index]
        if f"{lesson1}-Exercise" in list_of_lessons:
            list_of_lessons.remove(f"{lesson1}-Exercise")
            list_of_lessons.insert(lesson2_index + 1, f"{lesson1}-Exercise")
        if f"{lesson2}-Exercise" in list_of_lessons:
            list_of_lessons.remove(f"{lesson2}-Exercise")
            list_of_lessons.insert(lesson1_index + 1, f"{lesson2}-Exercise")


def exercise(lesson):
    if lesson in list_of_lessons:
        index = list_of_lessons.index(lesson)
        if f"{lesson}-Exercise" not in list_of_lessons:
            list_of_lessons.insert(index + 1, f"{lesson}-Exercise")
    else:
        list_of_lessons.append(lesson)
        list_of_lessons.append(f"{lesson}-Exercise")


list_of_lessons = input().split(', ')

while True:
    command = input()

    if command == "course start":
        break

    command_list = command.split(":")
    command_type = command_list[0]

    if command_type == "Add":
        command_type, lesson = command_list
        add(lesson)

    elif command_type == "Insert":
        command_type, lesson, index = command_list
        insert(lesson, int(index))

    elif command_type == "Remove":
        command_type, lesson = command_list
        remove(lesson)

    elif command_type == "Swap":
        command_type, lesson, lesson2 = command_list
        swap(lesson, lesson2)

    elif command_type == "Exercise":
        command_type, lesson = command_list
        exercise(lesson)


for i in range(1, len(list_of_lessons) + 1):
    print(f"{i}.{list_of_lessons[i-1]}")

