# -*- coding: utf-8 -*-
from hash_file import hashFile
import os
import xmlrpclib

url_api = 'http://api.opensubtitles.org/xml-rpc'
def download_sub(file_path, language):
    file_size = os.path.getsize( file_path )
    file_hash = hashFile( file_path )
    
    server = xmlrpclib.Server(url_api)
    print "\n******** INFO API ********"
    print server.ServerInfo()
    
    print "\n******** LOG IN ********"
    resp = server.LogIn("","","fr","MyAPP V2")
    token = str(resp["token"])
    print resp
    
    print "\n******** CHECK HASH IN DB ********"
    resp = server.CheckMovieHash(token,[file_hash])
    print resp
    
    print "\n******** SEARCH FOR SUBTITLE ********"
    resp = server.SearchSubtitles(token, [{'sublanguageid': language, 'moviehash': file_hash, 'moviebytesize': file_size}])
    print '{} subtitles found.'.format(len(resp['data']))
    subs = resp['data']
    
    print "\n******** DOWNLOADING SUBTITLE ********"
    resp = server.DownloadSubtitles(token, [ subs[0]['IDSubtitleFile'] ])
    import zlib
    import base64
    data = base64.standard_b64decode( resp['data'][0]['data'] )
    uncompressed_data = zlib.decompress(data, 47) # WHY 47 ???
    
    print "\n******** SAVING TO FILE ********"
    srt_file = '{}.srt'.format( os.path.splitext(file_path)[0] )
    print 'Saving to file ', srt_file
    with open(srt_file, 'wb') as f:
    	f.write(uncompressed_data)
    
    print "\n******** LOG OUT ********"
    print server.LogOut(token)


