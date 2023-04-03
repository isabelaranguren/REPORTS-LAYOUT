#!/usr/bin/env python
# coding: utf-8

# In[111]:


import pandas as pd
import numpy as np 

#READING RANKING FILE FROM CSV


# In[112]:


df = pd.read_csv('ABBA_RANK.csv');
# len(pd.DataFrame(data=df[df["Google HOU Rank"] == "1"])) + len(pd.DataFrame(data=df[df["Google HOU Rank"] == 1]))
# NEW_DF_ = [len(df[df["Google HOU Difference"] == "Entered"]), len(df[df["Google Mobile HOU Difference"] == "Entered"]), len(df[df["Bing US Difference"] == "Entered"]), len(df[df["Yahoo! Difference"] == "Entered"])]
# NEW_DF_PD = pd.DataFrame(NEW_DF_)
# NEW_CLEAN_DF = NEW_DF_PD.sum()[0]
# NEW_CLEAN_DF
# df[df["Google HOU Difference"] == "NaN"]
df[220:224]


# In[113]:


# RANKING DETAILS FILE VARIABLE 
df[195:196]


# In[114]:


# VARIABLES ATTACHED WITH THE STRING OF A COLUMN VARIABLE FROM THE RANKING DETAIL FILE
GHR = 'Google HOU Rank'
GHPR = 'Google HOU Previous Rank'
GHD = 'Google HOU Difference'

YAHR = 'Yahoo! Rank'
YAHP = 'Yahoo! Previous Rank'
YAHDIF = "Yahoo! Difference"

GMP = 'Google Mobile HOU Previous Rank'
GMHR = 'Google Mobile HOU Rank'
GMHD = 'Google Mobile HOU Difference'

BNGR = 'Bing US Rank'
BNGDF = "Bing US Difference"
BNGP = 'Bing US Previous Rank'

KW = 'Keyword'
VSBY = 'Visibility'

GP = 'Google HOU Rank'
KW = 'Keyword'
VSBY = 'Visibility'

BNGR = 'Bing US Rank'
KW = 'Keyword'
VSBY = 'Visibility'
BNGDF = "Bing US Difference"
BNGP = 'Bing US Previous'

KW = 'Keyword'
VSBY = 'Visibility'

SE = "SE"
NOTE = "NOTE"

RP = 'Ranking page(s)'

_URL_ = "URL"
URL_RANK =  "Google HOU URL Found"
GMHUF = "Google Mobile HOU URL Found"
GHUF=  "Google HOU URL Found"
BUUF =  "Bing US URL Found"
YUF = "Yahoo! URL Found"
LP_1= "Local Pack (1)"
GOD_SERP = "Google HOU SERP Features"
GOM_SERP = "Google Mobile HOU SERP Features"
BNG_SERP = "Bing US SERP Features"
YAH_SERP =  "Yahoo! SERP Features"


# In[115]:


GHR = 'Google HOU Rank'
GHPR = 'Google HOU Previous Rank'
GHD = 'Google HOU Difference'

YAHR = 'Yahoo! Rank'
YAHP = 'Yahoo! Previous Rank'
YAHDIF = "Yahoo! Difference"

GMP = 'Google Mobile HOU Previous Rank'
GMHR = 'Google Mobile HOU Rank'
GMHD = 'Google Mobile HOU Difference'

BNGR = 'Bing US Rank'
BNGDF = "Bing US Difference"
BNGP = 'Bing US Previous Rank'


GOD_F = {KW: df[KW],_URL_: df[URL_RANK], GHR: df[GHR], GHPR: df[GHPR], GHD: df[GHD]}

GOM_F = {KW: df[KW],_URL_: df[URL_RANK], GMP: df[GMP], GMHR: df[GMHR], GMHD: df[GMHD]}

BNG_F = {KW: df[KW],_URL_: df[URL_RANK], BNGR: df[BNGR], BNGDF: df[BNGDF], BNGP: df[BNGP]}

YAH_F = {KW: df[KW],_URL_: df[URL_RANK], YAHR: df[YAHR],YAHP: df[YAHP], YAHDIF: df[YAHDIF]}

GOD_H = pd.DataFrame(GOD_F)

GOM_H = pd.DataFrame(GOM_F)

BNG_H = pd.DataFrame(BNG_F)

YAH_H = pd.DataFrame(YAH_F)

GOD_CLEAN_1 = GOD_H[GOD_H[GHD] != "Stays out"]
GOM_CLEAN_1 = GOM_H[GOM_H[GMHD] != "Stays out"]
BNG_CLEAN_1 = BNG_H[BNG_H[BNGDF] != "Stays out"]
YAH_CLEAN_1 = YAH_H[YAH_H[YAHDIF] != "Stays out"]

