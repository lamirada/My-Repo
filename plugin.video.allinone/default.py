import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib, urllib2
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

try:
	from sqlite3 import dbapi2 as sqlite
	print "Loading sqlite3 as DB engine"
except:
	from pysqlite2 import dbapi2 as sqlite
	print "Loading pysqlite2 as DB engine"

addon_id = 'plugin.video.allinone'
plugin = xbmcaddon.Addon(id=addon_id)
net = Net()
addon = Addon('plugin.video.allinone', sys.argv)
DB = os.path.join(xbmc.translatePath("special://database"), 'allinone.db')
BASE_URL = 'http://oneclickwatch.org/'
BASE_URL1 = 'http://watchthetapes.com/'
BASE_URL2 = 'http://www.watchtvshowz.org/'
BASE_URL3 = 'http://viooz.pw/'
BASE_URL4 = 'http://www.ultra-vid.com/'
BASE_URL5 = 'http://moviesall4u.com/'
BASE_URL9 = 'http://www.oneclickmoviez.ag/'
BASE_URL10 = 'http://www.myvideolinks.eu/'
BASE_URL11 = 'http://www.ddlvalley.eu/'
BASE_URL12 = 'http://www.flixanity.com/'
BASE_URL14 = 'http://www.channelcut.me/'
BASE_URL15 = 'http://freemoviesntvshows.com/'
BASE_URL17 = 'http://tv-junky.eu/'
BASE_URL19 = 'http://all4youz.com/'
BASE_URL20 = 'http://world4ufree.com/'
BASE_URL21 = 'http://movies2k.eu/'
BASE_URL23 = 'http://300mbmovies4u.com/'
BASE_URL25 = 'http://www.rapgrid.com/'
BASE_URL29 = 'http://shows4u.info/'

#### PATHS ##########
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"

##### Queries ##########
mode = addon.queries['mode']
url = addon.queries.get('url', None)
content = addon.queries.get('content', None)
query = addon.queries.get('query', None)
startPage = addon.queries.get('startPage', None)
numOfPages = addon.queries.get('numOfPages', None)
listitem = addon.queries.get('listitem', None)
urlList = addon.queries.get('urlList', None)
section = addon.queries.get('section', None)

################################################################################ GetTitles  ################################################################################

