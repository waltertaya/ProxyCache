import cmd
import shlex


class CacheProxy(cmd.Cmd):
    ''' Implements a CLI for the cache proxy server '''
    prompt = 'caching-proxy '

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.port = None
        self.origin = None
        self.clear = None

    def preloop(self):
        ''' Runs before the loop starts '''
        print('Welcome to the cache proxy server console')

    def do_EOF(self, arg):
        ''' Exits console '''
        return True
    
    def emptyline(self):
        ''' Overwrites the empty line method '''
        return False
    
    def do_quit(self, arg):
        ''' Exits console '''
        return True
    
    # def precmd(self, line):
    #     ''' Overwrites the pre command method '''
    #     args = line.split()
    def onecmd(self, line):
        ''' Overwrites the one command method '''
        args = shlex.split(line)


if __name__ == '__main__':
    CacheProxy().cmdloop()
