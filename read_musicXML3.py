import chordfunction2 as cf
import association_rule as ar
chordfunction_list = []
chord_list=[]###
NN_list=[]
NT_list=[]
ND_list=[]
NSD_list=[]
TT_list=[]
TD_list=[]
TSD_list=[]
TN_list=[]
SDT_list=[]
SDSD_list=[]
SDD_list=[]
SDN_list=[]
DT_list=[]
DSD_list=[]
DD_list=[]
DN_list=[]
maxTT_list=[]
maxTD_list=[]
maxTSD_list=[]
maxTN_list=[]
maxSDT_list=[]
maxSDD_list=[]
maxSDSD_list=[]
maxSDN_list=[]
maxDT_list=[]
maxDD_list=[]
maxDSD_list=[]
maxDN_list=[]
maxNT_list=[]
maxND_list=[]
maxNSD_list=[]
maxNN_list=[]
def maxElem( lis ):
  L = lis[:]#copy
  S = set(lis)
  S = list(S)
  MaxCount=0
  ret='nothing'
  for elem in S:
    c=0
    while elem in L:
      ind = L.index(elem)
      foo = L.pop(ind)
      c+=1
    if c>MaxCount:
      MaxCount=c
      ret = elem
  return ret
def calculate(pitch_list, duration_list, fifths, mode):
    print("<<calculate>>")
    t=0
    sd=0
    dom=0
    i=0
    sumt=0
    sumsd=0
    sumd=0
    c_dcodelist=["CM7","Dm7","Em7","FM7","G7","Am7","Bm7(b5)"]
    d_dcodelist=["DM7","Em7","F#m7","GM7","A7","Bm7","C#m7(b5)"]
    e_dcodelist=["EM7","F#m7","G#m7","AM7","B7","C#m7","D#m7(b5)"]
    f_dcodelist=["FM7","Gm7","Am7","BbM7","C7","Dm7","Em7(b5)"]
    g_dcodelist=["GM7","Am7","Bm7","CM7","D7","Em7","F#m7(b5)"]
    a_dcodelist=["AM7","Bm7","C#m7","DM7","E7","F#m7","G#m7(b5)"]
    b_dcodelist=["BM7","C#m7","D#m7","EM7","F#7","G#m7","A#m7(b5)"]
    eb_dcodelist=["EbM7","Fm7","Gm7","AbM7","Bb7","Cm7","Dm7(b5)"]
    major_keylist = ["Cb","Gb","Db","Ab","Eb","Bb","F","C","G","D","A","E","B","F#","C#"]
    minor_keylist = ["Abm","Ebm","Bbm","Fm","Cm","Gm","Dm","Am","Em","Bm","F#m","C#m","G#m","D#m","A#m"]
    if mode=="major":
        key=major_keylist[fifths+7]
        print("key = " + key)
    elif mode=="minor":
        print("key = " + key)
        key=minor_keylist[fifths+7]
    for pl in pitch_list:
        judge_list = []
        if key=="C":
            CM7=["C","E","G","B"]#T
            Dm7=["D","F","A","C"]#SD
            Em7=["E","G","B","D"]#T
            FM7=["F","A","C","E"]#SD
            G7=["G","B","D","F"]#D
            Am7=["A","C","E","G"]#T
            Bm7_b5=["B","D","F","A"]#D
            for c in CM7:
                if pl==c:
                    judge_list.append(c_dcodelist[0])
            for d in Dm7:
                if pl==d:
                    judge_list.append(c_dcodelist[1])
            for e in Em7:
                if pl==e:
                    judge_list.append(c_dcodelist[2])
            for f in FM7:
                if pl==f:
                    judge_list.append(c_dcodelist[3])
            for g in G7:
                if pl==g:
                    judge_list.append(c_dcodelist[4])
            for a in Am7:
                if pl==a:
                    judge_list.append(c_dcodelist[5])
            for b in Bm7_b5:
                if pl==b:
                    judge_list.append(c_dcodelist[6])
            for j in judge_list:
                if c_dcodelist[0]==j or c_dcodelist[2]==j or c_dcodelist[5]==j:
                    t=t+1
                    sumt += duration_list[i]
                if c_dcodelist[1]==j or c_dcodelist[3]==j:
                    sd=sd+1
                    sumsd += duration_list[i]
                if c_dcodelist[4]==j or c_dcodelist[6]==j:
                    dom=dom+1
                    sumd += duration_list[i]
            i=i+1 #duration_list
        if key=="Eb":
            EbM7=["Eb","G","Bb","D"]#T
            Fm7=["F","Ab","C","Eb"]#SD
            Gm7=["G","Bb","D","F"]#T
            AbM7=["Ab","C","Eb","G"]#SD
            Bb7=["Bb","D","F","Ab"]#D
            Cm7=["C","Eb","G","Bb"]#T
            Dm7_b5=["D","F","Ab","C"]#D
            for eb in EbM7:
                if pl==eb:
                    judge_list.append(eb_dcodelist[0])
            for fm in Fm7:
                if pl==fm:
                    judge_list.append(eb_dcodelist[1])
            for gm in Gm7:
                if pl==gm:
                    judge_list.append(eb_dcodelist[2])
            for ab in AbM7:
                if pl==ab:
                    judge_list.append(eb_dcodelist[3])
            for bb in Bb7:
                if pl==bb:
                    judge_list.append(eb_dcodelist[4])
            for cm in Cm7:
                if pl==cm:
                    judge_list.append(eb_dcodelist[5])
            for dm in Dm7_b5:
                if pl==dm:
                    judge_list.append(eb_dcodelist[6])
            for j in judge_list:
                if eb_dcodelist[0]==j or eb_dcodelist[2]==j or eb_dcodelist[5]==j:
                    t=t+1
                    sumt += duration_list[i]
                if eb_dcodelist[1]==j or eb_dcodelist[3]==j:
                    sd=sd+1
                    sumsd += duration_list[i]
                if eb_dcodelist[4]==j or eb_dcodelist[6]==j:
                    dom=dom+1
                    sumd += duration_list[i]
            i=i+1 #duration_list
        if key=="G":
            GM7=["G","B","D","F#"]#T
            Am7=["A","C","E","G"]#SD
            Bm7=["B","D","F#","A"]#T
            CM7=["C","E","G","B"]#SD
            D7=["D","F#","A","C"]#D
            Em7=["E","G","B","D"]#T
            Fsm7_b5=["F#","A","C","E"]#D
            for gm in GM7:
                if pl==gm:
                    judge_list.append(g_dcodelist[0])
            for am in Am7:
                if pl==am:
                    judge_list.append(g_dcodelist[1])
            for bm in Bm7:
                if pl==bm:
                    judge_list.append(g_dcodelist[2])
            for cm in CM7:
                if pl==cm:
                    judge_list.append(g_dcodelist[3])
            for d in D7:
                if pl==d:
                    judge_list.append(g_dcodelist[4])
            for em in Em7:
                if pl==em:
                    judge_list.append(g_dcodelist[5])
            for fsm in Fsm7_b5:
                if pl==fsm:
                    judge_list.append(g_dcodelist[6])
            for j in judge_list:
                if g_dcodelist[0]==j or g_dcodelist[2]==j or g_dcodelist[5]==j:
                    t=t+1
                    sumt += duration_list[i]
                if g_dcodelist[1]==j or g_dcodelist[3]==j:
                    sd=sd+1
                    sumsd += duration_list[i]
                if g_dcodelist[4]==j or g_dcodelist[6]==j:
                    dom=dom+1
                    sumd += duration_list[i]
            i=i+1 #duration_list
        if key=="F":
            FM7=["F","A","C","E"]#T
            Gm7=["G","Bb","D","F"]#SD
            Am7=["A","C","E","G"]#T
            BbM7=["Bb","D","F","A"]#SD
            C7=["C","E","G","Bb"]#D
            Dm7=["D","F","A","C"]#T
            Em7_b5=["E","G","Bb","D"]#D
            for fm in FM7:
                if pl==fm:
                    judge_list.append(f_dcodelist[0])
            for gm in Gm7:
                if pl==gm:
                    judge_list.append(f_dcodelist[1])
            for am in Am7:
                if pl==am:
                    judge_list.append(f_dcodelist[2])
            for bb in BbM7:
                if pl==bb:
                    judge_list.append(f_dcodelist[3])
            for c in C7:
                if pl==c:
                    judge_list.append(f_dcodelist[4])
            for dm in Dm7:
                if pl==dm:
                    judge_list.append(f_dcodelist[5])
            for em in Em7_b5:
                if pl==em:
                    judge_list.append(f_dcodelist[6])
            for j in judge_list:
                if f_dcodelist[0]==j or f_dcodelist[2]==j or f_dcodelist[5]==j:
                    t=t+1
                    sumt += duration_list[i]
                if f_dcodelist[1]==j or f_dcodelist[3]==j:
                    sd=sd+1
                    sumsd += duration_list[i]
                if f_dcodelist[4]==j or f_dcodelist[6]==j:
                    dom=dom+1
                    sumd += duration_list[i]
            i=i+1 #duration_list
    print('t='+str(t),'sd='+str(sd),'dom='+str(dom))
    print ('T=' + str(sumt),'SD=' + str(sumsd),'D=' + str(sumd))
    if sumt==0 and sumsd==0 and sumd==0:
        chordfunction_list.append("N");
    elif sumt==max(sumt,sumsd,sumd):
        chordfunction_list.append("T");
    elif sumsd==max(sumt,sumsd,sumd):
        chordfunction_list.append("SD");
    else:
        chordfunction_list.append("D");
    for i, j in enumerate(chordfunction_list):
        print('chordfunction'+'{0}:{1}'.format(i+1, j))
    s=""
    cf2_list=[]
    for cf in chordfunction_list:
        if len(s)>0:
            s=s+cf
            cf2_list.append(s)
            s=""
        elif len(s)==0:
            s=s+cf
    NN=[]
    NT=[]
    ND=[]
    NSD=[]
    TT=[]
    TD=[]
    TSD=[]
    TN=[]
    SDT=[]
    SDSD=[]
    SDD=[]
    SDN=[]
    DT=[]
    DSD=[]
    DD=[]
    DN=[]
    for x in range(len(cf2_list)):
        if cf2_list[x]=="NN":
            NN.append(chord_list[x])
        elif cf2_list[x]=="NT":
            NT.append(chord_list[x])
        elif cf2_list[x]=="ND":
            ND.append(chord_list[x])
        elif cf2_list[x]=="NSD":
            NSD.append(chord_list[x])
        elif cf2_list[x]=="TT":
            TT.append(chord_list[x])
        elif cf2_list[x]=="TD":
            TD.append(chord_list[x])
        elif cf2_list[x]=="TSD":
            TSD.append(chord_list[x])
        elif cf2_list[x]=="TN":
            TN.append(chord_list[x])
        elif cf2_list[x]=="SDT":
            SDT.append(chord_list[x])
        elif cf2_list[x]=="SDSD":
            SDSD.append(chord_list[x])
        elif cf2_list[x]=="SDD":
            SDD.append(chord_list[x])
        elif cf2_list[x]=="SDN":
            SDN.append(chord_list[x])
        elif cf2_list[x]=="DT":
            DT.append(chord_list[x])
        elif cf2_list[x]=="DSD":
            DSD.append(chord_list[x])
        elif cf2_list[x]=="DD":
            DD.append(chord_list[x])
        elif cf2_list[x]=="DN":
            DN.append(chord_list[x])
    for i, j in enumerate(TT):
        print('TT'+'{0}:{1}'.format(i+1, j))
    for i, j in enumerate(TSD):
        print('TSD'+'{0}:{1}'.format(i+1, j))
    for i, j in enumerate(SDT):
        print('SDT'+'{0}:{1}'.format(i+1, j))
    for i, j in enumerate(TD):
        print('TD'+'{0}:{1}'.format(i+1, j))
    maxTT = maxElem(TT)
    maxTSD = maxElem(TSD)
    maxTD = maxElem(TD)
    maxTN = maxElem(TN)
    maxSDT = maxElem(SDT)
    maxSDSD = maxElem(SDSD)
    maxSDD = maxElem(SDD)
    maxSDN = maxElem(SDN)
    maxDT = maxElem(DT)
    maxDSD = maxElem(DSD)
    maxDD = maxElem(DD)
    maxDN = maxElem(DN)
    maxNN = maxElem(NN)
    maxNT = maxElem(NT)
    maxND = maxElem(ND)
    maxNSD = maxElem(NSD)
    print("maxTT=" + maxTT)
    print("maxTSD=" + maxTSD)
    print("maxSDT=" + maxSDT)
    print("maxTD=" + maxTD)
    print("---------------------------------")
    return maxTT,maxTSD,maxTD,maxTN,maxSDT,maxSDSD,maxSDD,maxSDN,maxDT,maxDSD,maxDD,maxDN,maxNT,maxNSD,maxND,maxNN
