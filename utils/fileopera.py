#!/usr/bin/python
# -*- coding: UTF-8 -*-

#author:ZHOGNQI
'''multiprocessing模块的使用'''
# from multiprocessing import Process
# import os
# def run_proc(name):
#     print('run child process %s (%s)..'%(name,os.getpid()))
# if __name__=='__main__':
#     print('Parent process %s'%(os.getpid()))
#     p= Process(target=run_proc,args=('test',))
#     print('child process will start ')
#     p.start()
#     p.join()
#     print('child process end')


'''pool进程池实例'''
# from multiprocessing import Pool
# import os,time,random
#
# def long_time_task(name):
#     print('run task %s (%s)..'%(name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds'%(name,(end-start)))
#
# if __name__ =='__main__':
#     print('parent process %s'%os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('waiting for all subprocess done..')
#     p.close()
#     p.join()
#     print('all subprocess done')
'''子进程'''
# import subprocess
# print('$ nslookup www.python.org')
# r=subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

'''进程间通信'''
# from multiprocessing import Process ,Queue
# import os, time,random
#
# #写数据进程执行的代码
# def write(q):
#     print('process to write :%s'%os.getpid())
#     for value in ['A','B','C']:
#         print('put %s to queue..'%value)
#         q.put(value)
#         time.sleep(random.random())
#
# #读数据进程执行的代码
# def read(q):
#     print('process to read :%s'%os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue'%value)
#
# if __name__ == '__main__':
#     # 父进程创建Queue,并传给各个子进程
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#     #启动子进程pw,写入
#     pw.start()
#     #启动子进程pr,读取
#     pr.start()
#     #等待pw结束
#     pw.join()
#     #pr进程里是死循环，无法等待其结束，只能强行终止
#     pr.terminate()


'''线程'''
# import time,threading
#
# # 新线程执行的代码
# def loop():
#     print('thread %s is running ..'%threading.current_thread().name)
#     n=0
#     while n<5:
#         n=n+1
#         print('thread %s >>>%s'%(threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended'% threading.current_thread().name)
#
# print('thread %s is running..'% threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended'%threading.current_thread().name)


'''lock'''
# import time,threading
# #假定这是你的银行存款
# balance=0
# lock=threading.Lock()
# def change_it(n):
#     #先存后取，结果应该为0
#     global balance
#     balance = balance+n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         #先要获取锁
#         lock.acquire()
#         try:
#             #放心地改吧
#             change_it(n)
#         finally:
#             #用完释放锁
#             lock.release()
#
# t1=threading.Thread(target=run_thread,args=(5,))
# t2=threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


'''ThreadLocal'''
# import threading
# local_school = threading.local()
# def process_student():
#     #获取当前线程关联的student：
#     std = local_school.student
#     print('hello,%s(in %s)'%(std,threading.current_thread().name))
#
# def process_thread(name):
#     local_school.student = name
#     process_student()
#
# t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
# t2=threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

'''分布式进程'''
# task_master.py
# import random,time,queue
# from multiprocessing.managers import BaseManager
#
# #发送任务的队列
# task_queue = queue.Queue()
# #接收结果的队列
# result_queue = queue.Queue()
#
# #从BaseManager继承的QueueManager
# class QueueManager(BaseManager):
#     pass
# #把两个Queue都注册到网络上，callable参数关联了Queue对象
# QueueManager.register('get')

'''偏函数例子'''
# from functools import partial
# import tkinter
#
# root = tkinter.Tk()
# MyButton = partial(tkinter.Button,root,fg='white',bg='blue')
# b1 = MyButton(text='Button1')
# b2 = MyButton(text='Button2')
# qb = MyButton(text='QUIT',bg='red',command=root.quit)
# b1.pack()
# b2.pack()
# qb.pack(fill=tkinter.X,expand=True)
# root.title('PFAs')
# root.mainloop()


'''变量作用域和名称空间'''
j,k = 1,2
def procl():
    j,k = 3,4
    print('j==%d and k==%d'%(j,k))
    k=5
def proc2():
    j = 6
    procl()
    print('j==%d and k== %d'%(j,k))
k=7
procl()
print('j==%d and k==%d'%(j,k))
j=8
proc2()
print('j==%d and k==%d'%(j,k))





# import os
# from io import StringIO
#
#
# def data_dir(data=None,fileName=None):
#     '''查找文件的路径'''
#     return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,fileName)
#
# with open(data_dir('data','testfile.txt'),'r', encoding='utf-8') as f:
#     print(f.readlines() )
#
# with open(data_dir('data','testfile.txt'),'a') as f:
#     print(f.write('\nthank you'))

'''测试练习题1'''
# sum=0
# while True:
#     i=int(input('请输入：'))
#     while i:
#         sum+=i
#         print(sum)
#         break
'''测试练习题2'''
# m=1
# while m:
#     i=int(input('请输入1到100之间的一个数：'))
#     if i>1 and i<100:
#         print('ok')
#         m=0


'''测试练习3:'''
#
# while True:
#     i=input('请选择：1 表示取5个数的和；2 表示取5个数的平均值；3 退出程序:''\r\n')
#     if i=='1':
#
#         list1=[1,2,3,4,5]
#         sum =0
#         for item in list1:
#             sum+=item
#         print(sum)
#     elif i=='2':
#         list1=[1,2,3,4,5]
#         sum = 0
#         for item in list1:
#             sum+=item
#         avg=float(sum/len(list1) )
#         print(avg)
#     elif i=='3':
#         break
#     else:
#         print('输入类型错误，请重新输入')

'''练习4——从大到小排序'''




