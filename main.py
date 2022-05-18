import tkinter
import mysql.connector
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import *
from PIL import ImageTk, Image
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def officerCompl():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='mypassword',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT roaster FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]


def rosterManagement():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='mypassword',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT roaster FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]



def fallUpdate():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='mypassword',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT recruitmentPlan FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def recruit():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='mypassword',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT recruitmentPlan FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def budget():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='mypassword',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT chapterBudget FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def chaptAcademicProgram():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='mypassword',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT academicProgram FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]


def chapBylaws():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='mypassword',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT bylaws FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]


def selectionChapters():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd='mypassword',  #"mypassword",
      auth_plugin='mysql_native_password',
      database="pks_chapter_data",
    )


    mycursor = mydb.cursor()
    mycursor.execute("SELECT chapter FROM 2020to2021Foundation")
    myresults = mycursor.fetchall()

    return myresults


def chapterDetails(root):
    global selectedChapter
    selectedChapter = cb.get()
    clear_frame()
    root.geometry('1000x500')
    root.title('Details on ' + selectedChapter+ ' Chapter')

    back = Button(root, text="back", fg='blue', command=lambda: home(root))
    back.place(x=20, y=450)

    awards = Button(root, text="Qualifying Awards", fg='blue')
    awards.place(x=100, y=450)

    trends = Button(root, text="trends", fg='blue')
    trends.place(x=250, y=450)

    total =0
########################################################################################################################
    q1Label = Label(root, text='Quarter 1:')
    q1Label.place(x=20, y=30)

    q1Count = 0
    q1Total = 6

    resultBylaws = chapBylaws()
    if resultBylaws['bylaws'] == 1:
        q1Count+= 1
        chaptBylaw = Label(root, background= 'green', text='Chapter By-laws')
        chaptBylaw.place(x=20, y=50)
    elif resultBylaws['bylaws'] == 0:
        chaptBylaw = Label(root, background= 'red', text='Chapter By-laws')
        chaptBylaw.place(x=20, y=50)

    resultAcademic = chaptAcademicProgram()
    if resultAcademic['academicProgram'] ==1:
        q1Count+=1
        academicProgram = Label(root, background='green',text='Academic Program')
        academicProgram.place(x=20, y=70)
    elif resultAcademic['academicProgram'] ==0:
        academicProgram = Label(root, background='red',text='Academic Program')
        academicProgram.place(x=20, y=70)

    resultBudget = budget()
    if resultBudget['chapterBudget'] == 1:
        q1Count+=1
        chaptBudget = Label(root, background= 'green', text='Chapter Budget')
        chaptBudget.place(x=20, y=90)
    elif resultBudget['chapterBudget'] == 0:
        chaptBudget = Label(root, background='red', text='Chapter Budget')
        chaptBudget.place(x=20, y=90)

    resultRecruitPlan = recruit()
    if resultRecruitPlan['recruitmentPlan'] == 1:
        q1Count+=1
        recruitPlan = Label(root, background='green', text='Recruitment Plan')
        recruitPlan.place(x=20, y=110)
    elif resultRecruitPlan['recruitmentPlan'] == 0:
        recruitPlan = Label(root, background='red', text='Recruitment Plan')
        recruitPlan.place(x=20, y=110)

    #resultFallChapUpdate = fallUpdate()
    fallChapUpdate = Label(root, text='Fall Chapter Updates')
    fallChapUpdate.place(x=20, y=130)

    resultRosterMange = rosterManagement()
    if resultRosterMange['roaster'] == 1:
        q1Count+=1
        rosterMange = Label(root, background='green', text='Roster Management')
        rosterMange.place(x=20, y=150)
    elif resultRosterMange['roaster'] == 0:
        rosterMange = Label(root, background='red', text='Roster Management')
        rosterMange.place(x=20, y=150)

    percentTotal = round(((q1Count/q1Total) * 100),2)
    q1Completed = Label(root, text='Quarter 1 Task Completed % - ' + str(percentTotal))
    q1Completed.place(x=20, y=170)