def extractChords(root,textg,stringroot,s,stringbass):
    print("<<extractChords>>")
    index = stringroot.find(root)
    abc = ["A","B","C","D","E","F","G"]
    if stringroot[index]==root:
        if textg == "7":
            s = s + root + "7"
        elif textg == "m":
            s = s + root + "m"
        elif textg == "m7":
            s = s + root + "m7"
        elif textg == "sus":
            s = s + root + "sus"
        elif textg == "6":
            s = s + root + "6"
        elif textg == "2":
            s = s + root + "2"
        else:
            s = s + root
        if stringbass != "nothing":
            for ab in abc:
                index2 = stringbass.find(ab)
                if stringbass[index2] == ab:
                    s = s + "/" + ab
        return s
""" Extract music data from xml file. """
def extract(xml_name):
    print("<<extract>>")
    #xml_name = raw_input("Please Enter FileName: ")
    from bs4 import BeautifulSoup
    #xml_name = "Imagine.xml"# Your MusicXML file
    #xml_name = "minuit.xml"# Your MusicXML file
    #xml_name = "Greensleeves.xml"# Your MusicXML file
    soup = BeautifulSoup(open(xml_name,'r').read(),"html.parser")
    string = ""
    count=0
    fifths_tag = soup.fifths
    fifths = int(fifths_tag.string)
    print("fifths=" + str(fifths))
    mode_tag = soup.mode
    mode = mode_tag.string
    print("mode=" + str(mode))
    divisions_tag = soup.divisions
    divisions = int(divisions_tag.string)
    print("divisions=" + str(divisions))
    divisions_list = [480,240,120,60]
    for m in soup.find_all("measure"):
        pitch_list = []
        duration_list = []
        mnumber = int(m.get("number")) #every measure
        if count == 1:
            mnumber = mnumber + 1
        if count==0 and mnumber==0:
            mnumber = mnumber + 1
            count=1
        print("<<measure_nubmer=" + str(mnumber) + ">>")
        if m.harmony is None:
            string = string + "N"
        else:
            for h in m.find_all("harmony"):
                if h.name == "harmony":
                    textg = h.kind.get("text")
                    index = 0
                    stringroot = str(h.root)
                    stringbass = "nothing"
                    if h.bass is not None:
                        stringbass = str(h.bass)
                    print(stringroot)
                    abc = ["A","B","C","D","E","F","G"]
                    for ab in abc:
                        judgement = extractChords(ab,textg,stringroot,string,stringbass)
                        if judgement is None:
                            pass
                        else:
                            string = judgement
        if mnumber % 2 == 0:
            chord_list.append(string)
            string = ""
            #chordfunction
            #if index > 0:
            #    index = stringroot.find("-1")
            #    if stringroot[index]=="-"
            #        tempstring = "Ab"
        for nb in m.find_all("note"):
            if nb.name == "note":
                if nb.chord:#pitch only
                    continue
                if nb.grace:
                    grace = nb.grace.get("slash")
                    if grace=="yes":
                        duration_list.append(60)
                if nb.pitch:
                    if nb.pitch.alter:
                        step = nb.pitch.step.string
                        if int(nb.pitch.alter.string)==1:
                            pitch_list.append(step+"#")
                        elif int(nb.pitch.alter.string)==-1:
                            pitch_list.append(step+"b")
                    else:
                        pitch_list.append(nb.pitch.step.string)
                if nb.rest:
                    continue
                if nb.duration:
                    tmp_duration= int(nb.duration.string)
                    duration_list.append(divisions_list[divisions-1]*tmp_duration)
        for i, j in enumerate(pitch_list):
            print('pitch'+'{0}:{1}'.format(i+1, j))
        for i, j in enumerate(duration_list):
            print('duration'+'{0}:{1}'.format(i+1, j))
        for i, j in enumerate(chord_list):
            print('chord_list'+'{0}:{1}'.format(i+1, j))
        result = calculate(pitch_list, duration_list, fifths, mode)
        if result[0]!="nothing": TT_list.insert(0,result[0])
        else: pass
        if result[1]!="nothing": TSD_list.insert(0,result[1])
        else: pass
        if result[2]!="nothing": TD_list.insert(0,result[2])
        else: pass
        if result[3]!="nothing": TN_list.insert(0,result[3])
        else: pass
        if result[4]!="nothing": SDT_list.insert(0,result[4])
        else: pass
        if result[5]!="nothing": SDSD_list.insert(0,result[5])
        else: pass
        if result[6]!="nothing": SDD_list.insert(0,result[6])
        else: pass
        if result[7]!="nothing": SDN_list.insert(0,result[7])
        else: pass
        if result[8]!="nothing": DT_list.insert(0,result[8])
        else: pass
        if result[9]!="nothing": DSD_list.insert(0,result[9])
        else: pass
        if result[10]!="nothing": DD_list.insert(0,result[10])
        else: pass
        if result[11]!="nothing": DN_list.insert(0,result[11])
        else: pass
        if result[12]!="nothing": NT_list.insert(0,result[12])
        else: pass
        if result[13]!="nothing": NSD_list.insert(0,result[13])
        else: pass
        if result[14]!="nothing": ND_list.insert(0,result[14])
        else: pass
        if result[15]!="nothing": NN_list.insert(0,result[15])
        else: pass
    #for i, j in enumerate(chordfunction_list):
    #    print('functionchord'+'{0}:{1}'.format(i+1, j))

    ar.create_transaction_list(chordfunction_list)
    #ar.count()
    del chordfunction_list[:]
    del chord_list[:]
