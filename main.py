from multipledispatch import dispatch
from time import time
import matplotlib.pyplot as plt

class Student:
    def __init__(self, studentId, name):
        self.studentId = studentId
        self.name = name

class HashTable:
    def __init__(self, size = 20):
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def _hash(self, key):
        return hash(key) % self.size

    @dispatch(Student)
    def add(self, student):
        key = student.studentId
        value = student

        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    @dispatch(int, Student)
    def add(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])


    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(key)

def testHash():
    print("\nHash Table Function Check")
    ht1 = HashTable()
    print(ht1.table)
    s1 = Student(12344,"John Smith")
    s2 = Student(67890, "Jane Doe")
    s3 = Student(54321, "Alice Johnson")
    s4 = Student(98765, "Bob Williams")
    s5 = Student(24680, "Eve Brown")
    s6 = Student(13579, "Charlie Davis")
    s7 = Student(11223, "Grace Wilson")
    s8 = Student(44556, "David Lee")
    s9 = Student(99999, "Olivia Martinez")
    s10 = Student(77777, "Sophia Anderson")
    ht1.add(s1)
    ht1.add(s2)
    ht1.add(s3)
    ht1.add(s4)
    ht1.add(s5)
    ht1.add(s6)
    ht1.add(s7)
    ht1.add(s8)
    ht1.add(s9)
    ht1.add(s10)
    print(ht1.table)

    print(ht1.search(s9.studentId).name)
    ht1.remove(s9.studentId)
    print(ht1.table)

def testDict():
    print("\nDictionary Function Check")
    studentDict = {}
    print(studentDict)
    s1 = Student(12344,"John Smith")
    s2 = Student(67890, "Jane Doe")
    s3 = Student(54321, "Alice Johnson")
    s4 = Student(98765, "Bob Williams")
    s5 = Student(24680, "Eve Brown")
    s6 = Student(13579, "Charlie Davis")
    s7 = Student(11223, "Grace Wilson")
    s8 = Student(44556, "David Lee")
    s9 = Student(99999, "Olivia Martinez")
    s10 = Student(77777, "Sophia Anderson")

    studentDict[s1.studentId] = s1
    studentDict[s2.studentId] = s2
    studentDict[s3.studentId] = s3
    studentDict[s4.studentId] = s4
    studentDict[s5.studentId] = s5
    studentDict[s6.studentId] = s6
    studentDict[s7.studentId] = s7
    studentDict[s8.studentId] = s8
    studentDict[s9.studentId] = s9
    studentDict[s10.studentId] = s10

    print(studentDict)
    print(studentDict[s9.studentId].name)
    studentDict.pop(s9.studentId)
    print(studentDict)

def testPerformance():
    hash_table_times = {'insert': [], 'retrieve': []}
    dict_times = {'insert': [], 'retrieve': []}

    for n in range(1000):
        ht = HashTable(n)
        student_dict = {}

        students = [Student(i, f"Student {i}") for i in range(n)]

        # Performance test for hash table
        start_time = time()
        for student in students:
            ht.add(student.studentId, student)
        hash_table_times['insert'].append(time() - start_time)

        start_time = time()
        for student in students:
            ht.search(student.studentId)
        hash_table_times['retrieve'].append(time() - start_time)

        # Performance test for dictionary
        start_time = time()
        for student in students:
            student_dict[student.studentId] = student
        dict_times['insert'].append(time() - start_time)

        start_time = time()
        for student in students:
            student_dict[student.studentId]
        dict_times['retrieve'].append(time() - start_time)

    return hash_table_times, dict_times

def plot_performance(hash_table_times, dict_times):
    plt.plot(range(1, 1001), hash_table_times['insert'], label='Hash Table Insert')
    plt.plot(range(1, 1001), hash_table_times['retrieve'], label='Hash Table Retrieve')
    plt.plot(range(1, 1001), dict_times['insert'], label='Dictionary Insert')
    plt.plot(range(1, 1001), dict_times['retrieve'], label='Dictionary Retrieve')
    plt.xlabel('Number of Students')
    plt.ylabel('Time (s)')
    plt.title('Performance Comparison: Hash Table vs Dictionary')
    plt.legend()
    plt.show()

hash_table_times, dict_times = testPerformance()
plot_performance(hash_table_times, dict_times)

