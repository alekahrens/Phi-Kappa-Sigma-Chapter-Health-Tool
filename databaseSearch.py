import mysql.connector

def chapterSize(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Chapter_Size_Greater_Or_Equal_To_PKS_Or_Campus_Average FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def newMember25OrHigher(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT New_Members_Greater_Or_Equal_To_25 FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def composite(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Submits_Composite_Copy_Or_Equivalent FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def noWellnessCheck(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Not_Responsible_For_Wellness_Check FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def invoicesPaidNet30(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Invoices_Paid_Net_30 FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def IFCAttendance(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Attends_All_Or_Greek_Council_Meeting_GA_Ver_Form FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def raiseMoneyPhi(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Philantrophy_Money_Donated FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def communityService(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Service_Hours_16_Per_Man FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def formalTraining(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Formal_Training FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]


def alumniNewsletter(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Alumni_Newsletter FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]


def chapterWebsite(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Active_Website_Or_Social_Media FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def philanthropicEvent(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Philantrophy_Events FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def brotherhoodEvents(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Two_Brotherhood_Building_Actives_Per_Month FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def socialEvent(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Social_Events FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def springGradesReport(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Chapter_GPA FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def monthlyMeetingMinutes(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Monthly_Chapter_Meetings FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def monthlyFinancials(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Monthly_Financial_Statements FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def tightRope4(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT tightrope_100 FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def pillarsNME4(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Uses_Pillars FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def noShowCause4(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT No_Show_Cause FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def membershipAgreement4(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Membership_Agreements_100 FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def GCAttandence(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Grand_Chapter_Attendence FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def rosterMange4(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute(
        "SELECT Roster FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def greekAdvisor(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Greek_Advisor_Verification_Form FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def finGreekBill(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT GreekBill FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def rosterMange3(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Roster FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def malteCross(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT One_Chapter_Member_Writes_Article_To_Maltes_Cross FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def budget3(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Chapter_Budget FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def officerCompl3(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Officer_Training_Or_Transition FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def MOHAttends(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Men_of_Honor_Attendence FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def tightRope(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT tightrope_100 FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]
def membershipAgreement1(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Membership_Agreements_100 FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def rosterMange2(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Roster FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def springRecruit(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Recruitment_Plan FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def IRS990(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT IRS_990 FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def officerCompl(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Officer_Training_Or_Transition FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]


def rosterManagement(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Roster FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]



def fallUpdate(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Fall_Updates FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def recruit(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Recruitment_Plan FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def budget(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Chapter_Budget FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]

def chaptAcademicProgram(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Academic_Program FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
    myresults = mycursor.fetchall()

    return myresults[0]


def chapBylaws(selectedChapter):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="pks_chapter_data",
    )

    mycursor = mydb.cursor(buffered=True, dictionary=True)
    mycursor.execute("SELECT Chapter_Bylaws FROM 2020to2021 where Chapter = '" + selectedChapter + "';")
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
    mycursor.execute("SELECT Chapter FROM 2020to2021")
    myresults = mycursor.fetchall()

    return myresults
