import pandas as pd
import numpy as np 
# from flask import Flask, request
# import sys, json

#VARIABLES ATTACHED WITH THE STRING OF A CLUMN VARIABLE FROM THE RANKING DETAIL FILE
GHR = 'Google HOU Rank'
KW = 'Keyword'
VSBY = 'Visibility'
GHD = 'Google HOU Difference'
GP = 'Google Previous'
GMHR = 'Google Mobile HOU Rank'
KW = 'Keyword'
VSBY = 'Visibility'
GMHD = 'Google Mobile HOU Difference'
GMP = 'Google Mobile HOU Previous'
BNGR = 'Bing US Rank'
KW = 'Keyword'
VSBY = 'Visibility'
BNGDF = "Bing US Difference"
BNGP = 'Bing US Previous'
YAHR = 'Yahoo! Rank'
KW = 'Keyword'
VSBY = 'Visibility'
YAHDIF = "Yahoo! Difference"
YAHP = 'Yahoo! Previous'
SE = "SE"
NOTE = "NOTE"
GMHR = 'Google Mobile HOU Rank'
GMHD = 'Google Mobile HOU Difference'
RPS = 'Ranking page(s)'
RP = 'Ranking pages'



def NEG_Y_FUNCTION(X, Y, ARRAY):
    Y = -Y
    z =  Y + X 
    ARRAY.append(z)
    
def X_GRT_Y_LOGIC_FUNCTION(X, Y, ARRAY):
    Y = int(Y)
    X = int(X)
    if X > Y or X == Y:     
        z = X - Y
        ARRAY.append(z)
    else:
        Y = str(Y)
        if "-" in Y:
            Y = int(Y)
            ARRAY.append(Y)
        else:
            ARRAY.append(Y)      
    
def Y_FUNCTION(X, Y, ARRAY):
    Y = int(Y)

    if Y >= 0:
        X_GRT_Y_LOGIC_FUNCTION(X, Y, ARRAY)
        
    else:
        NEG_Y_FUNCTION(X, Y, ARRAY)
    
def LOGIC_X_Y_STR(X, Y, RA):
    if "+" in Y:
        POS_Y = int(Y[1])
        X_GRT_Y_LOGIC_FUNCTION(X, POS_Y, RA)
    else:
        POS_X = int(X)
        Y_FUNCTION(POS_X, Y, RA)
        

def STANDARD_XY_FUNCTION(AR, AD, RA):
    if "(" in AR:
        NEW_AR = str(AR)
        RANK_X = int(NEW_AR[0])
        y = int(AD)
        Y_FUNCTION(RANK_X, y, RA)
    else:
        LOGIC_X_Y_STR(AR, AD, RA)        
        

        


def REMOVE_BARS_FUNCTION(ARRAY_R, X, R_A):
    
    if "(" in ARRAY_R[X]:
        NEW_AR = str(ARRAY_R[X])
        RANK_X = NEW_AR[0]
        R_A.append(RANK_X)
    else:
        R_A.append(ARRAY_R[X])

def BAR_RMV_ARRAY_OUTPUT (ARRAY_RANK):
    RankArray = []
    
    
    for x in range(len(ARRAY_RANK)):
        REMOVE_BARS_FUNCTION(ARRAY_RANK, x, RankArray)
    return RankArray

def NOT_A_FLOAT_FUNCTION(AR, AD, RA):
    if len(AD) > 3 or pd.isna(AD) == True:
        RA.append(0)
    else:
        STANDARD_XY_FUNCTION(AR, AD, RA)

#def DEL_STR (AR, AD, RA):
    #if len(NEW_AR) > 3 == True: 
        
        


def ITS_A_FLOAT_FUNCTION(AR, AD, RA): 
    if pd.isna(AD) == True:
        RA.append(0)
    else:
        STANDARD_XY_FUNCTION(AR, AD, RA)
        




##ARRAY_OUTPUT IS THE CONCLUSION LOGIC FORM FUNCTION INTEGRATED FROM OF ALL ABOVE FUNCTIONS 
##ARRAY_DIF TAKES IN THE ARRAY HOLDING THE DIFFERENCE COLUMN VARIABLES
##ARRAY_RANK TAKES IN THE ARRAY HOLDING THE RANK COLUMN VARIABLES