GOD_CLEAN_2 = GOD_CLEAN_1[GOD_CLEAN_1[GHD] != "Dropped"]
GOM_CLEAN_2 = GOM_CLEAN_1[GOM_CLEAN_1[GMHD] != "Dropped"]
BNG_CLEAN_2 = BNG_CLEAN_1[BNG_CLEAN_1[BNGDF] != "Dropped"]
YAH_CLEAN_2 = YAH_CLEAN_1[YAH_CLEAN_1[YAHDIF] != "Dropped"]

BNG_H[BNG_H[BNGDF] == "Entered"]



# In[116]:


#FIRST WE USE THE VARIABLE THAT STORES THE COLUMNS NAME. WE PLACE IT IN THE DF SQUARE BRACKET [] 
# PLACING IT IN THE SQUARE BRACKET SEARCHES THE 
# df (dataframe) column section for it's array under its name
#We use pandas (pd) to turn the dataframe (df) into an array

ArrayGHR = pd.array(GOD_CLEAN_2[GHR])
ArrayGHD = pd.array(GOD_CLEAN_2[GHD])
ArrayGMHR = pd.array(GOM_CLEAN_2[GMHR])
ArrayGMHD = pd.array(GOM_CLEAN_2[GMHD])


# In[117]:


def NEG_Y_FUNCTION(X, Y, ARRAY):
    Y = -Y
    z =  Y + X 
    ARRAY.append(z)
    
def X_GRT_Y_LOGIC_FUNCTION(X, Y, ARRAY):
    Y = int(Y)
    X = int(X)
    if X > Y or X == Y:
        
        z = X + Y
        ARRAY.append(z)
    else:
        Y = str(Y)
        if "-" in Y:
            Y = int(Y)
            ARRAY.append(Y)
        else:
            z = X + int(Y)
            ARRAY.append(z)      

            
def Y_FUNCTION(X, Y, ARRAY):
    Y = int(Y)

    if Y >= 0:
        X_GRT_Y_LOGIC_FUNCTION(X, Y, ARRAY)
        
    else:
        NEG_Y_FUNCTION(X, Y, ARRAY)

        
def LOGIC_X_Y_STR(X, Y, RA):
    if "+" in str(Y):
        POS_Y = int(str(Y)[1])
        X_GRT_Y_LOGIC_FUNCTION(X, POS_Y, RA)
    else:
        POS_X = int(X)
        Y_FUNCTION(POS_X, Y, RA)
        

        
def STANDARD_XY_FUNCTION(AR, AD, RA):
    if "(" in AR:
        NEW_AR = str(AR)
        RANK_X = int(NEW_AR[0])
        if "(" in str(AD):
            NEW_AD = str(AD)
            RANK_Y = int(NEW_AD[0])
            Y_FUNCTION(RANK_X, RANK_Y, RA)
        else:
            y = int(AD)
            Y_FUNCTION(RANK_X, y, RA)
    else:
        DIF_Y = int(AD)
        LOGIC_X_Y_STR(AR, DIF_Y, RA)
        


def REMOVE_BARS_FUNCTION(ARRAY_R, X, R_A):
    
    if "(" in str(ARRAY_R[X]):
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
        RA.append(30)
    else:
        if "N" in str(AR):
            RA.append(30)
        else:
            STANDARD_XY_FUNCTION(AR, AD, RA)

#def DEL_STR (AR, AD, RA):
    #if len(NEW_AR) > 3 == True: 
        
        


def ITS_A_FLOAT_FUNCTION(AR, AD, RA): 
    if pd.isna(AD) == True:
        RA.append(30)
    else:
        STANDARD_XY_FUNCTION(AR, AD, RA)
        




##ARRAY_OUTPUT IS THE CONCLUSION LOGIC FORM FUNCTION INTEGRATED FROM OF ALL ABOVE FUNCTIONS 
##ARRAY_DIF TAKES IN THE ARRAY HOLDING THE DIFFERENCE COLUMN VARIABLES
##ARRAY_RANK TAKES IN THE ARRAY HOLDING THE RANK COLUMN VARIABLES
##DCDF TAKES IN THE WHOLE DATAFRAME OF THE DC VARIABLE


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
        
    


# In[118]:


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
    if "+" in str(Y):
        POS_Y = int(str(Y)[1])
        ENTER_X_GRT_Y_LOGIC_FUNCTION(ARRAY, POS_Y, RA)
    else:
        if "N" in ARRAY:
            RA.append(30)
        else:
            POS_X = int(ARRAY)
            ENTER_Y_FUNCTION(POS_X, Y, RA)
        
        
        
