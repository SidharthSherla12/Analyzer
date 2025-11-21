#Used AI to expand the dataset to 100 students
class Student:
    def __init__(self, connection, l_name=None, h_name=None, avg=None, low=None, high=None):
        self.connection = connection
        self.l_name = l_name
        self.h_name = h_name
        self.avg = avg
        self.low = low
        self.high = high

    def average_marks(self):
        mrk = list(map(int, self.connection.values()))
        self.avg = round(sum(mrk)/len(mrk), 2)
        return self.avg

    def highest_marks(self):
        self.high = max(self.connection.values())
        for i in self.connection.keys():
            if self.connection[i] == self.high:
                self.h_name = i
        return self.h_name, self.high

    def lowest_marks(self):
        self.low = min(self.connection.values())
        for i in self.connection.keys():
            if self.connection[i] == self.low:
                self.l_name = i
        return self.l_name, self.low

def output(self):
    average = self.average_marks()
    highest = self.highest_marks()
    lowest = self.lowest_marks()
    def print_summary():
        print(f"Average: {average}")
        print(f"Highest Score {highest[0]}({highest[1]})")
        print(f"Lowest Score {lowest[0]}({lowest[1]})")

    def write_to_file():
        new_file = open('output.txt', 'w')
        new_file.write(f"Average: {average}\nHighest Score {highest[0]}({highest[1]} )\nLowest Score {lowest[0]}({lowest[1]} )")
        new_file.close()

    print_summary()
    write_to_file()

#driver code
path = "students.txt"
f = open(path)
register = {}
for i in f:
    split_value = i.split(',')
    name, marks = split_value[0], split_value[1]
    register[name] = marks
f.close()

students = Student(register)
output(students)