def ARRAY_OUTPUT (ARRAY_DIF, ARRAY_RANK):
    
    ## CREATES AN BLANK ARRAY TO APPEND NEW VARIABLES TO
    RankArray = []
    
    ##A FOR LOOP IS CREATED TO GO OVER ALL VARIABLES IN THE RANGE OF THE LENGTH 
    ##OF THE DIFFERENCE COLUMNS VARIABLE (ARRAY_DIF)
    
    for x in range(len(ARRAY_DIF)):
        
        ##IF THE ARRAYS VARIABLE AT THE INDEX POSITION IS A FLOAT THEN THIS WILL EXECUTE A FUNCTION
        #CALLED ITS_A_FLOAT_FUNCTION
        if isinstance(ARRAY_DIF[x], float) == True:
            ITS_A_FLOAT_FUNCTION(ARRAY_RANK[x], ARRAY_DIF[x], RankArray)
            
        ##IF THE ARRAYS VARIABLE AT THE INDEX POSITION IS 
        #NOT A FLOAT THEN THIS WILL EXECUTE A FUNCTION
        #CALLED NOT_A_FLOAT_FUNCTION


        else:
            NOT_A_FLOAT_FUNCTION(ARRAY_RANK[x], ARRAY_DIF[x], RankArray)

    
    ##RETURNS THE DATA STORED IN THE VARIABLE SO IT CAN BE STORED ELSEWHERE
    ##FOR FURTHER DATA MANIPLUATION
    return RankArray
        
    
        
    


def ENTER_NEG_Y_FUNCTION(X, Y, ARRAY):
    Y = -Y
    
    ARRAY.append(Y)

def ENTER_X_GRT_Y_LOGIC_FUNCTION(X, Y, ARRAY):
    ARRAY.append(Y)
    

        
    
def ENTER_NEG_Y_FUNCTION(X, Y, ARRAY):
    Y = -Y
    
    ARRAY.append(Y)

def ENTER_X_GRT_Y_LOGIC_FUNCTION(X, Y, ARRAY):
    ARRAY.append(Y)
    

        
    
def ENTER_Y_FUNCTION(X, Y, ARRAY):
    Y = int(Y)
    if Y >= 0:
        ENTER_X_GRT_Y_LOGIC_FUNCTION(X, Y, ARRAY)
        
    else:
        ENTER_NEG_Y_FUNCTION(X, Y, ARRAY)
    
def ENTER_LOGIC_X_Y_STR(ARRAY, Y, RA):
    Y = str(Y)
    if "+" in Y:
        POS_Y = int(Y[1])
        ENTER_X_GRT_Y_LOGIC_FUNCTION(ARRAY, POS_Y, RA)
    else:
        POS_X = int(ARRAY)
        ENTER_Y_FUNCTION(POS_X, Y, RA)
        
        
        
def ENTER_STANDARD_XY_FUNCTION(AR, AD, RA):
    if "(" in AR:
        NEW_AR = str(AR)
        RANK_X = int(NEW_AR[0])
        y = int(AD)
        ENTER_Y_FUNCTION(RANK_X, y, RA)
    else:
        DIF_Y = int(AD)
        ENTER_LOGIC_X_Y_STR(AR, DIF_Y, RA)

def ENTER_NOT_A_FLOAT_FUNCTION(AR, AD, RA):
    if len(AD) > 3 or pd.isna(AD) == True:
        RA.append(0)
    else:
        ENTER_STANDARD_XY_FUNCTION(AR, AD, RA)
        
def ENTER_ITS_A_FLOAT_FUNCTION(AR, AD, RA): 
    if pd.isna(AD) == True:
        RA.append(0)
    else:
        ENTER_STANDARD_XY_FUNCTION(AR, AD, RA)




def CHANGE_ENTER_FUNCTION(AR, AD, AP):
    RankArray = []
    
    for x in range(len(AD)):
        if isinstance(AD[x], float) == True:
            if pd.isna(AD[x]) == True:
                if len(AR[x]) > 3 or pd.isna(AR[x]) == True:
                    RankArray.append(30)
                else:
                    ARX = int(AR[x])
                    RankArray.append(30-ARX)
            else:
                ENTER_ITS_A_FLOAT_FUNCTION(AR[x], AD[x], RankArray)
        
        else:
            if len(AD[x]) > 3 or pd.isna(AD[x]) == True:
                if len(AR[x]) > 3 or pd.isna(AR[x]) == True:
                    RankArray.append(30)
                else:
                    ARX = int(AR[x])
                    RankArray.append(30-ARX)
            else:
                ENTER_NOT_A_FLOAT_FUNCTION(AR[x], AD[x], RankArray)
        
    return RankArray
        
          
    
   

def NOTE_Y_FUNCTION(X, Y, ARRAY): 
    X = int(X)
    Y = int(Y)
    if X > Y:
        ARRAY.append("⬆️")
        
    if X < Y:
        ARRAY.append("⬇️")
    
    if X == Y:
        ARRAY.append("🟰")


