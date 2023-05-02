from flask import Flask, render_template,request


app =Flask(__name__)

#http://localhost:5000/ 입력하면 Hello Flack이 표시됨
@app.route('/')
def index():
    return 'Hello Flack'      # 함수적고 항상 return으로 끝내기

#http://localhost:5000/hello /뒤에는 주소
# "/calc" 주소로 접속하면 GET 방식일 경우 계산기 HTML 페이지를 반환하고
@app.route('/calc',methods=['GET','POST'])
def calc():
    if request.method == 'GET':
        op_list = ['+','-','*','/','//','%']
        return render_template('07.calc.html',op_list=op_list)
    else:
        num1 = int(request.values['num1'])
        op = request.values['op']
        num2 = int(request.values['num2'])
        result =eval(f'{num1}{op}{num2}')# 입력된 두 수와 연산자로 계산
        return render_template('07.calc_res.html', 
                               num1=num1,op=op,num2=num2,result=result)
# 계산 결과 HTML 페이지 렌더링
if __name__ == '__main__':
    app.run(debug=True)