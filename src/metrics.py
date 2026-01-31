import numpy as np

def dex_score(df):
    bad = (
        0.4*(df["app_latency_ms"]/1000) +
        0.3*(df["login_time_s"]/100) +
        0.2*(df["crash_rate"]/0.3) +
        0.1*(1-df["device_health"])
    ).clip(0,1)
    df["dex_score"] = (1-bad)*100
    return df
