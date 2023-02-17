#import libraries
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from flask import Flask,render_template, request, jsonify
from flask_cors import CORS,cross_origin
import requests
import time
import datetime
import json
from selenium import webdriver
import pandas as pd
import smtplib
import jinja2
import selenium.webdriver.chrome.service as service
#import pdfkit

application=Flask(__name__)

@application.route('/')
def welcome():
	return render_template("index.html")

def a(b):
    return 

def c():
    a("l")
    return

c()
print("prathys")

def final_page():
	return render_template("result.html",course=4,sub_course=4,program=4,description=4,mentors=4)

final_page()


if __name__=="__main__":
	application.run(host="0.0.0.0",port=5000)