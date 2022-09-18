from czsc.chan.solid import *
from datetime import *
from czsc.traders.ts_backtest import TsDataCache
from czsc import CZSC, CzscAdvancedTrader, Freq
#from czsc.enum import Signals
if __name__ == '__main__':
	print('started in main')
	# 这里可以换成自己的股票池

	ts_codes = ['002049.sz', '300750.sz', '601318.ss', '300293.sz','QQQ','sqqq']
	for ts_code in ts_codes:
		try:
			end_date = datetime.now()
			start_date = end_date - timedelta(days=1000)
			# 需要先设置 Tushare Token，否则报错，无法执行
			# TsDataCache 是统一的 tushare 数据缓存入口，适用于需要重复调用接口的场景
			dc = TsDataCache(data_path=r"D:\PriProjects\czscChan\data", sdt=start_date.isoformat(), edt=end_date.isoformat())
			bars = dc.pro_bar_yahoo(ts_code=ts_code, asset='I', start_date=start_date.strftime("%Y%m%d"), end_date=end_date.strftime("%Y%m%d"), freq='D')
			kline=pd.DataFrame(bars)

			#df = pd.DataFrame(ka.kline)
			ka=KlineAnalyze(kline) # kline had to be instance of pd.DataFrame
			if is_third_buy(ka, ka1=None, ka2=None, tolerance=0.03, max_num=4):
				print("{} - 日线三买".format(ts_code))
			elif is_third_sell(ka, ka1=None, ka2=None, tolerance=0.03, max_num=4):
				print("{} - 日线三卖".format(ts_code))


			'''
			# 在浏览器中查看单标的单级别的分型、笔识别结果
			#bars = dc.pro_bar(ts_code='000001.SH', asset='I', start_date='20150101', end_date="20220427", freq='D')
			bars = dc.pro_bar_yahoo(ts_code=ts_code, asset='I', start_date=start_date.strftime("%Y%m%d"), end_date=end_date.strftime("%Y%m%d"), freq='D')
			
			c = CZSC(bars)
			ka=KlineAnalyze(bars)
			if c.signals['倒1五笔'] in [Signals.X5LB0.value, Signals.X5LB1.value]:
				print("{} - 日线三买".format(ts_code))
			if c.signals['倒1五笔'] in [Signals.X5LB0.value, Signals.X5LB1.value]:
				print("{} - 日线三卖".format(ts_code))

			'''
		except:
			print("{} - 执行失败".format(ts_code))
