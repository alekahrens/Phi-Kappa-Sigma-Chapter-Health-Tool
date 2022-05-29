import tkinter
from tkinter import filedialog
import databaseSearch as search
import mysql.connector
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

global newDatabase
global selectedChapter


def chapterDetails(root):
    selectedChapter = cb.get()
    clear_frame()
    root.geometry('1000x500')
    root.title('Details on ' + selectedChapter+ ' Chapter')

    global foundationalFlag

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

    awards = Button(root, text="Chapter Excellence", fg='blue', command=lambda: mscAwards(root, foundationalFlag, selectedChapter))
    awards.place(x=100, y=450)

    trends = Button(root, text="trends", fg='blue')
    trends.place(x=250, y=450)

    total =25
########################################################################################################################
    q1Label = Label(root, text='Quarter 1:')
    q1Label.place(x=20, y=30)

    q1Count = 0
    q1Total = 6

    resultBylaws = search.chapBylaws(selectedChapter)
    if resultBylaws['Chapter_Bylaws'] == 1:
        q1Count+= 1
        chaptBylaw = Label(root, background= 'green', text='Chapter By-laws')
        chaptBylaw.place(x=20, y=50)
    elif resultBylaws['Chapter_Bylaws'] == 0:
        chaptBylaw = Label(root, background= 'red', text='Chapter By-laws')
        chaptBylaw.place(x=20, y=50)
    elif resultBylaws['Chapter_Bylaws'] == None:
        q1Count+=1
        chaptBylaw = Label(root, background='yellow', text='Chapter By-laws')
        chaptBylaw.place(x=20, y=50)
    else:
        chaptBylaw = Label(root, text='Chapter By-laws')
        chaptBylaw.place(x=20, y=50)

    resultAcademic = search.chaptAcademicProgram(selectedChapter)
    if resultAcademic['Academic_Program'] ==1:
        q1Count+=1
        academicProgram = Label(root, background='green',text='Academic Program')
        academicProgram.place(x=20, y=70)
    elif resultAcademic['Academic_Program'] ==0:
        academicProgram = Label(root, background='red',text='Academic Program')
        academicProgram.place(x=20, y=70)
    elif resultAcademic['Academic_Program'] == None:
        q1Count+=1
        academicProgram = Label(root, background='yellow', text='Academic Program')
        academicProgram.place(x=20, y=70)
    else:
        academicProgram = Label(root, text='Academic Program')
        academicProgram.place(x=20, y=70)

    resultBudget = search.budget(selectedChapter)
    if resultBudget['Chapter_Budget'] == 1:
        q1Count+=1
        chaptBudget = Label(root, background= 'green', text='Chapter Budget')
        chaptBudget.place(x=20, y=90)
    elif resultBudget['Chapter_Budget'] == 0:
        chaptBudget = Label(root, background='red', text='Chapter Budget')
        chaptBudget.place(x=20, y=90)
    elif resultBudget['Chapter_Budget'] == None:
        q1Count+=1
        chaptBudget = Label(root, background='yellow', text='Chapter Budget')
        chaptBudget.place(x=20, y=90)
    else:
        chaptBudget = Label(root,text='Chapter Budget')
        chaptBudget.place(x=20, y=90)

    resultRecruitPlan = search.recruit(selectedChapter)
    if resultRecruitPlan['Recruitment_Plan'] == 1:
        q1Count+=1
        recruitPlan = Label(root, background='green', text='Recruitment Plan')
        recruitPlan.place(x=20, y=110)
    elif resultRecruitPlan['Recruitment_Plan'] == 0:
        recruitPlan = Label(root, background='red', text='Recruitment Plan')
        recruitPlan.place(x=20, y=110)
    elif resultRecruitPlan['Recruitment_Plan'] == None:
        q1Count+=1
        recruitPlan = Label(root, background='red', text='Recruitment Plan')
        recruitPlan.place(x=20, y=110)
    else:
        recruitPlan = Label(root, text='Recruitment Plan')
        recruitPlan.place(x=20, y=110)

    resultFallChapUpdate = search.fallUpdate(selectedChapter)
    if resultFallChapUpdate['Fall_Updates'] == 1:
        fallChapUpdate = Label(root, background='green',text='Fall Chapter Updates')
        fallChapUpdate.place(x=20, y=130)
    elif resultFallChapUpdate['Fall_Updates'] == 0:
        fallChapUpdate = Label(root, background='red',text='Fall Chapter Updates')
        fallChapUpdate.place(x=20, y=130)
    elif resultFallChapUpdate['Fall_Updates'] == None:
        fallChapUpdate = Label(root, background='yellow',text='Fall Chapter Updates')
        fallChapUpdate.place(x=20, y=130)
    else:
        fallChapUpdate = Label(root, text='Fall Chapter Updates')
        fallChapUpdate.place(x=20, y=130)

    resultRosterMange = search.rosterManagement(selectedChapter)
    if resultRosterMange['Roster'] == 1:
        q1Count+=1
        rosterMange = Label(root, background='green', text='Roster Management')
        rosterMange.place(x=20, y=150)
    elif resultRosterMange['Roster'] == 0:
        rosterMange = Label(root, background='red', text='Roster Management')
        rosterMange.place(x=20, y=150)
    elif resultRosterMange['Roster'] == None:
        q1Count+=1
        rosterMange = Label(root, background='yellow', text='Roster Management')
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

    resultOfficerCompl = search.officerCompl(selectedChapter)
    if resultOfficerCompl['Officer_Training_Or_Transition'] == 1:
        q2Count+=1
        officerComplLB = Label(root,background='green',text='Officer Compliance')
        officerComplLB.place(x=20, y=220)
    elif resultOfficerCompl['Officer_Training_Or_Transition'] == 0:
        officerComplLB = Label(root, background='red', text='Officer Compliance')
        officerComplLB.place(x=20, y=220)
    elif resultOfficerCompl['Officer_Training_Or_Transition'] == None:
        officerComplLB = Label(root, background='yellow', text='Officer Compliance')
        officerComplLB.place(x=20, y=220)
    else:
        officerComplLB = Label(root, text='Officer Compliance')
        officerComplLB.place(x=20, y=220)

    resultIRS = search.IRS990(selectedChapter)
    if resultIRS['IRS_990'] == 1:
        q2Count+=1
        IRS990form = Label(root, background='green',text='IRS 990')
        IRS990form.place(x=20, y=240)
    elif resultIRS['IRS_990'] == 0:
        IRS990form = Label(root, background='red',text='IRS 990')
        IRS990form.place(x=20, y=240)
    elif resultIRS['IRS_990'] == None:
        q2Count+=1
        IRS990form = Label(root, background='yellow', text='IRS 990')
        IRS990form.place(x=20, y=240)
    else:
        IRS990form = Label(root, text='IRS 990')
        IRS990form.place(x=20, y=240)

    resultSpringRecruit = search.springRecruit(selectedChapter)
    if resultSpringRecruit['Recruitment_Plan'] == 1:
        q2Count+=1
        springRecruitPlan = Label(root, background='green',text='Spring Recruitment Plan')
        springRecruitPlan.place(x=20, y=260)
    elif resultSpringRecruit['Recruitment_Plan'] == 0:
        springRecruitPlan = Label(root, background='red',text='Spring Recruitment Plan')
        springRecruitPlan.place(x=20, y=260)
    elif resultSpringRecruit['Recruitment_Plan'] == None:
        q2Count+=1
        springRecruitPlan = Label(root, background='yellow', text='Spring Recruitment Plan')
        springRecruitPlan.place(x=20, y=260)
    else:
        springRecruitPlan = Label(root, text='Spring Recruitment Plan')
        springRecruitPlan.place(x=20, y=260)

    resultRosterMange2 = search.rosterMange2(selectedChapter)
    if resultRosterMange2['Roster'] == 1:
        q2Count+=1
        rosterMangeQ2 = Label(root, background='green', text='Roster Management')
        rosterMangeQ2.place(x=20, y=280)
    elif resultRosterMange2['Roster'] == 0:
        rosterMangeQ2 = Label(root, background='red', text='Roster Management')
        rosterMangeQ2.place(x=20, y=280)
    elif resultRosterMange2['Roster'] == None:
        q2Count+=1
        rosterMangeQ2 = Label(root, background='yellow', text='Roster Management')
        rosterMangeQ2.place(x=20, y=280)
    else:
        rosterMangeQ2 = Label(root, text='Roster Management')
        rosterMangeQ2.place(x=20, y=280)

    resultMembership = search.membershipAgreement1(selectedChapter)
    if resultMembership['Membership_Agreements_100'] == 1:
        q2Count+=1
        membershipAgreement = Label(root, background='green',text='Membership Agreement')
        membershipAgreement.place(x=20, y=300)
    elif resultMembership['Membership_Agreements_100'] == 0:
        membershipAgreement = Label(root, background='red',text='Membership Agreement')
        membershipAgreement.place(x=20, y=300)
    elif resultMembership['Membership_Agreements_100'] == None:
        q2Count+=1
        membershipAgreement = Label(root, background='yellow', text='Membership Agreement')
        membershipAgreement.place(x=20, y=300)
    else:
        membershipAgreement = Label(root, text='Membership Agreement')
        membershipAgreement.place(x=20, y=300)

    resultTightrope = search.tightRope(selectedChapter)
    if resultTightrope['tightrope_100'] == 1:
        q2Count+=1
        tightropeCompletion = Label(root, background='green',text='Tightrope Completion(100%)')
        tightropeCompletion.place(x=20, y=320)
    elif resultTightrope['tightrope_100'] == 0:
        tightropeCompletion = Label(root, background='red',text='Tightrope Completion(100%)')
        tightropeCompletion.place(x=20, y=320)
    elif resultTightrope['tightrope_100'] == None:
        q2Count+=1
        tightropeCompletion = Label(root, background='yellow', text='Tightrope Completion(100%)')
        tightropeCompletion.place(x=20, y=320)
    else:
        tightropeCompletion = Label(root, text='Tightrope Completion(100%)')
        tightropeCompletion.place(x=20, y=320)

    resultMOH = search.MOHAttends(selectedChapter)
    if resultMOH['Men_of_Honor_Attendence'] == 1:
        q2Count+=1
        MOHAttend = Label(root, background='green',text='Men of Honor Attendance')
        MOHAttend.place(x=20, y=340)
    elif resultMOH['Men_of_Honor_Attendence'] == 0:
        MOHAttend = Label(root, background='red',text='Men of Honor Attendance')
        MOHAttend.place(x=20, y=340)
    elif resultMOH['Men_of_Honor_Attendence'] == None:
        q2Count+=1
        MOHAttend = Label(root, background='yellow', text='Men of Honor Attendance')
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

    resultOfficerCompl3 = search.officerCompl3(selectedChapter)
    if resultOfficerCompl3['Officer_Training_Or_Transition'] == 1:
        q3Count+=1
        officerComplLBQ3 = Label(root, background='green',text='Officer Compliance')
        officerComplLBQ3.place(x=250, y=50)
    elif resultOfficerCompl3['Officer_Training_Or_Transition'] == 0:
        officerComplLBQ3 = Label(root, background='red',text='Officer Compliance')
        officerComplLBQ3.place(x=250, y=50)
    elif resultOfficerCompl3['Officer_Training_Or_Transition'] == None:
        officerComplLBQ3 = Label(root, background='yellow',text='Officer Compliance')
        officerComplLBQ3.place(x=250, y=50)
    else:
        officerComplLBQ3 = Label(root, text='Officer Compliance')
        officerComplLBQ3.place(x=250, y=50)

    resultBudget3 = search.budget3(selectedChapter)
    if resultBudget3['Chapter_Budget'] == 1:
        q3Count+=1
        chaptBudgetQ3 = Label(root,background='green',text='Chapter Budget')
        chaptBudgetQ3.place(x=250, y=70)
    elif resultBudget3['Chapter_Budget'] == 0:
        chaptBudgetQ3 = Label(root,background='red',text='Chapter Budget')
        chaptBudgetQ3.place(x=250, y=70)
    elif resultBudget3['Chapter_Budget'] == None:
        q3Count+=1
        chaptBudgetQ3 = Label(root, background='yellow', text='Chapter Budget')
        chaptBudgetQ3.place(x=250, y=70)
    else:
        chaptBudgetQ3 = Label(root, text='Chapter Budget')
        chaptBudgetQ3.place(x=250, y=70)

    resultMalteCross = search.malteCross(selectedChapter)
    if resultMalteCross['One_Chapter_Member_Writes_Article_To_Maltes_Cross'] == 1:
        q3Count+=1
        malteseCrossReport = Label(root,background='green',text='Maltese Cross Report')
        malteseCrossReport.place(x=250, y=90)
    elif resultMalteCross['One_Chapter_Member_Writes_Article_To_Maltes_Cross'] == 0:
        malteseCrossReport = Label(root,background='red',text='Maltese Cross Report')
        malteseCrossReport.place(x=250, y=90)
    elif resultMalteCross['One_Chapter_Member_Writes_Article_To_Maltes_Cross'] == None:
        malteseCrossReport = Label(root,background='yellow',text='Maltese Cross Report')
        malteseCrossReport.place(x=250, y=90)
    else:
        malteseCrossReport = Label(root, text='Maltese Cross Report')
        malteseCrossReport.place(x=250, y=90)

    resultRosterMange3 = search.rosterMange3(selectedChapter)
    if resultRosterMange3['Roster'] == 1:
        q3Count+=1
        rosterMangeQ3 = Label(root,background='green',text='Roster Management')
        rosterMangeQ3.place(x=250, y=110)
    elif resultRosterMange3['Roster'] == 0:
        rosterMangeQ3 = Label(root, background='red',text='Roster Management')
        rosterMangeQ3.place(x=250, y=110)
    elif resultRosterMange3['Roster'] == None:
        q3Count+=1
        rosterMangeQ3 = Label(root, background='yellow', text='Roster Management')
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

    resultGreekBill = search.finGreekBill(selectedChapter)
    if resultGreekBill['GreekBill'] == 1:
        q4Count+=1
        fincialManageVerif = Label(root,background='green',text='Financial Management Verification')
        fincialManageVerif.place(x=250, y=220)
    elif resultGreekBill['GreekBill'] == 0:
        fincialManageVerif = Label(root, background='red',text='Financial Management Verification')
        fincialManageVerif.place(x=250, y=220)
    elif resultGreekBill['GreekBill'] == None:
        q4Count+=1
        fincialManageVerif = Label(root, background='red', text='Financial Management Verification')
        fincialManageVerif.place(x=250, y=220)
    else:
        fincialManageVerif = Label(root, text='Financial Management Verification')
        fincialManageVerif.place(x=250, y=220)

    resultGreekAdvisor = search.greekAdvisor(selectedChapter)
    if resultGreekAdvisor['Greek_Advisor_Verification_Form'] == 1:
        q4Count+=1
        greekAdvicorVerif = Label(root, background='green',text='Greek Advisor Verification')
        greekAdvicorVerif.place(x=250, y=240)
    elif resultGreekAdvisor['Greek_Advisor_Verification_Form'] == 0:
        greekAdvicorVerif = Label(root, background='red',text='Greek Advisor Verification')
        greekAdvicorVerif.place(x=250, y=240)
    elif resultGreekAdvisor['Greek_Advisor_Verification_Form'] == None:
        q4Count+=1
        greekAdvicorVerif = Label(root, background='yellow', text='Greek Advisor Verification')
        greekAdvicorVerif.place(x=250, y=240)
    else:
        greekAdvicorVerif = Label(root, text='Greek Advisor Verification')
        greekAdvicorVerif.place(x=250, y=240)

    resultRosterMange4 = search.rosterMange4(selectedChapter)
    if resultRosterMange4['Roster'] == 1:
        q4Count+=1
        rosterMangeQ4 = Label(root, background='green',text='Roster Management')
        rosterMangeQ4.place(x=250, y=260)
    elif resultRosterMange4['Roster'] == 0:
        rosterMangeQ4 = Label(root, background='red',text='Roster Management')
        rosterMangeQ4.place(x=250, y=260)
    elif resultRosterMange4['Roster'] == None:
        q4Count+=1
        rosterMangeQ4 = Label(root, background='red', text='Roster Management')
        rosterMangeQ4.place(x=250, y=260)
    else:
        rosterMangeQ4 = Label(root, text='Roster Management')
        rosterMangeQ4.place(x=250, y=260)

    resultGCAttand = search.GCAttandence(selectedChapter)
    if resultGCAttand['Grand_Chapter_Attendence'] == 1:
        q4Count+=1
        GCAttand = Label(root, background='green',text='Grand Chapter Attendance/OSI')
        GCAttand.place(x=250, y=280)
    elif resultGCAttand['Grand_Chapter_Attendence'] == 0:
        GCAttand = Label(root, background='red',text='Grand Chapter Attendance/OSI')
        GCAttand.place(x=250, y=280)
    elif resultGCAttand['Grand_Chapter_Attendence'] == None:
        q4Count+=1
        GCAttand = Label(root, background='yellow', text='Grand Chapter Attendance/OSI')
        GCAttand.place(x=250, y=280)
    else:
        GCAttand = Label(root, text='Grand Chapter Attendance/OSI')
        GCAttand.place(x=250, y=280)

    resultMembershipQ4 = search.membershipAgreement4(selectedChapter)
    if resultMembershipQ4['Membership_Agreements_100'] == 1:
        q4Count+=1
        membershipAgreementQ4 = Label(root, background='green',text='Membership Agreement')
        membershipAgreementQ4.place(x=250, y=300)
    elif resultMembershipQ4['Membership_Agreements_100'] == 0:
        membershipAgreementQ4 = Label(root, background='red',text='Membership Agreement')
        membershipAgreementQ4.place(x=250, y=300)
    elif resultMembershipQ4['Membership_Agreements_100'] == None:
        q4Count+=1
        membershipAgreementQ4 = Label(root, background='yellow', text='Membership Agreement')
        membershipAgreementQ4.place(x=250, y=300)
    else:
        membershipAgreementQ4 = Label(root, text='Membership Agreement')
        membershipAgreementQ4.place(x=250, y=300)

    resultNoShow = search.noShowCause4(selectedChapter)
    if resultNoShow['No_Show_Cause'] == 1:
        q4Count+=1
        noShowCause = Label(root, background='green',text='No Show Cause')
        noShowCause.place(x=250, y=320)
    elif resultNoShow['No_Show_Cause'] == 0:
        noShowCause = Label(root, background='red',text='No Show Cause')
        noShowCause.place(x=250, y=320)
    elif resultNoShow['No_Show_Cause'] == None:
        q4Count+=1
        noShowCause = Label(root, background='yellow', text='No Show Cause')
        noShowCause.place(x=250, y=320)
    else:
        noShowCause = Label(root, text='No Show Cause')
        noShowCause.place(x=250, y=320)

    resultPillars = search.pillarsNME4(selectedChapter)
    if resultPillars['Uses_Pillars'] == 1:
        q4Count+=1
        pillarsNME = Label(root, background='green',text='Pillars New Member Education')
        pillarsNME.place(x=250, y=340)
    elif resultPillars['Uses_Pillars'] == 0:
        pillarsNME = Label(root, background='red',text='Pillars New Member Education')
        pillarsNME.place(x=250, y=340)
    elif resultPillars['Uses_Pillars'] == None:
        q4Count+=1
        pillarsNME = Label(root, background='yellow', text='Pillars New Member Education')
        pillarsNME.place(x=250, y=340)
    else:
        pillarsNME = Label(root,text='Pillars New Member Education')
        pillarsNME.place(x=250, y=340)


    resultTightrope4 = search.tightRope4(selectedChapter)
    if resultTightrope4['tightrope_100'] == 1:
        q4Count+=1
        tightropeCompletionQ4 = Label(root, background='green',text='Tightrope Completion(100%)')
        tightropeCompletionQ4.place(x=250, y=360)
    elif resultTightrope4['tightrope_100'] == 0:
        tightropeCompletionQ4 = Label(root, background='red', text='Tightrope Completion(100%)')
        tightropeCompletionQ4.place(x=250, y=360)
    elif resultTightrope4['tightrope_100'] == None:
        q4Count+=1
        tightropeCompletionQ4 = Label(root, background='yellow', text='Tightrope Completion(100%)')
        tightropeCompletionQ4.place(x=250, y=360)
    else:
        tightropeCompletionQ4 = Label(root, text='Tightrope Completion(100%)')
        tightropeCompletionQ4.place(x=250, y=360)

    percentTotal4 = round(((q4Count/q4Total) * 100),2)
    q4Completed = Label(root, text='Quarter 4 Task Completed % - ' + str(percentTotal4))#
    q4Completed.place(x=250,y=380)
