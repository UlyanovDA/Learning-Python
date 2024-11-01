# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, sep=','):
    first = first.split(sep)
    second = second.split(sep)
    spisok = []
    for i in first:
        for j in second:
            if i == j:
                spisok.append(i)
    spisok.sort()
    return spisok


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
a = find_common_participants(participants_first_group, participants_second_group, '|')
print(a)