def ENTER_STANDARD_XY_FUNCTION(AR, AD, RA):
    if "(" in AR:
        NEW_AR = str(AR)
        RANK_X = int(NEW_AR[0])
        if "(" in str(AD):
            NEW_AD = str(AD)
            RANK_Y = int(NEW_AD[0])
            ENTER_Y_FUNCTION(RANK_X, RANK_Y, RA)
        else:
            y = int(AD)
            ENTER_Y_FUNCTION(RANK_X, y, RA)
    else:
        DIF_Y = int(AD)
        ENTER_LOGIC_X_Y_STR(AR, DIF_Y, RA)
#####
def ENTER_NOT_A_FLOAT_FUNCTION(AR, AD, RA):
    if len(AD) > 3 or pd.isna(AD) == True:
        if "(" in AR:
            ENTER_STANDARD_XY_FUNCTION(AR, AD, RA)
        else:
            RA.append(30)
    else:
        ENTER_STANDARD_XY_FUNCTION(AR, AD, RA)
        
def ENTER_ITS_A_FLOAT_FUNCTION(AR, AD, RA): 
    if pd.isna(AD) == True:
        RA.append(30)
    else:
        ENTER_STANDARD_XY_FUNCTION(AR, AD, RA)




def CHANGE_ENTER_FUNCTION(AR, AD, AP):
    RankArray = []
    
    for x in range(len(AD)):
        if isinstance(AD[x], float) == True:
            if pd.isna(AD[x]) == True:
                if len(AR[x]) > 3 or pd.isna(AR[x]) == True:
                    if "E" in str(AD[x]):
                        RankArray.append(30-ARX)
                    else:
                        RankArray.append(30)
                else:
                    ENTER_ITS_A_FLOAT_FUNCTION(AR[x], AD[x], RankArray)

            else:
                ENTER_ITS_A_FLOAT_FUNCTION(AR[x], AD[x], RankArray)
        
        else:
            if len(AD[x]) > 3 or pd.isna(AD[x]) == True or "E" in str(AD[x]):
                if len(AR[x]) > 3 or pd.isna(AR[x]) == True:
                    if "E" in str(AD[x]):
                        ARX = int(AR[x])
                        RankArray.append(30-ARX)
                    else:
                        RankArray.append(30)
                else:
                    ENTER_NOT_A_FLOAT_FUNCTION(AR[x], AD[x], RankArray)

            else:
                ENTER_NOT_A_FLOAT_FUNCTION(AR[x], AD[x], RankArray)
        
    return RankArray
        
    


# In[119]:


def NOTE_Y_FUNCTION(X, Y, ARRAY): 
    X = int(X)
    Y = int(Y)
    if X < Y:
        ARRAY.append("UP")
        
    if X > Y:
        ARRAY.append("DOWN")
    
    if X == Y:
        ARRAY.append("EQ")


def CHANGE_NOTE_FUNCTION(AR, AP):
    RankArray = []
    
    for x in range(len(AP)):
        
        if AP[x] == 30 or len(AR[x]) > 3 or len(str(AP[x])) > 3:
            RankArray.append('NEW')
        else:
            ARX = int(AR[x])
            NOTE_Y_FUNCTION(ARX, AP[x], RankArray)
        
    return RankArray




# In[120]:


Array_GHR = BAR_RMV_ARRAY_OUTPUT(ArrayGHR)



# In[121]:


GPD = ARRAY_OUTPUT(ArrayGHD, Array_GHR)

    


# In[122]:


Array_GMHR = BAR_RMV_ARRAY_OUTPUT(ArrayGMHR)
GMPDF = ARRAY_OUTPUT(ArrayGMHD, Array_GMHR)
ArrayBNGDF = pd.array(BNG_CLEAN_2[BNGDF])
ArrayBNGR = pd.array(BNG_CLEAN_2[BNGR])
Array_BNGR = BAR_RMV_ARRAY_OUTPUT(ArrayBNGR)
Array_BNGDF = BAR_RMV_ARRAY_OUTPUT(ArrayBNGDF)



# In[123]:


BNGDFF = ARRAY_OUTPUT(Array_BNGDF, Array_BNGR)
BNGDFF[223:224]


# In[124]:


ArrayYAHDIF = pd.array(YAH_CLEAN_2[YAHDIF])

ArrayYAHR = pd.array(YAH_CLEAN_2[YAHR])

Array_YAHR = BAR_RMV_ARRAY_OUTPUT(ArrayYAHR)

YAHDF = ARRAY_OUTPUT(ArrayYAHDIF, Array_YAHR)



# In[125]:


GODIF_NEW = CHANGE_ENTER_FUNCTION(Array_GHR, ArrayGHD, GPD)
GOMDIF_NEW = CHANGE_ENTER_FUNCTION(Array_GMHR, ArrayGMHD, GMPDF)
BNGDIF_NEW = CHANGE_ENTER_FUNCTION(Array_BNGR, ArrayBNGDF, BNGDFF)
YAHDIF_NEW = CHANGE_ENTER_FUNCTION(Array_YAHR, ArrayYAHDIF, YAHDF)
BNGDIF_NEW[223:224]



