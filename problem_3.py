import csv,math

def readcsv(filename):
    """
        Функция readcsv считывает данные из файла и возвращает два аргумента - header и content, заголовок и данные изх файла соответственно.

        Описание аргументов:
        filename - имя файла для чтения
    """
    with open(filename, encoding="UTF-8") as file:
        header = ""
        content = []
        for line in csv.reader(file):
            if header == "":
                header = line
                continue
            content.append(line)
        return header, content

def search(content, name):
    """
        Функция search линейно ищет корабль и выдаёт его последнее местоположение и расстояние до Земли.

        Описание аргументов:
        content - данные в виде листа в соответствующем условию порядке
        name - имя искомого корабля
    """
    ansq = None
    anscords = ""
    
    for line in content:
        if line[0] == name:
            dx, dy = list(map(int, line[2].split()))
            q = math.sqrt(dx**2 + dy**2)
            ansq = q
            anscords = line[2]
    if ansq == None:
        print("error.. er.. ror..")
        return
    print(f"Корабль {name} последний раз был на связи по координатам: {anscords}, что составляет: {ansq:.3f} космических единиц.")
    

def main():
    """
        Функция main считывает команду и запускает всю осталдьную программу.
    """
    _, content = readcsv("space.csv")
    while True:
        inp = input()
        if inp == "stop":
            exit()
        search(content, inp)
    

main()