def maxappend(cflist,maxlist):
    if len(cflist) != 0:
        maxlist.append(cflist[0])
        del cflist[:]
print("-------------start--------------")
while (True):
    #del chordfunction_list[:]
    #del chord_list[:]
    judge = raw_input("Continue? yes:1 no:0 ")
    print(judge)
    if judge=="1":
        musicXML_list=["Father_I_Adore_You.xml",
                    "His_Grace_is_Sufficient.xml",
                    "His_Name_is_Jesus.xml",
                    "Hosanna.xml",
                    "I_Need_Him.xml",
                    "I_Was_Glad_Glad_Glad.xml",
                    #"I_Will_Not_Forget_You.xml",
                    "Jesus_Oh_I_Love_You.xml",
                    "Jesus_Wonderful_Lord.xml",
                    "Let_the_Peace_of_God_Let_it_in.xml",
                    "O_That_Men_Would_Praise_the_Lord.xml",
                    "On_Your_Altar.xml",
                    "Search_Me_O_God.xml",
                    "The_Blessing.xml",
                    "The_Winter_Song.xml",
                    "Trust_In_Him.xml",
                    "Unto_Thee_O_My_Strength.xml",
                    "We_Have_A_Strong_City_In_That_Day.xml",
                    "YA-WHE_God_of_Abraham.xml",
                    "Your_Name_is_a_strong_tower.xml"]

        #musicXML_list=["Father_I_Adore_You.xml","His_Grace_is_Sufficient.xml"]
        for ml in musicXML_list:
            extract(ml)#execute
        ar.count()
        ar.calculate_sup()
        ar.calculate_conf()
        ar.calculate_lift()
        for i, j in enumerate(maxTT_list):
            print('maxTT_list'+'{0}:{1}'.format(i+1, j))
        if len(TT_list) != 0:
            maxTT_list.append(TT_list[0])
            del TT_list[:]
        maxappend(TSD_list,maxTSD_list)
        maxappend(TD_list,maxTD_list)
        maxappend(TN_list,maxTN_list)
        maxappend(SDT_list,maxSDT_list)
        maxappend(SDSD_list,maxSDSD_list)
        maxappend(SDD_list,maxSDD_list)
        maxappend(SDN_list,maxSDN_list)
        maxappend(DT_list,maxDT_list)
        maxappend(DSD_list,maxDSD_list)
        maxappend(DD_list,maxDD_list)
        maxappend(DN_list,maxDN_list)
        maxappend(NT_list,maxNT_list)
        maxappend(NSD_list,maxNSD_list)
        maxappend(ND_list,maxND_list)
        maxappend(NN_list,maxNN_list)

        if len(maxTT_list) != 0: print ("maxTT="+maxTT_list[0])
        if len(maxTD_list) != 0: print ("maxTD="+maxTD_list[0])
        if len(maxTSD_list) != 0: print ("maxTSD="+maxTSD_list[0])
        if len(maxSDT_list) != 0: print ("maxSDT="+maxSDT_list[0])
    elif judge=="0":break