# In[126]:


GOD_NOTE = CHANGE_NOTE_FUNCTION(Array_GHR, GPD)
GOM_NOTE = CHANGE_NOTE_FUNCTION(Array_GMHR, GMPDF)
BNG_NOTE = CHANGE_NOTE_FUNCTION(Array_BNGR, BNGDFF)
YAH_NOTE = CHANGE_NOTE_FUNCTION(Array_YAHR, YAHDF)
BNG_NOTE[223:224]



# In[127]:


#KW = keyword, GHRF = URL found, GHR = Rank, GHD = difference, GP = Google Previous, VSBY = visibilty,
#note = note

GOD = {KW: GOD_CLEAN_2[KW],RP: GOD_CLEAN_2[_URL_], GHR: Array_GHR,
       GHPR: GPD, GHD: GODIF_NEW, NOTE: GOD_NOTE}

GOM = {KW: GOM_CLEAN_2[KW], RP: GOM_CLEAN_2[_URL_], GMHR: Array_GMHR, 
       GMP: GMPDF, GMHD: GOMDIF_NEW, NOTE: GOM_NOTE}

BNG = {KW: BNG_CLEAN_2[KW], RP: BNG_CLEAN_2[_URL_], BNGR: Array_BNGR,
       BNGP: BNGDFF, BNGDF: BNGDIF_NEW, NOTE: BNG_NOTE}

YAH = {KW: YAH_CLEAN_2[KW],RP: YAH_CLEAN_2[_URL_], YAHR: Array_YAHR,
       YAHP: YAHDF, YAHDIF: YAHDIF_NEW, NOTE: YAH_NOTE}


# In[128]:


GOD_DF = pd.DataFrame(data=GOD)
GOD_DF


# In[129]:


GOD_NEW = pd.DataFrame(data=GOD_DF[GOD_DF[GHR] != "Not in top 30"])
GOD_LEN = len(GOD_NEW)
GOD_1 = pd.DataFrame(data=GOD_NEW[GOD_NEW[GHR] == "1"])
GOD_NEW_NOTE = pd.DataFrame(data=GOD_NEW[GOD_NEW[NOTE] == "NEW"])
GOD_NOTE = len(GOD_NEW_NOTE)
GOD_UP_NOTE = pd.DataFrame(data=GOD_NEW[GOD_NEW[NOTE] == "UP"])
GOD_UP = len(GOD_UP_NOTE)
GOD_DOWN_NOTE = pd.DataFrame(data=GOD_NEW[GOD_NEW[NOTE] == "DOWN"])
GOD_DOWN = len(GOD_DOWN_NOTE)
GOD_EQ_NOTE = pd.DataFrame(data=GOD_NEW[GOD_NEW[NOTE] == "EQ"])
GOD_EQ = len(GOD_EQ_NOTE)
GOD_LP_LEN = pd.DataFrame(data=df[GOD_SERP])
GOD_LP = len(GOD_LP_LEN)
GOD_1_LEN = len(GOD_1)
GOD_NOTE


# In[130]:


print(GOD_LP_LEN)


# In[131]:


LP_GOD_ = []
for x in range(len(df)):
    if LP_1 in str(GOD_LP_LEN[GOD_SERP][x]):
        LP_GOD_.append(GOD_LP_LEN[GOD_SERP][x])
    else:
        False
print(len(LP_GOD_))


# In[132]:


TOP_5GOD = []
GOD_FIRST_PAGE = []
GOD_TWO_PAGE = []

LP_GOD = pd.DataFrame()
for x in range(5):
    TOP_5GOD.append(len(GOD_NEW[GOD_NEW[GHR] == str(x+1)]))

for x in range(10):
    GOD_NEW[GHR]
    GOD_FIRST = len(pd.DataFrame(data=GOD_NEW[GOD_NEW[GHR] == str(x+1)]))
    GOD_FIRST_PAGE.append(GOD_FIRST)

for x in range(20):
    GOD_TWO = len(pd.DataFrame(data=GOD_NEW[GOD_NEW[GHR] == str(x+1)]))
    GOD_TWO_PAGE.append(GOD_TWO)


TOP_5GOD

len(GOD_DF[GOD_DF[NOTE] == "NEW"])


# In[133]:


