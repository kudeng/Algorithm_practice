from math import log2
import pandas

def f(n, total):
    return -(n/total)*log2(n/total)

def entropy(l):
    total = sum(l)
    s = 0
    for i in l:
        s += f(i, total)
    return s

def values(data):
    d = {}
    for i in data:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    print(list(d.values()))
    return list(d.values())


file = 'ml-bugs.csv'
max_ig = 0
data = pandas.read_csv(file)
total_entropy = entropy(values(data['Species']))
# print(f'total:{total_entropy}')
brown = data.loc[data['Color'] == 'Brown', 'Species']
nobrown = data.loc[data['Color'] != 'Brown', 'Species']
# print(brown)
# print(values(brown))
brown_entropy = entropy(values(brown))
nobrown_entropy = entropy(values(nobrown))
# print(brown_entropy)
ig_brown = total_entropy - (brown_entropy+nobrown_entropy)/2
print(f'brown ig:{ig_brown}')

blue = data.loc[data['Color'] == 'Blue', 'Species']
noblue = data.loc[data['Color'] != 'Blue', 'Species']
blue_entropy = entropy(values(blue))
noblue_entropy = entropy(values(noblue))
ig_blue = total_entropy - (blue_entropy+noblue_entropy)/2
print(f'blue ig:{ig_blue}')

green = data.loc[data['Color'] == 'Green', 'Species']
nogreen = data.loc[data['Color'] != 'Green', 'Species']
green_entropy = entropy(values(green))
nogreen_entropy = entropy(values(nogreen))
ig_green = total_entropy - (green_entropy+nogreen_entropy)/2
print(f'green ig:{ig_green}')

len17 = data.loc[data['Length (mm)'] < 17, 'Species']
nolen17 = data.loc[data['Length (mm)'] >= 17, 'Species']
len17_entropy = entropy(values(len17))
nolen17_entropy = entropy(values(nolen17))
ig_len17 = total_entropy - (len17_entropy+nolen17_entropy)/2
print(f'len17 ig:{ig_len17}')

len20 = data.loc[data['Length (mm)'] < 20, 'Species']
nolen20 = data.loc[data['Length (mm)'] >= 20, 'Species']
len20_entropy = entropy(values(len20))
nolen20_entropy = entropy(values(nolen20))
ig_len20 = total_entropy - (len20_entropy+nolen20_entropy)/2
print(f'len20 ig:{ig_len20}')