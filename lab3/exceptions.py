class InsufficientFundsError(Exception):
    pass


class AccountExistsError(Exception):
    pass


class AccountNotFoundError(Exception):
    pass


class UnauthorizedOperationError(Exception):
    pass


class InitError(Exception):
    pass