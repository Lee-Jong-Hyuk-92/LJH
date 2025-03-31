import numpy as np # 수학계산
from sklearn.manifold import TSNE # t-SNE(시각화 알고리즘)
from sklearn.datasets import load_wine # 와인데이터 로드
import matplotlib.pyplot as plt # 그림그리기


"""
1. 데이터를 불러오고, 
   2개의 변수만을 가질 수 있도록 고정하여 
   반환하는 함수를 구현합니다.
   
   [실습4]에서 구현한 함수를 그대로 사용할 수 있습니다. 
"""
def load_data():
    wine = load_wine()
    X, y = wine.data, wine.target
    
    column_start = 6
    X = X[:, column_start : column_start+2] # 와인 데이터에서 전체행, 6 ~8열 만 사용
    print(X.shape)
    return X
    
"""
2. t-SNE를 활용하여 
   2차원 데이터를 1차원으로 축소하는 함수를 완성합니다.
"""
def tsne_data(X):
    
    tsne = TSNE(n_components=1) # 1차원으로
    
    X_tsne = tsne.fit_transform(X)
    
    return tsne, X_tsne

def main():
    
    X = load_data()
    
    tsne, X_tsne = tsne_data(X)
    
    print("- original shape:   ", X.shape)
    print("- transformed shape:", X_tsne.shape)
    
    print("\n원본 데이터 X :\n", X[:5])
    print("\n차원 축소 이후 데이터 X_tsne\n",X_tsne[:5])
    
    
if __name__ == '__main__':
    main()
