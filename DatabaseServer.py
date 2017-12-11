import os
from flask import Flask, redirect, request, render_template, url_for, make_response, send_file, Markup
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
import sqlite3
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import smtplib
import mimetypes
import email
import email.mime.application



imageLocation = 'static/images/Acorn_logo_mini.png'


now = datetime.datetime.now()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER_CV = os.path.join(APP_ROOT,'static/file_uploads/cv_uploads')
UPLOAD_FOLDER_qualifications = os.path.join(APP_ROOT,'static/file_uploads/qualifications_uploads')
# UPLOAD_FOLDER_signature = os.path.join(APP_ROOT,'static/file_uploads/signature_uploads')

# mail = Mail()
# mail.init_app(app)
# mail_ext = Mail(app)

DATABASE = "CandidateCenter.db"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER_CV'] = UPLOAD_FOLDER_CV
app.config['UPLOAD_FOLDER_qualifications'] = UPLOAD_FOLDER_qualifications
# app.config['UPLOAD_FOLDER_CV'] = UPLOAD_FOLDER_CV

app.config.update(
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'nsadevelopment2017@gmail.com',
	MAIL_PASSWORD = 'development2017'
	)
mail = Mail(app)

#
# folder_path = "static/pdf-documents/doument.pdf"
# folder_name = os.path.basename(folder_path)
# pdf_name = folder_name + '.py'




