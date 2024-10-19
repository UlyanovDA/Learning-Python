# TODO Найдите количество книг, которое можно разместить на дискете

disk = 1.44
page = 100
strok = 50
symbol = 25
mem_1book = 4 * symbol * strok * page / 1024**2

count = int(disk // mem_1book)

print("Количество книг, помещающихся на дискету:", count)
