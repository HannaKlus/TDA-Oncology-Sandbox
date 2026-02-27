import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams

patient_A = 2 * np.random.randn(300,2)

ognisko_glowne = np.random.randn(200, 2)
wyspa_1 = np.random.randn(50,2)+[10, 10]
wyspa_2 = np.random.randn(50,2)+[-8, 12]
wyspa_3 = np.random.randn(50,2)+[12, -5]

patient_B = np.vstack([ognisko_glowne,wyspa_1, wyspa_2, wyspa_3])

result_A = ripser(patient_A, maxdim=1)
result_B = ripser(patient_B, maxdim=1)

diagram_A = result_A['dgms']
diagram_B = result_B['dgms']

plt.figure(figsize=(12,10))
plt.subplot(2,2,1)
plt.scatter(patient_A[:,0], patient_A[:,1], color='b')
plt.title('Patient A: raw data')
plt.xlim(-11, 11)
plt.ylim(-11, 11)
plt.subplot(2,2,2)
plt.scatter(patient_B[:,0], patient_B[:,1], color='r')
plt.title('Patient B: raw data')
plt.xlim(-14, 14)
plt.ylim(-14, 14)
plt.subplot(2,2,3)
plot_diagrams(diagram_A, show = False, title = 'Patient A: Barcode', xy_range=[-1, 11, -1, 11])
plt.subplot(2,2,4)
plot_diagrams(diagram_B, show = False, title = 'Patient B: Barcode', xy_range=[-1, 11, -1, 11])
plt.tight_layout()
plt.savefig('Patient_B_islands.png')
plt.show()