import requests
from bs4 import BeautifulSoup

nse = ['ABCOTS','ABINFRA','AMJUMBO','AISL','ASLIND','AVG','AILIMITED','ACCORD','AGNI','AMEYA','AMIABLE','ANNAPURNA','ATALREAL','AURDIS','BEWLTD','BETA','BMETRICS','BRIGHT','CMMIPL','CADSYS','CONTI','COOLCAPS','CMRSL','DKEGL','DUGLOBAL','DESTINY','DRL','DYNAMIC','EMKAYTOOLS','KRISHIVAL','EUROBOND','FELIX','FOCE','FROG','GIRIRAJ','GICL','GSTL','GOLDSTAR','INNOVANA','INNOVATIVE','IPSL','ISHAN','JFLLIFE','JAINAM','JALAN','KORE','JSLL','KHFM','KNAGRI','KANDARP','KCK','KOTYARK','KRISHNADEF','LATTEYS','LEMERITE','LEXUS','LLOYDS','MKPL','MPTODAY','MAHICKRA','MAKS','MANAV','MWL','MDL','MEGAFLEX','MILTON','MHHL','NPST','NIDAN','PROPEQUITY','PARTYCRUS','PASHUPATI','PAVNAIND','PENTAGOLD','PHANTOMFX','PIGL','PRECISION','PROLIFE','PULZ','QMSMEDI','QUADPRO','RMDRIP','RILINFRA','RELIABLE','REXPIPES','RICHA','RITEZONE','SSINFRA','SKP','SMVD','SPRL','SABAR','SECL','SHIGAN','TIRUPATI','SVLL','OSWALSEEDS','SRIRAM','SHUBHLAXMI','SIDDHIKA','SIGMA','SOLEX','SONAHISONA','SONUINFRA','SURANI','SWARAJ','SWASTIK','TAPIFRUIT','TARACHAND','THEJO','TIMESCAN','TRANSWIND','UWCSL','USASEEDS','URAVI','UCL','VMARCIND','VSCL','MADHAVBAUG','CLOUD','VEEKAYEM','VITAL','VIVIANA','VIVO','WALPAR']
bse = ['AAPLUSTRAD','AARTECH','AASHKA','ACFSL','ACHYUT','ACML','ADESHWAR','ADISHAKTI','ADVAIT','AFFORDABLE','AGRIMONY','AKI','AKM','ALKOSIGN','ALSL','AMBOAGRI','AML','AMRAFIN','ANGEL','ANUROOP','ARYACAPM','ATAM','ATHCON','BCCL','BENARA','BHANDERI','BILLWIN','BINDALEXPO','BMAL','BRANDBUCKT','BRRL','BVL','CAPPIPES','CARGOSOL','CARGOTRANS','CBPL','CHCL','CHOTHANI','CLARA','CNCRD','CNEL','CONTAINE','COSPOWER','CPML','CTCL','DAPS','DCL','DECCAN','DGL','DHYAANI','DIKSAT','DLCL','DML','DMR','DPL','DRA','DRONACHRYA','DWL','EFPL','EIGHTY','EKENNIS','ELIL','EPBIO','ESCORP','EVANS','EVOQ','FABINO','FILTRA','FOCUS','FONE4','FRANKLIN','GANGAPHARM','GARGI','GCMCAPI','GCMCOMM','GCSL','GEL','GENSOL','GETALONG','GFIL','GLHRL','GMPL','GOBLIN','GOEL','GROWINGTON','GUJHYSPIN','HANMAN','HBEL','HEALTHYLIFE','HPCBL','ICLORGANIC','INA','INDOUS','INFLAME','INNOVATIVE','INNOVATORS','JANUSCORP','JAYANT','JETINFRA','JETMALL','JIGAR','JOINTECAED','JONJUA','JSHL','KAARYAFSL','KCSL','KDML','KESAR','KMEW','KMSMEDI','LAL','LAXMIPATI','LEX','MAAGHADV','MACH','MAFIA','MANAS','MARKOLINES','MASL','MHEL','MILEFUR','MISQUITA','MMLF','MODIS','MRP','MRSS','NATURO','NAVIGANT','NAVODAYENT','NAYSAA','NINSYS','NOVATEOR','NSL','NVENTURES','OCTAWARE','OLATECH','OMNIPOTENT','OPCHAINS','PACE','PECOS','PGCRL','PJL','POBS','POLYMAC','PREVEST','PRIMEFRESH','PROMAX','PYXISFIN','QRIL','RACE','RAFL','RANJEET','RCAN','REETECH','RELICAB','REXSEAL','RHETAN','RIDINGS','RITHWIKFMS','RJBIOTECH','RMC','RONI','ROOPSHRI','RSTL','SAGAR','SAILANI','SAMOR','SBGLP','SBLI','SBRANDS','SCARNOSE','SDC','SECMARK','SEML','SFSL','SGFRL','SHANTIGURU','SHINEFASH','SHIVAEXPO','SHREESHAY','SILVERPRL','SIROHIA','SISL','SKIEL','SKIFL','SKL','SMAUTO','SMEL','SPICY','SPITZE','SPRAYKING','SRGSFL','SRSOLTD','SSPNFIN','SSTL','STELLAR','STML','SUNRETAIL','SUPERSHAKT','SUUMAYA','SVPHOUSING','SVRL','SVS','TANVI','TARINI','TECHNOPACK','TIMESGREEN','TITAANIUM','TLL','TRIVIKRAMA','TRL','UHZAVERI','UNISHIRE','VANTABIO','VEDANTASSET','VEERKRUPA','VGIL','VOEPL','VRFILMS','WAA','WAAREE','YUG']

def nse_mcap(symbol):

    # searching for stock on google
    search_url = 'https://www.google.com/search?q='+symbol+'+moneycontrol'
    r = requests.get(search_url)
    search_soup = BeautifulSoup(r.content, 'html.parser')
    results = search_soup.find_all('a')

    # converting to string
    anchors = ''
    for i in results:
        anchors += str(i)

    # extracting link from string
    splitted = anchors.split('https://www.moneycontrol.com/india/')
    splitted2 = splitted[1].split('&amp')

    # finding market cap
    try:
        url = 'https://www.moneycontrol.com/india/'+splitted2[0]
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        mcap = soup.find('td', class_='nsemktcap bsemktcap').text
        
    except:
        mcap = 'NaN'
    
    return mcap

def bse_mcap(symbol):
    
    # searching for stock on google
    search_url = 'https://www.google.com/search?q='+symbol+'+moneycontrol'
    r = requests.get(search_url)
    search_soup = BeautifulSoup(r.content, 'html.parser')
    results = search_soup.find_all('a')

    # converting to string
    anchors = ''
    for i in results:
        anchors += str(i)

    # extracting link from string
    splitted = anchors.split('https://www.moneycontrol.com/')
    splitted2 = splitted[1].split('&amp')

    # finding market cap
    try:
        url = 'https://www.moneycontrol.com/'+splitted2[0]
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        peers = soup.find('div', id='peers')
        child = str(peers).split('marketCap">')[1]
        mcap = child.split('<')[0]
    
    except:
        mcap = 'NaN'
    
    return mcap

print('NSE:')
for i in nse:
        print(i,',',nse_mcap(i))

print('BSE:')
for i in bse:
    print(i, ',', bse_mcap(i))
