# Adobe Connect
    Attend meetings, webinars, and virtual classrooms with Adobe Connect.
    View and participate, present content, and even fully host online meetings.


# Usage
## Reference Document: <a href="https://helpx.adobe.com/adobe-connect/webservices/topics.html"> Adobe Connect Api Doc </a>


```python
from AdobeConnect import AdobeConnect
AC = AdobeConnect(base_url='http://yourserver', admin_login="admin login", password="password")
```

## CreateUser (create_user)
    You can use this method to create a new user.
    After creating the user, returns an object that contains the created user information.

### parameters
<p><b>first_name</b>: user first name</p>
<p><b>last_name</b>: user last name</p>
<p><b>login</b>: The name with which the user can entered to Adobe Connect.</p>
<p><b>password</b>: this password will use for authentications.</p>
<p><b>email</b>: user email</p>
<p><b>custom_fields</b>: with this parameter you can set custom fields for any use.</p>
<p><b>user_type</b>: this parameter Specifies user type is the user.</p>
<p><b>send_email</b>: "true" or "false", if give "true", send an welcome eamil for new user.(default is false)</p>

### example
```python
>>> user = AC.create_user("first name", "last name", "username", "password", "email@email.com").user
>>> user.principal_id
>>> user.name
>>> user.login
```


## CreateMeeting (craete_meeting)
    To make a meeting, just specify a name and a brief description.
    Returns an object from the made meeting.

### parameters
<p><b>name</b>: user ID or group ID.</p>
<p><b>description</b>: write description for more information about the meeting.</p>
<p><b>lang</b>: default language for meetings is EN but you can change it.</p>
<p><b>date_begin</b>: Specifies when the meeting starts. Uses local time by default but you can change it.</p>
<p><b>date_end</b>: Specifies when the meeting is over. By default one week after the local time is set but you can change it.</p> 

### example
```python
>>> meeting = AC.create_meeting("meeting name", "this is desc", date_begin=date_begin, date_end=date_end).meeting
>>> meeting.meeting_id
>>> meeting.name
>>> meeting.sco_id
```


## SetMeetingAccess (set_meeting_access)
    You can specify user access to enter the room (host or view)

### parameters
<p><b>meeting_id</b>: The meeting ID you want to add the user to.</p>
<p><b>principal_id</b>: User or group ID you want to add to the meeting.</p>
<p><b>permission_id</b>: Access type 'host' or 'view'.</p>

### example
```python
>>> AC.set_meeting_access("meeting id", "principal id", permission_id="host")
```


## JoinMeeting (join_meeting)

### parameters
<p><b>meeting_id</b>: The meeting ID you want to remove from it.</p>
<p><b>login</b>: The name with which you can enter Adobe Connect.</p>
<p><b>password</b>: user password</p>

### example
```python
>>> # can join to the meeting with this link
>>> AC.join_meeting("meeting id", "username", "password")
```


## RemoveMeetingAccess (remove_meeting_access)
    If you want to block user access to the meeting, you can use this method.
    Returns a class whose status_code and response are accessible.

### parameters
<p><b>meeting_id</b>: The meeting ID you want to remove from it.</p>
<p><b>principal_id</b>:User or group ID you want remove from the meeting.</p>

### example
```python
AC.remove_meeting_access("meeting id", "principal id")
```


## DeletePrincipal (delete_principal)

### parameters
<p><b>principal_id</b>: user ID or Group ID</p>

### example
```python
AC.delete_principal("user id")
```


## DeleteSco (delete_sco)

### parameters
<p><b>sco_id</b>: sco id (meeting id is an sco id)</p>

### example
```python
AC.delete_sco("meeting id")
```