GOD_5_TOP = pd.DataFrame(data=TOP_5GOD)
GOD5_TOP = GOD_5_TOP.sum()[0]
GOD_FIRST_PAGE_TOP = pd.DataFrame(data=GOD_FIRST_PAGE)
GODFIRST_TOP = GOD_FIRST_PAGE_TOP.sum()[0]
GOD_TWO_PAGE_TOP = pd.DataFrame(data=GOD_TWO_PAGE)
GODTWO_TOP= GOD_TWO_PAGE_TOP.sum()[0]


# In[134]:


GOM_DF = pd.DataFrame(data=GOM)
GOM_DF

GOM_NEW = pd.DataFrame(data=GOM_DF[GOM_DF[GMHR] != "Not in top 30"])
GOM_LEN = len(GOM_DF)
GOM_1= pd.DataFrame(data=GOM_NEW[GOM_NEW[GMHR] == "1"])
GOM_NEW_NOTE = pd.DataFrame(data=GOM_NEW[GOM_NEW[NOTE] == "NEW"])
GOM_NOTE = len(GOM_NEW_NOTE)
GOM_UP_NOTE = pd.DataFrame(data=GOM_NEW[GOM_NEW[NOTE] == "UP"])
GOM_UP = len(GOM_UP_NOTE)
GOM_DOWN_NOTE = pd.DataFrame(data=GOM_NEW[GOM_NEW[NOTE] == "DOWN"])
GOM_DOWN = len(GOM_DOWN_NOTE)
GOM_EQ_NOTE = pd.DataFrame(data=GOM_NEW[GOM_NEW[NOTE] == "EQ"])
GOM_EQ = len(GOM_EQ_NOTE)
GOM_LP_LEN = pd.DataFrame(data=df[GOM_SERP])
GOM_LP = len(GOM_LP_LEN)
GOM_1_LEN = len(GOM_1)


TOP_5GOM = []
GOM_FIRST_PAGE = []
GOM_TWO_PAGE = []

# TODO: 

LP_GOM = []

for x in range(len(df)):
    if LP_1 in str(GOM_LP_LEN[GOM_SERP][x]):
        LP_GOM.append(GOM_LP_LEN[GOM_SERP][x])
    else:
        False
print(len(LP_GOM))


for x in range(5):
    GOM_5 = len(pd.DataFrame(data=GOM_NEW[GOM_NEW[GMHR] == str(x+1)]))
    TOP_5GOM.append(GOM_5)
    
for x in range(10):
    GOM_FIRST = len(pd.DataFrame(data=GOM_NEW[GOM_NEW[GMHR] == str(x+1)]))
    GOM_FIRST_PAGE.append(GOM_FIRST)

for x in range(20):
    GOM_TWO = len(pd.DataFrame(data=GOM_NEW[GOM_NEW[GMHR] == str(x+1)]))
    GOM_TWO_PAGE.append(GOM_TWO)
    

GOM_5_TOP = pd.DataFrame(data=TOP_5GOM)
GOM5_TOP = GOM_5_TOP.sum()[0]
GOM_FIRST_PAGE_TOP = pd.DataFrame(data=GOM_FIRST_PAGE)
GOMFIRST_TOP = GOM_FIRST_PAGE_TOP.sum()[0]
GOM_TWO_PAGE_TOP = pd.DataFrame(data=GOM_TWO_PAGE)
GOMTWO_TOP= GOM_TWO_PAGE_TOP.sum()[0]
GOM5_TOP



# In[135]:


BNG_DF = pd.DataFrame(data=BNG)

BNG_NEW = pd.DataFrame(data=BNG_DF[BNG_DF [BNGR] != "Not in top 30"])
BNG_LEN = len(BNG_NEW)
BNG_1= pd.DataFrame(data=BNG_NEW[BNG_NEW[BNGR] == "1"])
BNG_NEW_NOTE = pd.DataFrame(data=BNG_NEW[BNG_NEW[NOTE] == "NEW"])
BNG_NOTE = len(BNG_NEW_NOTE)
BNG_UP_NOTE = pd.DataFrame(data=BNG_NEW[BNG_NEW[NOTE] == "UP"])
BNG_UP = len(BNG_UP_NOTE)
BNG_DOWN_NOTE = pd.DataFrame(data=BNG_NEW[BNG_NEW[NOTE] == "DOWN"])
BNG_DOWN = len(BNG_DOWN_NOTE)
BNG_EQ_NOTE = pd.DataFrame(data=BNG_NEW[BNG_NEW[NOTE] == "EQ"])
BNG_EQ = len(BNG_EQ_NOTE)
BNG_LP_LEN = pd.DataFrame(data=df[BNG_SERP])
BNG_LP = len(BNG_LP_LEN)
BNG_1_LEN = len(BNG_1)


TOP_5BNG = []
BNG_FIRST_PAGE = []
BNG_TWO_PAGE = []

LP_BNG_ = []