########################################################################################################################
    data1 = {'Quarters': ['Q1','Q2', 'Q3','Q4'],
             'Scores': [percentTotal, percentTotal2, percentTotal3, percentTotal4]}
    df1 = DataFrame(data1,columns=['Quarters', 'Scores'])
    figure1 = plt.Figure(figsize=(6,5), dpi=75)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
    df1 = df1[['Quarters','Scores']].groupby('Quarters').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Quarters vs MCS Scores')
########################################################################################################################
    countTotal = q1Count+q2Count+q3Count+q4Count
    overall_score= round(((countTotal/total)*100),2)

    overall = Label(root, text='Overall MCS score is ' + str(overall_score) + '%')
    overall.place(x=150, y=420)

    if overall_score >= 80:
        foundationalFlag = True
    else:
        foundationalFlag = False
def mscAwards(root, passFoundation, selectedChapter):
    clear_frame()
    root.geometry('1100x600')
    root.title('Qualifying Chapter Excellence for ' + selectedChapter + ' Chapter')

    back = Button(root, text="back", fg='blue', command=lambda: home(root))
    back.place(x=20, y=550)

    if passFoundation == True:
        complete = Label(root, text='passed foundational tasks')
        complete.place(x=20, y=30)

        passLn = Label(root, background='green', text='accepted task')
        passLn.place(x=20, y=5)

        failLn = Label(root, background='red', text='rejected task')
        failLn.place(x=100, y=5)

        waivedLn = Label(root, background='yellow', text='waived task')
        waivedLn.place(x=180, y=5)

        notSubmittedLn = Label(root, borderwidth=1, relief="solid", text='Task not Submitted')
        notSubmittedLn.place(x=250, y=5)

        total = 29
