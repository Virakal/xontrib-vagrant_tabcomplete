from vagrant_tabcomplete import completer

comp_instance = completer.Completer()
comp = comp_instance.complete

completer add vagrant comp
