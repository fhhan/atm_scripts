import os 
from datetime import datetime, timedelta

fname = "yang.txt"
bgtime  = datetime.strptime("2017110100","%Y%m%d%H")
endtime = datetime.strptime("2018030100","%Y%m%d%H")


def step1(fname):
    file = open(fname,"r") 
    lines = file.readlines()
    file.close()
    
    data = {}
    flag = 1
    for line in lines:
        if (flag==1):
            flag=2                  
            pass
        else:
            content = line.split(",")
            thisTime = datetime.strptime(content[1],"%Y %m %d %H %M %S")
            data[thisTime] = [ float(i) if float(i)!=-999. else 0 for i in content[2:201] ]
    return data

def step2(data,bgtime,endtime):
    delta = timedelta(minutes=10)
    mean_data = {}
    while bgtime<endtime:
        if bgtime in data.keys():
            if data[bgtime].count(0) >= 150:            # if num of FillValue >= 75%, set 0
                mean_data[bgtime] = 0
            else:
                mean_data[bgtime] = sum(data[bgtime])
        else:
            mean_data[bgtime] = 0
        bgtime +=delta
    return mean_data

def step3(data,bgtime,endtime):
    delta = timedelta(days=1)
    data_d = {}
    it = bgtime
    
    while bgtime < endtime: 
        temp = data[bgtime]
        while ((bgtime <= it < bgtime+delta) and (it < endtime-timedelta(minutes=10))):
            it += timedelta(minutes=10)
            temp += data[it]

        data_d[bgtime] = temp
        bgtime += delta
       
    return data_d

def write_txt(data,file):
    fout = open(file,'w')
    for i,j in data.items():
        # eg change format:  2017-01-01 00:00:00 ->  2017-01-01
        data_str = str(i.strftime("%Y-%m-%d")) +' '+str(j)+'\n'
        
        fout.write(data_str)
    fout.close

data = step1(fname)
data1 = step2(data,bgtime,endtime)
#print(data1)
data2 = step3(data1,bgtime,endtime)
#print(data2)
write_txt(data2,"output.txt")

    