

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

    def should_complete(self):
        line = self.line.strip()

        if line.startswith('vagrant'):
            return True

        aliases = self._get_vagrant_aliases()

        return False

    def _get_vagrant_aliases(self):
        """Get a list of aliases that call vagrant"""
        # TODO: We need to do something smarter to handle e.g. `alises['vp'] = ['vagrant', 'plugin']` though!

        return {k for (k, v) in aliases.items() if hasattr(v, '__iter__') and v[0] == 'vagrant'}

    def _complete(self):
        if not self.should_complete():
            return

        return self.command_list

    @classmethod
    def complete(cls, prefix, line, begidx, endidx, ctx=None):
        comp = cls(prefix, line, begidx, endidx, ctx)
        return comp._complete()
