# zufang_crawler

## 步骤：

### 1、修改send_mail.py发件人邮箱和授权码，授权码可以从邮箱运营商网站获取

```python
my_sender = 'xxxxxx@qq.com'  # 发件人邮箱账号
my_pass = "xxxxxxx"  # 口令
```

### 2、昵称改不改都可以

```python
msg['From'] = formataddr(["666", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
msg['To'] = formataddr(["666", u])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
```



### 3、修改main.py的收件人邮箱

```python
send_mail.mail("xxxxxx@qq.com", mail_data)
```



### 4、在命令行安装python库

```shell
pip install -r requirements.txt
```

### 5、运行main.py

```python
python mian.py
```