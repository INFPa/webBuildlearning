from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)

# 设置用于加密 session 的密钥，请使用随机生成的密钥
app.secret_key = os.urandom(24)

# 用户数据库（仅用于演示，实际应用中应使用数据库存储）
users = {
    "user1": "password1",
    "user2": "password2",
}

# 登录页面
@app.route('/')
def login():
    return render_template('login.html')

# 处理登录请求
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return "登录失败，请检查用户名和密码"

# 仪表盘页面（需要登录）
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return "欢迎，" + session['username'] + "！这里是您的仪表盘。"
    return redirect(url_for('login'))

# 注销
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