@app.route("/Candidate/AddCandidate", methods = ['POST','GET'])
def CandidateAddDetails():
    if request.method =='GET':
    	return render_template('registrationForm.html')
    #
    # print("We're in son")
    # with open('templates/registrationForm.html') as f:
    #     pdfkit.from_file(f, 'test.pdf')



    if request.method =='POST':
        candidateTitle = request.form.get("title", default="Error")
        candidateFirstname = request.form.get("firstname", default="Error")
        candidateSecondname = request.form.get("surname", default="Error")
        candidateDob = request.form.get("dob", default="Error")
        candidateNI = request.form.get("nationalInsurance", default="Error")
        candidateAddress = request.form.get("candidateAddress", default="Error")
        candidateContactNumber = request.form.get("contactNumber", default="Error")
        candidateEmergencyNumber = request.form.get("emergencyContactNumber", default="Error")
        candidateEmail = request.form.get("email", default="Error")
        candidateTypeOfWork = request.form.get("work", default="Error")
        candidateQualifications = request.form.get("QualificationsandLicences", default="Error")
        candidateRepresenting = request.form.get("representingCompany", default="Error")
        candidateRepresentingName = request.form.get("representingCompanyName", default="Error")
        candidateAcceptance = request.form.get("acceptance", default="Error")


        # Candidate work elegibility questions
        candidateWorkElegibility = request.form.get("elegibilityChoice", default="Error")
        candidateDrivingLicense = request.form.get("drivingLicenseChoice", default="Error")
        candidateCriminalConvictions = request.form.get("criminaloffences", default="Error")
        candidateDisabilities = request.form.get("candidateDisabilities", default="Error")
        candidateDisabilityDetails = request.form.get("disabilityDescription", default="Error")

        # # Candidate's first refrence details
        candidateRefrence1Firstname = request.form.get("reference1Firstname", default="Error")
        candidateRefrence1Secondname = request.form.get("reference1Surname", default="Error")
        candidateRefrence1JobTitle = request.form.get("reference1JobTitle", default="Error")
        candidateRefrence1Company = request.form.get("reference1Company", default="Error")
        candidateRefrence1Address = request.form.get("reference1Address", default="Error")
        candidateRefrence1ContactNumber = request.form.get("reference1ContactNumber", default="Error")
        candidateRefrence1Email = request.form.get("reference1Email", default="Error")


        # # Candidate's second refrence details
        candidateRefrence2Firstname = request.form.get("reference2Firstname", default="Error")
        candidateRefrence2Secondname = request.form.get("reference2Surname", default="Error")
        candidateRefrence2JobTitle = request.form.get("reference2JobTitle", default="Error")
        candidateRefrence2Company = request.form.get("reference2Company", default="Error")
        candidateRefrence2Address = request.form.get("reference2Address", default="Error")
        candidateRefrence2ContactNumber = request.form.get("reference2ContactNumber", default="Error")
        candidateRefrence2Email = request.form.get("reference2Email", default="Error")


        # Do not share this token with anyone
        # dbx = dropbox.Dropbox('IXtRx8hFV-AAAAAAAAAAG2RtWRIM0QCKXfvOeV9fteYVzFsG4P3jfm7N7OLtqk3L')
        # dbx.users_get_current_account()
        # print(dbx.users_get_current_account())

        def allowed_file(filename):
            ext = filename.rsplit('.',1)[1]
            print(ext)
            return '.' in filename and ext in ALLOWED_EXTENSIONS

        filePath = 'no file upload so far'

        # We could also do a try & except here as well.

        msg = ''
        if request.method == 'POST':
            if 'file' not in request.files:
                msg = 'no file given'
            else:
                file = request.files['file']
                if file.filename == '':
                    msg = 'No file name'
                elif file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    filePath = os.path.join(app.config['UPLOAD_FOLDER_CV'], filename)
                file.save(filePath)
                msg1 = filePath

        msg = ''
        if request.method == 'POST':
            if 'file' not in request.files:
                msg = 'no file given'
            else:
                file = request.files['file2']
                if file.filename == '':
                    msg = 'No file name'
                elif file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    filePath = os.path.join(app.config['UPLOAD_FOLDER_qualifications'], filename)
                file.save(filePath)
                msg2 = filePath

        print("we're in the pdf function")
        pdf_name = candidateFirstname + ".pdf"
        # Save_pdf_filepath = os.path.join(os.path.expanduser("~"), "static/file_uploads/pdf_forms", pdf_name)

        # C:/Users/C1716791/Documents/Semester 1/IntroductionToWebDevelopment/AcornProject/static/file_uploads/pdf_forms

        c = canvas.Canvas(candidateFirstname + ".pdf")

        createPdf(c, candidateTitle, candidateFirstname,candidateSecondname,candidateDob,candidateNI,candidateAddress,candidateContactNumber, candidateEmergencyNumber, candidateEmail, candidateTypeOfWork, candidateQualifications, candidateRepresenting, candidateRepresentingName,
        candidateWorkElegibility, candidateDrivingLicense, candidateCriminalConvictions, candidateDisabilities,candidateDisabilityDetails,candidateRefrence1Firstname, candidateRefrence1Secondname, candidateRefrence1JobTitle, candidateRefrence1Company, candidateRefrence1Address, candidateRefrence1ContactNumber,
        candidateRefrence1Email, candidateRefrence2Firstname, candidateRefrence2Secondname, candidateRefrence2JobTitle,  candidateRefrence2Company, candidateRefrence2Address, candidateRefrence2ContactNumber, candidateRefrence2Email)

        # SUBJECT = "Email Data"
        #
        # msg = MIMEMultipart()
        # msg['Subject'] = SUBJECT
        # msg['From'] = 'nsadevelopment2017@gmail.com'
        # msg['To'] = 'vitzz.gaming@gmail.com'
        #
        # part = MIMEBase('application', "octet-stream")
        # part.set_payload(open("Mehdi.pdf", "rb").read())
        #
        # part.add_header('Content-Disposition', 'attachment; filename="Mehdi.pdf"')
        #
        # msg.attach(part)
        #
        # mail = smtplib.SMTP('smtp.gmail.com')
        # mail.sendmail('nsadevelopment2017@gmail.com','vitzz.gaming@gmail.com', msg.as_string())

	# MAIL_SERVER='smtp.gmail.com',
	# MAIL_PORT=465,
	# MAIL_USE_SSL=True,
	# MAIL_USERNAME = 'nsadevelopment2017@gmail.com',
	# MAIL_PASSWORD = 'development2017'
    #
    #
    #
    #     def send_mail():
    #         print("we're in the mail function")
    #         msg = Message("Send Mail Tutorial!",
    #         sender="nsadevelopment2017@gmail.com",
    #     	recipients=["vitzz.gaming@gmail.com"])
    #         msg.body = "Yo!\nHave you heard the good word of Python???"
    #         fp = open('Mehdi.pdf', 'rb')
    #         msgPdf = MIMEApplication(fp.read())
    #         msg.attach(msgPdf)
    #         fp.close()
    #
    #     send_mail()


        # def send_mail():
        #     msg = Message("Send Mail Tutorial!",
        #     sender="nsadevelopment2017@gmail.com",
        # 	recipients=["vitzz.gaming@gmail.com"])
        #     msg.body = "Yo!\nHave you heard the good word of Python???"
        #     filename=('Mehdi.pdf')
        #     fp=open(filename,'rb')
        #     att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
        #     fp.close()
        #     att.add_header('Hello','attachment',filename=filename)
        #     msg.attach(att)
        #     mail.send(msg)
        #     send_mail()
        # send_mail()

        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO CandidateDetails ('CandidateTitle','CandidateFirstname', 'CandidateSecondname','CandidateDateOfBirth','CandidateNI', 'CandidateAddress', 'CandidateContactNumber', 'CandidateEmergencyNumber', 'CandidateEmail', 'CandidateTypeOfWork', 'CandidateQualifications', 'CandidateRepresenting', 'CandidateRepresentingName', 'CandidateCVLocation','CandidateQualificationLocation',CandidateAcceptance)\
        			VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(candidateTitle, candidateFirstname, candidateSecondname, candidateDob, candidateNI, candidateAddress, candidateContactNumber, candidateEmergencyNumber, candidateEmail, candidateTypeOfWork, candidateQualifications, candidateRepresenting, candidateRepresentingName, msg1, msg2, candidateAcceptance) )

        cur.execute("INSERT INTO CandidateWorkElegibility ('CandidateWorkElegibility','CandidateDrivingLicense', 'CandidateCriminalConvictions', 'CandidateDisabilities', 'CandidateDisabilityDetails')\
                    VALUES (?,?,?,?,?)",(candidateWorkElegibility, candidateDrivingLicense, candidateCriminalConvictions, candidateDisabilities, candidateDisabilityDetails) )

        cur.execute("INSERT INTO CandidateRefrence1 ('RefrenceFirstname','RefrenceSecondname', 'RefrenceJobTitle', 'RefrenceCompany', 'RefrenceAddress' ,'RefrenceContact' , 'RefrenceEmail')\
                    VALUES (?,?,?,?,?,?,?)",(candidateRefrence1Firstname, candidateRefrence1Secondname, candidateRefrence1JobTitle, candidateRefrence1Company, candidateRefrence1Address, candidateRefrence1ContactNumber, candidateRefrence1Email) )

        cur.execute("INSERT INTO CandidateRefrence2 ('RefrenceFirstname','RefrenceSecondname', 'RefrenceJobTitle', 'RefrenceCompany', 'RefrenceAddress' ,'RefrenceContact' , 'RefrenceEmail')\
                    VALUES (?,?,?,?,?,?,?)",(candidateRefrence2Firstname, candidateRefrence2Secondname, candidateRefrence2JobTitle, candidateRefrence2Company, candidateRefrence2Address, candidateRefrence2ContactNumber, candidateRefrence2Email) )



        conn.commit()
        print("Candidate details successfully added")
        # except:
        # conn.rollback()
        # print("Error in insertion")
        # finally:
        conn.close()
        return render_template("thankyouPage.html")

        # File upload

    return "Hello2"
        # try:

