import pandas as pd

def detect(df, col, window=14, z=3):
    mu = df[col].rolling(window).mean()
    sd = df[col].rolling(window).std()
    df["anomaly"] = ((df[col]-mu)/sd).abs() > z
    return df