########################################################################################################################
    q2Label = Label(root, text='Quarter 2:')
    q2Label.place(x=20, y=200)

    q2Count = 0
    q2Total = 7

    #resultOfficerCompl = officerCompl()
    officerComplLB = Label(root,text='Officer Compliance')
    officerComplLB.place(x=20, y=220)

    IRS990form = Label(root, text='IRS 990')
    IRS990form.place(x=20, y=240)

    springRecruitPlan = Label(root, text='Spring Recruitment Plan')
    springRecruitPlan.place(x=20, y=260)

    rosterMangeQ2 = Label(root, text='Roster Management')
    rosterMangeQ2.place(x=20, y=280)

    membershipAgreement = Label(root, text='Membership Agreement')
    membershipAgreement.place(x=20, y=300)

    tightropeCompletion = Label(root, text='Tightrope Completion(100%)')
    tightropeCompletion.place(x=20, y=320)

    MOHAttend = Label(root, text='Men of Honor Attendance')
    MOHAttend.place(x=20, y=340)

    percentTotal2 = round(((q2Count/q2Total) * 100),2)
    q2Completed = Label(root, text='Quarter 2 Task Completed % - ')# + str(percentTotal2)
    q2Completed.place(x=20, y=360)
########################################################################################################################
    q3Label = Label(root, text='Quarter 3:')
    q3Label.place(x=250, y=30)

    q3Count = 0
    q3Total = 4

    officerComplLBQ3 = Label(root, text='Officer Compliance')
    officerComplLBQ3.place(x=250, y=50)

    chaptBudgetQ3 = Label(root,text='Chapter Budget')
    chaptBudgetQ3.place(x=250, y=70)

    malteseCrossReport = Label(root,text='Maltese Cross Report')
    malteseCrossReport.place(x=250, y=90)

    rosterMangeQ3 = Label(root,text='Roster Management')
    rosterMangeQ3.place(x=250, y=110)

    percentTotal3 = round(((q1Count/q1Total) * 100),2)
    q3Completed = Label(root, text='Quarter 3 Task Completed % - ')#+ str(percentTotal)
    q3Completed.place(x=250, y=130)
########################################################################################################################
    q4Label = Label(root, text='Quarter 4:')
    q4Label.place(x=250, y=200)

    q4Count = 0
    q4Total = 8

    #resultOfficerCompl = officerCompl()
    fincialManageVerif = Label(root,text='Financial Management Verification')
    fincialManageVerif.place(x=250, y=220)

    greekAdvicorVerif = Label(root, text='Greek Advisor Verification')
    greekAdvicorVerif.place(x=250, y=240)

    rosterMangeQ4 = Label(root, text='Roster Management')
    rosterMangeQ4.place(x=250, y=260)

    GCAttand = Label(root, text='Grand Chapter Attendance/OSI')
    GCAttand.place(x=250, y=280)

    membershipAgreementQ4 = Label(root, text='Membership Agreement')
    membershipAgreementQ4.place(x=250, y=300)

    noShowCause = Label(root, text='No Show Cause')
    noShowCause.place(x=250, y=320)

    pillarsNME = Label(root, text='Pillars New Member Education')
    pillarsNME.place(x=250, y=340)

    tightropeCompletionQ4 = Label(root, text='Tightrope Completion(100%)')
    tightropeCompletionQ4.place(x=250, y=360)

    percentTotal4 = round(((q2Count/q2Total) * 100),2)
    q4Completed = Label(root, text='Quarter 4 Task Completed % - ')# + str(percentTotal2)
    q4Completed.place(x=250,y=380)
########################################################################################################################
    data1 = {'Quarters': ['Q1','Q2', 'Q3','Q4'],
             'Sores': [percentTotal, percentTotal2, percentTotal3, percentTotal4]}
    df1 = DataFrame(data1,columns=['Quarter', 'Scores'])
    figure1 = plt.Figure(figsize=(6,5), dpi=75)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
    df1 = df1[['Quarter','Scores']].groupby('Quarter').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Quarters vs MCS Scores')
########################################################################################################################
    countTotal = q1Count+q2Count+q3Count+q4Count
    overallScore = round(((countTotal/total)*100),2)

    #if overallScore >= 80.00:

def home(root):
    clear_frame()
    frameHome = Frame(root, height=350)
    frameHome.pack(side=TOP, fill=X)
    root.geometry('500x350')
    root.title('Phi Kappa Sigma MSC/Chapter Health')

    bio = Label(text='Created by Alek Ahrens of the Beta Chi Chapter Fall 2020')
    bio.place(x=100,y=320)

    openImg = Image.open("../PKS_Chapter_Health_Tool/PKS.png")
    importImg = ImageTk.PhotoImage(openImg)
    img = tkinter.Label(image=importImg)
    img.image = importImg
    img.place(x=175, y=0)

    chapters=selectionChapters()
    global cb
    cb = Combobox(root, values=chapters, width=30, state='readonly')
    cb.place(x=150, y=200)

    submit = Button(root, text="Submit", fg='blue', command=lambda:chapterDetails(root))
    submit.place(x=225, y=250)


def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False,False)
    home(root)
    root.mainloop()

