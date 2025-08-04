import pandas as pd
from google.colab import files
import numpy as np
import matplotlib.pyplot as plt

data={"Student":["Anna","Bruno","Carlos","Diego","Eddie"],"Grade":[8.3,5.3,7.5,10,9.8]}

frame=pd.DataFrame(data)
display(frame)

average=frame["Grade"].mean()
max=frame["Grade"].max()
min=frame["Grade"].min()
stu_max=frame.loc[frame["Grade"].idxmax(),"Student"]
stu_min=frame.loc[frame["Grade"].idxmin(),"Student"]
print(f'The Average is {round(average,2)}')
print(f'The Student with the Highest Grade is {stu_max} and their grade is {max}')
print(f'The Student with the Lowest Grade is {stu_min} and their grade is {min}')

average=np.average(frame["Grade"])
max=np.max(frame["Grade"])
min=np.min(frame["Grade"])
print(f'The Average is {round(average,2)}')
print(f'The Highest Grade is {max}')
print(f'The Lowest Grade is {min}')