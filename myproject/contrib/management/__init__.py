from typing import List


def execute_command(argv: List[str]):
    manager = Management(argv)


class Management:
    argv: List[str]

    def __init__(self, argv: List[str] = ...):
        if len(argv) == 1:
            self.runserver()
        
        command = argv[1]
        if command == "runserver":
            self.runserver()

    
    def runserver(self, host="127.0.0.1", port=5000):
        from ... import create_app
        app = create_app()
        app.run(host=host, port=port)
        