def GetTitles(section, url, startPage= '1', numOfPages= '1'): #oneclickwatch
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                       
                match = re.compile('<h2.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles1(section, url, startPage= '1', numOfPages= '1'): #WTT
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('<h1 class="entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h1>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'wtt.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles2(section, url, startPage= '1', numOfPages= '1'): #WTShows
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('entry.+?href="(.+?)" .+?="(.+?)">.+?<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles2', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles3(section, url, startPage= '1', numOfPages= '1'): #viooz
        print 'allinone get Movie Titles Menu %s' % url 
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('postsbody.+?href="(.+?)".+?="(.+?)">.+?src=".+?src=(.+?)&amp;.+?"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles3', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')           
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles4(section, url, startPage= '1', numOfPages= '1'): #Uv
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('itemdets.+?href="(.+?)" title="(.+?)".+?.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles4', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')       
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles5(section, url, startPage= '1', numOfPages= '1'): #moviesall4u
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                 
                match = re.compile('entry-title.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles5', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')             
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------# 

def GetTitles9(section, url, startPage= '1', numOfPages= '1'): #oneclickmoviez
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + str(page) + ''
                        html = net.http_GET(pageUrl).content                     
                match = re.compile('<img class="img-preview spec-border"  src="http://www.oneclickmoviez.ag/templates/svarog/timthumb.php\?src=(.+?)&amp;.+?" alt=" ".+?<a class="link" href="(.+?)" title="(.+?)">',re.DOTALL).findall(html)
                if not match:
                    match = re.compile('<img class="img-preview spec-border show-thumbnail"  src="http://www.oneclickmoviez.ag/templates/svarog/timthumb.php\?src=(.+?)&amp;.+?" alt=" ".+?<a class="link" href="(.+?)" title="(.+?)">',re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')                        
                addon.add_directory({'mode': 'GetTitles9', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png') 
        setView('tvshows', 'tvshows-view')          
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles10(section, url, startPage= '1', numOfPages= '1'): #mvl
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                        
                match = re.compile(' <img src="(.+?)"  title=".+?" class="alignleft" alt="(.+?)" /></a>\r\n\t\t\r\n<h4><a href="(.+?)" rel="bookmark"', re.DOTALL).findall(html)
                for img, name, movieUrl in match:
                        addon.add_directory({'mode': 'GetLinks7', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')      
                addon.add_directory({'mode': 'GetTitles10', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')         
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles11(section, url, startPage= '1', numOfPages= '1'): #ddlvalley
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                       
                match = re.compile('<h2>.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks3', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles11', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles12(section, url, startPage= '1', numOfPages= '1'): # flixanity
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('text-align:center.+?href="(.+?)".+?.+?src=".+?src=(.+?)&amp;.+?".+?<p><strong>(.+?)</strong></p>', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles12', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles14(section, url, startPage= '1', numOfPages= '1'): #channelcut
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                     
                match = re.compile('<h2><a.+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles14', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles15(section, url, startPage= '1', numOfPages= '1'): # freemovies
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + ''
                        html = net.http_GET(pageUrl).content                    
                match = re.compile('img-preview spec-border.+?src=".+?src=(.+?)&amp;.+?".+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles15', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles17(section, url, startPage= '1', numOfPages= '1'): #Tv-junky
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('posttitle.+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'tvj.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles17', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles18(section, url, startPage= '1', numOfPages= '1'): #2nd list oneclickmoviez tv url 9
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        html = net.http_GET(pageUrl).content                    
        match = re.compile('<a class="link" href="(.+?)" title="(.+?)"',re.DOTALL).findall(html)
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------#

def GetTitles18a(section, url, startPage= '1', numOfPages= '1'): # 1st list oneclickmoviez tv url 9
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + str(page) + ''
                        html = net.http_GET(pageUrl).content                     
                match = re.compile('<img class="img-preview spec-border"  src="http://www.oneclickmoviez.ag/templates/svarog/timthumb.php\?src=(.+?)&amp;.+?" alt=" ".+?<a class="link" href="(.+?)" title="(.+?)">',re.DOTALL).findall(html)
                if not match:
                    match = re.compile('<img class="img-preview spec-border show-thumbnail"  src="http://www.oneclickmoviez.ag/templates/svarog/timthumb.php\?src=(.+?)&amp;.+?" alt=" ".+?<a class="link" href="(.+?)" title="(.+?)">',re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        addon.add_directory({'mode': 'GetTitles18', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')                        
                addon.add_directory({'mode': 'GetTitles18a', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png') 
        setView('tvshows', 'tvshows-view')          
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles19(section, url, startPage= '1', numOfPages= '1'): #all4u
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                   
                match = re.compile('posttitle.+?href="(.+?)".+?>(.+?)<.+?src=.+?.+?', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()},img=IconPath + 'a4u.png', fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles19', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')       
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles20(section, url, startPage= '1', numOfPages= '1'): #world4ufree
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                    
                match = re.compile('<div class="cover"><a href="(.+?)" title="(.+?)"><img src="(.+?)" alt=.+? class=.+? width=.+? height=.+? /></a></div>', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles20', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png') 
        setView('tvshows', 'tvshows-view')        
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles21(section, url, startPage= '1', numOfPages= '1'): #movies2k.eu
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<h2.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles21', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png') 
        setView('tvshows', 'tvshows-view')  
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles23(section, url, startPage= '1', numOfPages= '1'): # 300mbmovies4u
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<div class="cover"><a href="(.+?)".+?.+?<img src="(.+?)".+?alt="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles23', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles25(section, url, startPage= '1', numOfPages= '1'): #rapgrid
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<div class="battleTeaserPhoto"><a href="(.+?)" title="(.+?)"><img src="(.+?)" width="150" height="113"/></a></div>', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks5', 'section': section, 'url': 'http://www.rapgrid.com/' + movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetTitles27(section, url, startPage= '1', numOfPages= '1'): #flixanity2ndtv
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<a class="link" href="(.+?)" title="(.+?)">.+?<span',re.DOTALL).findall(html)
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': movieUrl}, {'title':  name.strip()},img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------#

def GetTitles27a(section, url, startPage= '1', numOfPages= '1'): #flixanity1st
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('text-align:center.+?href="(.+?)".+?.+?src=".+?src=(.+?)&amp;.+?".+?<p><strong>(.+?)</strong></p>', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        addon.add_directory({'mode': 'GetTitles27', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
       	xbmcplugin.endOfDirectory(int(sys.argv[1])) 

#--------------------------------------------------------------------------------------------------------------------------#

def GetTitles28(section, url, startPage= '1', numOfPages= '1'): #shows4u #tvshows2
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        html = net.http_GET(pageUrl).content
        match = re.compile('<a class="link" href="(.+?)" title="(.+?)"',re.DOTALL).findall(html)
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetLinks8', 'section': section, 'url': movieUrl}, {'title':  name.strip()},img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------#

def GetTitles28a(section, url, startPage= '1', numOfPages= '1'): #shows4u #tvshows1
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + ''
                        html = net.http_GET(pageUrl).content
                match = re.compile('<img class="img-preview spec-border"  src=".+?src=(.+?)&amp;.+?" alt=" ".+?<a class="link" href="(.+?)" title="(.+?)">',re.DOTALL).findall(html)
                if not match:
                    match = re.compile('<img class="img-preview spec-border show-thumbnail"  src=".+?src=(.+?)&amp;.+?" alt=" ".+?<a class="link" href="(.+?)" title="(.+?)">',re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        addon.add_directory({'mode': 'GetTitles28', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles28a', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------#

def GetTitles29(section, url, startPage= '1', numOfPages= '1'): #shows4u
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + ''
                        html = net.http_GET(pageUrl).content
                match = re.compile('<img class="img-preview spec-border"  src=".+?src=(.+?)&amp;.+?" alt=" ".+?<a class="link" href="(.+?)" title="(.+?)">',re.DOTALL).findall(html)
                if not match:
                    match = re.compile('<img class="img-preview spec-border show-thumbnail"  src=".+?src=(.+?)&amp;.+?" alt=" ".+?<a class="link" href="(.+?)" title="(.+?)">',re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks8', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles29', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###############################################################################Getlinks#############################################################################################

def GetLinks(section, url): #300mbmovies4u #oneclickmoviez #movies2k.eu
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------#

def GetLinks1(section, url): #flixanity #freemovies #series-cravings
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('src="(.+?)"').findall(content)
        match1 = re.compile('SRC="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match1 :
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------#

def GetLinks3(section, url): # ddlvalley
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(str(url)).content
        sources = []
        listitem = GetMediaInfo(html)
        print 'LISTITEM: '+str(listitem)
        content = html
        print'CONTENT: '+str(listitem)
        match = re.compile('href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                r = re.search('\part1\part2\part3\part4\part5\.rar.html\.rar\.file[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                print '*****************************' + host + ' : ' + url
                title = url.rpartition('/')
                title = title[2].replace('.html', '')
                title = title.replace('.htm', '')
                title = title.replace('.rar', '[COLOR red][B][I]RAR no streaming[/B][/I][/COLOR]')
                title = title.replace('DDLValley.net_', ' ')
                name = host+'-'+title
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)
        source = urlresolver.choose_source(sources)
        if source: stream_url = source.resolve()
        else: stream_url = ''
        xbmc.Player().play(stream_url)

#-----------------------------------------------------------------------#

def GetLinks5(section, url): # rapgrid
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("file: '(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------#

def GetLinks7(section, url): # mvl
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<li><a href="(.+?)">.+?</a></li>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('youtube.com','[COLOR lime]Movie Trailer[/COLOR]')
                        host = host.replace('youtu.be','[COLOR lime]Movie Trailer[/COLOR]')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------#

def GetLinks8(section, url):   #shows4u
        print 'GETLINKS FROM URL: '+url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<IFRAME SRC="(.+?)"').findall(content)
        match1 = re.compile('<iframe src="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match1 :
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################# PlayVideo #####################################################################################

def PlayVideo(url, listitem):
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
 
def GetDomain(url):
        tmp = re.compile('//(.+?)/').findall(url)
        domain = 'Unknown'
        if len(tmp) > 0 :
            domain = tmp[0].replace('www.', '')
        return domain

def GetMediaInfo(html):
        listitem = xbmcgui.ListItem()
        match = re.search('og:title" content="(.+?) \((.+?)\)', html)
        if match:
                print match.group(1) + ' : '  + match.group(2)
                listitem.setInfo('video', {'Title': match.group(1), 'Year': int(match.group(2)) } )
        return listitem

######################################################################menus####################################################################################################

def MainMenu():    #homescreen
        addon.add_directory({'mode': 'MovieMenu'}, {'title':  '[COLOR cornflowerblue][B]Movies >[/B][/COLOR] >'}, img=IconPath + 'films.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'TvMenu'}, {'title':  '[COLOR darkorange][B]Tv Shows >[/B][/COLOR] >'}, img=IconPath + 'tv2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'SportMenu'}, {'title':  '[COLOR lemonchiffon][B]Sport >[/B][/COLOR] >'}, img=IconPath + 'sport1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'MusicMenu'}, {'title':  '[COLOR cadetblue][B]Music Videos >[/B][/COLOR] >'}, img=IconPath + 'music.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'RadioMenu'}, {'title':  '[COLOR lightsteelblue][B]Radio >[/B][/COLOR]>'}, img=IconPath + 'radio.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'SearchMenu'}, {'title':  '[COLOR green][B]Searches [/B] [/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolver.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR pink][B]PLEASE CLICK HERE FOR INFO ON TheYids REPO[/B][/COLOR] >>'}, img=IconPath + 'helphub.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR gold][B]FOLLOW ME ON TWITTER [/B][/COLOR] [COLOR aqua][B][I]@TheYid009 [/B][/I][/COLOR] '}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def HelpMenu():   
        dialog = xbmcgui.Dialog()
        dialog.ok("TheYid's REPO", "I now have a donation button setup at xbmcHUB", "please help keep TheYid's REPO alive more info @","http://www.xbmchub.com/forums/")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def MusicMenu():   #MusicVideos
        addon.add_directory({'mode': 'GetTitles25', 'section': 'ALL', 'url': BASE_URL25 + '/battles',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cadetblue][B]Rap Battle videos[/B][/COLOR] [COLOR springgreen](Rap Grid) [/COLOR]>>'}, img=IconPath + 'rg.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def RadioMenu():   #radio
        #setView('radio', 'radio-view')

        addon.add_directory({'mode': 'RadioMenu', '': '', '': '',
                             '': '', '': ''}, {'title':  '[COLOR lime]~~~~~~~[/COLOR][COLOR yellow][B].....WE ARE.....[/B][/COLOR] [COLOR red][I][B](((LIVE)))[/B][/I][/COLOR] [COLOR yellow][B].....TheYids RADIO.....[/B][/COLOR][COLOR lime]~~~~~~~[/COLOR]'}, img=IconPath + 'radioty.png', fanart='http://geewall.com/mmc_uploads/6119-music-notes-wallpaper-37082.jpg')

        addon_handle = int(sys.argv[1])   # thanks to Android TV Boxes a member of xbmchub for this code thanks mate #
        xbmcplugin.setContent(addon_handle, 'audio')

        url = 'http://uk1-pn.webcast-server.net:8698'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Kool London[/B][/COLOR] >>          [COLOR lime](Drum n bass, jungle, oldskool hardcore)[/COLOR]', iconImage='http://s1.postimg.org/fko2kyu9b/icon.png')
        li.setProperty('fanart_image', 'http://koollondon.com/images/stories/kool-timetable-march-2014.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://176.31.239.83:9136/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Deja Classic [/B][/COLOR] >>         [COLOR lime](oldskool, UK Garage, RnB, HipHop)[/COLOR]', iconImage='http://s2.postimg.org/eg7k51z3t/icon.png')
        li.setProperty('fanart_image', 'http://s18.postimg.org/fnbfwgw3d/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://176.31.239.83:9041/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]DejaVu Live [/B][/COLOR] >>          [COLOR lime](Urban, RnB, HipHop)[/COLOR]', iconImage='http://s2.postimg.org/eg7k51z3t/icon.png')
        li.setProperty('fanart_image', 'http://s18.postimg.org/fnbfwgw3d/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://78.129.228.187:8008/;stream/1'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]House fm [/B][/COLOR] >>          [COLOR lime](House)[/COLOR]', iconImage='http://i1.sndcdn.com/artworks-000049756393-x4gokq-crop.jpg?435a760')
        li.setProperty('fanart_image', 'http://www.strictlyhousefm.co.uk/wp-content/uploads/2012/10/strictly-house-6.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://shine879.internetdomainservices.com:8204/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Shine879 [/B][/COLOR] >>          [COLOR lime](Drum n Bass, House, UK Garage)[/COLOR]', iconImage='https://lh4.ggpht.com/0rdHZ2GOZYeiDfo1jyuWzbiFa9VIHNulX8qvTgXG3bHWMxO28mrxxUrT2VYWeQgaU4k=w300')
        li.setProperty('fanart_image', 'http://dnbvideo.ru/wp-content/uploads/2013/09/antinox-liquid-drum-n-bass-4-1080p-hq.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://178.32.222.61:8080/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Flames radio [/B][/COLOR] >>          [COLOR lime](Funk, Reggae, RnB, Soul)[/COLOR]', iconImage='http://i1.sndcdn.com/artworks-000069969699-cvl43d-original.jpg?a0633e8')
        li.setProperty('fanart_image', 'http://www.disclosurenewsonline.com/wp-content/uploads/2014/01/burning-flames-yellow-fire1.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://typhoon.exequo.org:8000/rinseradio'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Rinse fm [/B][/COLOR] >>             [COLOR lime](Urban, RnB, HipHop)[/COLOR]', iconImage='http://s16.postimg.org/kdlyi29j9/icon.png')
        li.setProperty('fanart_image', 'http://s7.postimg.org/u3877stpn/fanart.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://bbc.co.uk/radio/listen/live/r1x.asx'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]bbc 1xtra[/B][/COLOR] >>             [COLOR lime](Urban, RnB, HipHop)[/COLOR]', iconImage='http://www.madtechrecords.com/wp-content/uploads/2013/08/artworks-000014947132-lbebhn-original.jpg')
        li.setProperty('fanart_image', 'http://s23.postimg.org/5jq12phff/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://tx.whatson.com/icecast.php?i=kissnationallow.mp3'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Kiss 100[/B][/COLOR] >>           [COLOR lime](Dance, RnB, HipHop)[/COLOR]', iconImage='http://images.clubtickets.com/image/200sq/c/kiss-100-wob-400.jpg')
        li.setProperty('fanart_image', 'http://336fcc281d9fb3480f2a-0af712088f38ef5910226b2ecb408482.r82.cf2.rackcdn.com/img-230-3-1366642376.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://media-ice.musicradio.com/CapitalXTRALondonMP3.m3u'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Capital Xtra[/B][/COLOR] >>           [COLOR lime](Dance, RnB, Urban)[/COLOR]', iconImage='http://www.musicweek.com/cimages/7ec1c3e8cda116edcba97d259933f288.jpg')
        li.setProperty('fanart_image', 'http://londonist.com/wp-content/uploads/2013/11/Capital-XTRA.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'mms://wma.sharp-stream.com/moswma'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Ministry of Sound Radio[/B][/COLOR] >>           [COLOR lime](Dance, House, Drum n Bass)[/COLOR]', iconImage='http://i1.sndcdn.com/artworks-000070064884-tec6ir-original.jpg?f775e59')
        li.setProperty('fanart_image', 'http://1.bp.blogspot.com/-pXdClkxvZu8/TleccVYC3EI/AAAAAAAAAic/A7aV-CrKcaU/s1600/Ministry-of-Sound.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://50.117.26.26:5448/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Upper Echelon Radio[/B][/COLOR] >>        [COLOR yellow](US)[/COLOR] [COLOR lime](HipHop)[/COLOR]', iconImage='https://lh4.ggpht.com/TQuDn_5thkjgYupY294UbkBiri4lf8InlIa7_MRj8OVwWhZcVcTxiX0CZV6eF00u9lP1=w300')
        li.setProperty('fanart_image', 'http://i1.ytimg.com/vi/L8IU9C3xZCk/maxresdefault.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://powerhitz.powerhitz.com:5030'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Power Hitz[/B][/COLOR] >>        [COLOR yellow](US)[/COLOR] [COLOR lime](RnB, HipHop)[/COLOR]', iconImage='http://sfweb3.radioline.fr/covers/39322/logo196.png')
        li.setProperty('fanart_image', 'http://w8themes.com/wp-content/uploads/2013/08/Musical-Wallpapers.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://209.105.250.73:8206'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Zmix 97[/B][/COLOR] >>        [COLOR yellow](US)[/COLOR] [COLOR lime](old school, HipHop, funk)[/COLOR]', iconImage='http://media-cache-ec0.pinimg.com/236x/d8/be/0b/d8be0ba53a350149e97eb0e643f5fd1f.jpg')
        li.setProperty('fanart_image', 'http://prettyriveracademy.com/wp-content/uploads/2013/08/hiphop6.jpg.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://s9.myradiostream.com:4418'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Urban hitz radio[/B][/COLOR] >>        [COLOR yellow](US)[/COLOR] [COLOR lime](RnB, HipHop)[/COLOR]', iconImage='https://pbs.twimg.com/profile_images/3424721247/d1111dabf5fd05d86d7fadde2be2e956.png')
        li.setProperty('fanart_image', 'http://upload.wikimedia.org/wikipedia/commons/8/87/The_official_Urban_Hitz_Radio_Logo_for_2013!.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://hot108jamz.hot108.com:4020'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Hot 108 jamz[/B][/COLOR] >>        [COLOR yellow](US)[/COLOR] [COLOR lime](HipHop)[/COLOR]', iconImage='http://i1.ytimg.com/i/DvfgG9q0DPIrVCfy6C-sFA/mq1.jpg?v=dbb2c7')
        li.setProperty('fanart_image', 'http://i1.sndcdn.com/artworks-000006705654-aw46p2-original.jpg?435a760')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://war.str3am.com:7550/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Power 106 FM[/B][/COLOR] >>        [COLOR yellow](Jamaican)[/COLOR] [COLOR lime](Reggae)[/COLOR]', iconImage='http://i.img.co/radio/62/27/2762_290.png')
        li.setProperty('fanart_image', 'http://th03.deviantart.net/fs70/PRE/f/2010/344/3/6/rasta_wallpaper_by_ipwnpt-d34luim.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://war.str3am.com:7970'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Ragga Kings[/B][/COLOR] >>        [COLOR yellow](Jamaican)[/COLOR] [COLOR lime](Reggae, Dancehall)[/COLOR]', iconImage='http://static.rad.io/images/broadcasts/33/32/1922/w175.png')
        li.setProperty('fanart_image', 'http://dubmarine.org/wp-content/uploads/2011/11/RaggakingsPodcast1111-INFRA.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        addon.add_directory({'mode': 'RadioMenu', '': '', '': '',
                             '': '', '': ''}, {'title':  '[COLOR mediumvioletred]~~~~~~~[/COLOR][COLOR aqua][B]Please report any broken links to @TheYid009 on twitter[/B][/COLOR][COLOR mediumvioletred]~~~~~~~[/COLOR]'}, img=IconPath + 'radioty.png', fanart='http://geewall.com/mmc_uploads/6119-music-notes-wallpaper-37082.jpg')

        xbmcplugin.endOfDirectory(addon_handle)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def SportMenu():   #sport
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL14 + '/watch/ufc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest UFC list[/B][/COLOR] [COLOR tomato](ChannelCut) [/COLOR]>>'}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL14 + '/watch/wwe',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest WWE list[/B][/COLOR] [COLOR tomato](ChannelCut) [/COLOR]>>'}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL14 + '/watch/impact-wrestling',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest Impact Wrestling list[/B][/COLOR] [COLOR tomato](ChannelCut) [/COLOR]>>'}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL14 + '/watch/tna',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest TNA list[/B][/COLOR] [COLOR tomato](ChannelCut) [/COLOR]>>'}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL14 + '/watch/fights',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest Fights list[/B][/COLOR] [COLOR tomato](ChannelCut) [/COLOR]>>'}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/wwf-wwe/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Wwf - Wwe[/B][/COLOR]  [COLOR plum](flixanity) [/COLOR] >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def MovieMenu():   #movies 
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR blue](OCW) [/COLOR]>>'}, img=IconPath + 'ocw.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'ZmMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR plum](flixanity) [/COLOR]>>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'OcmMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR peru](OneClickMoviez) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'PutMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](free movies) [/COLOR]>>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'TvsMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR darkorange](shows4u) [/COLOR]>>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'MovMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR lightslategray](ViooZ) [/COLOR]>>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'UvMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR floralwhite](Ultra-Vid) [/COLOR]>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR salmon](WTT) [/COLOR]>>'}, img=IconPath + 'wtt.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'WtMenu'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR lightsteelblue][B]International Movies Zone[/B][/COLOR] >>'}, img=IconPath + 'iz.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'RgMenu'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR mediumturquoise][B]Full HD Zone[/B][/COLOR] >>'}, img=IconPath + 'fhz.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def TvsMenu():   #shows4u
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR darkorange](shows4u) [/COLOR]>>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movies/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]movies[/B] [/COLOR][COLOR teal](imdb)[/COLOR] >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tvs1Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](IMDB rating) [/COLOR]>>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetSearchQuery7'},  {'title':  '[COLOR green][B]Search[/B][/COLOR] [COLOR darkorange](shows4u) [/COLOR] >> '}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tvs1Menu(): #shows4u
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/action/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/biography/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/music/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/musical/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/sci-fi/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci-Fi (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/sport/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/superhero/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Superhero (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/thriller/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/war/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/western/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles29', 'section': 'ALL', 'url': BASE_URL29 + '/movie-tags/wwf-wwe/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Wwf - Wwe (imdb) >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def RgMenu():   #yify  #mvl rg #HD zone
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/hollywood-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hollywood[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/hollywood-movie/english-yify-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Yify[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/hollywood/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hollywood [/B][/COLOR][COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL5 + '/category/english-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hollywood [/B][/COLOR] [COLOR fuchsia](Moviesall4u) [/COLOR]>>'}, img=IconPath + 'm4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/yify/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Yify[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/ganool/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Ganool[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/msd/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Msd[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/anoxmous/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Anoxmous[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/judas/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Judas[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL11 + '/category/movies/yify-rips/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Yify[/B][/COLOR] [COLOR mediumblue](DDLvalley) [/COLOR]>>'}, img=IconPath + 'ddl1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def WtMenu():   #Moviesall4u  #all4youz #world4ufree
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/hollywood-movie/english-movie-dual-audio/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Dual Audio[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/tamil-movie/tamil-hindi-dubbed-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Tamil hindi Dubbed[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/bollywood-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Bollywood[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/tamil-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Tamil[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles19', 'section': 'ALL', 'url': BASE_URL19 + '/category/hollywood/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hollywood [/B][/COLOR] [COLOR bisque](All4Youz) [/COLOR]>>'}, img=IconPath + 'a4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/bollywood/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Bollywood [/B][/COLOR] [COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/hindi-dubbed-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hindi Dubbed [/B][/COLOR] [COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/songs/indian-videos/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Indian Music Videos [/B][/COLOR] [COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL5 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Added [/B][/COLOR] [COLOR fuchsia](Moviesall4u) [/COLOR]>>'}, img=IconPath + 'm4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL5 + '/category/hindi-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hindi [/B][/COLOR] [COLOR fuchsia](Moviesall4u) [/COLOR]>>'}, img=IconPath + 'm4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL5 + '/category/indian-bangla-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Indian & Bangla Movies [/B][/COLOR] [COLOR fuchsia](Moviesall4u) [/COLOR]>>'}, img=IconPath + 'm4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles5', 'section': 'ALL', 'url': BASE_URL5 + '/category/dual-audio-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Dual Audio [/B][/COLOR] [COLOR fuchsia](Moviesall4u) [/COLOR]>>'}, img=IconPath + 'm4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles19', 'section': 'ALL', 'url': BASE_URL19 + '/category/box-office-hit/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Box Office [/B][/COLOR] [COLOR bisque](All4Youz) [/COLOR]>>'}, img=IconPath + 'a4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles19', 'section': 'ALL', 'url': BASE_URL19 + '/category/bollywood/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Bollywood [/B][/COLOR] [COLOR bisque](All4Youz) [/COLOR]>>'}, img=IconPath + 'a4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles19', 'section': 'ALL', 'url': BASE_URL19 + '/category/hiindi-dubbed/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hindi Dubbed [/B][/COLOR] [COLOR bisque](All4Youz) [/COLOR]>>'}, img=IconPath + 'a4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles19', 'section': 'ALL', 'url': BASE_URL19 + '/category/dual-audio/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Dual Audio [/B][/COLOR] [COLOR bisque](All4Youz) [/COLOR]>>'}, img=IconPath + 'a4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/hollywood-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Hollywood [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/hindi-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Hindi [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/hindi-dubbed/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Hindi Dubbed [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/malayalam-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Malayalam [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/tamil-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Tamil [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/telugu-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Telugu [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def MovMenu():   #moviesviooz
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR lightslategray](ViooZ) [/COLOR]>>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hd-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'HD Movies >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/sci-Fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/war',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def UvMenu():   #moviesUv
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR floralwhite](Ultra-Vid) [/COLOR]>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/hd',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'HD Movies >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery drama >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/romance-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/comedy/romantic-comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romantic comedy>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/sci-fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci-fi >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/family/holiday',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def ZmMenu(): #flixanity
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movies/new',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR plum](flixanity) [/COLOR]>>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/featuredmovies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Box Office[/B][/COLOR] >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movies/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]movies[/B] [/COLOR][COLOR teal](a/z)[/COLOR] >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movies/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]movies[/B] [/COLOR][COLOR teal](imdb)[/COLOR] >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Zm1Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](IMDB rating) [/COLOR]>>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Zm2Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](Newest) [/COLOR]>>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Zm3Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](ABC) [/COLOR]>>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery6'},  {'title':  '[COLOR green][B]Search[/B][/COLOR] [COLOR plum]flixanity[/COLOR] >> '}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Zm1Menu(): #flixanity
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/action/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/biography/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/music/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/musical/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/sci-fi/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci-Fi (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/sport/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/superhero/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Superhero (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/thriller/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/war/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/western/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/wwf-wwe/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Wwf - Wwe (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Zm2Menu(): #flixanity
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/biography',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary (imdb) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/family',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/music',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/musical',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/mystery',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/sci-fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci-Fi  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/superhero',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Superhero  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/war',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/wwf-wwe',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Wwf - Wwe  >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Zm3Menu(): #flixanity
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/action/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/adventure/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/animation/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/biography/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/comedy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/crime/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/documentary/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/drama/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/family/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/fantasy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/horror/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/music/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/musical/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/mystery/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/romance/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/sci-fi/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci-Fi (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/sport/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/superhero/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Superhero (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/thriller/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/war/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/western/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movie-tags/wwf-wwe/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Wwf - Wwe (abc) >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def PutMenu():          # freemoviesntvshows
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/new-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Added [/B][/COLOR] >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movies/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]ABC [/B][/COLOR] >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movies/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Top IMDB [/B][/COLOR] >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Put1Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](Latest added) [/COLOR]>>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'Put2Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](IMDB rating) [/COLOR]>>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'Put3Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](A/Z) [/COLOR]>>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Put1Menu():          # freemoviesntvshows
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/action-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/adventure-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/animation-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/-history-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/comedy-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/crime-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/drama-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/documentary-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/fantasy-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/family-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/horror-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/mystery-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/romance-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/sci-fi-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/sport-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/western-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Put2Menu():          # freemoviesntvshows
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/action-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/adventure-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/animation-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/-history-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'History >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/comedy-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/crime-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/drama-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/documentary-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/fantasy-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/family-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/horror-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/musical-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/mystery-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/romance-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/sci-fi-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/western-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Put3Menu():          # freemoviesntvshows
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/action-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/adventure-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/animation-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/-history-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'History >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/comedy-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/crime-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/drama-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/documentary-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/fantasy-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/family-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/horror-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/mystery-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/romance-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/sci-fi-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movie-tags/western-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'fm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def OcmMenu():          #one click moviez
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Added [/B][/COLOR] >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/featuredmovies/date/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Featured [/B][/COLOR] >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movies/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Top IMDB [/B][/COLOR] >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Ocm1Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR peru](Latest added) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'Ocm2Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR peru](IMDB rating) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'Ocm3Menu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR peru](A/Z) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery5'},  {'title':  '[COLOR green][B]Search[/B][/COLOR] [COLOR peru](OneClickMoviez) [/COLOR] >> '}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def Ocm1Menu():          #one click movies
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/biography',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/family',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/musical',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/mystery',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/sci-fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/war',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Ocm2Menu():          #one click moviez imdb
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/action/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/biography/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/musical/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/sci-fi/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/sport/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/thriller/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/war/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/western/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Ocm3Menu():          #one click watch abc
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/action/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/adventure/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/animation/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/biography/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/comedy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/crime/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/drama/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/documentary/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/fantasy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/family/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/horror/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/musical/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/mystery/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/romance/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/sci-fi/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/sport/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/thriller/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/warv',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles9', 'section': 'ALL', 'url': BASE_URL9 + '/movie-tags/western/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################---tv---##########################################################################################################

def TvMenu():       #tv
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR blue](OCW) [/COLOR]>>'}, img=IconPath + 'ocw.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'TsuMenu'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR darkorange](shows4u) [/COLOR]>>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'TzmMenu'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR plum](flixanity) [/COLOR]>>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'TvocmMenu'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR peru](OneClickMoviez) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles11', 'section': 'ALL', 'url': BASE_URL11 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR mediumblue](DDLvalley) [/COLOR]>>'}, img=IconPath + 'ddl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/tv',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR floralwhite](Ultra-Vid) [/COLOR]>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL2 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR darkslateblue](WTS) [/COLOR]>>'}, img=IconPath + 'wts1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/category/tvshows',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR salmon](WTT) [/COLOR]>>'}, img=IconPath + 'wtt.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL14 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes list[/B][/COLOR] [COLOR tomato](ChannelCut) [/COLOR]>>'}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles17', 'section': 'ALL', 'url': BASE_URL17 + '/category/shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes list[/B][/COLOR] [COLOR sienna](Tv-Junky) [/COLOR]>>'}, img=IconPath + 'tvj.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def TvocmMenu():   #oneclickmoviez
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-shows',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR peru](Latest added) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-shows/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR peru](Top IMDB) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-shows/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR peru](ABC) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tvocm1Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](Top IMDB ) [/COLOR]>>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tvocm1Menu():
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/action/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/biography/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Biography >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/musical/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Musical >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/sci-fi/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/sport/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/thriller/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/war/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles18a', 'section': 'ALL', 'url': BASE_URL9 + '/tv-tags/western/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

def TzmMenu():  #flixanitytv
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-shows',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Latest added[/B][/COLOR] >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-shows/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Top IMDB[/B][/COLOR] >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-shows/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]ABC[/B][/COLOR] >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tzm1Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](Top IMDB) [/COLOR]>>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tzm3Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](ABC) [/COLOR]>>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tzm2Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](Newest) [/COLOR]>>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tzm1Menu():
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/kids/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Kids >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/music/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/reality-tv/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality Tv >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/sci-fi/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/sport/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/thriller/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/war/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/talk-show/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Talk Show >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/wwf-wwe/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Wwf - Wwe >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tzm2Menu():
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/family',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/kids',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Kids >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/music',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/mystery',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/reality-tv',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality Tv >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/sci-fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/war',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/talk-show',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Talk Show >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/wwf-wwe',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Wwf - Wwe >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tzm3Menu():
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/adventure/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/animation/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/comedy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/crime/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/drama/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/documentary/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/fantasy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/family/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/horror/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/kids/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Kids >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/music/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/mystery/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/romance/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/reality-tv/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality Tv >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/sci-fi/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/sport/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/thriller/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/war/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/talk-show/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Talk Show >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/wwf-wwe/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Wwf - Wwe >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

def TsuMenu():  #tvshows4u
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-shows',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Latest added[/B][/COLOR] [COLOR darkorange](shows4u) [/COLOR]>>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-shows/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Top IMDB[/B][/COLOR] >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-shows/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]ABC[/B][/COLOR] >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tsu2Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](Newest 1st) [/COLOR]>>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tsu1Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](Top IMDB 1st) [/COLOR]>>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tsu3Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](ABC) [/COLOR]>>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tsu1Menu():
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/action/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/kids/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Kids >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/music/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/reality-tv/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality Tv >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/sci-fi/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/sport/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/thriller/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/war/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/talk-show/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Talk Show >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/western/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tsu2Menu():
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/family',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/kids',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Kids >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/music',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/mystery',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/reality-tv',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality Tv >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/sci-fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/war',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/talk-show',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Talk Show >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tsu3Menu():
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/action/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/adventure/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/animation/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/comedy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/crime/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/drama/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/documentary/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/fantasy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/family/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/horror/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/kids/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Kids >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/music/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/mystery/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/romance/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/reality-tv/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality Tv >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/sci-fi/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/sport/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/thriller/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/war/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/western/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

################################################################################searchmenu###############################################################################################

def SearchMenu():
        addon.add_directory({'mode': 'GetSearchQuery9'},  {'title':  '[COLOR blue][B]OneClickWatch[/B][/COLOR] [COLOR green]Search[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery1'},  {'title':  '[COLOR salmon][B]WatchTheTapes[/B][/COLOR] [COLOR green]Search[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery2'},  {'title':  '[COLOR darkslateblue][B]WatchTvShows[/B][/COLOR] [COLOR green]Search Tv Shows[/COLOR] '}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery3'},  {'title':  '[COLOR coral][B]TV junky[/B][/COLOR] [COLOR green]Search Tv Shows[/COLOR] '}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery4'},  {'title':  '[COLOR tomato][B]ChannelCut[/B][/COLOR] [COLOR green]Search Tv Shows[/COLOR] '}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

########################################################################search#################################################################################################

def GetSearchQuery9():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search9(query)
	else:
                return  
def Search9(query):
        url = 'http://www.google.com/search?q=site:oneclickwatch.org ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##---------------------------------------------------------------------------------------------------------------##

def GetSearchQuery2():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search TV Shows[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search2(query)
	else:
                return  
def Search2(query):
        url = 'http://www.google.com/search?q=site:watchtvshowz.org ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('Watch', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##---------------------------------------------------------------------------------------------------------------##

def GetSearchQuery1():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search1(query)
	else:
                return
def Search1(query):
        url = 'http://www.google.com/search?q=site:watchthetapes.com ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('Watch', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##---------------------------------------------------------------------------------------------------------------##

def GetSearchQuery3():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search TV Shows[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search3(query)
	else:
                return
def Search3(query):
        url = 'http://www.google.com/search?q=site:tv-junky.eu ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('Watch', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##---------------------------------------------------------------------------------------------------------------##

def GetSearchQuery4():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search TV Shows[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search4(query)
	else:
                return
def Search4(query):
        url = 'http://www.google.com/search?q=site:channelcut.me ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('Watch', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title})
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##---------------------------------------------------------------------------------------------------------------##

def GetSearchQuery5():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search OneClickMoviez[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search5(query)
	else:
                return
def Search5(query):
        url = 'http://www.google.com/search?q=site:oneclickmoviez.ag ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('ONE CLICK MOVIEZ', '').replace('Watch', '').replace('Online', '').replace('|', '')
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title}, img=IconPath + '1cm.png', fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##---------------------------------------------------------------------------------------------------------------##

def GetSearchQuery6():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search flixanity[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search6(query)
	else:
                return
def Search6(query):
        url = 'http://www.google.com/search?q=site:flixanity.com ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('Online', '').replace('Watch', '')
                addon.add_directory({'mode': 'GetLinks1', 'url': url}, {'title':  title}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

###################################################################################### setViews ##########################################################################

def setView(content, viewType):

	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if addon.get_setting('auto-view') == 'true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.get_setting(viewType) )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )

##############################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
elif mode == 'GetTitles2': 
	GetTitles2(section, url, startPage, numOfPages)
elif mode == 'GetTitles3': 
	GetTitles3(section, url, startPage, numOfPages)
elif mode == 'GetTitles4': 
	GetTitles4(section, url, startPage, numOfPages)
elif mode == 'GetTitles5': 
	GetTitles5(section, url, startPage, numOfPages)
elif mode == 'GetTitles9': 
	GetTitles9(section, url, startPage, numOfPages)
elif mode == 'GetTitles10': 
	GetTitles10(section, url, startPage, numOfPages)
elif mode == 'GetTitles11': 
	GetTitles11(section, url, startPage, numOfPages)
elif mode == 'GetTitles12': 
	GetTitles12(section, url, startPage, numOfPages)
elif mode == 'GetTitles14': 
	GetTitles14(section, url, startPage, numOfPages)
elif mode == 'GetTitles12a': 
	GetTitles12a(section, url, startPage, numOfPages)
elif mode == 'GetTitles15': 
	GetTitles15(section, url, startPage, numOfPages)
elif mode == 'GetTitles16': 
	GetTitles16(section, url, startPage, numOfPages)
elif mode == 'GetTitles17': 
	GetTitles17(section, url, startPage, numOfPages)
elif mode == 'GetTitles18': 
	GetTitles18(section, url, startPage, numOfPages)
elif mode == 'GetTitles18a': 
	GetTitles18a(section, url, startPage, numOfPages)
elif mode == 'GetTitles19': 
	GetTitles19(section, url, startPage, numOfPages)
elif mode == 'GetTitles20': 
	GetTitles20(section, url, startPage, numOfPages)
elif mode == 'GetTitles21': 
	GetTitles21(section, url, startPage, numOfPages)
elif mode == 'GetTitles23': 
	GetTitles23(section, url, startPage, numOfPages)
elif mode == 'GetTitles25': 
	GetTitles25(section, url, startPage, numOfPages)
elif mode == 'GetTitles27': 
	GetTitles27(section, url, startPage, numOfPages)
elif mode == 'GetTitles27a': 
	GetTitles27a(section, url, startPage, numOfPages)
elif mode == 'GetTitles28': 
	GetTitles28(section, url, startPage, numOfPages)
elif mode == 'GetTitles28a': 
	GetTitles28a(section, url, startPage, numOfPages)
elif mode == 'GetTitles29': 
	GetTitles29(section, url, startPage, numOfPages)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks1':
	GetLinks1(section, url)
elif mode == 'GetLinks3':
	GetLinks3(section, url)
elif mode == 'GetLinks5':
	GetLinks5(section, url)
elif mode == 'GetLinks7':
	GetLinks7(section, url)
elif mode == 'GetLinks8':
	GetLinks8(section, url)
elif mode == 'GetSearchQuery9':
	GetSearchQuery9()
elif mode == 'Search9':
	Search9(query)
elif mode == 'GetSearchQuery2':
	GetSearchQuery2()
elif mode == 'Search2':
	Search2(query)
elif mode == 'GetSearchQuery3':
	GetSearchQuery3()
elif mode == 'Search3':
	Search3(query)
elif mode == 'GetSearchQuery1':
	GetSearchQuery1()
elif mode == 'Search1':
	Search1(query)
elif mode == 'GetSearchQuery4':
	GetSearchQuery4()
elif mode == 'Search4':
	Search4(query)
elif mode == 'GetSearchQuery5':
	GetSearchQuery5()
elif mode == 'Search5':
	Search5(query)
elif mode == 'GetSearchQuery6':
	GetSearchQuery6()
elif mode == 'Search6':
	Search6(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'SearchMenu':
        SearchMenu()
elif mode == 'MovieMenu':
        MovieMenu()
elif mode == 'TvMenu':
        TvMenu()
elif mode == 'MusicMenu':
        MusicMenu()
elif mode == 'MovMenu':
        MovMenu()
elif mode == 'UvMenu':
        UvMenu()
elif mode == 'WtMenu':
        WtMenu()
elif mode == 'ZmMenu':
        ZmMenu()
elif mode == 'Zm1Menu':
        Zm1Menu()
elif mode == 'Zm2Menu':
        Zm2Menu()
elif mode == 'Zm3Menu':
        Zm3Menu()
elif mode == 'RgMenu':
        RgMenu()
elif mode == 'OmpMenu':
        OmpMenu()
elif mode == 'SportMenu':
        SportMenu()
elif mode == 'OmpazMenu':
        OmpazMenu()
elif mode == 'OcmMenu':
        OcmMenu()
elif mode == 'Ocm1Menu':
        Ocm1Menu()
elif mode == 'Ocm2Menu':
        Ocm2Menu()
elif mode == 'Ocm3Menu':
        Ocm3Menu()
elif mode == 'TvocmMenu':
        TvocmMenu()
elif mode == 'Tvocm1Menu':
        Tvocm1Menu()
elif mode == 'TzmMenu':
        TzmMenu()
elif mode == 'Tzm1Menu':
        Tzm1Menu()
elif mode == 'Tzm2Menu':
        Tzm2Menu()
elif mode == 'Tzm3Menu':
        Tzm3Menu()
elif mode == 'PutMenu':
        PutMenu()
elif mode == 'Put1Menu':
        Put1Menu()
elif mode == 'Put2Menu':
        Put2Menu()
elif mode == 'Put3Menu':
        Put3Menu()
elif mode == 'RadioMenu':
        RadioMenu()
elif mode == 'TvsMenu':
        TvsMenu()
elif mode == 'Tvs1Menu':
        Tvs1Menu()
elif mode == 'TsuMenu':
        TsuMenu()
elif mode == 'Tsu1Menu':
        Tsu1Menu()
elif mode == 'Tsu2Menu':
        Tsu2Menu()
elif mode == 'Tsu3Menu':
        Tsu3Menu()