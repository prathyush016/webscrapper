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


#e_sub_name=[]
course_list=[]
course_list.clear()
D=[]
d2=[]
file1 = open("myfile.txt", "w")

def sub_course(e,e_sub_name,sub_course_url):
	
	sub_uclient = uReq(str(sub_course_url))
	#sub_uclient=driver.get('sub_course_url')

	sub_course_page = sub_uclient.read()
	sub_uclient.close()
	sub_course_beautify=bs(sub_course_page,"html.parser")
	c1=json.loads(sub_course_beautify.find('script',{"id": "__NEXT_DATA__"}).get_text())
	d1=len(list(c1['props']['pageProps']['initialState']['filter']['initCourses']))
	for q in range(d1):
		sub_course_title=c1['props']['pageProps']['initialState']['filter']['initCourses'][q]['title']
		course_description=c1['props']['pageProps']['initialState']['filter']['initCourses'][q]['description']
		number_of_mentors=len(c1['props']['pageProps']['initialState']['filter']['initCourses'][q]['instructorsDetails'])
		mentor_name=str()
		for l in range(number_of_mentors):
			mentor_name1=c1['props']['pageProps']['initialState']['filter']['initCourses'][q]['instructorsDetails'][l]['name']
			if len(mentor_name1)==0:
				1==1
			else:
				mentor_name2=str(mentor_name1+',')
				mentor_name=mentor_name+mentor_name2
		str1=e+'|'+e_sub_name+'|'+sub_course_title+'|'+course_description+'|'+mentor_name
		file1.writelines(str1+"\n")
		
		
		d2.append([e,e_sub_name,sub_course_title,course_description,mentor_name])
		#return render_template("result.html",course=e,sub_course=e_sub_name,program=sub_course_title,description=course_description,mentors=mentor_name)
	return "sub courses list complete"

@application.route('/courses',methods=['GET','POST'])
def main_course():
	url = 'https://ineuron.ai/'
	uclient = uReq(url)
	iNeuron_page = uclient.read()
	uclient.close()
	iNeuron_beautify=bs(iNeuron_page,"html.parser")
	c=json.loads(iNeuron_beautify.find('script',{"id": "__NEXT_DATA__"}).get_text())
	d=list(c['props']['pageProps']['initialState']['init']['categories'].keys())
		
	for i in d:
		e=c['props']['pageProps']['initialState']['init']['categories'][str(i)]['title']
		e_sub=list(c['props']['pageProps']['initialState']['init']['categories'][str(i)]['subCategories'])
		for m in e_sub:
			e_sub_name=c['props']['pageProps']['initialState']['init']['categories'][str(i)]['subCategories'][str(m)]['title']
			e_sub_name1=str(e_sub_name).replace(" ","-")
			sub_course_url=url+'category/'+str(e_sub_name1)
			n=e+'|'+e_sub_name+'|'+sub_course_url
			course_list.append(n)
			sub_course(e,e_sub_name,sub_course_url)
			
	return render_template("results.html", len = len(d2), d2 = d2)

if __name__=="__main__":
	application.run(host="0.0.0.0",port=5000)

