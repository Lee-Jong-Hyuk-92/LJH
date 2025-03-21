from sklearn import svm
from sklearn.metrics import accuracy_score

def train_model(x_mat, y_vec):
    
    # <ToDo>: scikit-learn을 활용해서 모델을 생성하고, x_mat, y_vec으로 모델을 학습시킵니다.
    model = svm.SVC(kernel='linear')
    trained_model = model.fit(x_mat, y_vec)
    
    return trained_model

def evaluate_model(model, x_mat, y_vec):
    
    y_pred = model.predict(x_mat)
    mean_acc = accuracy_score(y_vec, y_pred)
    
    return mean_acc