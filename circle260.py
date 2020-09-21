L, R = map(int, input().split(' '))
alpha = L / R
import math
print("%.3f %.3f" % (R*math.cos(-alpha), R*math.sin(-alpha)))
print("%.3f %.3f" % (R*math.cos(alpha), R*math.sin(alpha)))