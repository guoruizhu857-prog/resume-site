from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key-change-in-production")


# ──────────────────────────────────────────────
#  📄 简历数据 —— 修改这些内容即可更新网站
# ──────────────────────────────────────────────

RESUME_DATA = {
    # ===== 基本信息 =====
    "name": "朱国瑞",
    "title": "小猪",
    "tagline": "你好我的朋友",
    "email": "your.email@example.com",
    "phone": "+86 138-0000-0000",
    "location": "北京，中国",
    "avatar": None,  # 放头像图片到 static/img/，然后填文件名如 "avatar.jpg"
    "website": "https://your-website.com",
    "github": "https://github.com/yourname",
    "linkedin": "https://linkedin.com/in/yourname",

    # ===== 个人简介 =====
    "about": (
        "这里写一段关于你的介绍。说说你的背景、擅长什么、对什么感兴趣。"
        "可以写 2-3 句话，让人快速了解你。"
    ),

    # ===== 工作经历 =====
    "experience": [
        {
            "company": "公司名称",
            "position": "职位",
            "period": "2022.09 - 至今",
            "description": [
                "负责/参与的项目或主要职责 1",
                "负责/参与的项目或主要职责 2",
                "取得的成果，最好有数据支撑（如：提升了 30% 效率）",
            ],
        },
        {
            "company": "前一家公司",
            "position": "职位",
            "period": "2020.07 - 2022.08",
            "description": [
                "工作内容描述 1",
                "工作内容描述 2",
            ],
        },
    ],

    # ===== 教育背景 =====
    "education": [
        {
            "school": "大学名称",
            "degree": "专业 · 学位（本科/硕士/博士）",
            "period": "2016.09 - 2020.06",
            "note": "GPA / 荣誉 / 相关课程（可选）",
        },
    ],

    # ===== 技能 =====
    "skills": [
        {"category": "编程语言", "list": ["Python", "JavaScript", "Java", "SQL"]},
        {"category": "框架与工具", "list": ["Flask", "React", "Docker", "Git"]},
        {"category": "语言", "list": ["中文（母语）", "英语（CET-6）"]},
    ],

    # ===== 项目作品 =====
    "projects": [
        {
            "name": "项目名称 1",
            "description": "简要介绍这个项目是做什么的，用了什么技术，解决了什么问题。",
            "tech": ["Flask", "Bootstrap", "SQLite"],
            "link": "https://github.com/yourname/project1",
            "image": None,  # 放项目截图到 static/img/，如 "project1.png"
        },
        {
            "name": "项目名称 2",
            "description": "另一个项目的简介。可以是课程项目、开源贡献、或自己的 side project。",
            "tech": ["Python", "Pandas", "Matplotlib"],
            "link": "https://github.com/yourname/project2",
            "image": None,
        },
    ],
}


# ──────────────────────────────────────────────
#  🚀 路由
# ──────────────────────────────────────────────

@app.route("/")
def index():
    """首页：展示完整简历"""
    return render_template("index.html", data=RESUME_DATA)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """联系页面 / 处理表单提交"""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # 简单验证
        if not name or not email or not message:
            flash("请填写所有字段", "warning")
        elif "@" not in email:
            flash("请输入有效的邮箱地址", "warning")
        else:
            # 🖐 在这里加上你的处理逻辑，比如发送邮件或存入数据库
            # 目前只是打印到控制台
            print(f"\n📩 收到新消息：")
            print(f"   发件人：{name} <{email}>")
            print(f"   内容：{message}\n")
            flash("消息已发送成功，感谢你的联系！", "success")
            return redirect(url_for("index"))

    return render_template("contact.html", data=RESUME_DATA)


# ──────────────────────────────────────────────
#  🏁 启动
# ──────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True)
