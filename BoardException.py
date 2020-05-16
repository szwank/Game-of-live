class BoardException(Exception):
    def init(self, message):
        super(BoardException, self).__init__(message)
