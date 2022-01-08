from .. import AdobeConnect
from names import get_first_name, get_last_name

base_url = "http://192.168.43.128"
login = "admin@gmail.com"
password = "12345678"

a = AdobeConnect(base_url, login, password)

meeting_name = get_first_name()

first_name = get_first_name()
last_name = get_last_name()
person1 = {
    "first_name": first_name,
    "last_name": last_name,
    "login": f"{first_name}{last_name}",
    "email": f"{first_name}{last_name}@gmail.com",
    "password": "12345678"
}

first_name = get_first_name()
last_name = get_last_name()
person2 = {
    "first_name": first_name,
    "last_name": last_name,
    "login": f"{first_name}{last_name}",
    "email": f"{first_name}{last_name}@gmail.com",
    "password": "12345678"
}

first_name = get_first_name()
last_name = get_last_name()

person3 = {
    "first_name": first_name,
    "last_name": last_name,
    "login": f"{first_name}{last_name}",
    "email": f"{first_name}{last_name}@gmail.com",
    "password": "12345678"
}


def test_create_user1():
    x = a.create_user(
        first_name=person1["first_name"],
        last_name=person1["last_name"],
        login=person1["login"],
        email=person1["email"],
        password=person1["password"]
    ).user
    assert x.name == f"{person1['first_name']} {person1['last_name']}"


def test_create_user2():
    x = a.create_user(
        first_name=person2["first_name"],
        last_name=person2["last_name"],
        login=person2["login"],
        email=person2["email"],
        password=person2["password"]
    ).user
    assert x.name == f"{person2['first_name']} {person2['last_name']}"


def test_create_user3():
    x = a.create_user(
        first_name=person3["first_name"],
        last_name=person3["last_name"],
        login=person3["login"],
        email=person3["email"],
        password=person3["password"]
    ).user
    assert x.name == f"{person3['first_name']} {person3['last_name']}"


def test_find_user():
    x = a.find_user(name=f"{person1['first_name']} {person1['last_name']}").user
    assert x.name == f"{person1['first_name']} {person1['last_name']}"


def test_user_list():
    x = a.users_list().users
    assert isinstance(x, list)


def test_create_meeting():
    x = a.create_meeting(name=meeting_name, description="testing").meeting
    assert x.name == meeting_name


def test_find_meeting():
    x = a.find_meeting(meeting_name=meeting_name).meeting
    assert x.name == meeting_name


def test_meetings_list():
    x = a.meetings_list().meetings
    assert isinstance(x, list)


def test_set_meeting_access1():
    x = a.set_meeting_access(
        meeting_id=a.find_meeting(meeting_name=meeting_name).meeting.meeting_id,
        principal_id=a.find_user(name=f"{person1['first_name']} {person1['last_name']}").user.user_id,
        permission_id="host"
    ).status_code
    assert x == "ok"


def test_set_meeting_access2():
    x = a.set_meeting_access(
        meeting_id=a.find_meeting(meeting_name=meeting_name).meeting.meeting_id,
        principal_id=a.find_user(name=f"{person2['first_name']} {person2['last_name']}").user.user_id,
        permission_id="host"
    ).status_code
    assert x == "ok"


def test_set_meeting_access3():
    x = a.set_meeting_access(
        meeting_id=a.find_meeting(meeting_name=meeting_name).meeting.meeting_id,
        principal_id=a.find_user(name=f"{person3['first_name']} {person3['last_name']}").user.user_id,
        permission_id="host"
    ).status_code
    assert x == "ok"


def test_remove_meeting_access():
    x = a.remove_meeting_access(
        meeting_id=a.find_meeting(meeting_name=meeting_name).meeting.meeting_id,
        principal_id=a.find_user(name=f"{person3['first_name']} {person3['last_name']}").user.user_id
    ).status_code
    assert x == "ok"
