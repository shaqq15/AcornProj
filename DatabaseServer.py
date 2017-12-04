import os
from flask import Flask, redirect, request, render_template, url_for, make_response, send_file
from werkzeug.utils import secure_filename
import sqlite3
import datetime
# import pdfkit
from reportlab.pdfgen import canvas



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
        import StringIO
        
        html = render_template('registrationForm.html')
        return render_pdf(HTML(string=html))









        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO CandidateDetails ('CandidateTitle','CandidateFirstname', 'CandidateSecondname','CandidateDateOfBirth','CandidateNI', 'CandidateAddress', 'CandidateContactNumber', 'CandidateEmergencyNumber', 'CandidateEmail', 'CandidateTypeOfWork', 'CandidateQualifications', 'CandidateRepresenting','CandidateCVLocation','CandidateQualificationLocation')\
        			VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(candidateTitle, candidateFirstname, candidateSecondname, candidateDob, candidateNI, candidateAddress, candidateContactNumber, candidateEmergencyNumber, candidateEmail, candidateTypeOfWork, candidateQualifications, candidateRepresenting, msg1, msg2) )

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




    #
    # def pdf():
    #     print("we're in the pdf function")
    #     output = cStringIO.StringIO()
    #     doc = SimpleDocTemplate("registrationForm.html",pagesize=letter)
    #     Story=[]
    #
    #     Story.append(Paragraph(ptext, styles["Justify"]))
    #
    #     doc.build(Story)
    #     pdf_out = output.getvalue()
    #     output.close()
    #
    #     response = make_response(pdf_out)
    #     response.headers['Content-Disposition'] = "attachment; filename='test.pdf"
    #     response.mimetype = 'static/pdf-documents'
    #     return send_file('registrationForm.html', as_attachment=True)
    # def render_pdf_weasyprint(html):
    #
    #     from weasyprint import HTML
    #     pdf = HTML(string=html.encode('utf-8'))
    #     return pdf.write_pdf()
    #
    #
    #     def render_pdf_xhtml2pdf(html):
    #         """mimerender helper to render a PDF from HTML using xhtml2pdf.
    #         Usage: http://philfreo.com/blog/render-a-pdf-from-html-using-xhtml2pdf-and-mimerender-in-flask/
    #             """
    #         from xhtml2pdf import pisa
    #         from cStringIO import StringIO
    #         pdf = StringIO()
    #         pisa.CreatePDF(StringIO(html.encode('utf-8')), pdf)
    #         resp = pdf.getvalue()
    #         pdf.close()
    #         return resp
    #
    #     def pdf():
    #
    #
    #
    #     pdfkit.from_url('http://127.0.0.1:5000/static/registrationForm.html','examplePDF.pdf')
    #
    #
    #     def render_pdf(html):
    #         from xhtml2pdf import pisa
    #         from cStringIO import StringIO
    #         pdf = StringIO()
    #         pisa.CreatePDF(StringIO(html.encode('utf-8')), pdf)
    #         resp = pdf.getvalue()
    #         pdf.close()
    #         return resp
    #     @mimerender(default='html', html=lambda html: html, pdf=render_pdf, override_input_key='format')
    #     def view_invoice(org_id, invoice_id):
    #         html = render_template('registrationForm.html', id=invoice_id)
    #         return { 'html': html }

        # def your_view():
        #     print("We're in the pdf file uplaod code!")
        #     subject = "Mail with PDF"
        #     receiver = "vitzz.gaming@gmail.com"
        #     print("PDF document has been sent")
        #     mail_to_be_sent = Message(subject=subject, recipients=[receiver])
        #     mail_to_be_sent.body = "This email contains PDF."
        #     pdf = create_pdf(render_template('registrationForm.html'))
        #     mail_to_be_sent.attach("file.pdf", "static/pdf-documents", pdf.getvalue())
        #     mail_ext.send(mail_to_be_sent)
        #     return redirect(url_for('other_view'))


                #
                #
                # print("we're in the pdf function")
                # output = StringIO()
                #
                # p = canvas.Canvas(output)
                # p.drawString(100, 100, 'Hello')
                # p.showPage()
                # p.save()
                #
                # pdf_out = output.getvalue()
                # output.close()
                #
                # response = make_response(pdf_out)
                # response.headers['Content-Disposition'] = "attachment; filename='test.pdf"
                # response.mimetype = 'application/pdf'
                # return response


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



if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="0.0.0.0", debug=True)
