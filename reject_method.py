import numpy as np
import matplotlib.pyplot as plt


#on essaye de simuler une suite iid de loi X de desité f(x)

#par la méthode de rejet on prend:
#   une loi qu'on sait simuler (Uniforme de densité g(x)) 
#   et un m réel tel que f(x) <= m*g(x) pour tout x

#on definira r(x) = f(x)/(m*g(x)) et le temps d'arrêt definit comme le minimum n >= 1 tel que U_n <= r(Y_n)

#Par la méthode de rejet, on a que cet temps d'arrêt suit une loi géométrique de paramètre 1/m et donc E[T] = m

#densité f(x) de la loi cible
def f(x):
    return 3/4 *(1-x**2)*np.abs((x<=1) & (x>=-1))

#intervalle de l'uniforme que on prend selon le support de f
a, b = -1, 1



#choix de m
m = 3/2

#fonction r(x)
def r(x, a, b):
    return f(x)/(m*(1/(b-a)))

#simulation d'un échantillon de taille n de la loi cible
def simulate_reject(n):
    samples = []
    for i in range(n):
        N = False
        while not N:
            #generate U_i avec densité g
            Y_i = np.random.uniform(a, b)

            #we see the value of r at U_i
            r_i = r(Y_i, a, b)
            U_i = np.random.uniform(0, 1)

            if U_i <= r_i:
                samples.append(Y_i)
                N = True
            #if not we repeat
    return np.array(samples), len(samples)/n  #return also the average number of iterations per sample

#drawing the samples
n = 10000
samples, avg_iterations = simulate_reject(n)

#draw a point cloud of the samples
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')
#draw the target density for comparison
x = np.linspace(-2, 2, 100)
plt.plot(x, f(x), 'r', lw=2)
plt.title(f'Simulation by Rejection Method (avg iterations per sample: {avg_iterations:.2f})')
plt.xlabel('x')
plt.ylabel('Density')
plt.show()





