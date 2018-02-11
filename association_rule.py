#association_rule.py
sup = {"TT":0,"TSD":0,"TD":0,"SDT":0,"SDSD":0,"SDD":0,"DT":0,"DSD":0,"DD":0}
conf = {"TT":0,"TSD":0,"TD":0,"SDT":0,"SDSD":0,"SDD":0,"DT":0,"DSD":0,"DD":0}
lift = {"TT":0,"TSD":0,"TD":0,"SDT":0,"SDSD":0,"SDD":0,"DT":0,"DSD":0,"DD":0}
newcf2_list = []
transaction_list = []
countTT = 0
countTSD = 0
countTD = 0
countSDT = 0
countSDSD = 0
countSDD = 0
countDT = 0
countDSD = 0
countDD = 0
def create_transaction_list(cflist):
    combiningcf1 = ""
    combiningcf2 = ""
    for cf in cflist:
        if cf != "N":
            if combiningcf1 == "":
                combiningcf1 = combiningcf1 + cf
                if combiningcf2!="":
                    combiningcf2 = combiningcf2 + cf
                    transaction_list.append(combiningcf2)
                    combiningcf2 = ""
            else:
                combiningcf1 = combiningcf1 + cf
                transaction_list.append(combiningcf1)
                combiningcf1 = ""
                if combiningcf2 == "":
                    combiningcf2 = combiningcf2 + cf
    #for i, j in enumerate(transaction_list):
    #    print('transaction_list'+'{0}:{1}'.format(i+1, j))
#count TT,TSD....
def count():
    for i, j in enumerate(transaction_list):
        print('transaction_list'+'{0}:{1}'.format(i+1, j))
    for tl in transaction_list:
        if tl == "TT":
            global countTT
            countTT = countTT + 1
        elif tl == "TSD":
            global countTSD
            countTSD = countTSD + 1
        elif tl == "TD":
            global countTD
            countTD = countTD + 1
        elif tl == "SDT":
            global countSDT
            countSDT = countSDT + 1
        elif tl == "SDSD":
            global countSDSD
            countSDSD = countSDSD + 1
        elif tl == "SDD":
            global countSDD
            countSDD = countSDD + 1
        elif tl == "DT":
            global countDT
            countDT = countDT + 1
        elif tl == "DSD":
            global countDSD
            countDSD = countDSD + 1
        elif tl == "DD":
            global countDD
            countDD = countDD + 1
    print ('countTT=' + str(countTT))
    print ('countTSD=' + str(countTSD))
    print ('countTD=' + str(countTD))
    print ('countSDT=' + str(countSDT))
    print ('countSDSD=' + str(countSDSD))
    print ('countSDD=' + str(countSDD))
    print ('countDT=' + str(countDT))
    print ('countDSD=' + str(countDSD))
    print ('countDD=' + str(countDD))

def calculate_sup():
    cflist = ["TT","TSD","TD","SDT","SDSD","SDD","DT","DSD","DD"]
    print("countTT="+str(countTT))
    print("transaction_list="+str(len(transaction_list)))
    sup["TT"] = float(countTT)/len(transaction_list)
    sup["TSD"] = float(countTSD)/len(transaction_list)
    sup["TD"] = float(countTD)/len(transaction_list)
    sup["SDT"] = float(countSDT)/len(transaction_list)
    sup["SDSD"] = float(countSDSD)/len(transaction_list)
    sup["SDD"] = float(countSDD)/len(transaction_list)
    sup["DT"] = float(countDT)/len(transaction_list)
    sup["DSD"] = float(countDSD)/len(transaction_list)
    sup["DD"] = float(countDD)/len(transaction_list)
    for cf in cflist:
        print ("sup"+cf+"=" + str(sup[cf]))

def calculate_conf():
    cflist = ["TT","TSD","TD","SDT","SDSD","SDD","DT","DSD","DD"]
    countT = 0
    countSD = 0
    countD = 0
    print("countTT="+str(countTT))
    print("transaction_list="+str(len(transaction_list)))
    for tl in transaction_list:
        if tl.find("T") > -1:
            countT = countT + 1
        if tl.find("SD") > -1:
            countSD = countSD + 1
        if tl == "TD" or tl == "DT" or tl == "DSD" or tl == "DD" or tl == "SDD":
            countD = countD + 1
    print("countT="+str(countT))
    print("countSD="+str(countSD))
    print("countD="+str(countD))
    conf["TT"] = float(countTT)/countT
    conf["TSD"] = float(countTSD)/countT
    conf["TD"] = float(countTD)/countT
    conf["SDT"] = float(countSDT)/countSD
    conf["SDSD"] = float(countSDSD)/countSD
    conf["SDD"] = float(countSDD)/countSD
    conf["DT"] = float(countDT)/countD
    conf["DSD"] = float(countDSD)/countD
    conf["DD"] = float(countDD)/countD
    for cf in cflist:
        print ("conf"+cf+"=" + str(conf[cf]))

