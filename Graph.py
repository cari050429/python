#defines a function that plots a mathematical function specified by the user, over a given domain, using a specified number of points.

import numpy as np
import math
import matplotlib.pyplot as plt

def plot_function(fun_str, domain, ns):
    ys = []
    xs = np.arange(domain[0], domain[1], (domain[1] - domain[0]) / (ns - 1))

    for x in xs:
        y = eval(fun_str)
        ys.append(y)

    plt.plot(xs, ys)
    plt.scatter(xs, ys)
    plt.title("{}".format(fun_str))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot()
    plt.xlim(domain[0], domain[1])

    print("{:>10s}    {:>10s}\n------------------------".format("x", "y"))
    for i in range(ns):
        print("{:>10.4f}    {:10.4f}".format(xs[i], ys[i]))

user_string = str(input("Input a mathematical string: "))
user_domain1 = float(input("Enter a min x: "))
user_domain2 = float(input("Enter a max x: "))
user_domain = user_domain1, user_domain2
user_int = int(input("Enter an integer: "))
plot_function(user_string, user_domain, user_int)
