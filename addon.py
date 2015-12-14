import xbmc,xbmcaddon,xbmcgui,json,random

def getAllMovies(randomType):
  rpccmd = {'jsonrpc': '2.0', 'method': 'VideoLibrary.GetMovies', 'params': { 'properties': [ 'file' ] }, 'id': 'libMovies'}

  if (randomType == '1'):
    rpccmd = {'jsonrpc': '2.0', 'method': 'VideoLibrary.GetMovies', 'params': { 'filter': { 'field': 'playcount', 'operator': 'greaterthan', 'value': '0' }, 'properties': [ 'file' ] }, 'id': 'libMovies'}
  if (randomType == '2'):
    rpccmd = {'jsonrpc': '2.0', 'method': 'VideoLibrary.GetMovies', 'params': { 'filter': { 'field': 'playcount', 'operator': 'lessthan', 'value': '1' }, 'properties': [ 'file' ] }, 'id': 'libMovies'}

  rpccmd = json.dumps(rpccmd)
  result = xbmc.executeJSONRPC(rpccmd)
  result = json.loads(result)
  return result

addon     = xbmcaddon.Addon()
addonName = addon.getAddonInfo('name')
addonIcon = addon.getAddonInfo('icon')

randomType         = addon.getSetting('randomType')
askForTypeOnLaunch = addon.getSetting('askForTypeOnLaunch')

if (askForTypeOnLaunch == 'true'):
  # TODO: Open dialog with multiselect and overwrite randomType

movies = getAllMovies(randomType)
movie  = random.choice(movies['result']['movies'])
time   = 5000

xbmc.executebuiltin('PlayMedia(%s)'%(movie['file']))
xbmc.executebuiltin('Notification(%s, %s %s, %d, %s)'%(addonName,"Playing ",movie['label'],time,addonIcon))