############################################################################################################################################################
        q1Label = Label(root, text='Quarter 1:')
        q1Label.place(x=20, y=70)

        q1Count = 0
        q1Total = 3

        resultMonthlyFinancialsQ1 = search.monthlyFinancials(selectedChapter)
        if resultMonthlyFinancialsQ1['Monthly_Financial_Statements'] == 1:
            q1Count += 1
            monthlyFinancialsCompQ1 = Label(root, background='green', text='Monthly Financials (May-August)')
            monthlyFinancialsCompQ1.place(x=20, y=90)
        elif resultMonthlyFinancialsQ1['Monthly_Financial_Statements'] == 0:
            monthlyFinancialsCompQ1 = Label(root, background='red', text='Monthly Financials (May-August)')
            monthlyFinancialsCompQ1.place(x=20, y=90)
        elif resultMonthlyFinancialsQ1['Monthly_Financial_Statements'] == None:
            q1Count += 1
            monthlyFinancialsCompQ1 = Label(root, background='yellow', text='Monthly Financials (May-August)')
            monthlyFinancialsCompQ1.place(x=20, y=90)
        else:
            monthlyFinancialsCompQ1 = Label(root,  text='Monthly Financials (May-August)')
            monthlyFinancialsCompQ1.place(x=20, y=90)

        resultMonthlyMinutesQ1 = search.monthlyMeetingMinutes(selectedChapter)
        if resultMonthlyMinutesQ1['Monthly_Chapter_Meetings'] == 1:
            q1Count += 1
            monthlyMinutesQ1 = Label(root, background='green', text='Monthly Meeting Minutes (August)')
            monthlyMinutesQ1.place(x=20, y=110)
        elif resultMonthlyMinutesQ1['Monthly_Chapter_Meetings'] == 0:
            monthlyMinutesQ1 = Label(root, background='red', text='Monthly Meeting Minutes (August)')
            monthlyMinutesQ1.place(x=20, y=110)
        if resultMonthlyMinutesQ1['Monthly_Chapter_Meetings'] == None:
            q1Count += 1
            monthlyMinutesQ1 = Label(root, background='green', text='Monthly Meeting Minutes (August)')
            monthlyMinutesQ1.place(x=20, y=110)

        resultSpringGrades = search.springGradesReport(selectedChapter)
        if resultSpringGrades['Chapter_GPA'] == 1:
            q1Count += 1
            springGradeReport = Label(root, background='green', text='Spring Grade Report')
            springGradeReport.place(x=20, y=130)
        elif resultSpringGrades['Chapter_GPA'] == 0:
            springGradeReport = Label(root, background='red', text='Spring Grade Report')
            springGradeReport.place(x=20, y=130)
        elif resultSpringGrades['Chapter_GPA'] == None:
            q1Count += 1
            springGradeReport = Label(root, background='yellow', text='Spring Grade Report')
            springGradeReport.place(x=20, y=130)
        else:
            springGradeReport = Label(root,text='Spring Grade Report')
            springGradeReport.place(x=20, y=130)

        percentTotal = round(((q1Count / q1Total) * 100), 2)
        q1Completed = Label(root, text='Quarter 1 Task Completed % - ' + str(percentTotal))  #
        q1Completed.place(x=20, y=150)
