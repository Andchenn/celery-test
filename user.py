from tasks import send_mail


def register():
    import time
    start = time.time()
    print("1.插入记录到数据库")
    print("2.celery 帮我发邮件")
    send_mail.delay("xx@gmail.com")
    print("3.告诉用户注册成功")
    print("耗时：%s秒" % (time.time() - start))


if __name__ == '__main__':
    register()
