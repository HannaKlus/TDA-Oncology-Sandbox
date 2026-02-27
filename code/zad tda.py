import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams

N = 200
patient_A = np.random.randn(N,2)
t = np.linspace(0, 2*np.pi, N)
#Wspolrzedne punktow na okregu o promieniu R = 5
t = np.linspace(0, 2*np.pi, N)
szum_x = np.random.randn(N) * 0.3
szum_y = np.random.randn(N) * 0.3
x = 5 * np.cos(t) + szum_x
y = 5 * np.sin(t) + szum_y
patient_B = np.column_stack([x, y])

result_A = ripser(patient_A, maxdim=1)
result_B = ripser(patient_B, maxdim=1)

diagram_A = result_A['dgms']
diagram_B = result_B['dgms']

plt.figure(figsize=(12, 10))
plt.subplot(2, 2, 1)
plt.scatter(patient_A[:,0], patient_A[:,1], color='blue', alpha=0.6)
plt.title("Patient A: Raw Data (Noise)")
plt.axis('equal')


plt.subplot(2, 2, 2)
plt.scatter(patient_B[:,0], patient_B[:,1], color='red', alpha=0.6)
plt.title("Patient B: Raw Data (Relapse)")
plt.axis('equal')


plt.subplot(2, 2, 3)
plot_diagrams(diagram_A, show=False, title = 'Patient A: Barcode')
plt.subplot(2, 2, 4)
plot_diagrams(diagram_B, show=False, title = 'Patient B: Barcode')
plt.tight_layout()
plt.savefig('Patient_B_circle')
plt.show()
