from pySpinW import Matlab
from pySpinW.swPlotter import winPlotter

m = Matlab(mlPath='/MATLAB/MATLAB_Runtime/v96')

af = m.sw_model('squareAF', 1.)

plt = winPlotter(af)
plt.add_lattice()
plt.add_atoms()
plt.plot()