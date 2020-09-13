import math

class Data:
    def __init__(self, t_value, h_value=0):
        self.t_value = t_value
        self.h_value = h_value


class Func:
    def __init__(self):
        pass

    def readfile(self, filename):
        t_list = []
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                t_list = line.split(',')
        return t_list

    def calc_lamda(self, t_list):
        lamda_list = []
        for t in t_list:
            lamda = 5 * math.sin(2 * math.pi * 1 * float(t))
            lamda_list.append(lamda)
        return lamda_list

    def function(self, lamda_list):
        h_list=[]
        for l in lamda_list:
            h = 3 * math.pi * math.exp(-float(l))
            h_list.append(h)
        return h_list

    def objects(self, t_list, h_list):
        object_list = []
        for i in range(len(t_list)):
            obj = Data(t_list[i], h_list[i])
            object_list.append(obj)
        return object_list