###############################################################################
        q2Label = Label(root, text='Quarter 2:')
        q2Label.place(x=20, y=200)

        q2Count = 0
        q2Total = 6

        resultsSocialEvent = search.socialEvent(selectedChapter)
        if resultsSocialEvent['Social_Events'] == 1:
            q2Count+=1
            socialEvent1 = Label(root, background='green', text='Social Event')
            socialEvent1.place(x=20, y=220)
        elif resultsSocialEvent['Social_Events'] == 0:
            socialEvent1 = Label(root, background='red', text='Social Event')
            socialEvent1.place(x=20, y=220)
        elif resultsSocialEvent['Social_Events'] == None:
            q2Count+=1
            socialEvent1 = Label(root, background='yellow', text='Social Event')
            socialEvent1.place(x=20, y=220)
        else:
            socialEvent1 = Label(root, text='Social Event')
            socialEvent1.place(x=20, y=220)

        resultsBrotherhoodEvents = search.brotherhoodEvents(selectedChapter)
        if resultsBrotherhoodEvents['Two_Brotherhood_Building_Actives_Per_Month'] == 1:
            q2Count += 1
            brotherhoodEvents1 = Label(root, background='green', text='Brotherhood Events')
            brotherhoodEvents1.place(x=20, y=240)
        elif resultsBrotherhoodEvents['Two_Brotherhood_Building_Actives_Per_Month'] == 0:
            brotherhoodEvents1 = Label(root, background='red', text='Brotherhood Events')
            brotherhoodEvents1.place(x=20, y=240)
        elif resultsBrotherhoodEvents['Two_Brotherhood_Building_Actives_Per_Month'] == None:
            q2Count += 1
            brotherhoodEvents1 = Label(root, background='yellow', text='Brotherhood Events')
            brotherhoodEvents1.place(x=20, y=240)
        else:
            brotherhoodEvents1 = Label(root, text='Brotherhood Events')
            brotherhoodEvents1.place(x=20, y=240)

        resultsMonthlyFinancials2 = search.monthlyFinancials(selectedChapter)
        if resultsMonthlyFinancials2['Monthly_Financial_Statements'] == 1:
            q2Count += 1
            monthlyFinancials2 = Label(root, background='green', text='Monthly Financials (September-October)')
            monthlyFinancials2.place(x=20, y=260)
        elif resultsMonthlyFinancials2['Monthly_Financial_Statements'] == 0:
            monthlyFinancials2 = Label(root, background='red', text='Monthly Financials (September-October)')
            monthlyFinancials2.place(x=20, y=260)
        elif resultsMonthlyFinancials2['Monthly_Financial_Statements'] == None:
            q2Count += 1
            monthlyFinancials2 = Label(root, background='yellow', text='Monthly Financials (September-October)')
            monthlyFinancials2.place(x=20, y=260)
        else:
            monthlyFinancials2 = Label(root, text='Monthly Financials (September-October)')
            monthlyFinancials2.place(x=20, y=260)

        resultsMonthlyMinutse2 = search.monthlyMeetingMinutes(selectedChapter)
        if resultsMonthlyMinutse2['Monthly_Chapter_Meetings'] == 1:
            q2Count += 1
            monthlyMeetingMinutes2 = Label(root, background='green', text='Monthly Meeting Minutes (September-October)')
            monthlyMeetingMinutes2.place(x=20, y=280)
        elif resultsMonthlyMinutse2['Monthly_Chapter_Meetings'] == 0:
            monthlyMeetingMinutes2 = Label(root, background='red', text='Monthly Meeting Minutes (September-October)')
            monthlyMeetingMinutes2.place(x=20, y=280)
        elif resultsMonthlyMinutse2['Monthly_Chapter_Meetings'] == None:
            q2Count += 1
            monthlyMeetingMinutes2 = Label(root, background='yellow', text='Monthly Meeting Minutes (September-October)')
            monthlyMeetingMinutes2.place(x=20, y=280)
        else:
            monthlyMeetingMinutes2 = Label(root, text='Monthly Meeting Minutes (September-October)')
            monthlyMeetingMinutes2.place(x=20, y=280)

        resultPhilanthropicEvent = search.philanthropicEvent(selectedChapter)
        if resultPhilanthropicEvent['Philantrophy_Events'] == 1:
            q2Count += 1
            philanthropicEvent1 = Label(root, background='green', text='Philanthropic Event')
            philanthropicEvent1.place(x=20, y=300)
        elif resultPhilanthropicEvent['Philantrophy_Events'] == 0:
            philanthropicEvent1 = Label(root, background='red', text='Philanthropic Event')
            philanthropicEvent1.place(x=20, y=300)
        elif resultPhilanthropicEvent['Philantrophy_Events'] == None:
            q2Count += 1
            philanthropicEvent1 = Label(root, background='yellow', text='Philanthropic Event')
            philanthropicEvent1.place(x=20, y=300)
        else:
            philanthropicEvent1 = Label(root, text='Philanthropic Event')
            philanthropicEvent1.place(x=20, y=300)

        resultChapterWebsite = search.chapterWebsite(selectedChapter)
        if resultChapterWebsite['Active_Website_Or_Social_Media'] == 1:
            q2Count += 1
            chapterWebsite1 = Label(root, background='green', text='Chapter Website')
            chapterWebsite1.place(x=20, y=320)
        elif resultChapterWebsite['Active_Website_Or_Social_Media'] == 0:
            chapterWebsite1 = Label(root, background='red', text='Chapter Website')
            chapterWebsite1.place(x=20, y=320)
        elif resultChapterWebsite['Active_Website_Or_Social_Media'] == None:
            q2Count += 1
            chapterWebsite1 = Label(root, background='yellow', text='Chapter Website')
            chapterWebsite1.place(x=20, y=320)
        else:
            chapterWebsite1 = Label(root, text='Chapter Website')
            chapterWebsite1.place(x=20, y=320)

        percentTotal2 = round(((q2Count / q2Total) * 100), 2)
        q2Completed = Label(root, text='Quarter 2 Task Completed % - ' + str(percentTotal2))  #
        q2Completed.place(x=20, y=340)
