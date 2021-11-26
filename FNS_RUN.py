
from __future__ import print_function
import time
import sys
import pandas as pd
from optparse import OptionParser
from bs4 import BeautifulSoup
import warnings
import requests
            
warnings.filterwarnings(action="ignore",message="CHECK PYTHON VERSION")
warnings.filterwarnings(action="ignore",message="ALREADY IMPORTED",category=UserWarning)
warnings.filterwarnings(action="ignore",category=DeprecationWarning)







def get_introduction():
    
    
    print("\n")
    print("""
          This program has been developed to ensure educational equality.
          Education should be free and accessible to all.
          
          The Internet should be free.
          All parameters are released as open source and developers can use it.
          """)


def DOWN_FILE_OBJ(target_url, file_name):
    
    r = requests.get(target_url+".pdf", stream=True)
    
    with open(file_name+".pdf", 'wb') as READING_T:
        
        for chunk_file in r.iter_content(2000):
        
            READING_T.write(chunk_file)
            

def doi_cracker(searc_parameters=str,searc_dir=str):
    
    
    try:
        print("\n")
        print("PROCESS HAS BEEN STARTED, PLEASE WAIT")
        print("\n")
        
        TRY_URL = searc_parameters
        SEARCH_URL = "https://sci-hub.ee" + "/" + TRY_URL
        
        X_TARGET_NEW = requests.get(SEARCH_URL)
                            
        NEXT_X_FUNCTION_NEW = BeautifulSoup(X_TARGET_NEW.text,"html.parser")
                            
        DIV_ART_NEW = NEXT_X_FUNCTION_NEW.find_all("div",id="article")
                            
        for x_text_path_new in DIV_ART_NEW:
                    
            EMBED_ID = x_text_path_new.find_all("embed")
                                
            for SRC_OPT in EMBED_ID:
                
                FILE_OPT = SRC_OPT.get("src")
                SPLIT_OPT = FILE_OPT.split(".pdf")
    
                DOWN_FILE_OBJ("https:"+SPLIT_OPT[0],searc_dir)
                
        print("THE PROCESS HAS BEEN SUCCESSFULLY COMPLETED")
        print("\n")
        time.sleep(0.8)
        print("THE SECTION IS CLOSED, CHECK YOUR FILE")
        print("IF YOU CANNOT SEE ANY SUCH FILE, CHECK IF THE DOI IS CORRECT")
        print("ADDITIONALLY, THIS ARTICLE MAY NOT BE SUITABLE FOR CRACKING")
        time.sleep(1.8)
        print("\n")
        
    except Exception as e:
        
        print(str(e))
        print("THERE IS A CONNECTION PROBLEM OR THIS ARTICLE IS NOT VALID YET")


