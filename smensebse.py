import requests
from bs4 import BeautifulSoup

nse = ['ABCOTS','ABINFRA','AMJUMBO','AISL','ASLIND','AVG','AILIMITED','ACCORD','AGNI','AMEYA','AMIABLE','ANNAPURNA','ATALREAL','AURDIS','BEWLTD','BETA','BMETRICS','BRIGHT','CMMIPL','CADSYS','CONTI','COOLCAPS','CMRSL','DKEGL','DUGLOBAL','DESTINY','DRL','DYNAMIC','EMKAYTOOLS','KRISHIVAL','EUROBOND','FELIX','FOCE','FROG','GIRIRAJ','GICL','GSTL','GOLDSTAR','INNOVANA','INNOVATIVE','IPSL','ISHAN','JFLLIFE','JAINAM','JALAN','KORE','JSLL','KHFM','KNAGRI','KANDARP','KCK','KOTYARK','KRISHNADEF','LATTEYS','LEMERITE','LEXUS','LLOYDS','MKPL','MPTODAY','MAHICKRA','MAKS','MANAV','MWL','MDL','MEGAFLEX','MILTON','MHHL','NPST','NIDAN','PROPEQUITY','PARTYCRUS','PASHUPATI','PAVNAIND','PENTAGOLD','PHANTOMFX','PIGL','PRECISION','PROLIFE','PULZ','QMSMEDI','QUADPRO','RMDRIP','RILINFRA','RELIABLE','REXPIPES','RICHA','RITEZONE','SSINFRA','SKP','SMVD','SPRL','SABAR','SECL','SHIGAN','TIRUPATI','SVLL','OSWALSEEDS','SRIRAM','SHUBHLAXMI','SIDDHIKA','SIGMA','SOLEX','SONAHISONA','SONUINFRA','SURANI','SWARAJ','SWASTIK','TAPIFRUIT','TARACHAND','THEJO','TIMESCAN','TRANSWIND','UWCSL','USASEEDS','URAVI','UCL','VMARCIND','VSCL','MADHAVBAUG','CLOUD','VEEKAYEM','VITAL','VIVIANA','VIVO','WALPAR']

def find_mcap(symbol):

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
    url = 'https://www.moneycontrol.com/india/'+splitted2[0]
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    mcap = soup.find('td', class_='nsemktcap bsemktcap').text
    
    return mcap

for i in nse:
    try:
        print(find_mcap(i))
    except:
        print('NAN')
