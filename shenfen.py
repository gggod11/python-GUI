from tkinter import *
import time,datetime

class A:
    def __init__(self):
        self.tk=Tk()
        self.tk.title('身份验证系统')
        self.tk.geometry('800x600')
        self.tk['bg']='light blue'

        #图片
        self.photo=PhotoImage(file='身份.png')
        self.label_1=Label(self.tk,image=self.photo)
        self.label_1.place(x=10,y=10)

        #请输入提示语
        self.label_2=Label(self.tk,text='请输入身份证号码:',font=('微软雅黑',20,'bold'),bg='navy',fg='light blue')
        self.label_2.place(x=350,y=10)

        #身份证号输入框和校验按钮
        self.entry_1=Entry(self.tk,font=('微软雅黑',20,'bold'),width=20)
        self.entry_1.place(x=350,y=60)
        self.button_1=Button(self.tk,text='校验',font=('微软雅黑',12,'bold'),fg='navy',width=8,command=self.jiaoyan)
        self.button_1.place(x=700,y=60)

        #是否有效显示
        self.label_3=Label(self.tk,text='是否有效:',bg='light blue',fg='navy',font=('微软雅黑',20,'bold'))
        self.label_3.place(x=350,y=180)
        self.result = StringVar()
        self.result.set('')
        self.entry_2=Entry(self.tk,font=('微软雅黑',20,'bold'),width=8,state=DISABLED,textvariable=self.result)
        self.entry_2.place(x=480,y=180)

        #性别显示
        self.label_4 = Label(self.tk, text='性别:', bg='light blue', fg='navy', font=('微软雅黑', 20, 'bold'))
        self.label_4.place(x=400, y=260)
        self.result2=StringVar()
        self.result2.set('')
        self.entry_3 = Entry(self.tk, font=('微软雅黑', 20, 'bold'), width=8,textvariable=self.result2,state=DISABLED)
        self.entry_3.place(x=480, y=260)

        #出生日期显示
        self.label_5 = Label(self.tk, text='出生日期:', bg='light blue', fg='navy', font=('微软雅黑', 20, 'bold'))
        self.label_5.place(x=350, y=340)
        self.result3=StringVar()
        self.result3.set('')
        self.entry_4 = Entry(self.tk, font=('微软雅黑', 20, 'bold'), width=16,textvariable=self.result3,state=DISABLED)
        self.entry_4.place(x=480, y=340)

        #所在地显示
        self.label_6 = Label(self.tk, text='所在地:', bg='light blue', fg='navy', font=('微软雅黑', 20, 'bold'))
        self.label_6.place(x=380, y=420)
        self.result4 = StringVar()
        self.result4.set('')
        self.entry_5 = Entry(self.tk, font=('微软雅黑', 20, 'bold'), width=16,textvariable=self.result4,state=DISABLED)
        self.entry_5.place(x=480, y=420)

        #关闭界面按钮
        self.button_2 = Button(self.tk, text='关闭', font=('微软雅黑', 12, 'bold'), fg='navy', width=8,command=self.close)
        self.button_2.place(x=700, y=550)

    #校验函数
    def jiaoyan(self):
        list1=['0','1','2','3','4','5','6','7','8','9','X']
        a=self.entry_1.get()

        try:
            end = a[-1]
            number = a[0:17]
            xishu_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            duiying_list = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
            jieguo_num = 0
            for index in range(len(number)):
                jieguo_num += int(number[index]) * int(xishu_list[index])
            yu_num = jieguo_num % 11
            end_num = duiying_list[yu_num]


            for i in a:
                year = a[6:10]
                month = a[10:12]
                day = a[12:14]
                sex = a[16:17]
                area = a[:6]
                if i in list1 and len(a) == 18 and end_num == end:

                    file = open('身份证归属地.txt',mode='r',encoding='utf-8')
                    text = file.readlines()
                    for i in text:
                        if area in i:
                            self.result4.set(i[8:])
                            break
                        continue
                    else:
                        year=0

                    statime = time.mktime(datetime.datetime(1970, 1, 1, 8, 00).timetuple())
                    nowtime = time.mktime(datetime.datetime(int(year), int(month), int(day)).timetuple())
                    endtime = time.time()
                    if statime <= nowtime <= endtime:
                        self.result.set('有效')
                        self.result3.set('%s-%s-%s'%(year,month,day))
                        if int(sex) % 2 == 0:
                            self.result2.set('女')
                        else:
                            self.result2.set('男')
                    else:
                        self.result.set('无效')
                        self.result2.set('')
                        self.result3.set('')
                        self.result4.set('')
                else:
                    self.result.set('无效')
                    self.result2.set('')
                    self.result3.set('')
                    self.result4.set('')
        except:
            self.result.set('无效')
            self.result2.set('')
            self.result3.set('')
            self.result4.set('')

    #关闭函数
    def close(self):
        self.tk.destroy()

    #运行函数
    def show(self):
        self.tk.mainloop()

if __name__ == '__main__':
    yasuo=A()
    yasuo.show()