import matplotlib.pyplot as plt

import matplotlib.animation as animation

from matplotlib import style

import matplotlib

matplotlib.use('MacOSX')

class Plot:
    def __init__(self, object_list):
        self.object_list=object_list

    def plot(self, object_list, N):
        style.use('fivethirtyeight')
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        x_values = []
        y_values = []
        for o in range(N):
            x_values.append(object_list[o].t_value)
            y_values.append(object_list[o].h_value)
        ax1.clear()
        ax1.plot(x_values, y_values)