for x in range(len(df)):
    if LP_1 in str(BNG_LP_LEN[BNG_SERP][x]):
        LP_BNG_.append(BNG_LP_LEN[BNG_SERP][x])
    else:
        False
    print(len(LP_BNG_))
        

for x in range(5):
    BNG_5 = len(pd.DataFrame(data=BNG_NEW[BNG_NEW[BNGR] == str(x+1)]))
    TOP_5BNG.append(BNG_5)
    
for x in range(10):
    BNG_FIRST = len(pd.DataFrame(data=BNG_NEW[BNG_NEW[BNGR] == str(x+1)]))
    BNG_FIRST_PAGE.append(BNG_FIRST)

for x in range(20):
    BNG_TWO = len(pd.DataFrame(data=BNG_NEW[BNG_NEW[BNGR] == str(x+1)]))
    BNG_TWO_PAGE.append(BNG_TWO)
    

BNG_5_TOP = pd.DataFrame(data=TOP_5BNG)
BNG5_TOP = BNG_5_TOP.sum()[0]
BNG_FIRST_PAGE_TOP = pd.DataFrame(data=BNG_FIRST_PAGE)
BNGFIRST_TOP = BNG_FIRST_PAGE_TOP.sum()[0]
BNG_TWO_PAGE_TOP = pd.DataFrame(data=BNG_TWO_PAGE)
BNGTWO_TOP= BNG_TWO_PAGE_TOP.sum()[0]
BNG_NEW[BNG_NEW["Keyword"] == "abba houston"]


# In[136]:


# for x in range(len(df)):
#     print(BNG_LP_LEN[BNG_SERP][x])
#     if LP_1 in str(BNG_LP_LEN[BNG_SERP][x]):
#         LP_BNG.append(BNG_LP_LEN[BNG_SERP][x])
#     else:
#         False
# print(LP_BNG)


# In[159]:


YAH_DF = pd.DataFrame(data=YAH)
YAH_DF
YAH_NEW = pd.DataFrame(data=YAH_DF[YAH_DF [YAHR] != "Not in top 30"])
YAH_LEN = len(YAH_NEW)
YAH_1= pd.DataFrame(data=YAH_NEW[YAH_NEW[YAHR] == "1"])
YAH_NEW_NOTE = pd.DataFrame(data=YAH_NEW[YAH_NEW[NOTE] == "NEW"])
YAH_NOTE = len(YAH_NEW_NOTE)
YAH_UP_NOTE = pd.DataFrame(data=YAH_NEW[YAH_NEW[NOTE] == "UP"])
YAH_UP = len(YAH_UP_NOTE)
YAH_DOWN_NOTE = pd.DataFrame(data=YAH_NEW[YAH_NEW[NOTE] == "DOWN"])
YAH_DOWN = len(YAH_DOWN_NOTE)
YAH_EQ_NOTE = pd.DataFrame(data=YAH_NEW[YAH_NEW[NOTE] == "EQ"])
YAH_EQ = len(YAH_EQ_NOTE)
YAH_LP_LEN = pd.DataFrame(data=df[YAH_SERP])
YAH_LP = len(YAH_LP_LEN)
YAH_1_LEN = len(YAH_1)


TOP_5YAH = []
YAH_FIRST_PAGE = []
YAH_TWO_PAGE = []

LP_YAH_ = []

# Search if Local Pack exists

for x in range(len(df)):
    if LP_1 in str(YAH_LP_LEN[YAH_SERP][x]):
        LP_YAH_.append(YAH_LP_LEN[YAH_SERP][x])
    else:
        False
    print(len(LP_YAH_))


for x in range(5):
    YAH_5 = len(pd.DataFrame(data=YAH_NEW[YAH_NEW[YAHR] == str(x+1)]))
    TOP_5YAH.append(YAH_5)
    
for x in range(10):
    YAH_FIRST = len(pd.DataFrame(data=YAH_NEW[YAH_NEW[YAHR] == str(x+1)]))
    YAH_FIRST_PAGE.append(YAH_FIRST)

for x in range(20):
    YAH_TWO = len(pd.DataFrame(data=YAH_NEW[YAH_NEW[YAHR] == str(x+1)]))
    YAH_TWO_PAGE.append(YAH_TWO)
    

YAH_5_TOP = pd.DataFrame(data=TOP_5YAH)
YAH5_TOP = YAH_5_TOP.sum()[0]
YAH_FIRST_PAGE_TOP = pd.DataFrame(data=YAH_FIRST_PAGE)
YAH_FIRST_TOP = YAH_FIRST_PAGE_TOP.sum()[0]
YAH_TWO_PAGE_TOP = pd.DataFrame(data=YAH_TWO_PAGE)
YAH_TWO_TOP= YAH_TWO_PAGE_TOP.sum()[0]
len(YAH_DF[YAH_DF[NOTE] == "NEW"])
YAH_NOTE


