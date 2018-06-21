# -*- coding: utf-8 -*- 

from django.db import connection

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

#from .models import Question
from .authmodels import GlobalDefaultMsgRuleInfo, GlobalMsgRuleInfo, TsinfoGlobal
from .models import Countrycodeinfo, Transmissioninfo

# Create your views here.


countrySelList = 0
countrySelCode = 0 
transSelList = 0
transSelCode = 0

viewFlag=0

def getCountryTransInfo() :
	global countrySelList
	global transSelList

	countrySelList = Countrycodeinfo.objects.using('default').all()
	transSelList = Transmissioninfo.objects.using('default').all()

	selInfo = {'countrySelList' : countrySelList,
				'transSelList' : transSelList}

	return selInfo

def getSelCodeInfo():
	global countrySelCode
	global transSelCode

	selCode = {'countrySelCode' : countrySelCode,
				'transSelCode' : transSelCode}

	return selCode


def index(request):
	global countrySelCode
	global transSelCode

	countrySelCode = 0
	transSelCode = 0

	selInfo = getCountryTransInfo()
	selCode = getSelCodeInfo()

	context = {'selInfo' : selInfo,
				'selCode' : selCode}

	return render (request, 'setMsg/base.html', context)

def defaultView(request):
	print ("default_view")

	global countrySelList, countrySelCode
	global transSelList, transSelCode
	global viewFlag


	if request.POST.has_key('country_sel') :
		countrySelCode = request.POST['country_sel']

	if request.POST.has_key('trans_sel') :
		transSelCode = request.POST['trans_sel']

	trans = Transmissioninfo.objects.using('default').get(trans_code = transSelCode)
	country = Countrycodeinfo.objects.using('default').get(country_code = countrySelCode)

	query = '''select *
			   from global_default_msg_rule_info A join tsinfo_global B on A.ts_code = B.ts_code
			   where country_code = %s and tsg_id = %s'''

	defaultRuleInfo = GlobalDefaultMsgRuleInfo.objects.raw(query, [countrySelCode, trans.tsg_id])

	selInfo = getCountryTransInfo()
	selCode = getSelCodeInfo()

	context = {'selInfo' : selInfo,
				'selCode' : selCode,
				'trans_name' : trans.trans_name,
				'defaultRuleInfo': defaultRuleInfo,
				'country_name' : country.country_name,
				'viewFlag' : viewFlag}

	return render(request, 'setMsg/post.html', context)

def defaultDetail(request, ts_code):
	print ("defaultDetail")

	global countrySelList, countrySelCode
	global transSelList, transSelCode

	global_msg = get_object_or_404(GlobalDefaultMsgRuleInfo, country_code = countrySelCode, ts_code = ts_code)

	selInfo = getCountryTransInfo()
	selCode = getSelCodeInfo()

	context = {'selInfo' : selInfo,
				'selCode' : selCode,
				'global_msg' : global_msg}

	return render (request, 'setMsg/default_detail.html', context)

def customView(request):
	print ("customView")

	global countrySelList, countrySelCode
	global transSelList, transSelCode
	global viewFlag

	trans = Transmissioninfo.objects.using('default').get(trans_code = transSelCode)
	country = Countrycodeinfo.objects.using('default').get(country_code = countrySelCode)

	query = '''select *
			   from global_msg_rule_info A join tsinfo_global B on A.ts_code = B.ts_code
			   where country_code = %s and tsg_id = %s'''

	msgRuleInfo = GlobalMsgRuleInfo.objects.raw(query, [countrySelCode, trans.tsg_id])

	selInfo = getCountryTransInfo()
	selCode = getSelCodeInfo()

	context = {'selInfo' : selInfo,
				'selCode' : selCode,
				'msgRuleInfo': msgRuleInfo,
				'country_name' : country.country_name,
				'trans_name' : trans.trans_name,
				'viewFlag' : viewFlag}

	return render (request, 'setMsg/custom.html', context)

def customDetail(request, ts_code):
	print ("default_detail")

	global countrySelList, countrySelCode
	global transSelList, transSelCode

	global_msg = get_object_or_404(GlobalDefaultMsgRuleInfo, countrySelCode = countrySelCode, ts_code = ts_code)

	context = {'global_msg' : global_msg,
				'countrySelCode' : countrySelCode,
				'countrySelList' : countrySelList,
				'transSelCode' : transSelCode,
				'transSelList' : transSelList}

	return render (request, 'setMsg/default_detail.html', context)


def insert(request):
	countrySelCode = request.POST['countrySelCode']
	ts_code = request.POST['ts_code']
	global_msg = GlobalDefaultMsgRuleInfo (countrySelCode=countrySelCode, ts_code=ts_code)
	global_msg.save()

	return HttpResponseRedirect("/setMsg")
	
def delete (request, countrySelCode, ts_code):
	global_msg = get_object_or_404(GlobalDefaultMsgRuleInfo, countrySelCode = countrySelCode, ts_code = ts_code)

	return HttpResponseRedirect("/setMsg")
