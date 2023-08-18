from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

QnA = ['','']

@app.route('/')
def landing():
   return render_template('landing.html')  # landing.html을 렌더링

@app.route('/today')
def index():
   return render_template('index.html')  # index.html을 렌더링


@app.route('/today', methods=['POST']) # '/today' url에서 post 요청이 들어왔을 때
def answer():
   q = request.form.get('userQuestion')
   a = request.form.get('userAnswer')  # 폼에서 전달된 답변 가져오기
   QnA[0] = q
   QnA[1] = a
   print('QnA 저장완료:', QnA[0], QnA[1])
   #  return redirect(url_for('questions'))
   return a

@app.route('/questions')
def questions():
   print('question.html 출력 완료')
   # 화면에 유저 답변 출력
   return render_template('questions.html')  # questions.html을 렌더링

@app.route('/questions/today', methods=['GET']) # url을 분리해줘야 함!!!
def queList():
   today_question = QnA[0]
   today_answer = QnA[1]
   print('/questions/today GET 요청 완료: ', QnA[0], QnA[1])
   # return (f"{QnA[0]}", f"{QnA[1]}")   # 메시지 반환
   return f"{QnA[0]}\n{QnA[1]}"  # 개행 문자('\n')로 구분하여 하나의 문자열로 반환
   # return QnA[0], QnA[1]   # 메시지 반환

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)




