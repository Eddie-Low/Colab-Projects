import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

grades=np.array([[7.0,8.5],[5.0,6.0],[9.0,9.5],[3.0,4.0],[6.0,7.0],[2.0,3.5],[8.5,9.0],[4.5,5.0]])

results=np.array([1,1,1,0,1,0,1,0])  

frame=pd.DataFrame(grades,columns=["Exam1","Exam2"])
frame["Result"]=results

X=frame[["Exam1","Exam2"]]
y=frame["Result"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)            
model=DecisionTreeClassifier()                         
model.fit(X_train,y_train)

y_preview=model.predict(X_test)                       

accuracy=accuracy_score(y_test,y_preview)
print(accuracy)                                       


new_grades=pd.DataFrame({"Exam1":[7.0,9.0],"Exam2":[7.0,10]})
prediction=model.predict(new_grades)                  
print(new_grades.assign(Result=prediction))