maxTT = maxElem(maxTT_list)
maxTD = maxElem(maxTD_list)
maxTSD = maxElem(maxTSD_list)
maxTN = maxElem(maxTN_list)
maxSDT = maxElem(maxSDT_list)
maxSDD = maxElem(maxSDD_list)
maxSDSD = maxElem(maxSDSD_list)
maxSDN = maxElem(maxSDN_list)
maxDT = maxElem(maxDT_list)
maxDSD = maxElem(maxDSD_list)
maxDD = maxElem(maxDD_list)
maxDN = maxElem(maxDN_list)
maxNT = maxElem(maxNT_list)
maxND = maxElem(maxND_list)
maxNSD = maxElem(maxNSD_list)
maxNN = maxElem(maxNN_list)

newcf2_list =[]
chf2_list = cf.chordfunction()
newcf2_list = ar.judge_chordfunction(chf2_list)
newchord_list1=[]
newchord_list2=[]
print chf2_list
print newcf2_list
for i in range(len(chf2_list)):
    if chf2_list[i] == "TT": newchord_list1.append(maxTT)
    elif chf2_list[i] == "TD": newchord_list1.append(maxTD)
    elif chf2_list[i] == "TSD": newchord_list1.append(maxTSD)
    elif chf2_list[i] == "TN": newchord_list1.append(maxTN)
    elif chf2_list[i] == "SDT": newchord_list1.append(maxSDT)
    elif chf2_list[i] == "SDSD": newchord_list1.append(maxSDSD)
    elif chf2_list[i] == "SDD": newchord_list1.append(maxSDD)
    elif chf2_list[i] == "SDN": newchord_list1.append(maxSDN)
    elif chf2_list[i] == "DD": newchord_list1.append(maxDD)
    elif chf2_list[i] == "DT": newchord_list1.append(maxDT)
    elif chf2_list[i] == "DSD": newchord_list1.append(maxDSD)
    elif chf2_list[i] == "DN": newchord_list1.append(maxDN)
    elif chf2_list[i] == "NN": newchord_list1.append(maxNN)
    elif chf2_list[i] == "NT": newchord_list1.append(maxNT)
    elif chf2_list[i] == "NSD": newchord_list1.append(maxNSD)
    elif chf2_list[i] == "ND": newchord_list1.append(maxND)
