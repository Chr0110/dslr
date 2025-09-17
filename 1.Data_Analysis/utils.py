import math

def mean(value):
    return sum(value) / len(value)

def std(value):
    its_mean = mean(value)
    diffs = [(x - its_mean) ** 2 for x in value]
    return math.sqrt(sum(diffs) / len(value))

def to_int(value):
    if value.strip() == '':
        return 0
    return float(value)

def minimum(value):
    min_value = value[0]
    for i in value:
        if i < min_value:
            min_value = i
    return min_value

def maximum(value):
    max_value = value[0]
    for i in value:
        if i > max_value:
            max_value = i
    return max_value

def twenty_five(value):
    per = int(len(value) * 0.25)
    return value[per]

def fifty(value):
    per = int(len(value) * 0.50)
    return value[per]

def seventy_five(value):
    per = int(len(value) * 0.75)
    return value[per]
