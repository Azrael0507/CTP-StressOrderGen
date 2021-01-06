# -*- coding: utf-8 -*-
from MyApi import *
import datetime
import time
import thosttraderapi as api


class CTradeSpi(api.CThostFtdcTraderSpi):
	myapi=''
	def __init__(self,myapi):
		api.CThostFtdcTraderSpi.__init__(self)
		self.myapi=myapi
		
	def OnFrontConnected(self) -> "void":
		print ("receive OnFrontConnected")
		self.myapi.ReqAuth()
		
	def OnRspAuthenticate(self, pRspAuthenticateField: 'CThostFtdcRspAuthenticateField', pRspInfo: 'CThostFtdcRspInfoField', nRequestID: 'int', bIsLast: 'bool') -> "void":	
		PrintReName("OnRspAuthenticate")
		PrintReMsg(pRspInfo)
		self.myapi.ReqLogin()
		
	def OnRspUserLogin(self, pRspUserLogin: 'CThostFtdcRspUserLoginField', pRspInfo: 'CThostFtdcRspInfoField', nRequestID: 'int', bIsLast: 'bool') -> "void":
		PrintReName("OnRspUserLogin")
		print ("ErrorID=", pRspInfo.ErrorID, "ErrorMsg=", pRspInfo.ErrorMsg)
		self.myapi.loginflag = True

		
	def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm: 'CThostFtdcSettlementInfoConfirmField', pRspInfo: 'CThostFtdcRspInfoField', nRequestID: 'int', bIsLast: 'bool') -> "void":
		PrintReName("OnRspSettlementInfoConfirm")
		PrintReMsg(pRspInfo)
		self.myapi.settleconfirm = True

'''
	def OnRspOrderInsert(self, pInputOrder: 'CThostFtdcInputOrderField', pRspInfo: 'CThostFtdcRspInfoField', nRequestID: 'int', bIsLast: 'bool') -> "void":
		PrintReName("OnRspOrderInsert")
		PrintReMsg(pRspInfo)

	def OnErrRtnOrderInsert(self, pInputOrder: 'CThostFtdcInputOrderField', pRspInfo: 'CThostFtdcRspInfoField') -> "void":
		PrintReName("OnErrRtnOrderInsert")
		PrintReMsg(pRspInfo)

	def OnRtnOrder(self, pOrder: 'CThostFtdcOrderField') -> "void":
		#self.endtime=datetime.datetime.now()
		#self.orrecount=self.orrecount + 1
		#print("原始回报时间：", datetime.datetime.now())
		#print("报单返回所用毫秒:", (datetime.datetime.now()-self.myapi.starttime).microseconds / 1000, "ms")
		#print("orrecount:", self.orrecount)
		PrintReName("OnRtnOrder")
		print("InstrumentID=", pOrder.InstrumentID,\
		"OrderRef=", pOrder.OrderRef,\
		"Direction=", pOrder.Direction,\
		"LimitPrice=", pOrder.LimitPrice,\
		"VolumeTotalOriginal=", pOrder.VolumeTotalOriginal,\
		"OrderStatus=", pOrder.OrderStatus)
'''
		

#静态处理方法内容
#打印排错返错信息
def PrintReMsg(pRspInfo):
	if pRspInfo is not None:
		print ("ErrorID=", pRspInfo.ErrorID, "ErrorMsg=", pRspInfo.ErrorMsg)
	else:
		print ("ErrorID= null ErrorMsg= null")
		return 1

def PrintReName(rename):
	print("receive", rename)