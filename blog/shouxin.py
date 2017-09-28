#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from subprocess import check_output

receiver = '2220781951@qq.com'    # 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="2220781951@qq.com"#用户名
mail_pass="ziwgertpifrydjci"   #口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格
sender = mail_user
receivers = [receiver]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header(mail_user, 'utf-8')
message['To'] =  Header(str(receivers), 'utf-8')

subject = 'my test'
message['Subject'] = Header(subject, 'utf-8')

try:
   smtpObj = smtplib.SMTP_SSL(mail_host, 465)
   smtpObj.login(mail_user,mail_pass)
   smtpObj.sendmail(sender, receivers, message.as_string())
   smtpObj.quit()
   print ("邮件发送成功")
except smtplib.SMTPException as e:
   print (e)