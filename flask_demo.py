from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <h1>我是首页</h1>
        <a href="/lnk">跳一跳</a>
        <br/>
        <a href="/test">跳一跳test</a>
    '''


@app.route('/lnk')
def lnk():
    return '我是链接过来的另一个页面'


@app.route('/test')
def test():
    args_q = request.args.get('q', '')
    if args_q == "a":
        return "一个神奇的网站 AAA"
    elif args_q == "b":
        return "一个垃圾网站 BBBB"
    else:
        return "JUST TEST PATH"



# def test(hello="hhh"):
    # print("test function")

# if __name__ == '__main__':
test(hello="world")
app.run()
    # app.run(debug=True, port=7788)