def calculate_lift():
    cflist = ["TT","TSD","TD","SDT","SDSD","SDD","DT","DSD","DD"]
    countT = 0
    countSD = 0
    countD = 0
    for tl in transaction_list:
        if tl.find("T") > -1:
            countT = countT + 1
        if tl.find("SD") > -1:
            countSD = countSD + 1
        if tl == "TD" or tl == "DT" or tl == "DSD" or tl == "DD" or tl == "SDD":
            countD = countD + 1
    try:
        lift["TT"] = conf["TT"]/(float(countT)/len(transaction_list))
        lift["TSD"] = conf["TSD"]/(float(countSD)/len(transaction_list))
        lift["TD"] = conf["TD"]/(float(countD)/len(transaction_list))
        lift["SDT"] = conf["SDT"]/(float(countT)/len(transaction_list))
        lift["SDSD"] = conf["SDSD"]/(float(countSD)/len(transaction_list))
        lift["SDD"] = conf["SDD"]/(float(countD)/len(transaction_list))
        lift["DT"] = conf["DT"]/(float(countT)/len(transaction_list))
        lift["DSD"] = conf["DSD"]/(float(countSD)/len(transaction_list))
        lift["DD"] = conf["DD"]/(float(countD)/len(transaction_list))
    except ZeroDivisionError:
        print("ZeroDivisionError!!")
    for cf in cflist:
        print ("lift"+cf+"=" + str(lift[cf]))

def judge_chordfunction(cf2_list):
    newcf2_list = cf2_list[:]
    for i, cf in enumerate(newcf2_list):
        if cf.find("N") == -1:
            if cf == "TT":
                if (lift["TSD"]-lift["TT"]) > 0.3:#0.471-0.632
                    cf = "TSD"
                elif (lift["TD"]-lift["TT"]) > 0.3:#0.3159-0.632
                    cf = "TD"
            elif cf == "TSD":
                if (lift["TT"]-lift["TSD"]) > 0.3:#0.632-0.47172
                    cf = "TT"
                elif (lift["TD"]-lift["TSD"]) > 0.3:#0.3159-0.47172
                    cf = "TD"
            elif cf == "TD":
                if (lift["TT"]-lift["TD"]) > 0.3:#0.632-0.31591Change
                    newcf2_list[i] = "TT"
                elif (lift["TSD"]-lift["TD"]) > 0.3:#0.47172-0.31591
                    cf = "TSD"
            elif cf == "SDT":
                if (lift["SDSD"]-lift["SDT"]) > 0.3:#0.1722-0.40269
                    cf = "SDSD"
                elif (lift["SDD"]-lift["SDT"]) > 0.3:#0.5798-0.40269
                    cf = "SDD"
            elif cf == "SDSD":
                if (lift["SDT"]-lift["SDSD"]) > 0.3:#0.40269-0.1722
                    cf = "SDT"
                elif (lift["SDD"]-lift["SDSD"]) > 0.3:#0.5798-0.1722Change
                    newcf2_list[i] = "SDD"
            elif cf == "SDD":
                if (lift["SDT"]-lift["SDD"]) > 0.3:#0.40269-0.5798
                    cf = "SDT"
                elif (lift["SDSD"]-lift["SDD"]) > 0.3:#0.1722-0.5798
                    cf = "SDSD"
            elif cf == "DT":
                if (lift["DSD"]-lift["DT"]) > 0.3:#0.15258-0.458579
                    cf = "DSD"
                elif (lift["DD"]-lift["DT"]) > 0.3:#0.270294-0.45857
                    cf = "DD"
            elif cf == "DSD":
                if (lift["DT"]-lift["DSD"]) > 0.3:#0.45857-0.15258Change
                    newcf2_list[i] = "DT"
                elif (lift["DD"]-lift["DSD"]) > 0.3:#0.270294-0.15258
                    cf = "DD"
            elif cf == "DD":
                if (lift["DT"]-lift["DD"]) > 0.3:#0.458579-0.270294
                    cf = "DT"
                elif (lift["DSD"]-lift["DD"]) > 0.3:#0.15258-0.270294
                    cf = "DSD"
    return newcf2_list