###############################################################################################################
        q3Label = Label(root, text='Quarter 3:')
        q3Label.place(x=320, y=70)

        q3Count = 0
        q3Total = 4

        resultMonthlyFinancialsQ3 = search.monthlyFinancials(selectedChapter)
        if resultMonthlyFinancialsQ3 ['Monthly_Financial_Statements'] == 1:
            q3Count += 1
            monthlyFinancialsCompQ3 = Label(root, background='green', text='Monthly Financials (December-January)')
            monthlyFinancialsCompQ3.place(x=320, y=90)
        elif resultMonthlyFinancialsQ3 ['Monthly_Financial_Statements'] == 0:
            monthlyFinancialsCompQ3 = Label(root, background='red', text='Monthly Financials (December-January)')
            monthlyFinancialsCompQ3.place(x=320, y=90)
        elif resultMonthlyFinancialsQ3 ['Monthly_Financial_Statements'] == None:
            q3Count += 1
            monthlyFinancialsCompQ3 = Label(root, background='yellow', text='Monthly Financials (December-January)')
            monthlyFinancialsCompQ3.place(x=320, y=90)
        else:
            monthlyFinancialsCompQ3 = Label(root, text='Monthly Financials (December-January)')
            monthlyFinancialsCompQ3.place(x=320, y=90)

        resultMonthlyMinutesQ3 = search.monthlyMeetingMinutes(selectedChapter)
        if resultMonthlyMinutesQ3['Monthly_Chapter_Meetings'] == 1:
            q3Count += 1
            monthlyMeetingMinutes3 = Label(root, background='green', text='Monthly Meeting Minutes (September-October)')
            monthlyMeetingMinutes3.place(x=320, y=110)
        elif resultMonthlyMinutesQ3['Monthly_Chapter_Meetings'] == 0:
            monthlyMeetingMinutes3 = Label(root, background='red', text='Monthly Meeting Minutes (September-October)')
            monthlyMeetingMinutes3.place(x=320, y=110)
        elif resultMonthlyMinutesQ3['Monthly_Chapter_Meetings'] == None:
            q3Count += 1
            monthlyMeetingMinutes3 = Label(root, background='yellow', text='Monthly Meeting Minutes (September-October)')
            monthlyMeetingMinutes3.place(x=320, y=110)
        else:
            monthlyMeetingMinutes3 = Label(root, text='Monthly Meeting Minutes (September-October)')
            monthlyMeetingMinutes3.place(x=320, y=110)

        resultGradeReport = search.springGradesReport(selectedChapter)
        if resultGradeReport['Chapter_GPA'] == 1:
            q3Count += 1
            gradeReport = Label(root, background='green', text='Grade Report')
            gradeReport.place(x=320, y=130)
        elif resultGradeReport['Chapter_GPA'] == 0:
            gradeReport = Label(root, background='red', text='Grade Report')
            gradeReport.place(x=320, y=130)
        elif resultGradeReport['Chapter_GPA'] == None:
            q3Count += 1
            gradeReport = Label(root, background='yellow', text='Grade Report')
            gradeReport.place(x=320, y=130)
        else:
            gradeReport = Label(root, text='Spring Grade Report')
            gradeReport.place(x=320, y=130)

        resultGoalsPlanning = search.officerCompl3(selectedChapter)
        if resultGoalsPlanning['Officer_Training_Or_Transition'] == 1:
            q3Count += 1
            goalPlanning = Label(root, background='green', text='Goals and Planning')
            goalPlanning.place(x=320, y=150)
        elif resultGoalsPlanning['Officer_Training_Or_Transition'] == 0:
            goalPlanning = Label(root, background='red', text='Goals and Planning')
            goalPlanning.place(x=320, y=150)
        elif resultGoalsPlanning['Officer_Training_Or_Transition'] == None:
            q3Count += 1
            goalPlanning = Label(root, background='yellow', text='Goals and Planning')
            goalPlanning.place(x=320, y=150)
        else:
            goalPlanning = Label(root, text='Goals and Planning')
            goalPlanning.place(x=320, y=150)

        percentTotal3 = round(((q3Count / q3Total) * 100), 2)
        q3Completed = Label(root, text='Quarter 3 Task Completed % - ' + str(percentTotal3))  #
        q3Completed.place(x=320, y=170)
