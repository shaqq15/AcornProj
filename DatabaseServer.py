import os
from flask import Flask, redirect, request, render_template
import sqlite3


@app.route("/Candidte/AddCandidate", methods = ['POST','GET'])
def CandidateAddDetails():
