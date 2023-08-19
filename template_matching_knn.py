import cv2
import pandas as pd
import numpy as np

def KNN(imgTrain, testImg,label, k=5):
    result = np.array([], float)
    num= np.zeros(10)
    for i in range(len(imgTrain)):
        result = np.append(result, cv2.matchTemplate(imgTrain[i], testImg, cv2.TM_SQDIFF_NORMED))
    max = np.argsort(result)
    labelSubset = label[max[0:k]]
    print(labelSubset)
    for i in range(k):
        num[labelSubset[i]] = (num[labelSubset[i]])+1
    num = np.argmax(num)
    return num

# df = pd.read_csv('train.csv')
# y = df['label'].to_numpy('int')
# df = df.drop('label', axis=1)

#Code to save the images from the dataset above:
# for i in range(200):
#     img = imgTrain.iloc[i,:].to_numpy(dtype='double')
#     img = img.reshape(28,28)
#     img = cv2.resize(img, (150,150))
#     cv2.imwrite(f'{i}.jpg',img)

images=[]
for i in range(200):
    images.append(cv2.imread(f'{i}.jpg',0))

testImg = cv2.imread('test/9.jpg',0)
num = KNN(images,testImg,y,5)
print(num)

cv2.waitKey(0)
cv2.destroyAllWindows()
