import os
import shutil
import filelist

__INSTALL__ = 'install'
__UPDATE__ = 'update'

class sync():
    """
    Syn config files
    to deploy dot files( default ):
        python sync.py install
    to update file to respo.:
        python sync.python update
    to add/rm files:
        modif
    """

    def __init__( self ):
        "$key is directory, $value is entries in the folder"
        self.filelist = filelist.filelist
        self.cwd = os.path.dirname( os.path.abspath( __file__ ))

    def deployFiles( self, folder, files, direct ):
        "copy files to repo. folder"
        if direct == __INSTALL__:
            copyFile( folder[1], folder[0], files )
        else:
            copyFile( folder[0], folder[1], files )

    def copyFile( self, src, dst, files ):
        "copy( src,dst )"
        os.chdir( src )
        for _file in files:
            shutil.copy( _file, dst )       # shutil.copy

    def startSync( self,mode ):
        "startSync"
        if mode is 'install':
            for folder in self.filelist:
                #self.deployFiles( folder, filelist[folder], __INSTALL__ )
                self.copyFile( folder[1],folder[0],filelist[folder] )
        else:
            for folder, files in self.filelist:
                #self.deployFiles( folder, filelist[folder], __UPDATE__ )
                self.copyFile( folder[0],folder[1],filelist[folder] )

if __name__ == '__main__':
    sync = sync()
    if len( sys.argv ) == 2:
        sync.startSync( __INSTALL__ )
    else:
        sync.startSync( sys.argv[2] )