##############################################################################################################
        q4Label = Label(root, text='Quarter 4:')
        q4Label.place(x=320, y=200)

        q4Count = 0
        q4Total = 16

        resultAlumniNewsletter = search.alumniNewsletter(selectedChapter)
        if resultAlumniNewsletter['Alumni_Newsletter'] == 1:
            q4Count += 1
            alumniNewsletter4 = Label(root, background='green', text='Alumni Newsletter')
            alumniNewsletter4.place(x=320, y=220)
        elif resultAlumniNewsletter['Alumni_Newsletter'] == 0:
            alumniNewsletter4 = Label(root, background='red', text='Alumni Newsletter')
            alumniNewsletter4.place(x=320, y=220)
        elif resultAlumniNewsletter['Alumni_Newsletter'] == None:
            q4Count += 1
            alumniNewsletter4 = Label(root, background='yellow', text='Alumni Newsletter')
            alumniNewsletter4.place(x=320, y=220)
        else:
            alumniNewsletter4 = Label(root, text='Alumni Newsletter')
            alumniNewsletter4.place(x=320, y=220)

        resultsSocialEvent4 = search.socialEvent(selectedChapter)
        if resultsSocialEvent4['Social_Events'] == 1:
            q4Count += 1
            socialEvent4 = Label(root, background='green', text='Social Event')
            socialEvent4.place(x=320, y=240)
        elif resultsSocialEvent4['Social_Events'] == 0:
            socialEvent4 = Label(root, background='red', text='Social Event')
            socialEvent4.place(x=320, y=240)
        elif resultsSocialEvent4['Social_Events'] == None:
            q4Count += 1
            socialEvent4 = Label(root, background='yellow', text='Social Event')
            socialEvent4.place(x=320, y=240)
        else:
            socialEvent4 = Label(root, text='Social Event')
            socialEvent4.place(x=320, y=240)

        resultMonthlyFinancialsQ4 = search.monthlyFinancials(selectedChapter)
        if resultMonthlyFinancialsQ4['Monthly_Financial_Statements'] == 1:
            q4Count += 1
            monthlyFinancialsCompQ4 = Label(root, background='green', text='Monthly Financials (February-April)')
            monthlyFinancialsCompQ4.place(x=320, y=260)
        elif resultMonthlyFinancialsQ4['Monthly_Financial_Statements'] == 0:
            monthlyFinancialsCompQ4 = Label(root, background='red', text='Monthly Financials (February-April)')
            monthlyFinancialsCompQ4.place(x=320, y=260)
        elif resultMonthlyFinancialsQ4['Monthly_Financial_Statements'] == None:
            q4Count += 1
            monthlyFinancialsCompQ4 = Label(root, background='yellow', text='Monthly Financials (February-April)')
            monthlyFinancialsCompQ4.place(x=320, y=260)
        else:
            monthlyFinancialsCompQ4 = Label(root, text='Monthly Financials (February-April)')
            monthlyFinancialsCompQ4.place(x=320, y=260)

        resultMonthlyMinutesQ4 = search.monthlyMeetingMinutes(selectedChapter)
        if resultMonthlyMinutesQ4['Monthly_Chapter_Meetings'] == 1:
            q4Count += 1
            monthlyMeetingMinutes4 = Label(root, background='green', text='Monthly Meeting Minutes (February-April)')
            monthlyMeetingMinutes4.place(x=320, y=280)
        elif resultMonthlyMinutesQ4['Monthly_Chapter_Meetings'] == 0:
            monthlyMeetingMinutes4 = Label(root, background='red', text='Monthly Meeting Minutes (February-April)')
            monthlyMeetingMinutes4.place(x=320, y=280)
        elif resultMonthlyMinutesQ4['Monthly_Chapter_Meetings'] == None:
            q4Count += 1
            monthlyMeetingMinutes4 = Label(root, background='yellow', text='Monthly Meeting Minutes (February-April)')
            monthlyMeetingMinutes4.place(x=320, y=280)
        else:
            monthlyMeetingMinutes4 = Label(root, text='Monthly Meeting Minutes (February-April)')
            monthlyMeetingMinutes4.place(x=320, y=280)

        resultsBrotherhoodEvents4 = search.brotherhoodEvents(selectedChapter)
        if resultsBrotherhoodEvents4['Two_Brotherhood_Building_Actives_Per_Month'] == 1:
            q4Count += 1
            brotherhoodEvents4 = Label(root, background='green', text='Brotherhood Events')
            brotherhoodEvents4.place(x=320, y=300)
        elif resultsBrotherhoodEvents4['Two_Brotherhood_Building_Actives_Per_Month'] == 0:
            brotherhoodEvents4 = Label(root, background='red', text='Brotherhood Events')
            brotherhoodEvents4.place(x=320, y=300)
        elif resultsBrotherhoodEvents4['Two_Brotherhood_Building_Actives_Per_Month'] == None:
            q4Count += 1
            brotherhoodEvents4 = Label(root, background='yellow', text='Brotherhood Events')
            brotherhoodEvents4.place(x=320, y=300)
        else:
            brotherhoodEvents4 = Label(root, text='Brotherhood Events')
            brotherhoodEvents4.place(x=320, y=300)

        resultFormalTraining = search.formalTraining(selectedChapter)
        if resultFormalTraining['Formal_Training'] == 1:
            q4Count += 1
            formalTraining4 = Label(root, background='green', text='Formal Training')
            formalTraining4.place(x=320, y=320)
        elif resultFormalTraining['Formal_Training'] == 0:
            formalTraining4 = Label(root, background='red', text='Formal Training')
            formalTraining4.place(x=320, y=320)
        elif resultFormalTraining['Formal_Training'] == None:
            q4Count += 1
            formalTraining4 = Label(root, background='yellow', text='Formal Training')
            formalTraining4.place(x=320, y=320)
        else:
            formalTraining4 = Label(root, text='Formal Training')
            formalTraining4.place(x=320, y=320)

        resultCommunityService = search.communityService(selectedChapter)
        if resultCommunityService['Service_Hours_16_Per_Man'] == 1:
            q4Count += 1
            communityService4 = Label(root, background='green', text='Community Service')
            communityService4.place(x=320, y=340)
        elif resultCommunityService['Service_Hours_16_Per_Man'] == 0:
            communityService4 = Label(root, background='red', text='Community Service')
            communityService4.place(x=320, y=340)
        elif resultCommunityService['Service_Hours_16_Per_Man'] == None:
            q4Count += 1
            communityService4 = Label(root, background='yellow', text='Community Service')
            communityService4.place(x=320, y=340)
        else:
            communityService4 = Label(root, text='Community Service')
            communityService4.place(x=320, y=340)

        resultPhilanthropicEvent4 = search.philanthropicEvent(selectedChapter)
        if resultPhilanthropicEvent4['Philantrophy_Events'] == 1:
            q4Count += 1
            philanthropicEvent4 = Label(root, background='green', text='Philanthropy Events')
            philanthropicEvent4.place(x=320, y=360)
        elif resultPhilanthropicEvent4['Philantrophy_Events'] == 0:
            philanthropicEvent4 = Label(root, background='red', text='Philanthropy Events')
            philanthropicEvent4.place(x=320, y=360)
        elif resultPhilanthropicEvent4['Philantrophy_Events'] == None:
            q4Count += 1
            philanthropicEvent4 = Label(root, background='yellow', text='Philanthropy Events')
            philanthropicEvent4.place(x=320, y=360)
        else:
            philanthropicEvent4 = Label(root, text='Philanthropy Events')
            philanthropicEvent4.place(x=320, y=360)

        resultRaiseMoneyPhi = search.raiseMoneyPhi(selectedChapter)
        if resultRaiseMoneyPhi['Philantrophy_Money_Donated'] == 1:
            q4Count += 1
            raiseMoneyPhi4 = Label(root, background='green', text='Philanthropy Money Donated')
            raiseMoneyPhi4.place(x=320, y=380)
        elif resultRaiseMoneyPhi['Philantrophy_Money_Donated'] == 0:
            raiseMoneyPhi4 = Label(root, background='red', text='Philanthropy Money Donated')
            raiseMoneyPhi4.place(x=320, y=380)
        elif resultRaiseMoneyPhi['Philantrophy_Money_Donated'] == None:
            q4Count += 1
            raiseMoneyPhi4 = Label(root, background='yellow', text='Philanthropy Events')
            raiseMoneyPhi4.place(x=320, y=380)
        else:
            raiseMoneyPhi4 = Label(root, text='Philanthropy Events')
            raiseMoneyPhi4.place(x=320, y=380)

        resultIFCAttendance = search.IFCAttendance(selectedChapter)
        if resultIFCAttendance['Attends_All_Or_Greek_Council_Meeting_GA_Ver_Form'] == 1:
            q4Count += 1
            IFCAttendance4 = Label(root, background='green', text='Attends All Council Meeting GA Ver Form')
            IFCAttendance4.place(x=320, y=400)
        elif resultIFCAttendance['Attends_All_Or_Greek_Council_Meeting_GA_Ver_Form'] == 0:
            IFCAttendance4 = Label(root, background='red', text='Attends All Council Meeting GA Ver Form')
            IFCAttendance4.place(x=320, y=400)
        elif resultIFCAttendance['Attends_All_Or_Greek_Council_Meeting_GA_Ver_Form'] == None:
            q4Count += 1
            IFCAttendance4 = Label(root, background='yellow', text='Attends All Council Meeting GA Ver Form')
            IFCAttendance4.place(x=320, y=400)
        else:
            IFCAttendance4 = Label(root, text='Attends All Council Meeting GA Ver Form')
            IFCAttendance4.place(x=320, y=400)

        resultChapterWebsite4 = search.chapterWebsite(selectedChapter)
        if resultChapterWebsite4['Active_Website_Or_Social_Media'] == 1:
            q4Count += 1
            chapterWebsite4 = Label(root, background='green', text='Chapter Website')
            chapterWebsite4.place(x=320, y=420)
        elif resultChapterWebsite4['Active_Website_Or_Social_Media'] == 0:
            chapterWebsite4 = Label(root, background='red', text='Chapter Website')
            chapterWebsite4.place(x=320, y=420)
        elif resultChapterWebsite4['Active_Website_Or_Social_Media'] == None:
            q4Count += 1
            chapterWebsite4 = Label(root, background='yellow', text='Chapter Website')
            chapterWebsite4.place(x=320, y=420)
        else:
            chapterWebsite4 = Label(root, text='Chapter Website')
            chapterWebsite4.place(x=320, y=420)

        resultInvoicesPaidNet30 = search.invoicesPaidNet30 (selectedChapter)
        if resultInvoicesPaidNet30['Invoices_Paid_Net_30'] == 1:
            q4Count += 1
            invoicesPaidNet304 = Label(root, background='green', text='Invoices Paid Net 30')
            invoicesPaidNet304.place(x=320, y=440)
        elif resultInvoicesPaidNet30['Invoices_Paid_Net_30'] == 0:
            invoicesPaidNet304 = Label(root, background='red', text='Invoices Paid Net 30')
            invoicesPaidNet304.place(x=320, y=440)
        elif resultInvoicesPaidNet30['Invoices_Paid_Net_30'] == None:
            q4Count += 1
            invoicesPaidNet304 = Label(root, background='yellow', text='Invoices Paid Net 30')
            invoicesPaidNet304.place(x=320, y=440)
        else:
            invoicesPaidNet304 = Label(root, text='Invoices Paid Net 30')
            invoicesPaidNet304.place(x=320, y=440)

        resultNoWellnessCheck = search.noWellnessCheck(selectedChapter)
        if resultNoWellnessCheck['Not_Responsible_For_Wellness_Check'] == 1:
            q4Count += 1
            noWellnessCheck4 = Label(root, background='green', text='Not Responsible For Wellness Check')
            noWellnessCheck4.place(x=320, y=460)
        elif resultNoWellnessCheck['Not_Responsible_For_Wellness_Check'] == 0:
            noWellnessCheck4 = Label(root, background='red', text='Not Responsible For Wellness Check')
            noWellnessCheck4.place(x=320, y=460)
        elif resultNoWellnessCheck['Not_Responsible_For_Wellness_Check'] == None:
            q4Count += 1
            noWellnessCheck4 = Label(root, background='yellow', text='Not Responsible For Wellness Check')
            noWellnessCheck4.place(x=320, y=460)
        else:
            noWellnessCheck4 = Label(root, text='Not Responsible For Wellness Check')
            noWellnessCheck4.place(x=320, y=460)

        resultComposite = search.composite(selectedChapter)
        if resultComposite['Submits_Composite_Copy_Or_Equivalent'] == 1:
            q4Count += 1
            composite4 = Label(root, background='green', text='Composite')
            composite4.place(x=320, y=480)
        elif resultComposite['Submits_Composite_Copy_Or_Equivalent'] == 0:
            composite4 = Label(root, background='red', text='Composite')
            composite4.place(x=320, y=480)
        elif resultComposite['Submits_Composite_Copy_Or_Equivalent'] == None:
            q4Count += 1
            composite4 = Label(root, background='yellow', text='Composite')
            composite4.place(x=320, y=480)
        else:
            composite4 = Label(root, text='Composite')
            composite4.place(x=320, y=480)

        resultNewMember25OrHigher = search.newMember25OrHigher(selectedChapter)
        if resultNewMember25OrHigher['New_Members_Greater_Or_Equal_To_25'] == 1:
            q4Count += 1
            newMember25OrHigher4 = Label(root, background='green', text='New Member 25 Or Higher')
            newMember25OrHigher4.place(x=320, y=500)
        elif resultNewMember25OrHigher['New_Members_Greater_Or_Equal_To_25'] == 0:
            newMember25OrHigher4 = Label(root, background='red', text='New Member 25 Or Higher')
            newMember25OrHigher4.place(x=320, y=500)
        elif resultNewMember25OrHigher['New_Members_Greater_Or_Equal_To_25'] == None:
            q4Count += 1
            newMember25OrHigher4 = Label(root, background='yellow', text='New Member 25 Or Higher')
            newMember25OrHigher4.place(x=320, y=500)
        else:
            newMember25OrHigher4 = Label(root, text='New Member 25 Or Higher')
            newMember25OrHigher4.place(x=320, y=500)

        resultChapterSize = search.chapterSize(selectedChapter)
        if resultChapterSize['Chapter_Size_Greater_Or_Equal_To_PKS_Or_Campus_Average'] == 1:
            q4Count += 1
            chapterSize4 = Label(root, background='green', text='Chapter Size')
            chapterSize4.place(x=320, y=520)
        elif resultChapterSize['Chapter_Size_Greater_Or_Equal_To_PKS_Or_Campus_Average'] == 0:
            chapterSize4 = Label(root, background='red', text='Chapter Size')
            chapterSize4.place(x=320, y=520)
        elif resultChapterSize['Chapter_Size_Greater_Or_Equal_To_PKS_Or_Campus_Average'] == None:
            q4Count += 1
            chapterSize4 = Label(root, background='yellow', text='Chapter Size')
            chapterSize4.place(x=320, y=520)
        else:
            chapterSize4 = Label(root, text='Chapter Size')
            chapterSize4.place(x=320, y=520)

        percentTotal4 = round(((q4Count / q4Total) * 100), 2)
        q4Completed = Label(root, text='Quarter 4 Task Completed % - ' + str(percentTotal4))  #
        q4Completed.place(x=320, y=540)

        countTotal = q1Count + q2Count + q3Count + q4Count
        overall_score = round(((countTotal / total) * 100), 2)

        overall = Label(root, text='Overall MCS score is ' + str(overall_score) + '%')
        overall.place(x=20, y=420)
