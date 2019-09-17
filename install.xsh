import sys
sys.path.insert(0, '')

if 'vagrant' in __xonsh__.completers:
    completer remove vagrant

source './xontrib/vagrant_tabcomplete.xsh'
