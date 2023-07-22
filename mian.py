import linajia
import woaiwojia
import send_mail

if __name__ == '__main__':
    data_list = linajia.get_lianjia_data()

    data_list += woaiwojia.get_lianjia_data()
    print(data_list)
    mail_data = send_mail.get_html(data_list)
    send_mail.mail("xxxxxx@qq.com", mail_data)