def search_all(search_parameters=str,search_range=int,type_mx=str):
    
    time.sleep(0.8)
    print("\n")
    print(f"YOUR SEARCH PARAMETER: {search_parameters}")
    print(f"YOUR SEARCH POWER: {search_range}")
    print("\n")
    time.sleep(0.8)
    
    print("PROCESS HAS BEEN STARTED - DON'T CANCEL PLEASE WAIT")
    print("\n")
    
    
    try:
        ALL_LIST_HAL = []
        SERIES_HAL_LIST = []
        
        for PAGE_RANGE in range(search_range):
        
            URL_SEARCH_HAL = f"https://hal.archives-ouvertes.fr/search/index/?q={search_parameters}&docType_s=ART+OR+COMM+OR+OUV+OR+COUV+OR+DOUV+OR+OTHER+OR+UNDEFINED+OR+REPORT+OR+THESE+OR+HDR+OR+LECTURE&page={PAGE_RANGE}"
    
            REQ_SEARCH_HAL = requests.get(URL_SEARCH_HAL).text
            BS_URL_HAL = BeautifulSoup(REQ_SEARCH_HAL,"html.parser")
            
            
            DIV_AR = BS_URL_HAL.find_all("tr")
            for x_all in DIV_AR:
                
                Clear_Null = x_all.text.replace(" ","").replace("\n","")
                
                ALL_LIST_HAL.append(Clear_Null)
            
                
            for x_in_list in ALL_LIST_HAL:
                
                if x_in_list.startswith("L") != True and x_in_list.startswith("P") != True:
                    COMP_LINK_HAL = "https://hal.archives-ouvertes.fr"
                    print(str(COMP_LINK_HAL + "/" + x_in_list[0:14]))
                    SERIES_HAL_LIST.append(COMP_LINK_HAL + "/" + x_in_list[0:14])
                    
                    
            
        HAL_SERIES = pd.Series(SERIES_HAL_LIST,name="LINK")
        
            
        print("\n")
        print("PROCESS SUCCESSFULLY COMPLETED - WAIT")
        time.sleep(1.1)
        print("\n")
        
    except:
        
        print("PROBLEM DETECTED, STARTING OTHER PROCESS")
        time.sleep(1.1)
        print("\n")
    
    try:

        TOTAL_ARTICLE_LIST = []
        TOTAL_ARTICLE_NAME_LIST = []
        for PAGE_RANGE in range(search_range):
            
            LIBGEN_TARGET_PATH = requests.get(f"https://libgen.is/scimag/?q={search_parameters}&page={PAGE_RANGE}").text
            LIBGEN_SOUP_MAIN = BeautifulSoup(LIBGEN_TARGET_PATH,"html.parser")
            
            LIBGEN_TABLE_ALL = LIBGEN_SOUP_MAIN.find_all("table",class_="catalog")
            
            for X_ALL_TABLE in LIBGEN_TABLE_ALL:
                
                X_ALL_A = X_ALL_TABLE.find_all("a")
                
                for X_TARGET_A in X_ALL_A:
                    
                    if X_TARGET_A.text != "[edit]" and X_TARGET_A.text != "Sci-Hub" and X_TARGET_A.text != "Libgen.gs" and X_TARGET_A.text != "BookSC":
                        
                        TOTAL_ARTICLE_NAME_LIST.append(X_TARGET_A.text)
                        
                        
                    ALL_TARGET_HREF = X_TARGET_A.get("href")
                    HREF_TARGET_SPLIT = ALL_TARGET_HREF.split("/")
                    
                    if HREF_TARGET_SPLIT[2] == "sci-hub.se":
                        
                        TOTAL_ARTICLE_LIST.append(ALL_TARGET_HREF)
                        print(ALL_TARGET_HREF)
                        
                        
        LINK_SERIES_L = pd.Series(TOTAL_ARTICLE_LIST,name="LINK")
        
        
        
        print("\n")
        print("PROCESS SUCCESSFULLY COMPLETED - WAIT")
        time.sleep(1.1)
        print("\n")
        
    except:
        
        print("PROBLEM DETECTED, STARTING OTHER PROCESS")
        time.sleep(1.1)
        print("\n")
    
    
    #
    try:
        
        ARXIV_PDF_LIST = []
        for PAGE_RANGE in range(search_range):
            
            ARXIV_TARGET_PATH = requests.get(f"https://arxiv.org/search/?query={search_parameters}&searchtype=all&start={int(PAGE_RANGE)*50}").text
            ARXIV_TARGET_SOUP = BeautifulSoup(ARXIV_TARGET_PATH,"html.parser")
                
            ARXIV_TARGET_DIV = ARXIV_TARGET_SOUP.find_all("ol",class_="breathe-horizontal")
    
            for X_LOOP_OL in ARXIV_TARGET_DIV:
                    
                ALL_LI_ARXIV = X_LOOP_OL.find_all("li",class_="arxiv-result")
                    
                for X_LOOP_LI in ALL_LI_ARXIV:
                        
                    ARXIV_ALL_A = X_LOOP_LI.find_all("a")
                    ARXIV_ALL_P_TITLE = X_LOOP_LI.find_all("p",class_="title is-5 mathjax")
                    
                    for X_LOOP_A in ARXIV_ALL_A:
                            
                        X_ALL_HREF = X_LOOP_A.get("href")
                            
                        if X_ALL_HREF != None:
                                
                            ALL_HREF_SPLIT = X_ALL_HREF.split("/")
                                
                            if ALL_HREF_SPLIT[-2] == "pdf":
                                
                                for X_P_TITLE_TARGET in ARXIV_ALL_P_TITLE:
    
                                    
                                    ARXIV_PDF_LIST.append(X_ALL_HREF)
                                    print(X_ALL_HREF)
                                    
                                    
    
    
        LINK_SERIES_AR = pd.Series(ARXIV_PDF_LIST,name="LINK")

        print("\n")
        print("PROCESS SUCCESSFULLY COMPLETED - WAIT")
        time.sleep(1.1)
        print("\n")
    
    except:
        
        print("PROBLEM DETECTED, STARTING OTHER PROCESS")
        time.sleep(1.1)
        print("\n")
    
    #
    try:
        
        CITATIONSY_MAIN_TARGET = requests.get(f"https://citationsy.com/archives/search.php?CitationsyArchives_search={search_parameters}").text
        CITATIONSY_MAIN_SOUP = BeautifulSoup(CITATIONSY_MAIN_TARGET,"html.parser")
        
        CITATIONSY_ALL_DIV = CITATIONSY_MAIN_SOUP.find_all("div",class_="CitationsyArchives_results")
        
        CITATIONSKY_HREF_LIST = []
        for X_LOOP_DIV in CITATIONSY_ALL_DIV:
            CITATIONSY_ALL_TARGET = X_LOOP_DIV.find_all("a")
            
            for X_LOOP_A in CITATIONSY_ALL_TARGET:
                CITATIONSKY_ALL_HREF = X_LOOP_A.get("href")
                CITATIONSKY_ALL_TITLE = X_LOOP_A.find_all("div",class_="CitationsyArchives_search_result")
                HREF_TARGET_SPLIT_ALL = CITATIONSKY_ALL_HREF.split("=")
                
                for X_LOOP_EM in CITATIONSKY_ALL_TITLE:
                    
                    print(X_LOOP_EM.text)
                    print("https://sci-hub.ee/"+HREF_TARGET_SPLIT_ALL[-1])
                    CITATIONSKY_HREF_LIST.append("https://sci-hub.ee/"+HREF_TARGET_SPLIT_ALL[-1])
                    
                    
    
    
    
        LINK_SERIES_CI = pd.Series(CITATIONSKY_HREF_LIST,name="LINK")
        
        print("\n")
        print("PROCESS SUCCESSFULLY COMPLETED - WAIT")
        time.sleep(1.1)
        print("\n")
    
    except:
        
        print("PROBLEM DETECTED, STARTING OTHER PROCESS")
        time.sleep(1.1)
        print("\n")
    
    
    try:
        
        SCIENCE_ALL_HREF_LIST = []
        for X_RANGE_ALL in range(1,search_range):
    
            SCIENCEFOR_MAIN_URL = requests.get(f"https://www.sciencenewsforstudents.org/page/{X_RANGE_ALL}?s={search_parameters}").text
            SCIENCEFOR_MAIN_SOUP = BeautifulSoup(SCIENCEFOR_MAIN_URL,"html.parser")
            
            SCIENCEFOR_ALL_DIV = SCIENCEFOR_MAIN_SOUP.find_all("section",class_="river-no-sidebar__wrapper___dY6V_")
            
            for X_LOOP_DIV in SCIENCEFOR_ALL_DIV:
                
                SCIENCEFOR_ALL_H3 = X_LOOP_DIV.find_all("h3")
                
                for X_LOOP_H3 in SCIENCEFOR_ALL_H3:
                    
                    SCIENCEFOR_ALL_A = X_LOOP_H3.find_all("a")
                    
                    for X_LOOP_A in SCIENCEFOR_ALL_A:
                        
                        SCIENCE_ALL_HREF = X_LOOP_A.get("href")
                        HREF_TARGET_SPLIT = SCIENCE_ALL_HREF.split("/")

                        SCIENCE_ALL_HREF_LIST.append(SCIENCE_ALL_HREF)
                        
                        print(SCIENCE_ALL_HREF)
                        
                        
                        
                        
        LINK_SERIES_SC = pd.Series(SCIENCE_ALL_HREF_LIST,name="LINK")
        
        ALL_OUT_RESULT_SEARCH = [LINK_SERIES_SC,
                                 LINK_SERIES_CI,
                                 LINK_SERIES_AR,
                                 LINK_SERIES_L,
                                 HAL_SERIES]
        
        ALL_FRAMES_OUT = pd.concat(ALL_OUT_RESULT_SEARCH)
        ALL_FRAMES_OUT.to_csv(f"{type_mx}.csv")
        print("\n")
        print("THE PROCESS HAS BEEN SUCCESSFULLY COMPLETED - END")
        time.sleep(0.8)
        print("THE SECTION IS CLOSED")
        time.sleep(0.8)
        print("\n")
    
    except:
        
        print("THERE IS A PERMANENT PROBLEM, PLEASE CHECK YOUR INTERNET CONNECTION OR CONTACT THE DEVELOPER")
        time.sleep(1.1)
        print("\n")





