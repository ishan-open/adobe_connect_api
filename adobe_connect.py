from requests import get
from urllib.parse import quote
from datetime import datetime, timedelta
import re
import json
import xmltodict
from .core.actions import Actions
from .utils import Url
from .exceptions.adobe_exceptions import *
from .response import (
    Base,
    FindPrincipalId,
    PrincipalsList,
    CreateUserResponse,
    CreateCustomField,
    GuestListResponse,
    GetPrincipalIdCurrentUser,
    FindSco,
    ScoShortcuts,
    Permissions,
    CreateMeeting,
    PollResults,
    MeetingUsage,
    CheckAccountPasscode,
    CustomFields,
    FindUserResponse,
    FindGroupResponse,
    UsersListResponse,
    GroupsListResponse,
    MeetingsListResponse,
    FindMeetingResponse,
    SetMeetingAccess,
)


class AdobeConnect:
    """
    create an instance from AdobeConnect,
    with create this is instance you can access to AdobeConnect webservices.

    Parameters
    ----------
        base_url : str
            server address of adobe connect. this create a base url for all queries.
        admin_login : str
            The name with which the admin enters Adobe Connect.
        password : str
            admin login password.

    Examples
    --------
    >>> from AdobeConnect import AdobeConnect
    >>> a = AdobeConnect("http://192.168.227.128", "admin@gmail.com", "Admin12345")
    """

    def __init__(
            self,
            base_url: str,
            admin_login: str,
            password: str
    ):
        """
        all the basic parameters that web service needs, will be made in here.

        Parameters
        ----------
            base_url : str
                server address of adobe connect. this create a base url for all queries.
            admin_login : str
                The name with which the admin enters Adobe Connect.
            password : str
                admin login password.
        """
        self.admin_login = admin_login
        self.password = password
        self.hostname = base_url
        self.base_url = f"{base_url}/api/xml?action="
        self.url_builder = Url(self.base_url)

    def get_login_cookies(self, login: str = None, password: str = None) -> dict:
        """
        In order for Adobe Connect to respond to our request, we need authentication session,
        which is stored as an access cookie to be sent with the request.
        Returns the Login Session Cookies.

        Parameters
        ----------
        login : str
            User Login in adobe connect.

        password : str
            User Password in adobe connect.

        Notes
        -----
        ====== it will returns 'cookies' ======

        Returns
        -------
        cookies
            dict

        """
        if not login:
            login = self.admin_login
        if not password:
            password = self.password
        url = self.base_url + Actions.login + f"&login={quote(login)}&password={quote(password)}"
        res = get(url)
        res.encoding = 'utf-8'
        content = json.loads(json.dumps(xmltodict.parse(res.content)))
        if content["results"]["status"]["@code"] == "no-access":
            raise NoAccess
        elif content["results"]["status"]["@code"] == "no-data":
            raise NoData
        cookies = res.cookies.get_dict()
        return cookies

    def login(self, user: str, password: str) -> dict:
        return self.url_builder.post_url(Actions.login + f"&login={user}&password={password}")

    def logout(self) -> dict:
        return self.url_builder.post_url(Actions.logout)

    def find_principal(
                self,
                name: str = None,
                login: str = None,
                email: str = None,
                filter_type: str = None
            ) -> FindPrincipalId:
        """
        With this function you can find a specific user or group and access its information.
        Returns an object.

        Parameters
        ----------
        name : str
            The name by which the user or group is known in Adobe Connect.(it's required)

        login : str, optional
            user can entered to Adobe Connect.
            for group this is similar with name.
            for be hundred percent sure of the result.(default is None)

        email : str, optional
            The user's email. for be hundred percent sure of the result.(default is None)

        filter_type : str, optional
            By sending this parameter, you specify that you are looking for a user or group.

        Notes
        -----
        ====== it will returns 'FindPrincipalId' ======

        Returns
        -------
        FindPrincipalId
            you can access to these attr's

        Examples
        --------
        >>> from AdobeConnect import AdobeConnect
        >>> a = AdobeConnect("http://192.168.227.128", "admin@gmail.com", "Admin12345")
        >>> principal = a.find_principal(name="ali reza", filter_type="user").principal
        >>> principal.type
        'user'
        >>> principal.name
        'ali reza'
        >>> principal.login
        'alireza@gmail.com'

        """
        parameters = {
            "filter-name": name,
            "filter-login": login,
            "filter-email": email,
            "filter-type": filter_type,
        }
        return FindPrincipalId(self.url_builder.get_url(Actions.principal_list, parameters, self.get_login_cookies()))

    def find_user(self, name: str = None, login: str = None, email: str = None) -> FindUserResponse:
        """
        Returns an object from the user That information you can access.

        Parameters
        ----------
        name : str
            The name by which the user is known in Adobe Connect.(it's required)

        login : str, optional
            The name with which the user can entered to Adobe Connect.
            for be hundred percent sure of the result.(default is None)

        email : str, optional
            The user's email. for be hundred percent sure of the result.(default is None)

        Notes
        -----
        ====== it will returns 'FindUserResponse' ======
        Returns
        -------
        FindUserResponse
            object, you can access to user's attrs.

        Examples
        --------
        >>> from AdobeConnect import AdobeConnect
        >>> a = AdobeConnect("http://192.168.227.128", "admin@gmail.com", "Admin12345")
        >>> a.find_user(name="amir abbasi").user.name

        """
        parameters = {
            "filter-name": name,
            "filter-login": login,
            "filter-email": email,
            "filter-type": "user",
        }
        return FindUserResponse(self.url_builder.get_url(Actions.principal_list, parameters, self.get_login_cookies()))

    def find_group(self, name: str, login: str = None) -> FindGroupResponse:
        """
        Returns an object from the group That information you can access.

        Parameters
        ----------
        name : str
            The name by which the user is known in Adobe Connect.(it's required)

        login : str, optional
            The same is the name of the group. for be hundred percent sure of the result.(default is None)

        Notes
        -----
        ====== it will returns 'FindGroupResponse' ======

        Returns
        -------
        FindGroupResponse
            object, you can access to group's attrs.
        """
        parameters = {
            "filter-name": name,
            "filter-login": login,
            "filter-type": "group",
        }
        return FindGroupResponse(self.url_builder.get_url(Actions.principal_list, parameters, self.get_login_cookies()))

    def users_list(
            self,
            filter_like_name: str = None,
    ) -> UsersListResponse:
        """
        Returns a list of users objects, you can iterate on it, and access on each object properties.

        Parameters
        ----------
        filter_like_name : str
            The name you want to find similars like that.(optional)

        Notes
        -----
        ====== it will returns 'UsersListResponse' ======

        Returns
        -------
        UsersListResponse
            list of users objects.
        """
        parameters = {
            "filter-type": "user",
            "filter-like-name": filter_like_name,
        }
        return UsersListResponse(self.url_builder.get_url(Actions.principal_list, parameters, self.get_login_cookies()))

    def groups_list(
            self,
            filter_like_name: str = None,
    ) -> GroupsListResponse:
        """
        Returns a list of group objects, you can iterate on it, and access on each object properties.

        Parameters
        ----------
        filter_like_name : str
            The name you want to find similars like that.(optional)

        Notes
        -----
        ====== it will returns 'GroupsListResponse' ======

        Returns
        -------
        GroupsListResponse
            list of groups objects.
        """
        parameters = {
            "filter-type": "group",
            "filter-like-name": filter_like_name,
        }
        return GroupsListResponse(self.url_builder.get_url(
            Actions.principal_list, parameters, self.get_login_cookies()
        ))

    def guests_list(self) -> GuestListResponse:
        """
        Returns a list of guest objects, you can iterate on it, and access on each object properties.

        Parameters
        ----------
        Takes no parameters.

        Notes
        -----
        ====== it will returns 'GuestListResponse' ======

        Returns
        -------
        GuestListResponse : list of guests objects
        """
        parameter = {
            "filter-type": "guest"
        }
        return GuestListResponse(self.url_builder.get_url(
            Actions.report_bulk_users, parameter, self.get_login_cookies()
        ))

    def current_user(self) -> GetPrincipalIdCurrentUser:
        """
        Returns some information about current user loged in.

        Parameters
        ----------
        Takes no parameters.

        Notes
        -----
        ====== it will returns 'GetPrincipalIdCurrentUser' ======

        Returns
        -------
        GetPrincipalIdCurrentUser
            object
        """
        return GetPrincipalIdCurrentUser(self.url_builder.get_url(Actions.common_info, {}, self.get_login_cookies()))

    def create_user(
            self,
            first_name: str,
            last_name: str,
            login: str,
            password: str,
            email: str,
            custom_fields: dict = {},
            user_type: str = "user",
            send_email: str = None,
    ) -> CreateUserResponse:
        """
        You can use this method to create a new user.
        After creating the user, returns an object that contains the created user information.

        Parameters
        ----------
        first_name : str

        last_name : str

        login : str
            The name with which the user can entered to Adobe Connect.

        password : str
            this password will use for authentications.

        email : str

        custom_fields : dict
            with this parameter you can set custom fields for any use.

        user_type : str
            this parameter Specifies user type is the user.

        send_email : "true" or "false", if give "true", send an welcome eamil for new user.(default is false)

        Notes
        -----
        ====== it will returns 'CreateUserResponse' ======

        Returns
        -------
        CreateUserResponse
            object, you can access to user's attrs.
        """
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise InvalidEmailAddress
        parameters = {
            "first-name": first_name,
            "last-name": last_name,
            "login": login,
            "password": password,
            "type": user_type,
            "send-email": send_email,
            "has-children": "0",
            "email": email
        }
        parameters.update(custom_fields)
        return CreateUserResponse(self.url_builder.post_url(
            Actions.principal_update, parameters, self.get_login_cookies()
        ))

    def update_user(
            self,
            user_id: str,
            login: str = None,
            first_name: str = None,
            last_name: str = None,
            password: str = None,
            email: str = None,
            user_type: str = None,
            send_email: str = None,
            custom_fields: dict = {},
    ) -> Base:
        """
        You can use this method to update a new user.
        After updating the user, returns a status code.
        will returns an object.

        Parameters
        ----------
        user_id : str
            The ID of the user whose information you want to change.

        login : str
            The name with which the user can entered to Adobe Connect.

        first_name : str

        last_name : str

        password : str
            this password will use for authentications.

        email : str

        user_type : str
            this parameter Specifies user type is the user.

        send_email : "true" or "false", if give "true", send an welcome eamil for new user.(default is false)

        custom_fields : dict
            with this parameter you can set custom fields for any use.

        Notes
        -----
        ====== it will returns 'Base' ======

        Returns
        -------
        Base
            this object provide status_code and response
        """
        parameters = {
            "principal-id": user_id,
            "first-name": first_name,
            "last-name": last_name,
            "login": login,
            "password": password,
            "type": user_type,
            "send-email": send_email,
            "has-children": "0",
            "email": email
        }
        parameters.update(custom_fields)
        return Base(self.url_builder.post_url(Actions.principal_update, parameters, self.get_login_cookies()))

    def add_group_member(
            self,
            group_id: str,
            principal_id: str,
    ) -> Base:
        """
        You can add a number of specific users to specific groups.
        You can even define a group as a member of another group.
        will returns an object.

        Parameters
        ----------
        group_id : str
            Specify the group to which you want to add a user or group.

        principal_id : str
            user ID or Group ID

        Notes
        -----
        ====== it will returns 'Base' ======

        Returns
        -------
        Base
            this object provide status_code and response
        """
        parameters = {
            "group-id": group_id,
            "principal-id": principal_id,
            "is-member": "true"
        }
        return Base(self.url_builder.post_url(Actions.group_membership_update, parameters, self.get_login_cookies()))

    def remove_group_member(
            self,
            group_id: str,
            principal_id: str,
    ) -> Base:
        """
        to remove user or group from an specified group.
        will returns an object.

        Parameters
        ----------
        group_id : str
            Specify the group to which you want to add a user or group.

        principal_id : str
            user ID or Group ID

        Notes
        -----
        ====== it will returns 'Base' ======

        Returns
        -------
        Base
            this object provide status_code and response
        """
        parameters = {
            "group-id": group_id,
            "principal-id": principal_id,
            "is-member": "false"
        }
        return Base(self.url_builder.post_url(Actions.group_membership_update, parameters, self.get_login_cookies()))

    def group_members(
            self,
            group_id: str,
            filter_name: str = None,
            filter_like_name: str = None,
    ) -> PrincipalsList:
        """
        Returns users or groups that are specified in the group as a list of objects

        Parameters
        ----------
        group_id : str

        filter_name : str
            If you are looking for a specific user, send this parameter.

        filter_like_name : str
            If you are looking for one or more users,
            you can see only users with the same name by sending this parameter.

        Notes
        -----
        ====== it will returns 'PrincipalsList' ======

        Returns
        -------
        PrincipalsList
            list of objects
        """
        parameters = {
            "group-id": group_id,
            "filter-is-member": "true",
            "filter-name": filter_name,
            "filter-like-name": filter_like_name,
        }
        return PrincipalsList(self.url_builder.get_url(Actions.principal_list, parameters, self.get_login_cookies()))

    def is_member(
            self,
            principal_id: str,
    ) -> PrincipalsList:
        """
        Returns a list of objects in which a particular user or a specific group is a member.

        Parameters
        ----------
        principal_id : str
            user ID or group ID.

        Notes
        -----
        ====== it will returns 'PrincipalsList' ======

        Returns
        -------
        PrincipalsList
            list of objects
        """
        parameters = {
            "principal-id": principal_id,
            "filter-is-member": "true",
        }
        return PrincipalsList(self.url_builder.get_url(Actions.principal_list, parameters, self.get_login_cookies()))

    def create_meeting(
            self,
            name: str,
            description: str,
            lang: str = "en",
            date_begin: datetime = None,
            date_end: datetime = None
    ) -> CreateMeeting:
        """
        To make a meeting, just specify a name and a brief description.
        Returns an object from the made meeting.

        Parameters
        ----------
        name : str
            user ID or group ID.

        description : str
            write description for more information about the meeting.
        lang : str
            default language for meetings is EN but you can change it.
        date_begin : datetime
            Specifies when the meeting starts. Uses local time by default but you can change it.
        date_end : datetime
            Specifies when the meeting is over. By default one week after the local time is set but you can change it.

        Notes
        -----
        ====== it will returns 'CreateMeeting' ======

        Returns
        -------
        CreateMeeting
            an object you can access it properties.
        """

        folder_id = ""
        for i in self.sco_shortcuts().shortcuts:
            if i.type == "meetings":
                folder_id = i.sco_id

        if date_begin is not None:
            date = date_begin
            hour = date.hour if date.hour > 9 else f"0{date.hour}"
            minute = date.minute if date.minute > 9 else f"0{date.minute}"
            date_begin = date_begin = f"{date.date()}T{hour}:{minute}"

        if date_end is not None:
            date = date_end
            hour = date.hour if date.hour > 9 else f"0{date.hour}"
            minute = date.minute if date.minute > 9 else f"0{date.minute}"
            date_end = f"{date.date()}T{hour}:{minute}"

        if date_begin is None:
            date = datetime.now()
            hour = date.hour if date.hour > 9 else f"0{date.hour}"
            minute = date.minute if date.minute > 9 else f"0{date.minute}"
            date_begin = date_begin = f"{date.date()}T{hour}:{minute}"

        if date_end is None:
            date2 = date + timedelta(minutes=120)
            hour = date2.hour if date2.hour > 9 else f"0{date2.hour}"
            minute = date2.minute if date2.minute > 9 else f"0{date2.minute}"
            date_end = f"{date.date()}T{hour}:{minute}"

        parameters = {
            "folder-id": folder_id,
            "description": description,
            "name": name,
            "type": "meeting",
            "lang": lang,
            "date-begin": date_begin,
            "date-end": date_end,
        }

        return CreateMeeting(self.url_builder.post_url(Actions.sco_update, parameters, self.get_login_cookies()))

    # permission id = host or view
    def set_meeting_access(self, meeting_id: str, principal_id: str, permission_id: str = "view") -> SetMeetingAccess:
        """
        You can specify user access to enter the room (host or view)

        Parameters
        ----------
        meeting_id : str
             The meeting ID you want to add the user to.
        principal_id : str
            User or group ID you want to add to the meeting.
        permission_id : str
            Access type 'host' or 'view'.

        Notes
        -----
        ====== it will returns 'SetMeetingAccess' ======

        Returns
        -------
        SetMeetingAccess
            this object provide return_code
        """
        parameters = {
            "acl-id": meeting_id,
            "principal-id": principal_id,
            "permission-id": permission_id
        }
        return SetMeetingAccess(self.url_builder.post_url(
            Actions.permissions_update, parameters, self.get_login_cookies()
        ))

    def remove_meeting_access(self, meeting_id: str, principal_id: str) -> SetMeetingAccess:
        """
        If you want to block user access to the meeting, you can use this method.
        Returns a class whose status_code and response are accessible.

        Parameters
        ----------
        meeting_id : str
             The meeting ID you want to remove from it.
        principal_id : str
            User or group ID you want remove from the meeting.

        Notes
        -----
        ====== it will returns 'SetMeetingAccess' ======

        Returns
        -------
        SetMeetingAccess
            this object provide return_code
        """
        parameters = {
            "acl-id": meeting_id,
            "principal-id": principal_id,
            "permission-id": "remove"
        }
        return SetMeetingAccess(self.url_builder.post_url(
            Actions.permissions_update, parameters, self.get_login_cookies()
        ))

    def set_meeting_multiple_access(self, muliples):
        results = []
        for i in muliples:
            if i["meeting_id"] and i["principal_id"] and i["permission_id"]:
                try:
                    x = self.set_meeting_access(i["meeting_id"], i["principal_id"], i["permission_id"])
                    if x.return_code == 'ok':
                        results.append({i["principal_id"]: x.return_code})
                except InvalidMeetingId:
                    results.append({i["principal_id"]: "InvalidMeetingID"})
                except InvalidPrincipalId:
                    results.append({i["principal_id"]: "InvalidPrincipalID"})
                except InvalidPermissionID:
                    results.append({i["principal_id"]: "InvalidPermissionID"})

        return results

    def remove_meeting_multiple_access(self, muliples):
        results = []
        for i in muliples:
            if i["meeting_id"] and i["principal_id"]:
                try:
                    x = self.remove_meeting_access(i["meeting_id"], i["principal_id"])
                    if x.return_code == 'ok':
                        results.append({i["principal_id"]: x.return_code})
                except InvalidMeetingId:
                    results.append({i["principal_id"]: "InvalidMeetingID"})
                except InvalidPrincipalId:
                    results.append({i["principal_id"]: "InvalidPrincipalID"})
                except InvalidPermissionID:
                    results.append({i["principal_id"]: "InvalidPermissionID"})
        return results

    def join_meeting(self, meeting_id: str, login: str, password: str) -> str:
        """
        Parameters
        ----------
        meeting_id : str
             The meeting ID you want to remove from it.
        login : str
            The name with which you can enter Adobe Connect.

        password : str

        Notes
        -----
        ====== it will returns 'join url' ======

        Returns
        -------
        str
            join url, can join to the meeting with this url.
        """
        return f"{self.hostname}/{self.find_meeting(meeting_id).meeting.url_path}" \
               f"?session={self.get_login_cookies(login, password)['BREEZESESSION']}"

    def sco_shortcuts(self) -> ScoShortcuts:
        return ScoShortcuts(self.url_builder.get_url(Actions.sco_shortcuts, {}, self.get_login_cookies()))

    def find_sco(
            self,
            sco_id: str,
            filter_name: str = None,
            filter_type: str = None,
            filter_like_name: str = None,
            filter_url_path: str = None,
            filter_gt_date=None,
            filter_lt_date=None,
    ) -> FindSco:
        parameters = {
            "sco-id": sco_id,
            "filter-name": filter_name,
            "filter-type": filter_type,
            "filter-url-path": filter_url_path,
            "filter-gt-date": filter_gt_date,
            "filter-lt-date": filter_lt_date,
            "filter-like-name": filter_like_name,
        }
        return FindSco(self.url_builder.get_url(Actions.sco_expanded_contents, parameters, self.get_login_cookies()))

    def meetings_list(self) -> MeetingsListResponse:
        """
        Returns a list of all meetings objects.

        Parameters
        ----------
        Takes no parameters

        Notes
        -----
        ====== it will returns 'MeetingsListResponse' ======

        Returns
        -------
        MeetingsListResponse
            list of all meetings objects.
        """
        for i in self.sco_shortcuts().shortcuts:
            if i.type == "meetings":
                return MeetingsListResponse(self.find_sco(sco_id=i.sco_id).response)

    def find_meeting(self, meeting_id: str = None, meeting_name: str = None) -> FindMeetingResponse:
        """
        Returns an object from a specific meeting.

        Parameters
        ----------
        meeting_id : str

        meeting_name : str
            You can find that meeting by using the name of the meeting.

        Notes
        -----
        ====== it will returns 'FindMeetingResponse' ======

        Returns
        -------
        FindMeetingResponse
            Returns an object from a specific meeting.
        """
        for i in self.meetings_list().meetings:
            if i.name == meeting_name or meeting_id == i.sco_id:
                return FindMeetingResponse(i.__dict__)
        raise NotFound

    def create_custom_field(
            self,
            object_type: str,
            account_id: str,
            name: str,
            comments: str,
            field_type: str = "text",
            is_required: str = "false",
            is_primary: str = "false",
            display_seq: str = "9"
    ) -> CreateCustomField:
        """
        Returns an object from a specific meeting.

        Parameters
        ----------
        object_type : str

        account_id : str

        name : str

        comments : str

        field_type : str
            It is better to "text".

        is_required : str
            "true" or "false"

        is_primary : str
            "true" or "false"

        display_seq : str
            By sending this parameter, you specify its location.(default is 9)

        Notes
        -----
        ====== it will returns 'CreateCustomField' ======

        Returns
        -------
        CreateCustomField
            Returns an object from created custom field.
        """
        parameters = {
            "object-type": object_type,
            "permission-id": "manage",
            "account-id": account_id,
            "name": name,
            "comments": comments,
            "field-type": field_type,
            "is-required": is_required,
            "is-primary": is_primary,
            "display-seq": display_seq
        }
        return CreateCustomField(self.url_builder.post_url(
            Actions.custom_field_update, parameters, self.get_login_cookies()
        ))

    def delete_custom_field(
            self,
            field_id: str,
            object_type: str,
    ) -> Base:
        """
        Returns an object from a specific meeting.

        Parameters
        ----------
        field_id : str
            The ID of field you want to delete.
        object_type : str
            The type of field you want to delete.

        Notes
        -----
        ====== it will returns 'Base' ======

        Returns
        -------
        Base
            this object provide status_code and response
        """
        parameters = {
            "field-id": field_id,
            "object-type": object_type
        }
        return Base(self.url_builder.post_url(Actions.custom_fields_delete, parameters, self.get_login_cookies()))

    def set_custom_field(
            self,
            acl_id: str,
            field_id: str,
            value: str
    ) -> Base:
        """
        Returns an object from a specific meeting.

        Parameters
        ----------
        acl_id : str
            The ID of object(user, group, meeting, sco) you want to set custom field on it.
        field_id : str
            The ID of field you want to set it.
        value : str
            The value to be assigned to the field.

        Notes
        -----
        ====== it will returns 'Base' ======

        Returns
        -------
        Base
            this object provide status_code and response
        """
        parameters = {
            "acl-id": acl_id,
            "field-id": field_id,
            "value": value
        }
        return Base(self.url_builder.get_url(Actions.acl_field_update, parameters, self.get_login_cookies()))

    def custom_fields_list(self) -> CustomFields:
        """
        Returns a list of custom field objects.

        Parameters
        ----------
        Takes no parameters

        Notes
        -----
        ====== it will returns 'CustomFields' ======

        Returns
        -------
        CustomFields
            list of custom field objects.
        """
        return CustomFields(self.url_builder.get_url(Actions.custom_fields, {}, self.get_login_cookies()))

    def download_link(self, url_path) -> str:
        """
        Returns an url for download file.

        Parameters
        ----------
        url_path : str

        Notes
        -----
        ====== it will returns 'download url' ======

        Returns
        -------
        str
            download link
        """
        return f"{self.hostname}/{url_path}/output/{url_path}zip?download=zip"

    def poll_results(self, sco_id: str) -> PollResults:
        return PollResults(self.url_builder.get_url(
            Actions.report_quiz_interactions, {"sco-id": sco_id}, self.get_login_cookies()
        ))

    def delete_sco(self, sco_id) -> Base:
        return Base(self.url_builder.get_url(Actions.sco_delete, {"sco-id": sco_id}, self.get_login_cookies()))

    def delete_principal(self, principal_id) -> Base:
        return Base(self.url_builder.get_url(
            Actions.principals_delete, {"principal-id": principal_id}, self.get_login_cookies()
        ))

    def meeting_usage(
            self,
            filter_sco_id: str = None,
            filter_principal_id: str = None,
            filter_gt_date_create: str = None,
            filter_gt_date: str = None,
            filter_lt_date: str = None,
    ) -> MeetingUsage:
        parameters = {
            "filter-type": "meeting",
            "filter-sco-id": filter_sco_id,
            "filter-principal-id": filter_principal_id,
            "filter-gt-date-create": filter_gt_date_create,
            "filter-gt-date": filter_gt_date,
            "filter-lt-date": filter_lt_date
        }
        return MeetingUsage(
            self.url_builder.get_url(
                Actions.report_bulk_consolidated_transactions,
                parameters,
                self.get_login_cookies())
        )

    def check_permissions(
            self,
            sco_id: str,
            principal_id: str = None,
    ) -> Permissions:
        parameters = {
            "acl-id": sco_id,
            "principal-id": principal_id
        }
        return Permissions(self.url_builder.get_url(Actions.permissions_info, parameters, self.get_login_cookies()))

    # Enable and disable the ability to passcode protect meeting rooms
    def set_account_passcode(self, account_id: str) -> Base:
        parameters = {
            "account-id": account_id,
            "feature-id": "id-meeting-passcode-notallowed",
            "enable": "false",
        }
        return Base(self.url_builder.post_url(Actions.meeting_feature_update, parameters, self.get_login_cookies()))

    def remove_account_passcode(self, account_id: str) -> Base:
        parameters = {
            "account-id": account_id,
            "feature-id": "id-meeting-passcode-notallowed",
            "enable": "true",
        }
        return Base(self.url_builder.post_url(Actions.meeting_feature_update, parameters, self.get_login_cookies()))

    def check_account_passcode(self, account_id: str) -> CheckAccountPasscode:
        parameters = {
            "account-id": account_id,
        }
        return CheckAccountPasscode(self.url_builder.get_url(
            Actions.meeting_feature_info, parameters, self.get_login_cookies()
        ))

    def meeting_passcode(self, sco_id: str, value: str) -> Base:
        parameters = {
            "acl-id": sco_id,
            "field-id": "meeting-passcode",
            "value": value,
        }
        return Base(self.url_builder.get_url(Actions.acl_field_update, parameters, self.get_login_cookies()))
