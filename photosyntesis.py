import matplotlib.pyplot as plt
import math

p1 = float(input("Print p1 \n"))
p2 = float(input("Print p2 \n"))
p = float(input("Print p \n"))
a = float(input("Print alpha \n"))
E = 10**(-6)
a1 = 0.1
a2 = 0.1
b1 = 0.01
b2 = 0.002


def calculate_M(y):
    M = (0.1*p*E - p2*y)*(y-1)*(p2*y-p1)*a*(1-a)
    return M


def calculate_N(y):
    N = a*p2*y*(y-1)*(0.1*p*E*(p1*(a1+b1+1)-p2*y*(a1+1))-p2*y*(p1-p2*y))   # KMP
    N += (1-a)*p2*y*(p2*y-p1)*(0.1*p*E*(b2+a2+1-y) - p2*y*(a2+1-y))        # KMP
    return N


def calculate_Z(y):
    Z = 0.1*p*E*p2*y*y*(p1*(a1+b1+1) - p2*y*(a1+1))*(b2+a2+1-y) - (p2*y)**3*(a2+1-y)*(p1-p2*y)  # KMP
    return Z


result = []
result_2 = []
y = 0.0

while y < 0.99:
    M = calculate_M(y)
    N = calculate_N(y)
    Z = calculate_Z(y)
    if N*N-4*M*Z > 0:
        result.append((-N-math.sqrt(N*N-4*M*Z))/2/M)
        result_2.append(p2*y)
    y += 0.01

fig1 = plt.figure()
plt.scatter(result, result_2)
plt.xlabel("Irradiance")
plt.ylabel("Respiration rate")
text = "p1 = " + str(p1) + ", p2 = " + str(p2) + ", p = " + str(p) + ", alpha = " + str(a)
plt.title(text)
plt.grid()
plt.show()