def lucky_shot(searc_parameters=str,search_power=int):
    
    time.sleep(0.8)
    print("\n")
    print("SESSION HAS BEEN LAUNCHED")
    time.sleep(0.8)
    print("THIS PROCESS TAKES LONG TIME, PLEASE DO NOT DEACTIVATE")
    time.sleep(0.5)
    print("\n")
    
    try:
        
    
        ALL_NOT_PUBLIC_TARGET = []
        TESTING_PDF_LIST = []
        ALL_DOWN_OPEN_LIST = []
        
        X_TARGET = requests.get("https://www.nature.com/siteindex").text
        NEXT_X_FUNCTION = BeautifulSoup(X_TARGET,"html.parser")
    
        
            
        X_DATA_LINK = NEXT_X_FUNCTION.find_all("div",class_="cleared pt40 pb20 ma0 border-gray-medium border-bottom-1",id=f"journals-{searc_parameters}")
        
        for x_range_one in X_DATA_LINK:
            
            x_LI = x_range_one.find_all("li")
            
            for x_all in x_LI:
                
                X_PARAMS_Text = x_all.text
                
                print("\n")
                print("TARGET TITLE: ",X_PARAMS_Text)
                print("\n")
                
                X_A_ALL = x_all.find_all("a")
                
                for x_href in X_A_ALL:
                    
                    HREF_TARGET = x_href.get("href")
    
                    
                    for x_range_input_value in range(1,search_power):
                        
                        X_TARGET_NEW = requests.get(f"https://www.nature.com/{HREF_TARGET[1:]}/articles/?searchType=journalSearch&sort=PubDate&page={x_range_input_value}").text
                        NEXT_X_NEW_FUNCTION = BeautifulSoup(X_TARGET_NEW,"html.parser") 
    
                        X_DATA_LINK_NEW = NEXT_X_NEW_FUNCTION.find_all("li",class_="app-article-list-row__item")
    
                        for x_range_one_new in X_DATA_LINK_NEW:
    
                            X_ALL_A = x_range_one_new.find_all("a")
    
                            for x_href_target in X_ALL_A:
    
                                HREF_TARGET = x_href_target.get("href")
    
    
                                HREF_TARGET = x_href_target.get("href")
    
                                X_TARGET_ALL = requests.get(f"https://www.nature.com/{HREF_TARGET[1:]}").text
                                NEXT_X_FUNCTION_ALL = BeautifulSoup(X_TARGET_ALL,"html.parser")
                                
    
                                X_DATA_LINK_ALL = NEXT_X_FUNCTION_ALL.find_all("aside",class_="c-article-extras u-hide-print")
    
                                for x_range_one in X_DATA_LINK_ALL:
    
                                    X_ALL_A = x_range_one.find_all("a")
    
                                    for x_span in X_ALL_A:
    
                                        ALL_SPAN = x_span.find_all("span")
    
                                        for x_span_first in ALL_SPAN:
    
                                            TESTING_PDF_LIST.append(x_span_first.text)
    
                                            if TESTING_PDF_LIST[0] == "Download PDF":
    
                                                ALL_DOWN_OPEN_LIST.append(f"https://www.nature.com/{HREF_TARGET[1:]}")
    
                                            elif TESTING_PDF_LIST[0] == "Access through your institution":
    
                                                ALL_NOT_PUBLIC_TARGET.append(f"https://www.nature.com/{HREF_TARGET[1:]}")

                                            else:
                                                pass

                                            TESTING_PDF_LIST = []
                                            
                                        print(f"{X_PARAMS_Text} RUNNING!")
    
    except:       
        print("\n")
        print("THERE IS A PERMANENT PROBLEM, PLEASE CHECK YOUR INTERNET CONNECTION OR CONTACT THE DEVELOPER")
        print("\n")
        time.sleep(0.1)
        pass
        
    
    try:
        
        DOWN_SERIES = pd.Series(ALL_DOWN_OPEN_LIST,name="FREE")
        DOWN_SERIES.to_csv("DOWNLOADABLE_FREE.csv")
        NOT_DOWN_SERIES = pd.Series(ALL_NOT_PUBLIC_TARGET,name="UNACCESSIBLE")
        NOT_DOWN_SERIES.to_csv("NOT_DOWNLOADABLE.csv")
        print("\n")
        time.sleep(0.1)
        print("LIST WAS DOWNLOADED")
        print("PLEASE CHECK YOUR FILE")
        time.sleep(0.1)
        print("\n")
            
    
    except:
        
        
        print("\n")
        print("THERE IS A PERMANENT PROBLEM, PLEASE CHECK YOUR INTERNET CONNECTION OR CONTACT THE DEVELOPER")
        print("\n")
        sys.exit()
        

