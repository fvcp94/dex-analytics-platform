import numpy as np
import pandas as pd

def generate_dex_data(n_users=3000, n_days=90, seed=42):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(end=pd.Timestamp.today(), periods=n_days)

    users = pd.DataFrame({
        "user_id": [f"U{i:05d}" for i in range(n_users)],
        "region": rng.choice(["NA", "EU", "APAC"], n_users),
        "persona": rng.choice(["Engineer","Ops","Finance","HR","Sales"], n_users)
    })

    rows = []
    for d in dates:
        rows.append(pd.DataFrame({
            "date": d,
            "user_id": users["user_id"],
            "region": users["region"],
            "persona": users["persona"],
            "login_time_s": rng.normal(35,10,n_users).clip(10,200),
            "app_latency_ms": rng.normal(300,80,n_users).clip(50,3000),
            "crash_rate": rng.normal(0.05,0.02,n_users).clip(0,0.3),
            "device_health": rng.normal(0.85,0.05,n_users).clip(0.3,0.99)
        }))

    endpoint = pd.concat(rows, ignore_index=True)

    tickets = endpoint.sample(frac=0.05, random_state=seed).copy()
    tickets["ticket_id"] = [f"INC{i:06d}" for i in range(len(tickets))]
    tickets["category"] = rng.choice(["VPN","Teams","Outlook","VDI","Network"], len(tickets))
    tickets["priority"] = rng.choice(["P1","P2","P3","P4"], len(tickets), p=[0.02,0.1,0.3,0.58])
    tickets["mttr_hours"] = rng.gamma(2,6,len(tickets))

    changes = pd.DataFrame({
        "change_id":[f"CHG{i:04d}" for i in range(10)],
        "change_date": rng.choice(dates,10),
        "type": rng.choice(["Patch","Upgrade","Config"],10),
        "risk": rng.choice(["Low","Med","High"],10)
    })

    return {
        "endpoint_daily": endpoint,
        "tickets": tickets,
        "changes": changes
    }
