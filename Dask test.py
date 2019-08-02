from dask.distributed import Client
from dask.distributed import wait
import numpy as np

client = Client(processes=False)

from pySpinW import Matlab, Hamiltonian
m = Matlab('/MATLAB/MATLAB_Runtime/v96/')
m.daskArrays = True


npts = 10000
chunks = np.ceil(npts/24)

s = m.sw_model('squareAF', 1.)
ham = s.genHam(([0, 0, 0], [1, 1, 0], npts))

thisHam = Hamiltonian(client, ham, chunks=chunks)
# f1 = thisHam.cholesky_gu(thisHam.ham)
# res = ham.compute()
thisHam.hermitSolve()
a, b = thisHam.compute()

wait(b)
print(b)
#
# result = client.gather(a)
print('Yay')

