def merger():
    fc=len(f_pid)
    sc=len(s_pid)
    isc=ifc=min=flag=0
    if (fc !=0 and sc!=0):
        while (isc<sc and ifc<fc):
            if(f_at[ifc] == s_at[isc]):
                m_pid.append(f_pid [ifc])
                m_at.append(f_at[ifc])
                m_bt.append(f_bt[ifc])
                m_rat.append(f_rat[ifc])
                m_rbt.append(f_bt[ifc])
                ifc +=1
                m_pid.append(s_pid [isc])
                m_at.append(s_at[isc])
                m_bt.append(s_bt[isc])
                m_rat.append(s_rat[isc])
                m_rbt.append(s_bt[ifc])
                isc +=1
            elif(f_at[ifc] < s_at[isc]):
                m_pid.append(f_pid [ifc])
                m_at.append(f_at[ifc])
                m_bt.append(f_bt[ifc])
                m_rat.append(f_rat[ifc])
                m_rbt.append(f_bt[ifc])
                ifc +=1
            elif(f_at[ifc] > s_at[isc]):
                m_pid.append(s_pid [isc])
                m_at.append(s_at[isc])
                m_bt.append(s_bt[isc])
                m_rat.append(s_rat[isc])
                m_rbt.append(s_bt[ifc])
                isc +=1
        mc=len(m_pid)
        if(mc != (fc+sc)):
            if fc != ifc:
                while(ifc != fc):
                    m_pid.append(f_pid [ifc])
                    m_at.append(f_at[ifc])
                    m_bt.append(f_bt[ifc])
                    m_rat.append(f_rat[ifc])
                    m_rbt.append(f_bt[ifc])
                    ifc +=1
            elif sc!=isc:
                while(isc!=sc):
                    m_pid.append(s_pid [isc])
                    m_at.append(s_at[isc])
                    m_bt.append(s_bt[isc])
                    m_rat.append(s_rat[isc])
                    m_rbt.append(s_bt[isc])
                    isc +=1
    elif fc==0:
        while(isc!=sc):
            m_pid.append(s_pid [isc])
            m_at.append(s_at[isc])
            m_bt.append(s_bt[isc])
            m_rat.append(s_rat[isc])
            m_rbt.append(s_bt[ifc])
            isc +=1    
    elif sc==0:
        while(ifc!=fc):
            m_pid.append(f_pid [ifc])
            m_at.append(f_at[ifc])
            m_bt.append(f_bt[ifc])
            m_rat.append(f_rat[ifc])
            m_rbt.append(f_bt[ifc])
            ifc +=1
    else:
        print("There are invalid data")



def inputs(count):
    print()
    if count==0:
        print("NO QUERIES")
    else:
        for i in range(count):
            print()
            time=int(input(f"{i+1}. Please enter the timing of arrival :-"))
            if (time>=1060 and time<1100) or (time>=1160 and time<=1200):
                print("Invalid time type")
            elif time>=1000 and time<=1200:
                t=int(input("1.FACULTY or 2.STUDENT ->"))
                if t==1:
                    q_id=input("Provide QUERY id ->")
                    if (q_id not in f_pid) and len(q_id)==4:
                        f_pid.append('T '+q_id)
                        f_at.append(time)
                        f_rat.append(time)
                        exe = int(input("Execution time ->"))
                        f_bt.append(exe)
                    else:
                        print("\"id already existed so this wont be taken or Invalid length\"\n")
                
                elif t==2:
                    q_id=input("Provide QUERY id ->")
                    if (q_id not in s_pid) and len(q_id)==4:
                        s_pid.append('S '+q_id)
                        s_at.append(time)
                        s_rat.append(time)
                        exe = int(input("Execution time ->"))
                        s_bt.append(exe)
                    else:
                        print("\"id already existed so this wont be taken or Invalid length\"\n")
                    
                else:
                    print("Invalid input")

            elif time<1000:
                print("you are early come between 1000 - 1200")
            else:
                print("late better luck next time")



def waitingtime(m_wt):
    rem_bt = [0]*mc
    for i in range(mc):
        rem_bt[i] = m_bt[i]
    t=0
    while(True):
        done = True
        for i in range(mc):
            while(rem_bt[i]>0 and t!=120):
                done=False
                if (rem_bt[i] > quanta):
                    t += quanta
                    rem_bt[i] -= quanta
                elif (rem_bt[i]<=quanta and rem_bt[i]!=0):
                    t += rem_bt[i]
                    m_wt[i] = t - m_bt[i]
                    rem_bt[i]=0
                    m_ct[i] = t
        if (done == True):
            break

def turnaroundtime(m_wt,m_tat):
    for i in range(mc):
        m_tat[i] = m_bt[i] + m_wt[i]



def roundrobin():
    m_wt = [0]*mc
    m_tat = [0]*mc
    waitingtime(m_wt)
    turnaroundtime(m_wt,m_tat)
    print("Execution table\n")
    print('QueryID\t\t\tArrival Time\t\t\tExecution Time\t\t\tWaiting Time\t\t\tTurn-Around Time')
    total_wt = 0
    total_tat = 0
    total_exe = 0
    total = 0
    sum = 0
    for i in range(mc):
        print()
        total = m_ct[i]
        sum += (m_ct[i]-m_bt[i])
        total_wt = total_wt + m_wt[i]
        total_tat= total_tat + m_tat[i]
        total_exe= total_exe + m_bt[i]
        print(m_pid[i],"\t\t\t",m_at[i],'\t\t\t\t',m_bt[i],"\t\t\t\t",m_wt[i],"\t\t\t\t",m_tat[i])
    avg=sum/mc
    print("\n\nAverage waiting time =  %.3f"%(total_wt/mc))
    print("Average turn around time = %.3f"%(total_tat/mc))
    print("Average excutiont ime = %.3f"%(total_exe/mc))
    print("\nTotal time Spent on Queries = %d"%(total))
    print("Average Query time = %.3f"%(avg))
    print("\n\n\t\t\t\t\t\t\t\tTHANK YOU QUERIES ARE COMPLETED")


if __name__ == "__main__":
    print("\n\t\t\t\t\t\t\t\t\t\tWELCOME TO DOUBT CLEARING SESSION\n\n\n")
    print("'  ----- read instructions carefully -----  '")
    print("* write the time in the formate -- (10:11) -> 1011")
    print("* query id only in interger form")
    print("* qury id should be length 4")
    print("* give the data according to arrival\n\n")
    input(("______PRESS ENTER TO CONTINUE______\n\n\n").lower())
    f_pid=[]
    s_pid=[]
    m_pid=[]
    f_at=[]
    s_at=[]
    m_at=[]
    f_bt=[]
    s_bt=[]
    m_bt=[]
    f_rat=[]
    s_rat=[]
    m_rat=[]
    m_rbt=[]
    quer=int(input("Give Number of QUERIES ->"))
    quanta=int(input("\nGive the QUANTUM TIME ->"))
    inputs(quer)
    merger()
    mc=len(m_pid)
    m_ct = [0]*mc
    roundrobin()