#################################################################################################################################
        data1 = {'Quarters': ['Q1', 'Q2', 'Q3', 'Q4'],
                 'Scores': [percentTotal, percentTotal2, percentTotal3, percentTotal4]}
        df1 = DataFrame(data1, columns=['Quarters', 'Scores'])
        figure1 = plt.Figure(figsize=(6, 5), dpi=75)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
        df1 = df1[['Quarters', 'Scores']].groupby('Quarters').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Quarters vs MCS Scores')
def homeChapter(root):
    clear_frame()
    frameHomeChap = Frame(root, height=350)
    frameHomeChap.pack(side=TOP, fill=X)
    root.geometry('500x350')
    root.title('Phi Kappa Sigma MCS')

    openImg = Image.open("../PKS_Chapter_Health_Tool/PKS.png")
    importImg = ImageTk.PhotoImage(openImg)
    img = tkinter.Label(image=importImg)
    img.image = importImg
    img.place(x=175, y=0)

    chapters=search.selectionChapters()
    global cb
    cb = Combobox(root, values=chapters, width=30, state='readonly')
    cb.place(x=150, y=200)

    back = Button(root, text='Back', fg='blue', command=lambda: home(root))
    back.place(x=200, y=250)

    submit = Button(root, text="Submit", fg='blue', command=lambda:chapterDetails(root))
    submit.place(x=265, y=250)

