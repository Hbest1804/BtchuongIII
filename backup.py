import os
import shutil
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

def send_email(sender, receiver, subject, body, password):
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
        server.quit()
        print(f"Email đã được gửi đến {receiver}")
    except Exception as e:
        print(f" Lỗi khi gửi email: {e}")

def job():
    try:
        db_folder = "."
        backup_folder = "bk"
        os.makedirs(backup_folder, exist_ok=True)

        backed_up_files = []

        for file_name in os.listdir(db_folder):
            if file_name.endswith(".sql") or file_name.endswith(".sqlite3"):    
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                src_path = os.path.join(db_folder, file_name)
                dst_filename = f"{file_name}_{timestamp}"
                dst_path = os.path.join(backup_folder, dst_filename)
                shutil.copy2(src_path, dst_path)
                backed_up_files.append(dst_filename)

        sender_email = os.getenv("SENDER_EMAIL")
        app_password = os.getenv("SENDER_PASSWORD")
        receiver_email = os.getenv("RECEIVER_EMAIL")

        subject = "✅ Backup database thành công"
        if backed_up_files:
            body = "Các file đã được backup:\n" + "\n".join(backed_up_files)
        else:
            body = "⚠️ Không tìm thấy file .sql hoặc .sqlite3 nào để backup."

        send_email(sender_email, receiver_email, subject, body, app_password)

    except Exception as e:
        sender_email = os.getenv("SENDER_EMAIL")
        app_password = os.getenv("SENDER_PASSWORD")
        receiver_email = os.getenv("RECEIVER_EMAIL")
        subject = "❌ Backup database thất bại"
        body = f"Lỗi xảy ra trong quá trình backup:\n{str(e)}"
        send_email(sender_email, receiver_email, subject, body, app_password)


schedule.every().day.at("20:21").do(job)

if __name__ == "__main__":
    print("⏳ Đang chạy lịch backup...")
    while True:
        schedule.run_pending()
        time.sleep(2)
