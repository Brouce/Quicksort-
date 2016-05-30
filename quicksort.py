import numpy as np

def quicksort(lyst):
    finalarray=np.array([])
    aray=np.array(lyst)
    divider=aray[0]
    leftarray=np.array([])
    rightarray=np.array([])
    for i in aray:
        if i>=divider:
            rightarray=np.append(rightarray,i)
        else:
             leftarray=np.append(leftarray,i)
    
    for i in range(0,len(leftarray)):
        leftspot=0
        rightspot=1
        for i in leftarray:
            i2=leftarray[rightspot]
            if i>i2:
                np.put(leftarray,rightspot,i)
                np.put(leftarray,leftspot,i2)
                leftspot=leftspot+1
                rightspot=rightspot+1
                print(leftarray)
                if rightspot==len(leftarray):
                    break
            else:
                leftspot=leftspot+1
                rightspot=rightspot+1
                if rightspot==len(leftarray):
                    break
    
    
    for j in range(0,len(rightarray)):
        lefty=0
        righty=1
        for j in rightarray:
            j2=rightarray[righty]
            if j>j2:
                np.put(rightarray,righty,j)
                np.put(rightarray,lefty,j2)
                lefty=lefty+1
                righty=righty+1
                print(rightarray)
                if righty==len(rightarray):
                    break
            else:
                lefty=lefty+1
                righty=righty+1
                if righty==len(rightarray):
                    break
    finalarray=np.append(finalarray,leftarray)
    finalarray=np.append(finalarray,rightarray)
    return(finalarray)
    
    
    
                    
                
        
    
            