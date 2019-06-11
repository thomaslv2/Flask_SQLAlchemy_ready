from flask import Blueprint, request, render_template

user = Blueprint("user", __name__)


@user.route("/login",methods=["POST","GET"])
def user_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # 进行数据库查询
        # select * from user where username="username" and password="password"
        # if 查询成功:
        # return "登录成功"
        # else:

        return "登陆失败"

    return render_template("login.html")
