from czsc.chan.solid import *
from datetime import *
from czsc.traders.ts_backtest import TsDataCache
from czsc import CZSC, CzscAdvancedTrader, Freq
#from czsc.enum import Signals
if __name__ == '__main__':
	print('started in main')
	# 这里可以换成自己的股票池

	ts_codes = ['002049.sz','300750.sz', '601318.ss', '300293.sz','QQQ','sqqq']
	for ts_code in ts_codes:
		try:
			end_date = datetime.now()
			start_date = end_date - timedelta(days=1000)
			# 需要先设置 Tushare Token，否则报错，无法执行
			# TsDataCache 是统一的 tushare 数据缓存入口，适用于需要重复调用接口的场景
			dc = TsDataCache(data_path=r"D:\PriProjects\czscChan\data", sdt=start_date.isoformat(), edt=end_date.isoformat())
			bars_day = dc.pro_bar_yahoo(ts_code=ts_code, asset='I', start_date=start_date.strftime("%Y%m%d"), end_date=end_date.strftime("%Y%m%d"), freq='D')
			bars_week = dc.pro_bar_yahoo(ts_code=ts_code, asset='I', start_date=start_date.strftime("%Y%m%d"), end_date=end_date.strftime("%Y%m%d"), freq='D')
			bars_hour = dc.pro_bar_minutes__yahoo(ts_code=ts_code, sdt=start_date.strftime("%Y%m%d"), edt=end_date.strftime("%Y%m%d"), freq='60min', asset=None, adj=None, raw_bar=True)
			
			kline_day=pd.DataFrame(bars_day)
			kline_week=pd.DataFrame(bars_week)
			kline_hour=pd.DataFrame(bars_hour)
			ka=KlineAnalyze(kline_day) # kline had to be instance of pd.DataFrame
			ka1=KlineAnalyze(kline_week)
			ka2=KlineAnalyze(kline_hour)
			b1, detail = is_first_buy(ka, ka1=ka1, ka2=ka2, tolerance=0.03)
			if b1:
				print("{} - 日线一买".format(ts_code))
			
			b2, detail = is_second_buy(ka, ka1=ka1, ka2=ka2, tolerance=0.03)
			if b2:
				print("{} - 日线二买".format(ts_code))

			b3, detail = is_third_buy(ka, ka1=ka1, ka2=ka2, tolerance=0.03, max_num=4)
			if b3:
				print("{} - 日线三买".format(ts_code))

			s1, detail=is_first_sell(ka, ka1=ka1, ka2=ka2, tolerance=0.03)
			if s1:
				print("{} - 日线一卖".format(ts_code))
			s2, detail=is_second_sell(ka, ka1=ka1, ka2=ka2, tolerance=0.03)
			if s2:
				print("{} - 日线二卖".format(ts_code))

			s3, detail=is_third_sell(ka, ka1=ka1, ka2=ka2, tolerance=0.03, max_num=4)
			if s3:
				print("{} - 日线三卖".format(ts_code))

			if not ( b1 or b2 or b3 or s1 or s2 or s3):
				print("{} - 不是缠论买卖点".format(ts_code))

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
