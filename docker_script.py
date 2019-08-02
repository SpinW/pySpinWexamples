from pySpinW import Matlab

m = Matlab('/MATLAB/MATLAB_Runtime/v96/')

# Test calling a function
hkl = m.sw_qscan(([0, 0, 0], [1, 1, 0], 500))

# Test multiple returns
a, b = m.sw_mirror([0.1, 0, 0])
c = m.sw_mirror([0.1, 0, 0])
_, d = m.sw_mirror([0.1, 0, 0])

# Test call class
s = m.spinw()

# Print a method call with out arguments
print(s.abc())
# Function call with 2 types of argument
s.genlattice('lat_const', [3, 8, 8], 'angled', [90, 90, 90])
s.addatom('r', [0, 0, 0], label='MCu2')
s.plot()

# Test model generation
af = m.sw_model('squareAF', 1.)
# Do a calculation
spec = af.spinwave(([0, 0, 0], [1, 1, 0], 500))
print(spec)

# NOTE You can not set subfields manually for MatlabProxyObjects :-(

m.figure()
m.sw_plotspec(spec, nargout=0)
print('YaY NO cRAsh ;-)')
