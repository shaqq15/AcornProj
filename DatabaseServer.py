import os
from flask import Flask, redirect, request, render_template
import sqlite3
import datetime
# import pdfkit

# pdfkit.from_url('http://127.0.0.1:5000/static/registrationForm.html','examplePDF.pdf')

now = datetime.datetime.now()
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT,'../static/file_uploads')

DATABASE = "CandidateCenter.db"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['../static/file_uploads']=UPLOAD_FOLDER

@app.route("/Candidate/AddCandidate", methods = ['POST','GET'])
def CandidateAddDetails():
    if request.method =='GET':
    	return render_template('registrationForm.html')
    if request.method =='POST':
        candidateTitle = request.form.get("title", default="Error")
        candidateFirstname = request.form.get("firstname", default="Error")
        candidateSecondname = request.form.get("surname", default="Error")
        candidateFirstlineAddress = request.form.get("CandidateAddress1", default="Error")
        candidateSecondlineAddress = request.form.get("CandidateAddress2", default="Error")
        candidatePostcode = request.form.get("CandidatePostcode", default="Error")
        candidateContactNumber = request.form.get("contactNumber", default="Error")
        candidateEmergencyNumber = request.form.get("emergencyContactNumber", default="Error")
        candidateEmail = request.form.get("email", default="Error")
        candidateTypeOfWork = request.form.get("work", default="Error")
        candidateQualifications = request.form.get("QualificationsandLicences", default="Error")
        candidateRepresenting = request.form.get("representingCompany", default="Error")

        # Candidate work elegibility questions
        candidateWorkElegibility = request.form.get("elegibilityChoice", default="Error")
        candidateDrivingLicense = request.form.get("drivingLicenseChoice", default="Error")
        candidateCriminalConvictions = request.form.get("criminaloffences", default="Error")
        candidateDisabilities = request.form.get("candidateDisabilities", default="Error")
        candidateDisabilityDetails = request.form.get("disabilityDescription", default="Error")

        # # Candidate's first refrence details
        candidateRefrence1Firstname = request.form.get("refrence1Firstname", default="Error")
        candidateRefrence1Secondname = request.form.get("refrence1Secondname", default="Error")
        candidateRefrence1JobTitle = request.form.get("refrence1JobTitle", default="Error")
        candidateRefrence1Company = request.form.get("refrence1Company", default="Error")
        candidateRefrence1AddressLine1 = request.form.get("refrence1Address1", default="Error")
        candidateRefrence1AddressLine2 = request.form.get("refrence1Address2", default="Error")
        candidateRefrence1Postcode = request.form.get("refrence1Postcode", default="Error")
        candidateRefrence1ContactNumber = request.form.get("refrence1ContactNumber", default="Error")
        candidateRefrence1Email = request.form.get("refrence1Email", default="Error")


        # # Candidate's second refrence details
        candidateRefrence2Firstname = request.form.get("refrence1Firstname", default="Error")
        candidateRefrence2Secondname = request.form.get("refrence1Secondname", default="Error")
        candidateRefrence2JobTitle = request.form.get("refrence2JobTitle", default="Error")
        candidateRefrence2Company = request.form.get("refrence2Company", default="Error")
        candidateRefrence2AddressLine1 = request.form.get("refrence2Address1", default="Error")
        candidateRefrence2AddressLine2 = request.form.get("refrence2Address2", default="Error")
        candidateRefrence2Postcode = request.form.get("refrence2Postcode", default="Error")
        candidateRefrence2ContactNumber = request.form.get("refrence2ContactNumber", default="Error")
        candidateRefrence2Email = request.form.get("refrence2Email", default="Error")

        # try:

        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO CandidateDetails ('CandidateTitle','CandidateFirstname', 'CandidateSecondname', 'CandidateFirstlineAddress', 'CandidateSecondlineAddress', 'CandidatePostcode', 'CandidateContactNumber', 'CandidateEmergencyNumber', 'CandidateEmail', 'CandidateTypeOfWork', 'CandidateQualifications', 'CandidateRepresenting')\
					VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(candidateTitle, candidateFirstname, candidateSecondname, candidateFirstlineAddress, candidateSecondlineAddress, candidatePostcode, candidateContactNumber, candidateEmergencyNumber, candidateEmail, candidateTypeOfWork, candidateQualifications, candidateRepresenting) )

        cur.execute("INSERT INTO CandidateWorkElegibility ('CandidateWorkElegibility','CandidateDrivingLicense', 'CandidateCriminalConvictions', 'CandidateDisabilities', 'CandidateDisabilityDetails')\
            		VALUES (?,?,?,?,?)",(candidateWorkElegibility, candidateDrivingLicense, candidateCriminalConvictions, candidateDisabilities, candidateDisabilityDetails) )

        cur.execute("INSERT INTO CandidateRefrence1 ('RefrenceFirstname','RefrenceSecondname', 'RefrenceJobTitle', 'RefrenceCompany', 'RefrenceAddress1' ,'RefrenceAddress2', 'RefrencePostcode','RefrenceContact' , 'RefrenceEmail')\
            		VALUES (?,?,?,?,?,?,?,?,?)",(candidateRefrence1Firstname, candidateRefrence1Secondname, candidateRefrence1JobTitle, candidateRefrence1Company, candidateRefrence1AddressLine1, candidateRefrence1AddressLine2, candidateRefrence1Postcode, candidateRefrence1ContactNumber, candidateRefrence1Email) )

        cur.execute("INSERT INTO CandidateRefrence2 ('RefrenceFirstname','RefrenceSecondname', 'RefrenceJobTitle', 'RefrenceCompany', 'RefrenceAddress1' ,'RefrenceAddress2', 'RefrencePostcode','RefrenceContact' , 'RefrenceEmail')\
                    VALUES (?,?,?,?,?,?,?,?,?)",(candidateRefrence2Firstname, candidateRefrence2Secondname, candidateRefrence2JobTitle, candidateRefrence2Company, candidateRefrence2AddressLine1, candidateRefrence2AddressLine2, candidateRefrence2Postcode, candidateRefrence2ContactNumber, candidateRefrence2Email) )

        conn.commit()
        print("Candidate details successfully added")
        # except:
        # conn.rollback()
        # print("Error in insertion")
        # finally:
        conn.close()
        return render_template("thankyouPage.html")

    return "Hello2"

def allowed_file(filename):
    ext = filename.rsplit('.',1)[1]
    print(ext)
    return '.' in filename and ext in ALLOWED_EXTENSIONS


@app.route("/", methods = ['POST','GET'])
def file_upload():
    msg = ''
    if request.method == 'POST':
        if 'file' not in request.files:
            msg = 'No file given'
        else:
            file = request.files.['file']
            if file.filename =="":
                msg='no file name'
            elif file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filePath = os.path.join(app.config/['file_uploads'], filename)
            file.save(filePath)
            msg=filePath
        return render_template('thankyouPage.html', msg=msg)


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

@app.route("/Admin", methods = ['GET'])
def adminpage():
    if request.method =='GET':
    	return render_template('admin.html')

if __name__ == "__main__":
    app.run(debug=True)