# Source: For the creation of the Pdf document, I used the report lab module. https://www.reportlab.com/docs/reportlab-userguide.pdf Used on the 04/12/2017 at 22:07


def createPdf(c,candidateTitle, candidateFirstname,candidateSecondname,candidateDob,candidateNI,candidateAddress,candidateContactNumber, candidateEmergencyNumber, candidateEmail, candidateTypeOfWork, candidateQualifications, candidateRepresenting, candidateRepresentingName,
 candidateWorkElegibility, candidateDrivingLicense, candidateCriminalConvictions, candidateDisabilities,candidateDisabilityDetails,candidateRefrence1Firstname, candidateRefrence1Secondname, candidateRefrence1JobTitle, candidateRefrence1Company, candidateRefrence1Address, candidateRefrence1ContactNumber,
 candidateRefrence1Email, candidateRefrence2Firstname, candidateRefrence2Secondname, candidateRefrence2JobTitle,  candidateRefrence2Company, candidateRefrence2Address, candidateRefrence2ContactNumber, candidateRefrence2Email):

    c.drawImage(imageLocation, 10, 770)

    c.drawString(10,760, "Title: " + candidateTitle)
    c.drawString(150,760, "Firstname: " + candidateFirstname)
    c.drawString(330,760, "Secondname: " + candidateSecondname)
    c.drawString(10,740, "Date of birth: " + candidateDob)
    c.drawString(200,740, "National Insurance Number: " + candidateNI)
    c.drawString(10,720, "Address: " + candidateAddress)
    c.drawString(10,700, "Contact Number: " + candidateContactNumber)
    c.drawString(250,700, "Emergency contact Number: " + candidateEmergencyNumber)
    c.drawString(10,664, "Email: " + candidateEmail)
    c.drawString(10,650, "Type of work required: " + candidateTypeOfWork)
    c.drawString(10,620, "Qualifications: " + candidateQualifications)
    c.drawString(200,620, "Company Representing: " + candidateRepresenting)


    c.drawString(10,590, "Work Elegibility: " + candidateWorkElegibility)
    c.drawString(200,590, "Driving Licence: " + candidateDrivingLicense)
    c.drawString(10,540, "Criminal Convictions: " + candidateCriminalConvictions)
    c.drawString(250,540, "Disabilities: " + candidateDisabilities)
    c.drawString(10,500, "Disability Details: " + candidateDisabilityDetails)


    c.drawString(10,460, "Refrence 1 Firstname: " + candidateRefrence1Firstname)
    c.drawString(300,460, "Refrence 2 Firstname: " + candidateRefrence2Firstname)

    c.drawString(10,440, "Refrence 1 Surname: " + candidateRefrence1Secondname)
    c.drawString(300,440, "Refrence 2 Secondname: " + candidateRefrence2Secondname)


    c.drawString(10,420, "Refrence 1 Job Title: " + candidateRefrence1JobTitle)
    c.drawString(300,420, "Refrence 2 Job Title: " + candidateRefrence2JobTitle)


    c.drawString(10,400, "Refrence 1 Company: " + candidateRefrence1Company)
    c.drawString(300,400, "Refrence 2 Company: " + candidateRefrence2Company)


    c.drawString(10,380, "Refrence 1 Address: " + candidateRefrence1Address)
    c.drawString(300,380, "Refrence 2 Address: " + candidateRefrence2Address)


    c.drawString(10,360, "Refrence 1 Contact Number: " + candidateRefrence1ContactNumber)
    c.drawString(300,360, "Refrence 2 Contact Number: " + candidateRefrence2ContactNumber)

    c.drawString(10,340, "Refrence 1 Email: " + candidateRefrence1Email)
    c.drawString(300,340, "Refrence 2 Email: " + candidateRefrence2Email)

    c.showPage()
    c.save()






