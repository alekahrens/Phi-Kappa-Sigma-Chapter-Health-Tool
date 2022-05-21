import tkinter
import mysql.connector
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import *
from PIL import ImageTk, Image
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def tightRope4():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT tightrope FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def pillarsNME4():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT usePillars FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def noShowCause4():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT noShowCause FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def membershipAgreement4():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT membershipAgreements FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def GCAttandence():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT GCAttendance FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def rosterMange4():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT roaster FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def greekAdvisor():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT greekAdvisorVerification FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def finGreekBill():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT greekBill FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def rosterMange3():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT roaster FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def malteCross():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT chapterBudget FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def budget3():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT chapterBudget FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def officerCompl3():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT MOHAttendance FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def MOHAttends():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT MOHAttendance FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def tightRope():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT tightrope FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]
def membershipAgreement1():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT membershipAgreements FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def rosterMange2():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT roaster FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def springRecruit():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT recruitmentPlan FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def IRS990():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT IRS990 FROM 2020to2021Foundation where chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def officerCompl():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
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
        passwd='PKSFall2021!*',  # "mypassword",
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
        passwd='PKSFall2021!*',  # "mypassword",
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
        passwd='PKSFall2021!*',  # "mypassword",
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
        passwd='PKSFall2021!*',  # "mypassword",
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
        passwd='PKSFall2021!*',  # "mypassword",
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
        passwd='PKSFall2021!*',  # "mypassword",
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
      passwd='PKSFall2021!*',  #"mypassword",
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

    passLn = Label(root, background='green', text='accepted task')
    passLn.place(x=20, y=5)

    failLn = Label(root, background='red', text='rejected task')
    failLn.place(x=100, y=5)

    waivedLn = Label(root, background='yellow', text='waived task')
    waivedLn.place(x=180, y=5)

    notSubmittedLn = Label(root, borderwidth=1,relief="solid",text='Task not Submitted')
    notSubmittedLn.place(x=250, y=5)

    back = Button(root, text="back", fg='blue', command=lambda: home(root))
    back.place(x=20, y=450)

    awards = Button(root, text="Qualifying Awards", fg='blue')
    awards.place(x=100, y=450)

    trends = Button(root, text="trends", fg='blue')
    trends.place(x=250, y=450)

    total =25
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
    else:
        chaptBylaw = Label(root, text='Chapter By-laws')
        chaptBylaw.place(x=20, y=50)

    resultAcademic = chaptAcademicProgram()
    if resultAcademic['academicProgram'] ==1:
        q1Count+=1
        academicProgram = Label(root, background='green',text='Academic Program')
        academicProgram.place(x=20, y=70)
    elif resultAcademic['academicProgram'] ==0:
        academicProgram = Label(root, background='red',text='Academic Program')
        academicProgram.place(x=20, y=70)
    else:
        academicProgram = Label(root, text='Academic Program')
        academicProgram.place(x=20, y=70)

    resultBudget = budget()
    if resultBudget['chapterBudget'] == 1:
        q1Count+=1
        chaptBudget = Label(root, background= 'green', text='Chapter Budget')
        chaptBudget.place(x=20, y=90)
    elif resultBudget['chapterBudget'] == 0:
        chaptBudget = Label(root, background='red', text='Chapter Budget')
        chaptBudget.place(x=20, y=90)
    else:
        chaptBudget = Label(root,text='Chapter Budget')
        chaptBudget.place(x=20, y=90)

    resultRecruitPlan = recruit()
    if resultRecruitPlan['recruitmentPlan'] == 1:
        q1Count+=1
        recruitPlan = Label(root, background='green', text='Recruitment Plan')
        recruitPlan.place(x=20, y=110)
    elif resultRecruitPlan['recruitmentPlan'] == 0:
        recruitPlan = Label(root, background='red', text='Recruitment Plan')
        recruitPlan.place(x=20, y=110)
    else:
        recruitPlan = Label(root, text='Recruitment Plan')
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
    else:
        rosterMange = Label(root, text='Roster Management')
        rosterMange.place(x=20, y=150)

    percentTotal = round(((q1Count/q1Total) * 100),2)
    q1Completed = Label(root, text='Quarter 1 Task Completed % - ' + str(percentTotal))
    q1Completed.place(x=20, y=170)