def CHANGE_NOTE_FUNCTION(AR, AP):
    RankArray = []
    
    for x in range(len(AP)):
        
        if AP[x] == 0 or len(AR[x]) > 3:
            RankArray.append('⭐')
        else:
            ARX = int(AR[x])
            NOTE_Y_FUNCTION(ARX, AP[x], RankArray)
        
    return RankArray
          

          
# app = Flask(__name__) 
# @app.route('/FindFrame', methods = ['POST']) 
# def FIND_FRAME ():
def FIND_FRAME (FILE_PATH1):

    
    # data = request.get_json() 
    # print(data)
    # ls = data[2]

    # df = pd.read_csv(data[0])

    # dc = pd.read_csv(data[1])

    df = pd.read_csv(FILE_PATH1)


    ArrayGHR = pd.array(df[GHR])
    ArrayGHD = pd.array(df[GHD])
    ArrayGMHR = pd.array(df[GMHR])
    ArrayGMHD = pd.array(df[GMHD])

    Array_GHR = BAR_RMV_ARRAY_OUTPUT(ArrayGHR)
    GPD = ARRAY_OUTPUT(ArrayGHD, Array_GHR)
    Array_GMHR = BAR_RMV_ARRAY_OUTPUT(ArrayGMHR)
    GMPDF = ARRAY_OUTPUT(ArrayGMHD, Array_GMHR)
    ArrayBNGDF = pd.array(df[BNGDF])
    ArrayBNGR = pd.array(df[BNGR])
    Array_BNGR = BAR_RMV_ARRAY_OUTPUT(ArrayBNGR)    
    BNGDFF = ARRAY_OUTPUT(ArrayBNGDF, Array_BNGR)
    ArrayYAHDIF = pd.array(df[YAHDIF])
    ArrayYAHR = pd.array(df[YAHR])
    Array_YAHR = BAR_RMV_ARRAY_OUTPUT(ArrayYAHR)
    YAHDF = ARRAY_OUTPUT(ArrayYAHDIF, Array_YAHR)
    GODIF_NEW = CHANGE_ENTER_FUNCTION(Array_GHR, ArrayGHD, GPD)
    GOMDIF_NEW = CHANGE_ENTER_FUNCTION(Array_GMHR, ArrayGMHD, GMPDF)
    BNGDIF_NEW = CHANGE_ENTER_FUNCTION(Array_BNGR, ArrayBNGDF, BNGDFF)
    YAHDIF_NEW = CHANGE_ENTER_FUNCTION(Array_YAHR, ArrayYAHDIF, YAHDF)
    GOD_NOTE = CHANGE_NOTE_FUNCTION(Array_GHR, GPD)
    GOM_NOTE = CHANGE_NOTE_FUNCTION(Array_GMHR, GMPDF)
    BNG_NOTE = CHANGE_NOTE_FUNCTION(Array_BNGR, BNGDFF)
    YAH_NOTE = CHANGE_NOTE_FUNCTION(Array_YAHR, YAHDF)


    GOD = {KW: df[KW],RP: df[RPS], GHR: Array_GHR,
       GP: GPD, GHD: GODIF_NEW, NOTE: GOD_NOTE}

    GOM = {KW: df[KW],RP: df[RPS], GMHR: Array_GMHR, 
       GMP: GMPDF, GMHD: GOMDIF_NEW, NOTE: GOM_NOTE}

    BNG = {KW: df[KW],RP: df[RPS], BNGR: Array_BNGR,
       BNGP: BNGDFF, BNGDF: BNGDIF_NEW, NOTE: BNG_NOTE}

    YAH = {KW: df[KW],RP: df[RPS], YAHR: Array_YAHR,
       YAHP: YAHDF, YAHDIF: YAHDIF_NEW, NOTE: YAH_NOTE}
    GOD_DF = pd.DataFrame(data=GOD)
    GOM_DF = pd.DataFrame(data=GOM)
    BNG_DF = pd.DataFrame(data=BNG)
    YAH_DF = pd.DataFrame(data=YAH)

    REPORT_NAME = ['ReportSERPPositionsGOD.csv', 'ReportSERPPositionsGOM.csv', 'ReportSERPPositionsBNG.csv', 'ReportSERPPositionsYAH.csv']
    frames = [GOD_DF, GOM_DF, BNG_DF, YAH_DF]
    for i in range(len(frames)):
        frames[i].to_csv(REPORT_NAME[i], index = None, header = False, sep='|')
    # CHOSEN_FRApythME = REPORT_NAME[ls]
    # return json.dumps({"result": CHOSEN_FRAME})
    # print(frames[0:3])
    return frames

# FIND_FRAME ('ABBA_TEST.csv')

# if __name__ == "__main__":
#     app.run(port=5000)
