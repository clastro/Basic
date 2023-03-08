#allclose

np.allclose([1e10,1e-7], [1.00001e10,1e-8])
#False
np.allclose([1e10,1e-8], [1.00001e10,1e-9])
#True
np.allclose([1e10,1e-8], [1.0001e10,1e-9])
#False
np.allclose([1.0, np.nan], [1.0, np.nan])
#False
np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True)
#True