def search_libgen_in(search_power=int):
    
    try:
        
        print("\n")
        print("PROCESS HAS BEEN STARTED, PLEASE WAIT")
        time.sleep(1.2)
        print("\n")
    
        for x_range in range(search_power):
        
            URL_SEARCH_LIB = f"https://libgen.is/rss/index.php?&page={x_range}"
            
            REQ_SEARCH_LIB = requests.get(URL_SEARCH_LIB).text
            BS_URL_LIB = BeautifulSoup(REQ_SEARCH_LIB,"html.parser")
            DIV_AR_LIB = BS_URL_LIB.find_all("item")
            
            for x_all in DIV_AR_LIB:
                
                CLEAR_ALL_LIB = x_all.text.split("<a")[1].split(">")[0].replace(" ","").replace("href=","").replace('"','')
                print(CLEAR_ALL_LIB)
                time.sleep(0.1)
                
    except:

        print("\n")
        print("THERE IS A PERMANENT PROBLEM, PLEASE CHECK YOUR INTERNET CONNECTION OR CONTACT THE DEVELOPER")
        print("\n")
        sys.exit()
        
def how_to_use():

    print("""
          
          
     IIIIIIIIIIIIIIIIIIII        PPPPPPPPPPPPPPPPP        VVVVVVVV           VVVVVVVV
     I::::::::II::::::::I        P::::::::::::::::P       V::::::V           V::::::V
     I::::::::II::::::::I        P::::::PPPPPP:::::P      V::::::V           V::::::V
     II::::::IIII::::::II        PP:::::P     P:::::P     V::::::V           V::::::V
       I::::I    I::::I            P::::P     P:::::P      V:::::V           V:::::V 
       I::::I    I::::I            P::::P     P:::::P       V:::::V         V:::::V  
       I::::I    I::::I            P::::PPPPPP:::::P         V:::::V       V:::::V   
       I::::I    I::::I            P:::::::::::::PP           V:::::V     V:::::V    
       I::::I    I::::I            P::::PPPPPPPPP              V:::::V   V:::::V     
       I::::I    I::::I            P::::P                       V:::::V V:::::V      
       I::::I    I::::I            P::::P                        V:::::V:::::V       
       I::::I    I::::I            P::::P                         V:::::::::V        
     II::::::IIII::::::II        PP::::::PP                        V:::::::V         
     I::::::::II::::::::I ...... P::::::::P                         V:::::V          
     I01000110II00110100I .::::. P01000110P                          V:::V           
     IIIIIIIIIIIIIIIIIIII ...... PPPPPPPPPP                           VVV      
         
            
    This program has been developed to ensure educational equality.
    Education should be free and accessible to all.
          
    The Internet should be free.
    All parameters are released as open source and developers can use it.
          
          
          python FNS_RUN.py -s <your_search_parameter> <your_search_power>
          python FNS_RUN.py -l
          python FNS_RUN.py -c
          python FNS_RUN.py -r <your_search_power>
          python FNS_RUN.py -a <your_search_power>
          
          
          -s / --search : Search for a title (define a power level of searching)
          -l / --luckyshot : Reach Nature articles (follow orders)
          -c / --crackdoi : Try to find a paid DOI as public (follow orders)
          -r / --libgenrandom : Get Libgen documents randomly (define a power level of searching)
          -a / --allrun : Run for all (define a power level of searching)
          -h / --help : Help
          
          
          NOTED:
              
              For searching with names longer than one word, add '_' without any spaces between the words
          
          """) 
          
          
          
          
