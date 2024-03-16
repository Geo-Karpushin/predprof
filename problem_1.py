import csv

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

def createreport(content):
    """
        Функция createreport создаёт отчёт согласно условиям задачи. Результат записывается в space_new.txt.

        Описание аргументов:
        content - данные в виде листа в соответствующем условию порядке
    """
    reportfile = open("space_new.txt", mode="w")
    for line in content:
        if line[2] == "0 0":
            dx, dy = list(map(int, line[3].split()))
            sx, sy = dx - len(line[1]), dy - len(line[1])
            reportfile.write(f"При получении данных о корабле {line[0]} возникли сбои. Предположительные координаты - {sx},{sy}.\n")
    

def main():
    """
        Функция main запускает всю осталдьную программу.
    """
    _, content = readcsv("space.csv")
    createreport(content)
    

main()
