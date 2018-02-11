# chordfunction2.py
def chordfunction():
    chordfunction_list = []
    cf2_list=[]
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
        #cf2_list=[]
        del cf2_list[:]
        for cf in chordfunction_list:
            if len(s)>0:
                s=s+cf
                cf2_list.append(s)
                s=""
            elif len(s)==0:
                s=s+cf
        for i, j in enumerate(cf2_list):
            print('cf2_list'+'{0}:{1}'.format(i+1, j))
    """ Extract music data from xml file. """
    def extract():
        print("<<extract>>")
        #xml_name = raw_input("Please Enter FileName: ")
        from bs4 import BeautifulSoup
        #xml_name = "Your_Name_is_a_strong_tower.xml"# Your MusicXML file
        xml_name = "I_Will_Not_Forget_You.xml"# Your MusicXML file
        #xml_name = "Jesus_Oh_I_Love_You.xml"# Your MusicXML file
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
            calculate(pitch_list, duration_list, fifths, mode)
    print("-------------start--------------")
    extract()#execute
    return cf2_list
