
chordfunction_list = []
chord_list=[]###
def maxElem( lis ):
  L = lis[:]#copy
  S = set(lis)
  S = list(S)
  MaxCount=0
  ret='nothing...'
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
    print("maxTT=" + maxElem(TT))
    print("maxTSD=" + maxElem(TSD))
    print("maxSDT=" + maxElem(SDT))
    print("maxTD=" + maxElem(TD))
    print("---------------------------------")
""" Extract music data from xml file. """
def extract():
    #xml_name = raw_input("Please Enter FileName: ")
    from bs4 import BeautifulSoup
    xml_name = "Imagine.xml"# Your MusicXML file
    #xml_name = "minuit.xml"# Your MusicXML file
    #xml_name = "Greensleevs.xml"# Your MusicXML file
    soup = BeautifulSoup(open(xml_name,'r').read(),"html.parser")
    string = ""
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
        mnumber = m.get("number") #every measure
        print("<<measure_nubmer=" + mnumber + ">>")
        if m.harmony is None:
            if len(string)>0:
                string = string + "N"
                chord_list.append(string)
                string = ""
            else:
                string = string + "N"
        else:
            #for h in m.find_all("harmony"):
            #    if h.name == "harmony":
                    print m.harmony.kind.get("text")
                    index = 0
                    stringroot = str(m.harmony.root)
                    print(stringroot)
                    #if index > 0:
                    #    index = stringroot.find("-1")
                    #    if stringroot[index]=="-"
                    #        tempstring = "Ab"
                    #m.harmony.kind.get("text")
                    index = stringroot.find("A")
                    print stringroot[index]
                    if stringroot[index]=="A":
                        textg = m.harmony.kind.get("text")
                        if textg == "7":
                            if len(string)>0:
                                string = string + "A7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "A7"
                        elif textg == "m":
                            if len(string)>0:
                                string = string + "Am"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Am"
                        elif textg == "m7":
                            if len(string)>0:
                                string = string + "Am7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Am7"
                        else:
                            if len(string)>0:
                                string = string + "A"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "A"
                    print index
                    print stringroot[index]
                    index = stringroot.find("B")
                    print stringroot[index]
                    if stringroot[index]=="B":
                        textg = m.harmony.kind.get("text")
                        if textg == "7":
                            if len(string)>0:
                                string = string + "B7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "B7"
                        elif textg == "m":
                            if len(string)>0:
                                string = string + "Bm"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Bm"
                        elif textg == "m7":
                            if len(string)>0:
                                string = string + "Bm7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Bm7"
                        else:
                            if len(string)>0:
                                string = string + "B"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "B"
                    index = stringroot.find("C")
                    print stringroot[index]
                    if stringroot[index]=="C":
                        textg = m.harmony.kind.get("text")
                        if textg == "7":
                            if len(string)>0:
                                string = string + "C7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "C7"
                        elif textg == "m":
                            if len(string)>0:
                                string = string + "Cm"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Cm"
                        elif textg == "m7":
                            if len(string)>0:
                                string = string + "Cm7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Cm7"
                        else:
                            if len(string)>0:
                                string = string + "C"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "C"
                    index = stringroot.find("D")
                    print stringroot[index]
                    if stringroot[index]=="D":
                        textg = m.harmony.kind.get("text")
                        if textg == "7":
                            if len(string)>0:
                                string = string + "D7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "D7"
                        elif textg == "m":
                            if len(string)>0:
                                string = string + "Dm"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Dm"
                        elif textg == "m7":
                            if len(string)>0:
                                string = string + "Dm7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Dm7"
                        else:
                            if len(string)>0:
                                string = string + "D"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "D"
                    index = stringroot.find("E")
                    print stringroot[index]
                    if stringroot[index]=="E":
                        textg = m.harmony.kind.get("text")
                        if textg == "7":
                            if len(string)>0:
                                string = string + "E7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "E7"
                        elif textg == "m":
                            if len(string)>0:
                                string = string + "Em"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Em"
                        elif textg == "m7":
                            if len(string)>0:
                                string = string + "Em7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Em7"
                        else:
                            if len(string)>0:
                                string = string + "E"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "E"
                    index = stringroot.find("F")
                    print stringroot[index]
                    if stringroot[index]=="F":
                        textg = m.harmony.kind.get("text")
                        if textg == "7":
                            if len(string)>0:
                                string = string + "F7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "F7"
                        elif textg == "m":
                            if len(string)>0:
                                string = string + "Fm"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Fm"
                        elif textg == "m7":
                            if len(string)>0:
                                string = string + "Fm7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Fm7"
                        else:
                            if len(string)>0:
                                string = string + "F"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "F"
                    index = stringroot.find("G")
                    print stringroot[index]
                    if stringroot[index]=="G":
                        textg = m.harmony.kind.get("text")
                        if textg == "7":
                            print("G7")
                            if len(string)>0:
                                string = string + "G7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "G7"
                        elif textg == "m":
                            print("Gm")
                            if len(string)>0:
                                string = string + "Gm"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Gm"
                        elif textg == "m7":
                            print("Gm7")
                            if len(string)>0:
                                string = string + "Gm7"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "Gm7"
                        else:
                            if len(string)>0:
                                string = string + "G"
                                chord_list.append(string)
                                string = ""
                            else:
                                string = string + "G"
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
        print("<<calculate>>")
        calculate(pitch_list, duration_list, fifths, mode)
print("-------------start--------------")
while (True):
    judge = raw_input("Continue? yes:1 no:0 ")
    print(judge)
    if judge=="1": extract()#execute
    elif judge=="0": break
    else: break
