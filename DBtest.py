import tkinter as tk
from tkinter import messagebox
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

# DB 연결 함수
def get_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', '1111'),  # ← 바꿔주세요
        db=os.getenv('DB_NAME', 'dino_game'),  # ← 바꿔주세요
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# 회원가입 처리
def register_user():
    username = entry_username.get()
    password = entry_password.get()
    if not username or not password:
        messagebox.showwarning("입력 오류", "아이디와 비밀번호를 입력하세요.")
        return
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(sql, (username, password))
        conn.commit()
        messagebox.showinfo("성공", "회원가입 성공!")
    except pymysql.err.IntegrityError:
        messagebox.showerror("오류", "이미 존재하는 사용자입니다.")
    finally:
        conn.close()

# 로그인 처리
def login_user():
    username = entry_username.get()
    password = entry_password.get()
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            if result:
                messagebox.showinfo("성공", f"{username}님, 로그인 성공!")
            else:
                messagebox.showerror("실패", "아이디 또는 비밀번호가 틀렸습니다.")
    finally:
        conn.close()

# GUI 생성
root = tk.Tk()
root.title("로그인 시스템")
root.geometry("300x200")

# UI 구성
tk.Label(root, text="아이디:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="비밀번호:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="로그인", command=login_user).pack(pady=5)
tk.Button(root, text="회원가입", command=register_user).pack()

root.mainloop()