# In[138]:


GOD_NEW_NOTE[GOD_NEW_NOTE['Ranking page(s)'].isnull() == False]
GOM_NEW_NOTE[GOM_NEW_NOTE['Ranking page(s)'].isnull() == False]
BNG_NEW_NOTE[BNG_NEW_NOTE['Ranking page(s)'].isnull() == False]
# YAH_NEW_NOTE[YAH_NEW_NOTE['Ranking page(s)'].isnull() == False]


# In[139]:


ARR = [GOM_1_LEN, GOD_1_LEN, BNG_1_LEN, YAH_1_LEN]
ARR_1 = pd.DataFrame(ARR)
TOP_1 = ARR_1.sum()[0]
TOP_1


# In[140]:


ARR_TOP_5 = [GOM5_TOP, GOD5_TOP, BNG5_TOP, YAH5_TOP]
TOP_5 = pd.DataFrame(ARR_TOP_5)
TOP_5 = TOP_5.sum()[0]
TOP_5


# In[141]:


ARR_FIRST_PAGE = [GODFIRST_TOP, GOMFIRST_TOP, BNGFIRST_TOP, YAH_FIRST_TOP]
FIRST_PAGE_DF = pd.DataFrame(ARR_FIRST_PAGE)
FIRST_PAGE = FIRST_PAGE_DF.sum()[0]
FIRST_PAGE


# In[142]:


ARR_TWO_PAGE = [GODTWO_TOP, GOMTWO_TOP, BNGTWO_TOP, YAH_TWO_TOP]
FIRST_TWO_DF = pd.DataFrame(ARR_TWO_PAGE)
FIRST_TWO = FIRST_TWO_DF.sum()[0]
FIRST_TWO


# In[143]:


ARR_NEW_PAGE = [len(GOD_NEW_NOTE[GOD_NEW_NOTE['Ranking page(s)'].isnull() == False]), len(GOM_NEW_NOTE[GOM_NEW_NOTE['Ranking page(s)'].isnull() == False]), len(BNG_NEW_NOTE[BNG_NEW_NOTE['Ranking page(s)'].isnull() == False]), len(YAH_NEW_NOTE[YAH_NEW_NOTE['Ranking page(s)'].isnull() == False])]
FIRST_NEW_DF = pd.DataFrame(ARR_NEW_PAGE)
FIRST_NEW = FIRST_NEW_DF.sum()[0] 


# In[144]:


ARR_UP_PAGE = [GOD_UP, GOM_UP, BNG_UP, YAH_UP]
ARR_UP_DF = pd.DataFrame(ARR_UP_PAGE)
ARR_UP = ARR_UP_DF.sum()[0]
ARR_UP


# In[145]:


ARR_DOWN_PAGE = [GOD_DOWN, GOM_DOWN, BNG_DOWN, YAH_DOWN]
ARR_DOWN_DF = pd.DataFrame(ARR_DOWN_PAGE)
ARR_DOWN = ARR_DOWN_DF.sum()[0]
ARR_DOWN


# In[146]:


ARR_EQ_PAGE = [GOD_EQ, GOM_EQ, BNG_EQ, YAH_EQ]
ARR_EQ_DF = pd.DataFrame(ARR_EQ_PAGE)
ARR_EQ = ARR_EQ_DF.sum()[0]
ARR_EQ


# In[147]:


ARR_GL = [ARR_UP, ARR_DOWN]
ARR_GL_DF = pd.DataFrame(ARR_GL)
ARR_GLDF = ARR_GL_DF.sum()[0]
ARR_GLDF


# In[158]:


print(LP_YAH)


# In[149]:


report = [
"Actual SEO Media Report for Abba Corporate Transportation and Limousine Services Report for: abbalimos.com Report Date Range: 2/1/2023 through 2/28/2023 Report Section: Summary",
"",
"SUM A",
"General Report Statistics",
"Report Created",
"Keywords Analyzed",
"Ranking Check Depth",
"Engines Analyzed",
"Geographic Target",
"Baseline Report Date",
"Baseline Keyword Count",
"Services",
"",
"SUM B",
"Visibility Statistics",
"Listings in the First Position",
"Listings in the Top 5 Positions",
"Listings on the First Page",
"Listings on the First Two Pages",
"Listings New",
"Listings Which Moved Up",
"Listings Which Moved Down",
"Listings Which Did Not Change",
"Total Positions Gained/Lost",
"",
"GRAPH B",
"GRAPH C",
"GOD",
"GOM",
"BIN",
"YAH",
"",
"GRAPH D",
"GOD",
"GOD",
"BIN",
"YAH"
]


# In[150]:


