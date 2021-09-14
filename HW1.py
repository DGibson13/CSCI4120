#David Gibson
#CSCI 4120

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd


#Hiding warnings because the loop uses a soon-to-be-deprecated behavior
#All the warning boxes made it very difficult to see the results in jupyter notebook
import warnings
warnings.filterwarnings('ignore')

def sliceTargets(irisArray):
    data=[]
    target=[]
    for x in range(len(irisArray)):
        data.append(irisArray[x, :4])
        target.append(irisArray[x, 4])
    return data, target

def main():
    url = 'https://raw.githubusercontent.com/ruiwu1990/CSCI_4120/master/KNN/iris.data'     
    scores={}
    scores_list=[]
    
    data=[]
    targets=[]
    df = pd.read_csv(url, header=None)
    rawdata = df.to_numpy()
    k_range = range(1,20)
    
    for k in k_range:
        #The 5x repetition is commented because I did not finish implementing it
        #for x in range(4):
            # prepare data
            data, targets = sliceTargets(rawdata)       
            X_train, X_test, y_train, y_test = train_test_split(data,targets,test_size=0.33)
        
            neighbors = KNeighborsClassifier(n_neighbors=k)        
            neighbors.fit(X_train, y_train)
            y_predict=neighbors.predict(X_test)
            scores[k] = metrics.accuracy_score(y_test,y_predict)
            scores_list.append(metrics.accuracy_score(y_test,y_predict))
        
    print(scores)
    
    plt.plot(k_range,scores_list)
    plt.xlabel('K value')
    plt.ylabel('Testing accuracy')
    
main()