import os

def adecrypt(path,p):
    
    tries = 0

    if p[0xE7] == 00: print '\nFile does not appear to be encrypted.'
    
    while p[0xE7] != 00:
        pathn = path[:-3] + 'dc.pkx'
        
        if os.path.exists(pathn):
            print '\nFile appears to already have been decrypted as %s.' % pathn
            path = pathn
            break
        
        else: print '\nFile appears to be encrypted, will attempt to decrypt...'
        
        if tries > 0:
            print 'Decryption has been attempted %d times, Pokemon data may be invalid.' % tries
            left = 4 - tries
            print 'Will try %d more times...' % left
        if tries > 3:
            print 'Decryption has failed 4 times, data is probably invalid.'
            print '\n\nPress ctrl + c to exit...'
            while True:
                nothing = raw_input()
        
        os.system('xyc.exe ' + path + ' ' + pathn)
        path = pathn
        tries += 1
        print 'File decrypted and saved as %s' % (path)
        break

    return path
