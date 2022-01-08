class SubCode:
    invalid = "invalid"
    no_access = "no-access"
    no_data = "no-data"
    too_much_data = "too-much-data"
    account_expired = "account-expired"
    denied = "denied"
    no_login = "no-login"
    illegalparent = "illegalparent"
    no_quota = "no-quota"
    not_available = "not-available"
    not_secure = "not-secure"
    pending_activation = "pending-activation"
    pending_license = "pending-license"
    sco_expired = "sco-expired"
    sco_not_started = "sco-not-started"
    valuelessthanorequal = "valuelessthanorequal"
    duplicate = "duplicate"
    format = "format"


class Error(Exception):
    pass


class Duplicate(Error):
    def __init__(self):
        self.message = "Duplicate Error, already exists."

    def __str__(self):
        return self.message


class NotFound(Error):
    def __init__(self):
        self.message = "Not found any thing like that."

    def __str__(self):
        return self.message


class InvalidMeetingId(Error):
    def __init__(self):
        self.message = "Invalid Meeting ID, there is no meeting id like this."

    def __str__(self):
        return self.message


class InvalidPrincipalId(Error):
    def __init__(self):
        self.message = "Invalid User ID or Group ID, there is no ID like this."

    def __str__(self):
        return self.message


class InvalidPermissionID(Error):
    def __init__(self):
        self.message = "Invalid Permission ID, there is no permission id like this."

    def __str__(self):
        return self.message


class InvalidEmailAddress(Error):
    def __init__(self):
        self.message = "Invalid email address."

    def __str__(self):
        return self.message


class NoData(Error):
    def __init__(self):
        self.message = "login or password is invalid!"

    def __str__(self):
        return self.message


class NoAccess(Error):
    def __init__(self):
        self.message = "can't login, maybi server doesn't work!"

    def __str__(self):
        return self.message