DATA_REPORTS = ["","","","","3/1/2023",len(df), "25",'Google, Bing, Yahoo', 'Local', '7/15/2020', '47', 'SEO',"","","", TOP_1, TOP_5, FIRST_PAGE, FIRST_TWO, FIRST_NEW, ARR_UP, ARR_DOWN, ARR_EQ, ARR_GLDF,"",len(df),"",len(GOD_NEW), len(GOM_NEW),len(BNG_NEW), len(YAH_NEW),"","", LP_GOD, LP_GOM, LP_BNG, LP_YAH]

pd.DataFrame(index=report, data=DATA_REPORTS)


# In[151]:


REPORT_NAME = ['ReportSERPPositionsGOD.csv', 'ReportSERPPositionsGOM.csv', 'ReportSERPPositionsBNG.csv', 'ReportSERPPositionsYAH.csv']
frames = [GOD_DF, GOM_DF, BNG_DF, YAH_DF]
for i in range(len(frames)):
    frames[i].to_csv("C:\\Users\\cee03\\OneDrive\\Documents\\ActualSEO_workrelated\\TSS\\" + REPORT_NAME[i], index = None, header = False, sep='|')


# In[152]:


import sys

def GET_FRAME (CHOSEN_DFRAME):
    frames = [GOD_DF, GOM_DF, BNG_DF, YAH_DF]
    CHOSEN_FRAME = frames[CHOSEN_DFRAME]
    output = CHOSEN_FRAME.to_json()
    print(output)
    sys.stdout.flush()


    return CHOSEN_FRAME

GET_FRAME(0)


# In[153]:


from ftplib import FTP



with FTP("ftp.actualseomedia.com") as ftp:
    ftp.encoding = "utf-8"
    filename = "public_html//reports//abba//data//ReportGraphC.csv"
    file_1 = "ReportGraphC.csv"
    ftp.login(user="actual18", passwd="Actualseo5150!")
    ftp.retrbinary(f"RETR {filename}", open(file_1, "wb").write)

file_x= open(file_1, "r")

DF_REPGRH = pd.DataFrame(data=file_x)

ARRAY_REPGRH = pd.array(DF_REPGRH[0][1:5])

ARRAY_GRHC = []

for i in range(len(ARRAY_REPGRH)):
    
    NEW_ELEMENT = ARRAY_REPGRH[i].replace("\n", "")
    ARRAY_GRHC.append(NEW_ELEMENT)
    
ARRAY_GRHC



# In[154]:


import ftplib

HOSTNAME = "ftp.actualseomedia.com"
USERNAME = "actual18"
PASSWORD = "Actualseo5150!"

ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

ftp_server.encoding = "utf-8"

filename = "public_html//reports//abba//data//ReportGraphC.csv"

file = "ReportGraphC.csv"

    # Command for Downloading the file "RETR filename"
ftp_server.retrbinary(f"RETR {filename}", open(file, "wb").write)

file= open(file, "r")
DF_REPGRH = pd.DataFrame(data=file)


# In[155]:


ARRAY_REPGRH = pd.array(DF_REPGRH[0][1:5])
ARRAY_GRHC = []
for i in range(len(ARRAY_REPGRH)):
    NEW_ELEMENT = ARRAY_REPGRH[i].replace("\n", "")
    ARRAY_GRHC.append(NEW_ELEMENT)
ARRAY_GRHC


# In[157]:


BNG_DF = pd.read_csv('C:\\Users\\cee03\\OneDrive\\Documents\\ActualSEO_workrelated\\texanmosquito\\BIN.csv');
GOD_DF = pd.read_csv('C:\\Users\\cee03\\OneDrive\\Documents\\ActualSEO_workrelated\\texanmosquito\\GOD.csv');
GOM_DF = pd.read_csv('C:\\Users\\cee03\\OneDrive\\Documents\\ActualSEO_workrelated\\texanmosquito\\GOM.csv');
YAH_DF = pd.read_csv('C:\\Users\\cee03\\OneDrive\\Documents\\ActualSEO_workrelated\\texanmosquito\\YAH.csv');

DF_BNG = pd.DataFrame(data=BNG_DF)
DF_GOD = pd.DataFrame(data=GOD_DF)
DF_GOM = pd.DataFrame(data=GOM_DF)
DF_YAH = pd.DataFrame(data=YAH_DF)

frames = [DF_GOD, DF_GOM, DF_BNG, DF_YAH]
 
REPORT_NAME = ['ReportSERPPositionsGOD.csv', 'ReportSERPPositionsGOM.csv','ReportSERPPositionsBNG.csv', 'ReportSERPPositionsYAH.csv']
for i in range(len(frames)):
    frames[i].to_csv("reports" + REPORT_NAME[i], index = None, header = False, sep='|')




# In[ ]:




