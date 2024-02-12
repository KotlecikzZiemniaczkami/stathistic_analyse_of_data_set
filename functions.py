from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math
from scipy.stats import norm, t

def del_ret(lista):
    buf = []
    for i in lista:
        if i not in buf:
            buf.append(i)
        else:
            continue
    return buf


def histogram(arlist, tekst):
    field = del_ret(arlist).sort()
    number = min(arlist)
    '''for i in range(200):
                number += 0.01
                field.append(number)'''
    plt.style.use('fivethirtyeight')
    plt.title(tekst)
    plt.xlabel('poszczególne wartości')
    plt.ylabel('liczba wystąpień')
    plt.hist(arlist, bins=field, edgecolor='black')
    plt.xticks(field, rotation=45, ha='right')

    plt.show()

# mean (srednia)
def avg(data):
    mean = 0
    for i in data:
        mean += i
    mean = mean / len(data)
    return mean

# median (mediana)
def median(data):
    data.sort()
    if len(data) % 2 == 0:
        return (data[len(data) // 2] + data[(len(data) // 2) - 1]) / 2
    else:
        return data[(len(data) - 1) // 2]

# moda
def mode_without_pandas(data):
    counter = {}
    for i in data:
        if i in counter.keys():
            counter[i] += 1
        else:
            counter[i] = 0
    maximum = max(counter.keys())
    mVal = ''
    maxi = 0
    for i in counter.keys():
        if counter[i] > maxi and counter[i] != maximum and counter[i] != 1:
            maxi = counter[i]
            mVal = i
    if mVal == '':
        return np.nan
    return mVal

# rozstep proby
def sample_range(data):
    return max(data) - min(data)

# wariancja
def variance(data):
    divider = 1/len(data)
    mean = avg(data)
    vrnc = 0
    for i in range(len(data)):
        vrnc += (data[i] - mean)*(data[i] - mean)
    vrnc *= divider
    return vrnc

# odchylenie standardowe
def standard_deviation(data):
    return math.sqrt(variance(data))

# function to generate quartiles (kwartyle)
def quartile(data, high: bool = False):
    data.sort()
    ind = len(data) // 2
    if len(data) % 2 == 1:
        ind = ind + 1
    if high:
        return median(data[ind:])
    return median(data[:ind])

# rozstep miedzykwartylowy
def interquartile_range(data):
    return quartile(data, True) - quartile(data)

# preparing for nice showing the data (position indicators/wskazniki polozenia)
def position_indicators(list, name):
    quest_of_position_indicators = pd.DataFrame()
    quest_of_position_indicators['measure'] = ['mean', 'median', 'moda']
    quest_of_position_indicators[name] = [avg(list),
                                          median(list),
                                          mode_without_pandas(list)]
    quest_of_position_indicators.set_index('measure', inplace=True)
    return quest_of_position_indicators

# preparing for nice showing the data (dispersion rates/wskazniki rozproszenia(skali))
def dispersion_rates(list, name):
    quest_of_position_indicators = pd.DataFrame()
    quest_of_position_indicators['measure'] = ['sample range', 'variance', 'standard deviation', 'higher quartile',
                                               'lower quartile', 'interquartile range']
    quest_of_position_indicators[name] = [sample_range(list),
                                          variance(list),
                                          standard_deviation(list),
                                          quartile(list, True),
                                          quartile(list),
                                          interquartile_range(list)]
    quest_of_position_indicators.set_index('measure', inplace=True)
    return quest_of_position_indicators

# H0 : μ1 = x, H1 : μ1 != x
def test(data, dataset_num: int):
    print('enter the average value which correctness you want to check for dataset number ' + str(dataset_num))
    test_average_value = float(input())
    Z = ((avg(data) - test_average_value)/standard_deviation(data))*math.sqrt(len(data))
    # making calculations easier
    if Z < 0:
        Z *= -1
    print('enter accuracy level for the test:')
    significance = float(input())
    # reading with which what test_average_value will be compared in critical area (we just build a critical area)
    Za = norm.ppf(1 - (significance/2))

    # checking if we can reject the hypothesis
    if Z > Za:
        print('We can reject given hypothesis')
    else:
        print('With given level of significance we can\'t reject this hypothesis')

# H0 : μ1 − μ2 = 0
def test3(data1, data2):
    print('give an accuracy level:')
    significance = float(input())
    first_devider = variance(data1)/len(data1)
    second_devider = variance(data2)/len(data2)
    T = (avg(data1) - avg(data2))/math.sqrt(first_devider + second_devider)
    if T < 0:
        T *= -1
    # stopnie swobody
    v = ((first_devider + second_devider)**2)/(((first_devider**2)/(len(data1)-1)) + ((second_devider**2)/(len(data2)-1)))
    Ta = t.ppf(1-significance, v)
    if T > Ta:
        print('We can reject given hypothesis that u1 and u2 are equal')
    else:
        print('We can\'t reject given hypothesis that u1 and u2 are equal')