for i, j in enumerate(newchord_list1):
    print('newchord(1)'+'{0}:{1}'.format(i+1, j))

for i in range(len(newcf2_list)):
    if newcf2_list[i] == "TT": newchord_list2.append(maxTT)
    elif newcf2_list[i] == "TD": newchord_list2.append(maxTD)
    elif newcf2_list[i] == "TSD": newchord_list2.append(maxTSD)
    elif newcf2_list[i] == "TN": newchord_list2.append(maxTN)
    elif newcf2_list[i] == "SDT": newchord_list2.append(maxSDT)
    elif newcf2_list[i] == "SDSD": newchord_list2.append(maxSDSD)
    elif newcf2_list[i] == "SDD": newchord_list2.append(maxSDD)
    elif newcf2_list[i] == "SDN": newchord_list2.append(maxSDN)
    elif newcf2_list[i] == "DD": newchord_list2.append(maxDD)
    elif newcf2_list[i] == "DT": newchord_list2.append(maxDT)
    elif newcf2_list[i] == "DSD": newchord_list2.append(maxDSD)
    elif newcf2_list[i] == "DN": newchord_list2.append(maxDN)
    elif newcf2_list[i] == "NN": newchord_list2.append(maxNN)
    elif newcf2_list[i] == "NT": newchord_list2.append(maxNT)
    elif newcf2_list[i] == "NSD": newchord_list2.append(maxNSD)
    elif newcf2_list[i] == "ND": newchord_list2.append(maxND)
for i, j in enumerate(newchord_list2):
    print('newchord(2)'+'{0}:{1}'.format(i+1, j))
print newchord_list1
print newchord_list2
