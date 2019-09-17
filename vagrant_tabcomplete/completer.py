class Completer:
    def complete(self, prefix, line, begidx, endidx, ctx):
        if not line.startswith('vagrant '):
            return

        return {'test', 'this', 'thng'}
