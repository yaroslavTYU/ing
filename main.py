def read_from_file(filename):
    with open(filename, "r", ) as file:
        columns  = tuple(file.readline().split(","))
        data = []
        for line in file:
            line = line.split(",")
            data.append((int(line[0]),line[1],line[2], int(line[3]),int(line[4]),int(line[5])))
    return columns, data #считывать базы данных

def write_to_file(filename):
    with open(filename, "w") as file:
        file.write(",".join(columns)+"\n")
        for line in data:
            line  = [str(i) for i in line]
            file.write(",".join(line)+"\n")
def del_to_file(filename, id):
    for i in
columns = ("id","name",'lastname','age','height','weight')
data = [
    (1,"l","l",1,1,10),
    (2, "a", "a", 2, 1, 10),
    (3, "b", "b", 5, 23, 44)
]# создание базы данных

write_to_file("csv")
read_from_file("csv")
