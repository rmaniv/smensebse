import requests
from bs4 import BeautifulSoup
import time
from html_table_parser.parser import HTMLTableParser
from pprint import pprint
import pandas as pd

nse = ['ABCOTS','ABINFRA','AMJUMBO','AISL','ASLIND','AVG','AILIMITED','ACCORD','AGNI','AMEYA','AMIABLE','ANNAPURNA','ATALREAL','AURDIS','BEWLTD','BETA','BMETRICS','BRIGHT','CMMIPL','CADSYS','CONTI','COOLCAPS','CMRSL','DKEGL','DUGLOBAL','DESTINY','DRL','DYNAMIC','EMKAYTOOLS','KRISHIVAL','EUROBOND','FELIX','FOCE','FROG','GIRIRAJ','GICL','GSTL','GOLDSTAR','INNOVANA','INNOVATIVE','IPSL','ISHAN','JFLLIFE','JAINAM','JALAN','KORE','JSLL','KHFM','KNAGRI','KANDARP','KCK','KOTYARK','KRISHNADEF','LATTEYS','LEMERITE','LEXUS','LLOYDS','MKPL','MPTODAY','MAHICKRA','MAKS','MANAV','MWL','MDL','MEGAFLEX','MILTON','MHHL','NPST','NIDAN','PROPEQUITY','PARTYCRUS','PASHUPATI','PAVNAIND','PENTAGOLD','PHANTOMFX','PIGL','PRECISION','PROLIFE','PULZ','QMSMEDI','QUADPRO','RMDRIP','RILINFRA','RELIABLE','REXPIPES','RICHA','RITEZONE','SSINFRA','SKP','SMVD','SPRL','SABAR','SECL','SHIGAN','TIRUPATI','SVLL','OSWALSEEDS','SRIRAM','SHUBHLAXMI','SIDDHIKA','SIGMA','SOLEX','SONAHISONA','SONUINFRA','SURANI','SWARAJ','SWASTIK','TAPIFRUIT','TARACHAND','THEJO','TIMESCAN','TRANSWIND','UWCSL','USASEEDS','URAVI','UCL','VMARCIND','VSCL','MADHAVBAUG','CLOUD','VEEKAYEM','VITAL','VIVIANA','VIVO','WALPAR']
bse_code = ['543319','542580','543346','539570','536737','543499','540146','543309','780018','543377','543230','541402','537492','542020','540718','543453','535916','543678','540923','539265','541006','542865','539403','541401','538716','543236','539099','536492','780004','543497','541178','538576','543209','540148','535279','543439','543543','539637','538817','543621','543618','542934','542678','540681','780013','543435','543619','535142','543606','543172','542727','540903','540652','543651','542002','542248','780006','542155','543753','543516','540151','541299','540811','543410','543594','540144','543713','540695','534927','534839','543518','541053','543475','543746','538684','543595','540455','542668','543500','543444','539098','543312','543521','539839','540945','539680','543709','538319','535917','543324','540613','542851','543372','541703','539864','542477','543520','543239','542850','543538','780012','539222','540938','538731','780014','542592','543546','535217','542935','540152','543620','541304','541083','541983','541353','780001','542924','543544','540394','538794','543286','540850','540651','780019','542653','534659','542446','538765','540756','537784','539788','543542','543273','540812','540468','540952','537669','541196','543624','541973','543613','542503','540402','543364','534563','780009','540150','541337','542801','535910','543539','543262','539229','543579','539521','543305','538668','540698','536644','539843','542771','542628','543522','540416','543578','543400','539116','543637','539352','539273','543540','539401','543352','537573','543363','540404','543375','534109','543460','537785','538921','541945','543285','543617','539760','540426','543744','543590','541151','540843','536456','540358','542145','542599','540082','539836','540715','543541','543376','780015','543218','543366','540782','543537','535647','543234','543515','543519','543391','534708','543244','540072','541112','540736','543536','538667','543598','542728','542146','540269','543065','541799','540084','543464','540079','536710','535466','543615','539026','543461','536738','543622','536671','542683','542025','780008','541701','543274','539041','543373','543745','539842','540332','538496','543656','537119','543310','539985','543616','538579','541228','541338','537582','540729','543623','543545','543241','890163','543597','542654','541445','539337','780016','538128','540550']
bse_symbol = ['AAPLUSTRAD','AARTECH','AASHKA','ACEWIN','ACFSL','ACHYUT','ACML','ADESHWAR','ADHIRAJ (ITP)','ADISHAKTI','ADVAIT','AFFORDABLE','AGRIMONY','AKI','AKM','ALKOSIGN','ALSL','AMBOAGRI','AML','AMRAFIN','ANGEL','ANUROOP','ARAMBHAN','ARIHANTINS','ARYACAPM','ATAM','ATHCON','ATWL','AUTUMN (ITP)','BCCL','BENARA','BHANDERI','BILLWIN','BINDALEXPO','BMAL','BRANDBUCKT','BRRL','BVL','CAPPIPES','CARGOSOL','CARGOTRANS','CBPL','CHCL','CHOTHANI','CITYON (ITP)','CLARA','CNCRD','CNEL','CONTAINE','COSPOWER','CPML','CRPRISK','CTCL','DAPS','DCL','DECCAN','DEKSON (ITP)','DGL','DHARNI','DHYAANI','DIKSAT','DLCL','DML','DMR','DPL','DRA','DRONACHRYA','DWL','EBFL','EFPL','EIGHTY','EIS','EKENNIS','ELIL','ENCASH','EPBIO','ESCORP','EVANS','EVOQ','FABINO','FILTRA','FOCUS','FONE4','FRANKLIN','FSSPL','GANGAPHARM','GARGI','GCMCAPI','GCMCOMM','GCSL','GEL','GENSOL','GETALONG','GFIL','GHUSHINE','GLEAM','GLHRL','GMPL','GOBLIN','GOEL','GOKULSOL (ITP)','GROWINGTON','GUJHYSPIN','HANMAN','HASJUICE (ITP)','HBEL','HEALTHYLIFE','HPCBL','ICLORGANIC','IGRL','INA','INDOUS','INFLAME','INNOVATIVE','INNOVATORS','JAISUKH DEAL (ITP)','JANUSCORP','JAYANT','JDML','JETINFRA','JETMALL','JFL','JIGAR','JIGYASA (ITP)','JINAAM','JOINTECAED','JONJUA','JSHL','KAARYAFSL','KCSL','KDML','KESAR','KMEW','KMSL','KMSMEDI','LAL','LAXMIPATI','LEX','MAAGHADV','MACH','MAFIA','MAHIP','MANAS','MARKOLINES','MASL','MCL (ITP)','MHEL','MILEFUR','MISQUITA','MMLF','MODIS','MRP','MRSS','NATURO','NAVIGANT','NAVODAYENT','NAYSAA','NEL','NEWEVER','NINSYS','NOVATEOR','NSL','NVENTURES','OCTAWARE','OLATECH','OMNIPOTENT','OPCHAINS','PACE','PBFL','PECOS','PGCRL','PJL','POBS','POLYMAC','PREVEST','PRIMEFRESH','PROMAX','PYXISFIN','QRIL','RACE','RAFL','RANJEET','RCAN','REETECH','RELICAB','RELSTRUCT','REXSEAL','RHETAN','RIDINGS','RITHWIKFMS','RJBIOTECH','RMC','RONI','ROOPSHRI','RSTL','RUBY','SAGAR','SAILANI','SAMOR','SANASATECH (ITP)','SBGLP','SBLI','SBRANDS','SCARNOSE','SDC','SECMARK','SEML','SFSL','SGFRL','SHANTIGURU','SHINEFASH','SHIVAEXPO','SHREESHAY','SIDDH','SILVERPRL','SIROHIA','SISL','SKIEL','SKIFL','SKL','SMAUTO','SMEL','SPICY','SPITZE','SPRAYKING','SRGSFL','SRL','SRSOLTD','SSPNFIN','SSTL','STELLAR','STML','SUBHTEX','SUICH','SUNRETAIL','SUPERNOVA (ITP)','SUPERSHAKT','SUUMAYA','SVPHOUSING','SVRL','SVS','SYSCO','TANVI','TARINI','TECHNOPACK','TENTIMETAL','TIMESGREEN','TITAANIUM','TLL','TRIVIKRAMA','TRL','UHZAVERI','UNISHIRE','VANTABIO','VEDANTASSET','VEERKRUPA','VGIL','VIDLIPP','VOEPL','VRFILMS','WAA','WAAREE','WEBSL (ITP)','WOMENSNEXT','YUG']

