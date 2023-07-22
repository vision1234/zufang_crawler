#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import logging
import arrow

# 第三方 SMTP 服务

my_sender = 'xxxxxx@qq.com'  # 发件人邮箱账号
my_pass = "xxxxxxx"  # 口令
my_user = ['xxxxxx@qq.com']  # 收件人邮箱账号


def mail(u, datas):
    ret = True
    # for u in my_user:
    try:
        mes_str = datas
        msg = MIMEText(mes_str, _subtype="html", _charset='utf-8')
        msg['From'] = formataddr(["Vision", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["Vision", u])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "租房推送"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [u, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        logging.exception(e)
        ret = False
    return ret


def get_html(data_list):
    mail_module = ""
    items = ""
    with open("zufang.html", "r", encoding='utf-8') as f:
        mail_module = f.read()
    # print(mail_module)
    item_module = """
         <div class="listing-item">
                <div class="image-container">
                    <img src="{img_url}" alt="Property 1">
                </div>
                <div class="listing-details">
                    <h3><a href='{source_url}';>{title}</a></h3>
                    <p><span>价格：{price}     </span> 来源：{source}</p>
                </div>
            </div>
    """
    for row in data_list:
        item = item_module.format(img_url=row["img_url"], source_url=row["source_url"], title=row["title"],
                                  price=row["price"],
                                  source=row["source"])
        items += item
    # print(items)
    to_day = arrow.now().format("YYYY-MM-DD")
    mail_text = mail_module.replace("{items}", items).replace("{date}", to_day).replace("{num}", str(len(data_list)))
    return mail_text
