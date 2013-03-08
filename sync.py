import os
import shutil

class sync():
    "Syn config files"
    def _init__(self):
        # $key is directory, $value is entries in the folder
        self.filelist = {'~/.vim':['Bundles.vim','setting.vim','autocmd','mapping.vim','myvimrc.vim']}
        self.cwd = os.path.dirname( os.path.abspath(__file__))

    def copyFile(self, _file):
        "copy files to repo. folder"
        # TODO


    def checkFile(self, _file):
        "check file if it is modified"
        # TODO

    def handleFileList(self, filelist = self.filelist):
        for _dir, _files in filelist:
            os.chdir( _dir )
            _cwd = os.getcwd()
            for _file in _files:
                if self.checkFile( _file ):
                    self.copyFile( _file )
