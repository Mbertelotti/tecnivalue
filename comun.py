import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from datetime import date


def multihist_load(tickers):
    df = yf.Ticker(tickers[0])
    df_hist = df.history(period="max")["Close"].to_frame()
    df_hist.columns=[tickers[0]]

    for ticker in tickers[1:]:
        try:
            dat = yf.Ticker(ticker)
            dat_hist = dat.history(period="max")["Close"].to_frame()
            dat_hist.columns=[ticker]
            df_hist=df_hist.join(dat_hist,how="outer",rsuffix="_"+ticker)
        except:
            pass
    return df_hist



def multihist_add(tickers,df_hist=None):
    if df_hist==None:
        df_hist=multihist_load(tickers)
    else:
        for ticker in tickers:
            if ticker not in df_hist.columns:
                try:
                    dat = yf.Ticker(ticker)
                    dat_hist = dat.history(period="max")["Close"].to_frame()
                    dat_hist.columns=[ticker]
                    df_hist=df_hist.join(dat_hist,how="outer",rsuffix="_"+ticker)
                except:
                    pass
    return df_hist