def run_parameters():
    
    OPTION_PARSER = OptionParser(add_help_option=False,epilog="FREE NET AND EDUCATION")
    
    OPTION_PARSER.add_option("-s",
                             "--search",
                             help="Search for a title",
                             dest="search_x",
                             type="string")
    
    OPTION_PARSER.add_option("-l",
                             "--luckyshot",
                             help="Run for cracking and detecting articles",
                             dest="shot_x",
                             action="store_true")
    
    OPTION_PARSER.add_option("-c",
                             "--crackdoi",
                             help="Try to crack doi",
                             dest="crack_x",
                             action="store_true")
    
    OPTION_PARSER.add_option("-r",
                             "--libgenrandom",
                             help="Get Libgen documents randomly",
                             dest="libgen_x",
                             type="int")
    
    OPTION_PARSER.add_option("-a",
                             "--allrun",
                             help="Run for all",
                             dest="all_x",
                             action="store_true")
    
    OPTION_PARSER.add_option("-h",
                             "--help",
                             help="Help",
                             dest="print_help",
                             action="store_true")
    
    
    Option_Search, Option_Power = OPTION_PARSER.parse_args()
    
    if Option_Search.search_x:
        
        try:
            get_introduction()
            time.sleep(1.8)
        
            Searching_Parameter = str(Option_Search.search_x).lower().replace(" ","").replace("ı","i")
            Power_Parameter = int(Option_Power[0])
            time.sleep(1.2)
            
            print("\n")
            print("Article links related to the search you want will be saved on your desktop")
            ANS_APR = str(input("Do you approve (y/N): ")).lower().replace(" ","")
            
            if ANS_APR == "y":
            
                search_all(Searching_Parameter,Power_Parameter,"OUTPUT_ALL")
                
            else:
                print("\n")
                pass
        
        except:
            print("\n")
            print("THERE IS A PERMANENT PROBLEM, PLEASE CHECK YOUR INTERNET CONNECTION OR INPUT")
            print("\n")
            sys.exit()
            
    elif Option_Search.all_x:
        
        get_introduction()
        time.sleep(1.8)

        print("\n")
        print("This process will search for articles related to all English words")
        print("The process can take a long time")
        print("\n")
        print("All results will be saved on your computer")
        print("When you want to cancel the operation, you have to force close the panel")
        print("\n")
        time.sleep(1.8)
        
        try:
            
            print("EXAMPLE: ", "50")
            POW_AT = str(input("PLEASE TYPE YOUR POWER TO SEARCH (type '/' to exit): ")).lower().replace(" ","")
            print("\n")
            
            if POW_AT != "/" and POW_AT != None:
                
                POW_AT = int(POW_AT)
                Headers_OP = open("txt_search.txt","r")
                HEAD_READ = Headers_OP.read()
                
                LIST_HEAD = HEAD_READ.replace("\n",",").replace(" ","").split(",")
                Headers_OP.close()
                
                LIST_HEAD.pop()
    
                for x_counting,x_word in enumerate(LIST_HEAD):
                    
                    x_word = str(x_word)
                    
                    search_all(x_word,POW_AT,f"{x_counting}_{x_word}_result")
                    print("\n")
                    print(f"{x_counting} IS DONE - WAIT")
                    print("\n")
                    time.sleep(0.5)
                    
            else:
                
                print("\n")
                pass
            
        except:
            
            print("\n")
            print("THERE IS A PERMANENT PROBLEM, PLEASE CHECK YOUR INTERNET CONNECTION OR INPUT")
            print("\n")
            sys.exit()
        
            
    elif Option_Search.libgen_x:
        
        try:
            get_introduction()
            time.sleep(1.8)
            
            Power_Parameter = int(Option_Search.libgen_x)
            time.sleep(1.2)
            
            search_libgen_in(Power_Parameter)
        
        except:
            print("\n")
            print("THERE IS A PERMANENT PROBLEM, PLEASE CHECK YOUR INTERNET CONNECTION OR INPUT")
            print("\n")
            sys.exit()
            
    elif Option_Search.shot_x:
        
        try:
            
            get_introduction()
            time.sleep(1.8)

            print("\n")
            print("EXAMPLE: ", "A")
            R_WORD = str(input("PLEASE TYPE YOUR WORD TO ACCESS (type '/' to exit): ")).upper().replace(" ","").replace("İ","I")
            print("\n")
            
            if R_WORD != "/" and R_WORD !=None:
                time.sleep(1.5)
                print("EXAMPLE: ", "5")
                R_POWER = int(input("PLEASE TYPE YOUR TITLE SEARCH POWER (type '/' to exit): "))
                print("\n")
                
                if R_POWER != "/" and R_POWER !=None:
                    time.sleep(1.5)
                    print("YOUR WORD: ", R_WORD)
                    print("YOUR POWER: ", R_POWER)
                    print("\n")
                    time.sleep(1.5)
                    
                    lucky_shot(R_WORD,R_POWER)
                    
                else:
                    print("\n")
                    pass
                
            else:
                print("\n")
                pass

        
        except:
            print("\n")
            print("THERE IS A PERMANENT PROBLEM, PLEASE CHECK YOUR INTERNET CONNECTION OR INPUT")
            print("\n")
            sys.exit()
            
    elif Option_Search.crack_x:
        
        try:
            
            get_introduction()
            time.sleep(1.8)
            print("\n")
            print("EXAMPLE: ", "https://doi.org/10.1038/s41422-021-00552-3")
            print("YOU CAN TRY TO CONVERT BY USING A ARTICLE WEB PAGE: ", "https://..../..../....")
            print("\n")
            DOI_INPUT = str(input("PLEASE TYPE YOUR DOI TO CRACK (type '/' to exit): "))
            print("\n")
            if DOI_INPUT != "/" and DOI_INPUT != None:
                time.sleep(1.5)
                print("EXAMPLE: ", "D:/NATURE_ARTICLE/")
                DOI_DIR = str(input("PLEASE TYPE A DIRECTION TO SAVE (type '/' to exit): "))
                print("\n")
                
                if DOI_DIR != "/" and DOI_DIR != None:
                    
                    time.sleep(1.5)
                    print("YOUR DOI: ", DOI_INPUT)
                    print("YOUR DIR: ", DOI_DIR)
                    print("\n")
                    time.sleep(1.5)
                    
                    if DOI_DIR.endswith("/") == True:
                    
                        doi_cracker(DOI_INPUT,DOI_DIR+"OUT_RESULT_ARTICLE")
                        
                    elif DOI_DIR.endswith("/") != True:
                        
                        doi_cracker(DOI_INPUT,DOI_DIR+"/OUT_RESULT_ARTICLE")
                        
                    else:
                        
                        print("\n")
                        print("CHECK YOUR DIRECTION TO SAVE, IT IS INVALID")
                        
                else:
                    print("\n")
                    pass
                
            else:
                print("\n")
                pass
                
        
        except:
            print("\n")
            print("SUCH DOI MAY NOT HAVE BEEN PUBLISHED YET OR CHECK YOUR PARAMETERS")
            print("\n")
            sys.exit()
            
    elif Option_Search.print_help:
        
        how_to_use()
        sys.exit()
    
    
    
 
if __name__ == "__main__":
    
    if len(sys.argv) >= 1:
        time.sleep(0.2)
        run_parameters()
        
    elif len(sys.argv) == 0:
        how_to_use()
        sys.exit()
    
