import re


class Completer:
    command_list = {
        'box',
        'cloud',
        'connect',
        'destroy',
        'docker-exec',
        'docker-logs',
        'docker-run',
        'global-status',
        'halt',
        'help',
        'init',
        'list-commands',
        'login',
        'package',
        'plugin',
        'provision',
        'push',
        'rdp',
        'reload',
        'resume',
        'rsync',
        'rsync-auto',
        'share',
        'snapshot',
        'ssh',
        'ssh-config',
        'status',
        'suspend',
        'up',
        'version',
    }

    def __init__(self, prefix, line, begidx, endidx, ctx):
        self.prefix = prefix
        self.line = line
        self.begidx = begidx
        self.endidx = endidx
        self.ctx = ctx
        self.tokens = re.split(r'\s+', line.strip())

    def should_complete(self):
        return self.tokens[0] == 'vagrant'

    def _complete(self):
        if not self.should_complete():
            return

        return self.command_list

    @classmethod
    def complete(cls, prefix, line, begidx, endidx, ctx=None):
        comp = cls(prefix, line, begidx, endidx, ctx)
        return comp._complete()