@app.route("/Candidate/Registration", methods = ['POST','GET'])
def UserLogin():
    if request.method == 'GET':
        return render_template('loginRegistration.html')
    if request.method == 'POST':
        UserFirstname = request.form.get("userFirstname", default="Error")
        UserSurname = request.form.get("userSurname", default="Error")
        UserEmail = request.form.get("UserEmail", default="Error")
        username = request.form.get("Username", default="Error")
        password = request.form.get("Userpassword", default="Error")
        timeAccessed = str(now)

        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO UserLogins ('UserFirstname','UserSurname', 'UserEmail', 'Username', 'Password', 'DateLastAccessed')\
					VALUES (?,?,?,?,?,?)",(UserFirstname, UserSurname, UserEmail, username, password, timeAccessed) )

        conn.commit()
        print("User added")
        conn.close()
        return "Hello"

    return "Hello2"




@app.route("/Login/UserLogin", methods = ['GET'])
def UserLoginPage():
    if request.method =='GET':
    	return render_template('login_page.html')

@app.route("/Admin", methods = ['GET','POST'])
def adminpage():
    if request.method =='GET':
    	return render_template('admin.html')
    def CandidateAddress():
        con = sql.connect("CandidateCenter.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("SELECT CandidateAddress FROM CandidateDetails")

        rows = cur.fetchall();
        return render_template("admin.html",rows = rows)
    if request.method == 'POST':
        def CandidateAddress():
            con = sql.connect("CandidateCenter.db")
            con.row_factory = sql.Row

            cur = con.cursor()
            cur.execute("SELECT CandidateAddress FROM CandidateDetails")

            rows = cur.fetchall();
            return render_template("admin.html",rows = rows)

@app.route("/CandidateDatabase", methods=['GET'])
def database():
    if request.method=='GET':
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT * FROM CandidateDetails")
        data = cur.fetchall()
        return render_template("Candidatedatabase.html", data=data)

@app.route("/CandidateRefrence1", methods=['GET'])
def database2():
    if request.method=='GET':
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT * FROM CandidateRefrence1")
        data = cur.fetchall()
        return render_template("CandidateRefrence1.html", data=data)

@app.route("/CandidateRefrence2", methods=['GET'])
def database3():
    if request.method=='GET':
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT * FROM CandidateRefrence2")
        data = cur.fetchall()
        return render_template("CandidateRefrence2.html", data=data)

@app.route("/CandidateWorkElegibility", methods=['GET'])
def database4():
    if request.method=='GET':
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT * FROM CandidateWorkElegibility")
        data = cur.fetchall()
        return render_template("CandidateWorkElegibility.html", data=data)


# @app.route("/Graphs", methods=['GET','POST'])
# def graphs():
#     if request.method=='GET':
#         return render_template("graphs.html")
#     if request.method =='POST':
#         def chart():
#             labels = ["January","February","March","April","May","June","July","August"]
#             values = [10,9,8,7,6,4,7,8]
#             colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
#             return render_template('graphs.html', set=zip(values, labels, colors))

@app.route("/Graphs")
def chart():
	legend = 'Monthly Candidates'
	labels = ["September", "October", "November", "December"]
	values = [0, 0, 28, 76]

	legend2 = 'Candidates elegible to work in the UK'
	labels2 = ["Not elegible to work in the UK", "Elegible to work in the UK"]
	values2 = [1, 102]

	legend3 = 'Candidates with criminal convictions'
	labels3 = ["Without convictions", "With convictions"]
	values3 = [0, 103]

	legend4 = 'Candidates with diabilities'
	labels4 = ["Without disabilities", "With disabilities"]
	values4 = [4, 100]

	return render_template('graphs.html', values=values, labels=labels, legend=legend, values2=values2, labels2=labels2, legend2=legend2, values3=values3, labels3=labels3, legend3=legend3, values4=values4, labels4=labels4, legend4=legend4)


@app.route("/Maps", methods=['GET'])
def maps():
    if request.method=='GET':
		# conn = sqlite3.connect(DATABASE)
        # cur = conn.cursor()
        # cur.execute("SELECT CandidateAddress FROM CandidateDetails")
        # data = cur.fetchall()
        return render_template("maps.html")

@app.route("/Statistics", methods=['GET'])
def stats():
    if request.method=='GET':
        return render_template("statistics.html")


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="0.0.0.0", debug=True)
	# app.run(host='0.0.0.0', port=5001)
