"""邮件发送工程化骨架:双部分正文 + 配置化 + 失败隔离。
离线环境用本地调试 SMTP 演示: python -m smtpd -n -c DebuggingServer localhost:1025
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def build_message(from_addr, to_addrs, subject, text, html):
    msg = MIMEMultipart("alternative")  # 同一内容多格式, 客户端自选
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = ", ".join(to_addrs)
    msg.attach(MIMEText(text, "plain", "utf-8"))
    msg.attach(MIMEText(html, "html", "utf-8"))
    return msg


def send_alert(smtp_host="localhost", smtp_port=1025, use_tls=False,
               user=None, password=None, **kw):
    msg = build_message(
        "alert@mycorp.com", ["oncall@mycorp.com"],
        "[WARN] 磁盘使用率 92%",
        "磁盘使用率 92%, 请及时处理。",
        "<h3 style='color:orange'>磁盘使用率 92%</h3><p>主机 db-1, 请及时处理。</p>",
    )
    try:
        with smtplib.SMTP(smtp_host, smtp_port, timeout=10) as s:
            if use_tls:
                s.starttls()
            if user:
                s.login(user, password)  # 密码来自环境变量, 不硬编码
            s.send_message(msg)
        return True
    except (smtplib.SMTPException, OSError) as e:
        print("告警发送失败, 记录并稍后重试:", e)  # 失败不拖垮主流程
        return False


if __name__ == "__main__":
    ok = send_alert()  # 无本地 SMTP 时会走失败分支, 恰好演示失败隔离
    print("发送结果:", ok)
