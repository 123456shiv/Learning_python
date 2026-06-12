import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Marks": [60, 70, 80, 90, 100]
})

print(data)

data.plot()
plt.show()