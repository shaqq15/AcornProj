import os
from flask import Flask, redirect, request, render_template
import sqlite3
# import pdfkit

# pdfkit.from_url('http://127.0.0.1:5000/static/registrationForm.html','examplePDF.pdf')

DATABASE = "CandidateCenter.db"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

@app.route("/Candidte/AddCandidate", methods = ['POST','GET'])
def CandidateAddDetails():
    if request.method =='GET':
    	return render_template('registrationForm.html')
    if request.method =='POST':
        candidateTitle = request.form.get("title", default="Error")
        candidateFirstname = request.form.get("firstname", default="Error")
        candidateSecondname = request.form.get("Secondname", default="Error")
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
        return "Hello"

    return "Hello2"


if __name__ == "__main__":
    app.run(debug=True)
