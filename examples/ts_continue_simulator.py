# -*- coding: utf-8 -*-
"""
author: zengbin93
email: zeng_bin8888@163.com
create_dt: 2022/5/6 15:54
describe: 使用 Tushare 数据对交易策略进行持续仿真研究
"""
from ts_fast_backtest import TsDataCache
from czsc.traders.ts_simulator import TradeSimulator
from czsc.strategies import trader_strategy_a


def main():
    data_path = r"D:\PriProjects\czscChan\data"
    dc = TsDataCache(data_path, sdt='2020-09-15', edt='2022-09-15')
    ts = TradeSimulator(dc, trader_strategy_a)
    # ts.update_trader('000001.SH', 'I')
    # trader = ts.update_trader('000001.SH', 'I')
    ts_codes = ['002049.sz', '300750.sz']
    ts.update_traders(ts_codes, asset='I')


if __name__ == '__main__':
    main()