########################################################################################################################
    q2Label = Label(root, text='Quarter 2:')
    q2Label.place(x=20, y=200)

    q2Count = 0
    q2Total = 7

    resultOfficerCompl = officerCompl()
    if resultOfficerCompl == 1:
        q2Count+=1
        officerComplLB = Label(root,background='green',text='Officer Compliance')
        officerComplLB.place(x=20, y=220)
    elif resultOfficerCompl == 0:
        officerComplLB = Label(root, background='red', text='Officer Compliance')
        officerComplLB.place(x=20, y=220)
    else:
        officerComplLB = Label(root, text='Officer Compliance')
        officerComplLB.place(x=20, y=220)

    resultIRS = IRS990()
    if resultIRS['IRS990'] == 1:
        q2Count+=1
        IRS990form = Label(root, background='green',text='IRS 990')
        IRS990form.place(x=20, y=240)
    elif resultIRS['IRS990'] == 0:
        IRS990form = Label(root, background='red',text='IRS 990')
        IRS990form.place(x=20, y=240)
    else:
        IRS990form = Label(root, text='IRS 990')
        IRS990form.place(x=20, y=240)

    resultSpringRecruit = springRecruit()
    if resultSpringRecruit['recruitmentPlan'] == 1:
        q2Count+=1
        springRecruitPlan = Label(root, background='green',text='Spring Recruitment Plan')
        springRecruitPlan.place(x=20, y=260)
    elif resultSpringRecruit['recruitmentPlan'] == 0:
        springRecruitPlan = Label(root, background='red',text='Spring Recruitment Plan')
        springRecruitPlan.place(x=20, y=260)
    else:
        springRecruitPlan = Label(root, text='Spring Recruitment Plan')
        springRecruitPlan.place(x=20, y=260)

    resultRosterMange2 = rosterMange2()
    if resultRosterMange2['roaster'] == 1:
        q2Count+=1
        rosterMangeQ2 = Label(root, background='green', text='Roster Management')
        rosterMangeQ2.place(x=20, y=280)
    elif resultRosterMange2['roaster'] == 0:
        rosterMangeQ2 = Label(root, background='red', text='Roster Management')
        rosterMangeQ2.place(x=20, y=280)
    else:
        rosterMangeQ2 = Label(root, text='Roster Management')
        rosterMangeQ2.place(x=20, y=280)

    resultMembership = membershipAgreement1()
    if resultMembership['membershipAgreements'] == 1:
        q2Count+=1
        membershipAgreement = Label(root, background='green',text='Membership Agreement')
        membershipAgreement.place(x=20, y=300)
    elif resultMembership['membershipAgreements'] == 0:
        membershipAgreement = Label(root, background='red',text='Membership Agreement')
        membershipAgreement.place(x=20, y=300)
    else:
        membershipAgreement = Label(root, text='Membership Agreement')
        membershipAgreement.place(x=20, y=300)

    resultTightrope = tightRope()
    if resultTightrope['tightrope'] == 1:
        q2Count+=1
        tightropeCompletion = Label(root, background='green',text='Tightrope Completion(100%)')
        tightropeCompletion.place(x=20, y=320)
    elif resultTightrope['tightrope'] == 0:
        tightropeCompletion = Label(root, background='red',text='Tightrope Completion(100%)')
        tightropeCompletion.place(x=20, y=320)
    else:
        tightropeCompletion = Label(root, text='Tightrope Completion(100%)')
        tightropeCompletion.place(x=20, y=320)

    resultMOH = MOHAttends()
    if resultMOH['MOHAttendance'] == 1:
        q2Count+=1
        MOHAttend = Label(root, background='green',text='Men of Honor Attendance')
        MOHAttend.place(x=20, y=340)
    elif resultMOH['MOHAttendance'] == 0:
        MOHAttend = Label(root, background='red',text='Men of Honor Attendance')
        MOHAttend.place(x=20, y=340)
    else:
        MOHAttend = Label(root, text='Men of Honor Attendance')
        MOHAttend.place(x=20, y=340)

    percentTotal2 = round(((q2Count/q2Total) * 100),2)
    q2Completed = Label(root, text='Quarter 2 Task Completed % - '+ str(percentTotal2))#
    q2Completed.place(x=20, y=360)
