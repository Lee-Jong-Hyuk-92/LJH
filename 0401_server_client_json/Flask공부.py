from flask import Flask

app = Flask(__name__) # app이라는 플라스크 객체 생성, 플라스크 앱 만들고

@app.route('/') # 라우팅 만들고
def home():
    return "홈페이지입니다"
# 127.0.0.1:5000/ 여기로 들어가면 home함수 작동

@app.route('/hello')
def say_hello():
    return "안녕하세요!"
# 127.0.0.1:5000/hello 여기로 들어가면 say_hello함수 작동

@app.route('/bye')
def say_bye():
    return "잘가요!"
# 127.0.0.1:5000/bye 여기로 들어가면 say_bye함수 작동

@app.route('/predict', methods=['POST'])
def predict():
    ...
# 127.0.0.1/predict에 접속하면 predict함수 실행, post방식만 가능 
'''
GET	데이터를 가져올 때	검색, 조회
POST	데이터를 보낼 때	로그인, 회원가입, 예측 요청
PUT	기존 데이터를 수정할 때	게시글 수정
PATCH	일부만 수정할 때	이름만 바꾸기
DELETE	데이터를 삭제할 때	게시글 삭제
OPTIONS	가능한 메서드를 물어볼 때	서버 허용 요청 확인 (CORS 등)
'''
if __name__ == '__main__': # main이면 실행시켜켜
    app.run()