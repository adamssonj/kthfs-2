from data import Func

from plot import Plot

import matplotlib.animation as animation

import matplotlib.pyplot as plt


def main():
    fig = plt.figure()
    func = Func()
    t_list = func.readfile("data_file.txt")
    lamda_list = func.calc_lamda(t_list)
    h_list = func.function(lamda_list)
    N = len(t_list)
    object_list = func.objects(t_list, h_list)
    p = Plot(object_list)
    p.plot(object_list, N)
    animation.FuncAnimation(fig, p.plot, interval=1000)
    plt.show()


main()