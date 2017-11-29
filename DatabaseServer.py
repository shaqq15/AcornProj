import os
from flask import Flask, redirect, request, render_template, url_for
import dropbox
from werkzeug.utils import secure_filename
import sqlite3
import datetime

# HTML('http://127.0.0.1:5000/Candidate/AddCandidate').write_pdf('static/sample.pdf')
# pdfkit.from_url('http://127.0.0.1:5000/static/registrationForm.html','examplePDF.pdf')

now = datetime.datetime.now()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT,'static/file_uploads')

DATABASE = "CandidateCenter.db"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/Candidate/AddCandidate", methods = ['POST','GET'])
def CandidateAddDetails():
    if request.method =='GET':
    	return render_template('registrationForm.html')
    if request.method =='POST':
        candidateTitle = request.form.get("title", default="Error")
        candidateFirstname = request.form.get("firstname", default="Error")
        candidateSecondname = request.form.get("surname", default="Error")
        candidateAddress = request.form.get("candidateAddress", default="Error")
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
        candidateRefrence1Firstname = request.form.get("reference1Firstname", default="Error")
        candidateRefrence1Secondname = request.form.get("reference1Surname", default="Error")
        candidateRefrence1JobTitle = request.form.get("reference1JobTitle", default="Error")
        candidateRefrence1Company = request.form.get("reference1Company", default="Error")
        candidateRefrence1AddressLine1 = request.form.get("reference1Address1", default="Error")
        candidateRefrence1AddressLine2 = request.form.get("reference1Address2", default="Error")
        candidateRefrence1Postcode = request.form.get("reference1Postcode", default="Error")
        candidateRefrence1ContactNumber = request.form.get("reference1ContactNumber", default="Error")
        candidateRefrence1Email = request.form.get("reference1Email", default="Error")


        # # Candidate's second refrence details
        candidateRefrence2Firstname = request.form.get("reference2Firstname", default="Error")
        candidateRefrence2Secondname = request.form.get("reference2Surname", default="Error")
        candidateRefrence2JobTitle = request.form.get("reference2JobTitle", default="Error")
        candidateRefrence2Company = request.form.get("reference2Company", default="Error")
        candidateRefrence2AddressLine1 = request.form.get("reference2Address1", default="Error")
        candidateRefrence2AddressLine2 = request.form.get("reference2Address2", default="Error")
        candidateRefrence2Postcode = request.form.get("reference2Postcode", default="Error")
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
                    filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filePath)
                msg = filePath

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
                    filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filePath)
                msg = filePath





        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO CandidateDetails ('CandidateTitle','CandidateFirstname', 'CandidateSecondname', 'CandidateAddress', 'CandidateContactNumber', 'CandidateEmergencyNumber', 'CandidateEmail', 'CandidateTypeOfWork', 'CandidateQualifications', 'CandidateRepresenting')\
        			VALUES (?,?,?,?,?,?,?,?,?,?)",(candidateTitle, candidateFirstname, candidateSecondname, candidateAddress, candidateContactNumber, candidateEmergencyNumber, candidateEmail, candidateTypeOfWork, candidateQualifications, candidateRepresenting) )

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

        # File upload

    return "Hello2"
        # try:








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


# PDF convert code
#
# class Pdf():
#
#     def render_pdf(self, name, html):
#
#         from xhtml2pdf import pisa
#         from StringIO import StringIO
#
#         pdf = StringIO()
#
#         pisa.CreatePDF(StringIO(html), pdf)
#
#         return pdf.getvalue()
#
#
# @app.route('/pdf/Candidate', methods=['GET'])
# def candidate_form(candidate, tin):
#
#     #pdf = StringIO()
#     html = render_template('registrationForm.html', business_name=business_name, tin=tin)
#     file_class = Pdf()
#     pdf = file_class.render_pdf(candidate, html)
#     headers = {
#         'content-type': 'application.pdf',
#         'content-disposition': 'attachment; filename=form.pdf'}
#     return pdf, 200, headers


        #
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        # file = request.files['file']
        # print("We have started the uploading process")
        # # if user does not select file, browser also
        # # submit a empty part without filename
        # if file.filename == '':
        #     print("We have started looking for the file")
        #     flash('No selected file')
        #     return redirect(request.url)
        # if file and allowed_file(file.filename):
        #     print("We have nearly uploaded the file.")
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     return redirect(url_for('uploaded_file',
        #                             filename=filename))


















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
