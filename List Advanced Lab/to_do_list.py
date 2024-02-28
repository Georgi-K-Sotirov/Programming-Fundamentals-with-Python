def to_do_list():
    to_do_task = []

    while True:
        task = input()

        if task == "End":
            break

        to_do_task.append(task)

    sorted_notes = sorted(to_do_task, key=lambda x: int(x.split('-')[0]))
    sorted_notes = [note.split('-')[1] for note in sorted_notes]

    return sorted_notes


result = to_do_list()
print(result)