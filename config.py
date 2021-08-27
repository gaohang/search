from datetime import datetime, timedelta

#hosts = ['localhost']
hosts = ['192.168.1.126'] #test
auth = ('search', 'gAAAAABgoOLf6izHRhQ0SH8z0e7yUcqGmpO19qCk9zzSUP9oyiezS5UkWf6eaXsZHcRq2TcckfbXi7Ni7e3EDR5nqs-GaWr8ag==')

dt_today = (datetime.now() - timedelta(hours=5)).strftime('%Y%m%d')
hour_today = (datetime.now() - timedelta(hours=5)).strftime('%H')
dt_yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
p_date_today = (datetime.now() - timedelta(hours=5)).strftime('%Y-%m-%d')
