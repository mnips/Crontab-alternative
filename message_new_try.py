
import schedule
import time

def job(t):
    print "I'm working...", t
    exit()
i=0
# hr=1
# min=0
# sec=0
# ans=str(hr)+":"+str(min)+":"+str(sec)
# schedule.every().day.at(ans).do(job,'It is 01:00')
schedule.every().second.do(job,"It is 1.00")
while True:
    '''
    if(sec<59):
        sec=sec+
    if(min<59):
        min=min+1
    else:
        min=0
        hr=hr+1
        if(hr>23):
            hr=0

    ans=str(hr)+":"+str(min)+":"+str(sec)
    '''
    # i=i+1
    # if(i==100):
    #     break
    schedule.run_pending()

    #time.sleep(60) # wait one minute
    #6652002