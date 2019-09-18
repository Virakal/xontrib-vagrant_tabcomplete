import re


class Completer:
    top_level_commands = {
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
        self.wants_next_val = line.endswith(' ')

    def should_complete(self):
        return self.tokens[0] == 'vagrant'

    def _complete(self):
        if not self.should_complete():
            return

        # If we only have `vagrant`, list all top level commands
        if len(self.tokens) == 1:
            return self.top_level_commands

        # Otherwise find the completer for the top level command, "vagrant rsync-auto" dispatches to complete_rsync_auto() for example
        if self.wants_next_val:
            return self.complete_subcommand()
        else:
            return self.complete_top_level_command()

    def complete_subcommand(self):
        command = self.tokens[1]
        method_name = "complete_%s" % command.lower().replace('-', '_')

        try:
            method = getattr(self, method_name)
        except AttributeError:
            # We can't complete this
            return

        return method()

    def complete_top_level_command(self):
        return {x for x in self.top_level_commands if x.startswith(self.prefix)}

    @classmethod
    def complete(cls, prefix, line, begidx, endidx, ctx):
        comp = cls(prefix, line, begidx, endidx, ctx)
        return comp._complete()