########################################################################################################################
    q3Label = Label(root, text='Quarter 3:')
    q3Label.place(x=250, y=30)

    q3Count = 0
    q3Total = 4

    resultOfficerCompl3 = officerCompl3()
    if resultOfficerCompl3 == 1:
        q3Count+=1
        officerComplLBQ3 = Label(root, background='green',text='Officer Compliance')
        officerComplLBQ3.place(x=250, y=50)
    elif resultOfficerCompl3 == 0:
        officerComplLBQ3 = Label(root, background='red',text='Officer Compliance')
        officerComplLBQ3.place(x=250, y=50)
    else:
        officerComplLBQ3 = Label(root, text='Officer Compliance')
        officerComplLBQ3.place(x=250, y=50)

    resultBudget3 = budget3()
    if resultBudget3['chapterBudget'] == 1:
        q3Count+=1
        chaptBudgetQ3 = Label(root,background='green',text='Chapter Budget')
        chaptBudgetQ3.place(x=250, y=70)
    elif resultBudget3['chapterBudget'] == 0:
        chaptBudgetQ3 = Label(root,background='red',text='Chapter Budget')
        chaptBudgetQ3.place(x=250, y=70)
    else:
        chaptBudgetQ3 = Label(root, text='Chapter Budget')
        chaptBudgetQ3.place(x=250, y=70)

    resultMalteCross = malteCross()
    if resultMalteCross == 1:
        q3Count+=1
        malteseCrossReport = Label(root,background='green',text='Maltese Cross Report')
        malteseCrossReport.place(x=250, y=90)
    elif resultMalteCross == 0:
        malteseCrossReport = Label(root,background='red',text='Maltese Cross Report')
        malteseCrossReport.place(x=250, y=90)
    else:
        malteseCrossReport = Label(root, text='Maltese Cross Report')
        malteseCrossReport.place(x=250, y=90)

    resultRosterMange3 = rosterMange3()
    if resultRosterMange3['roaster'] == 1:
        q3Count+=1
        rosterMangeQ3 = Label(root,background='green',text='Roster Management')
        rosterMangeQ3.place(x=250, y=110)
    elif resultRosterMange3['roaster'] == 0:
        rosterMangeQ3 = Label(root, background='red',text='Roster Management')
        rosterMangeQ3.place(x=250, y=110)
    else:
        rosterMangeQ3 = Label(root, text='Roster Management')
        rosterMangeQ3.place(x=250, y=110)

    percentTotal3 = round(((q3Count/q3Total) * 100),2)
    q3Completed = Label(root, text='Quarter 3 Task Completed % - '+ str(percentTotal3))#
    q3Completed.place(x=250, y=130)
