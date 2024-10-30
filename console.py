import cmd
import shlex

import colorama

import os
from app import create_app
from cache import Cache

cache = Cache()


class CacheProxy(cmd.Cmd):
    ''' Implements a CLI for the cache proxy server '''
    prompt = colorama.Fore.GREEN + colorama.Style.BRIGHT + 'caching-proxy ' + colorama.Style.RESET_ALL

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.port = None
        self.origin = None
        self.cache = {}

    def preloop(self):
        ''' Runs before the loop starts '''
        print('Welcome to the cache proxy server console')

    def do_EOF(self, arg):
        ''' Exits console '''
        return True
    
    def emptyline(self):
        ''' Overwrites the empty line method '''
        return False
    
    # Aliases
    do_exit = do_EOF
    do_quit = do_EOF
    do_q = do_EOF
    
    # def precmd(self, line):
    #     ''' Overwrites the pre command method '''
    #     args = line.split()
    def onecmd(self, line):
        ''' Overwrites the one command method '''
        args = shlex.split(line)

        if '--port' in args:
            self.port = args[args.index('--port') + 1]
            print(f'Port set to {self.port}')

        if '--origin' in args:
            self.origin = args[args.index('--origin') + 1]
            print(f'Origin set to {self.origin}')
        
        if '--clear-cache' in args:
            cache.clear()
            return False
            # self.clear_cache()
            # print('Cache cleared')

        if self.port and self.origin:
            print(f"Starting proxy server at localhost:{self.port}, forwarding to {self.origin}")
            os.environ['ORIGIN_URL'] = self.origin
            app = create_app()
            app.run(port=self.port)

        return super().onecmd(line)
    
    # def clear_cache(self):
    #     ''' Clears the cache '''
    #     cache.clear()
    
    def do_show(self, arg):
        ''' Shows the cache, list of keys 
        Usage: show
        '''
        list_cache = []
        for key in cache.cache.keys():
            list_cache.append(key.decode('utf-8'))
        print(list_cache)
        return False
    
    def do_clear(self, args):
        ''' Clears the terminal 
        Usage: clear
        '''
        os.system('clear')
        return False


if __name__ == '__main__':
    CacheProxy().cmdloop()