def mcap(symbol):
    try:
        r = requests.get('https://www.screener.in/company/'+symbol+'/')
        soup = BeautifulSoup(r.content, 'html.parser')
        s = str(soup).split('Market Cap')[1].split('<span class="number">')[1].split('</span>')[0]
        mcap = float(s)
    except:
        mcap = 'NaN'
    
    return mcap

def url_get_contents(symbol):
    r = requests.get('https://www.screener.in/company/'+symbol+'/')
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def pnl(symbol):
    p = HTMLTableParser()
    p.feed(url_get_contents(symbol).decode('utf-8'))
    df = pd.DataFrame(p.tables[1])
    try:
        sales = df.iloc[1,-2].replace(',','')
        net_profit = df.iloc[-3,-2].replace(',','')
        eps = df.iloc[-2,-2].replace(',','')
        return sales+','+net_profit+','+eps
    except:
        sales_ = df.iloc[1,-1].replace(',','')
        net_profit_ = df.iloc[-3,-1].replace(',','')
        eps_ = df.iloc[-2,-1].replace(',','')
        return sales_+','+net_profit_+','+eps_

print('NSE,MCAP (in Rs. cr),Sales (in Rs. cr),Net Profit (in Rs. cr),EPS (in Rs.),URL')
for i in nse:
    print(i+','+str(mcap(i))+','+pnl(i)+','+'https://www.screener.in/company/'+i+'/')
    time.sleep(3)

print('BSE,MCAP (in Rs. cr),Sales (in Rs. cr),Net Profit (in Rs. cr),EPS (in Rs.),URL')
for i in range(265):
    print(bse_symbol[i]+','+str(mcap(bse_code[i]))+pnl(bse_code[i])+','+'https://www.screener.in/company/'+bse_code[i]+'/')
    time.sleep(3)
