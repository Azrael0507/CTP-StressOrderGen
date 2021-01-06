# -*- coding: utf-8 -*-
from MySpi import *
import datetime
import thosttraderapi as api
import configparser

configins=configparser.ConfigParser()
configins.read('config.ini')
#Addr
FrontAddr=configins['network']['tradefront']
#AuthInfo
APPID=configins['authinfo']['appid']
AUTHCODE=configins['authinfo']['authcode']
#LoginInfo
BROKERID=configins['baseinfo']['brokerid']
PASSWORD=configins['baseinfo']['password']
#OrderInfo
EXCHANGEID=configins['ordercon']['exid']
INSTRUMENTID=configins['ordercon']['instrid']
ORDERTYPE=configins['ordercon']['orprtype']
#DIRECTION=configins['ordercon']['direction']
#OFFSET=configins['ordercon']['offsetflag']
HEDGEFLAG=configins['ordercon']['hedgeflag']
PRICE=float(configins['ordercon']['limitprice'])
VOLUME=int(configins['ordercon']['volumetotorg'])
MINVOL=int(configins['ordercon']['minvol'])
STOPPRICE=float(configins['ordercon']['stopprice'])
VOLUMECONDITION=configins['ordercon']['volumecon']
CONTIGENCON=configins['ordercon']['contingencon']
#stressconfig
insertfreq = configins['stressconfig']['insertfreq']
oneturnsleep = float(insertfreq)


class CTradeApi(api.CThostFtdcTraderApi):
	def __init__(self):
		self.tspi=''
		self.tapi=''
		self.invid=''
		self.loginflag = False
		self.settleconfirm = False

	def start(self, invid):
		self.invid = invid
		#print("in start" + self.invid)
		self.tapi=api.CThostFtdcTraderApi.CreateFtdcTraderApi()
		self.tspi=CTradeSpi(self)
		self.tapi.RegisterFront(FrontAddr)
		#print(FrontAddr)
		self.tapi.RegisterSpi(self.tspi)
		self.tapi.SubscribePrivateTopic(api.THOST_TERT_QUICK)
		self.tapi.SubscribePublicTopic(api.THOST_TERT_QUICK)
		self.tapi.Init()
		#print("init end")

	def ReqAuth(self):
		authfield = api.CThostFtdcReqAuthenticateField()
		authfield.BrokerID=BROKERID
		authfield.UserID=self.invid
		authfield.AppID=APPID
		authfield.AuthCode=AUTHCODE
		self.tapi.ReqAuthenticate(authfield,0)
		PrintSendName("ReqAuthenticate")

	def ReqLogin(self):
		loginfield = api.CThostFtdcReqUserLoginField()
		loginfield.BrokerID=BROKERID
		#loginfield.UserID=self.USERID
		loginfield.UserID=self.invid
		loginfield.Password=PASSWORD
		loginfield.UserProductInfo="python dll"
		self.tapi.ReqUserLogin(loginfield,0)
		PrintSendName("ReqUserLogin")

	def ReqQrySettleInfo(self):
		qryinfofield = api.CThostFtdcQrySettlementInfoField()
		qryinfofield.BrokerID=self.BROKERID
		#qryinfofield.InvestorID=self.USERID
		qryinfofield.InvestorID=self.invid
		self.tapi.ReqQrySettlementInfo(qryinfofield,0)
		PrintSendName("ReqQrySettlementInfo")

	def ReqSettleInfoConfirm(self):
		pSettlementInfoConfirm=api.CThostFtdcSettlementInfoConfirmField()
		pSettlementInfoConfirm.BrokerID=BROKERID
		pSettlementInfoConfirm.InvestorID=self.invid
		self.tapi.ReqSettlementInfoConfirm(pSettlementInfoConfirm,0)
		PrintSendName("ReqSettlementInfoConfirm")

	def ReqOrIn(self, dirt, offset):
		pInOrder=api.CThostFtdcInputOrderField()
		pInOrder.BrokerID=BROKERID
		pInOrder.InvestorID=self.invid
		pInOrder.UserID=self.invid
		pInOrder.ExchangeID=EXCHANGEID
		pInOrder.InstrumentID=INSTRUMENTID
		pInOrder.Direction=str(dirt)
		pInOrder.LimitPrice=PRICE
		pInOrder.VolumeTotalOriginal=VOLUME
		pInOrder.OrderPriceType=ORDERTYPE
		pInOrder.ContingentCondition=CONTIGENCON
		pInOrder.CombOffsetFlag=str(offset)
		pInOrder.CombHedgeFlag=HEDGEFLAG
		pInOrder.TimeCondition=api.THOST_FTDC_TC_GFD
		pInOrder.VolumeCondition=VOLUMECONDITION
		pInOrder.MinVolume=MINVOL
		pInOrder.IsAutoSuspend=0
		pInOrder.StopPrice=STOPPRICE
		pInOrder.ForceCloseReason=api.THOST_FTDC_FCC_NotForceClose
		self.tapi.ReqOrderInsert(pInOrder, 0)
		PrintSendName("ReqOrderInsert")

	def LoginCheck(self):
		return self.loginflag

	def SettConfirmCheck(self):
		return self.settleconfirm


def PrintSendName(sendname):
	print("send", sendname, "ok")