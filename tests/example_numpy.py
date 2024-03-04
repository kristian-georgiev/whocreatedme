import numpy as np
import whocreatedme as wcme
wcme.trace(numpy=True)

np.save("./test.npy", np.random.randn(50, 50))