########################################################################################################################
    q4Label = Label(root, text='Quarter 4:')
    q4Label.place(x=250, y=200)

    q4Count = 0
    q4Total = 8

    resultGreekBill = finGreekBill()
    if resultGreekBill['greekBill'] == 1:
        q4Count+=1
        fincialManageVerif = Label(root,background='green',text='Financial Management Verification')
        fincialManageVerif.place(x=250, y=220)
    elif resultGreekBill['greekBill'] == 0:
        fincialManageVerif = Label(root, background='red',text='Financial Management Verification')
        fincialManageVerif.place(x=250, y=220)
    else:
        fincialManageVerif = Label(root, text='Financial Management Verification')
        fincialManageVerif.place(x=250, y=220)

    resultGreekAdvisor = greekAdvisor()
    if resultGreekAdvisor['greekAdvisorVerification'] == 1:
        q4Count+=1
        greekAdvicorVerif = Label(root, background='green',text='Greek Advisor Verification')
        greekAdvicorVerif.place(x=250, y=240)
    elif resultGreekAdvisor['greekAdvisorVerification'] == 0:
        greekAdvicorVerif = Label(root, background='red',text='Greek Advisor Verification')
        greekAdvicorVerif.place(x=250, y=240)
    else:
        greekAdvicorVerif = Label(root, text='Greek Advisor Verification')
        greekAdvicorVerif.place(x=250, y=240)

    resultRosterMange4 = rosterMange4()
    if resultRosterMange4['roaster'] == 1:
        q4Count+=1
        rosterMangeQ4 = Label(root, background='green',text='Roster Management')
        rosterMangeQ4.place(x=250, y=260)
    elif resultRosterMange4['roaster'] == 0:
        rosterMangeQ4 = Label(root, background='red',text='Roster Management')
        rosterMangeQ4.place(x=250, y=260)
    else:
        rosterMangeQ4 = Label(root, text='Roster Management')
        rosterMangeQ4.place(x=250, y=260)

    resultGCAttand = GCAttandence()
    if resultGCAttand['GCAttendance'] == 1:
        q4Count+=1
        GCAttand = Label(root, background='green',text='Grand Chapter Attendance/OSI')
        GCAttand.place(x=250, y=280)
    elif resultGCAttand['GCAttendance'] == 0:
        GCAttand = Label(root, background='red',text='Grand Chapter Attendance/OSI')
        GCAttand.place(x=250, y=280)
    else:
        GCAttand = Label(root, text='Grand Chapter Attendance/OSI')
        GCAttand.place(x=250, y=280)

    resultMembershipQ4 = membershipAgreement4()
    if resultMembershipQ4['membershipAgreements'] == 1:
        q4Count+=1
        membershipAgreementQ4 = Label(root, background='green',text='Membership Agreement')
        membershipAgreementQ4.place(x=250, y=300)
    elif resultMembershipQ4['membershipAgreements'] == 0:
        membershipAgreementQ4 = Label(root, background='red',text='Membership Agreement')
        membershipAgreementQ4.place(x=250, y=300)
    else:
        membershipAgreementQ4 = Label(root, text='Membership Agreement')
        membershipAgreementQ4.place(x=250, y=300)

    resultNoShow = noShowCause4()
    if resultNoShow['noShowCause'] == 1:
        q4Count+=1
        noShowCause = Label(root, background='green',text='No Show Cause')
        noShowCause.place(x=250, y=320)
    elif resultNoShow['noShowCause'] == 0:
        noShowCause = Label(root, background='red',text='No Show Cause')
        noShowCause.place(x=250, y=320)
    else:
        noShowCause = Label(root, text='No Show Cause')
        noShowCause.place(x=250, y=320)

    resultPillars = pillarsNME4()
    if resultPillars['usePillars'] == 1:
        q4Count+=1
        pillarsNME = Label(root, background='green',text='Pillars New Member Education')
        pillarsNME.place(x=250, y=340)
    elif resultPillars['usePillars'] == 0:
        pillarsNME = Label(root, background='red',text='Pillars New Member Education')
        pillarsNME.place(x=250, y=340)
    else:
        pillarsNME = Label(root,text='Pillars New Member Education')
        pillarsNME.place(x=250, y=340)


    resultTightrope4 = tightRope4()
    if resultTightrope4['tightrope'] == 1:
        q4Count+=1
        tightropeCompletionQ4 = Label(root, background='green',text='Tightrope Completion(100%)')
        tightropeCompletionQ4.place(x=250, y=360)
    elif resultTightrope4['tightrope'] == 0:
        tightropeCompletionQ4 = Label(root, background='red', text='Tightrope Completion(100%)')
        tightropeCompletionQ4.place(x=250, y=360)
    else:
        tightropeCompletionQ4 = Label(root, text='Tightrope Completion(100%)')
        tightropeCompletionQ4.place(x=250, y=360)

    percentTotal4 = round(((q4Count/q4Total) * 100),2)
    q4Completed = Label(root, text='Quarter 4 Task Completed % - ' + str(percentTotal4))#
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

    if overallScore >= 80.00:

def home(root):
    clear_frame()
    frameHome = Frame(root, height=350)
    frameHome.pack(side=TOP, fill=X)
    root.geometry('500x350')
    root.title('Phi Kappa Sigma MCS/Chapter Health')

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

