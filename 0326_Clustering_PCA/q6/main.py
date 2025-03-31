import preprocess as pre
import model as md
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def silhouette_calculator(X, cluster):
    
    # 군집화 결과에 대한 silhouette score를 계산합니다.
    # <TODO> dictionary 형태에서 value들을 추출해서 리스트 형태로 변환해 줍니다.
    silhouette = silhouette_score(X, list(cluster.values()))
    
    return silhouette

# <TODO> 여러분이 답으로 제출하고 싶은 군집의 개수로 your_choice 함수의 '?' 부분에 넣은 후 제출하세요.
def your_choice(X):
    return md.KMeans(K=3).fit(X)  # 원하는 군집 수로 설정

def main():
    X = pre.load_data()
    
    # 군집 모델 학습
    Kmeans = your_choice(X)
    
    # silhouette score 계산
    silhouette = silhouette_calculator(X, Kmeans.labels)
    
    # 결과 출력
    print('K = {}, silhouette 값: {}'.format(Kmeans.K, silhouette))

if __name__ == "__main__":
    main()