def awardsReport(root):
    clear_frame()
    frameAwardsReport = Frame(root, height=350)
    frameAwardsReport.pack(side=TOP, fill=X)
    root.geometry('1000x500')
    root.title('MCS Awards Report')

    back = Button(root, text="back", fg='blue', command=lambda: home(root))
    back.place(x=20, y=450)

def databaseUpgrade(root):
    clear_frame()
    frameHome = Frame(root, height=350)
    frameHome.pack(side=TOP, fill=X)
    root.geometry('500x350')
    root.title('Database Upgrade')

    startYear = Label(root, text='Start year of MCS')
    startYear.place(x=20, y=20)

    startYearInput = tk.Entry(root)
    startYearInput.place(x=20, y=40)

    endYear = Label(root, text='End year of MCS')
    endYear.place(x=20, y=80)

    endYearInput = tk.Entry(root)
    endYearInput.place(x=20, y=100)

    btnBrowse = Button(root, text="Select Database", fg='blue', command=lambda: browseFiles())
    btnBrowse.place(x=20, y=160)

    back = Button(root, text="back", fg='blue', command=lambda: home(root))
    back.place(x=20, y=300)

    upload = Button(root, text='Upload new database', fg='blue')
    upload.place(x=355, y=300)

    openImg = Image.open("../PKS_Chapter_Health_Tool/pks-grand-chapter-seal.png")
    importImg = ImageTk.PhotoImage(openImg)
    img = tkinter.Label(image=importImg)
    img.image = importImg
    img.place(x=175, y=0)

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("CSV files",
                                                      ".csv"),
                                                     ("all files",
                                                      ".")))
    data = filename

    newDatabase = data

def home(root):
    clear_frame()
    frameHome = Frame(root, height=350)
    frameHome.pack(side=TOP, fill=X)
    root.geometry('500x350')
    root.title('Phi Kappa Sigma MCS')
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file="../PKS_Chapter_Health_Tool/pks-grand-chapter-seal.png"))

    openImg = Image.open("../PKS_Chapter_Health_Tool/PKS.png")
    importImg = ImageTk.PhotoImage(openImg)
    img = tkinter.Label(image=importImg)
    img.image = importImg
    img.place(x=175, y=0)

    chaptSearch = Button(root, text='Chapter Search', fg='blue', command=lambda:homeChapter(root))
    chaptSearch.place(x=90, y=250)

    dataBase = Button(root, text='Database', fg='blue', command=lambda: databaseUpgrade(root))
    dataBase.place(x=225, y=250)

    chaptAwards = Button(root, text='Chapters Awards', fg='blue', command=lambda: awardsReport(root))
    chaptAwards.place(x=320, y=250)

    bio = Label(text='Created by Alek Ahrens of the Beta Chi Chapter Fall 2020')
    bio.place(x=100,y=320)

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False,False)
    home(root)
    root.mainloop()

