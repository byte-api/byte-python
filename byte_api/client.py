from .api import Api
from .types import *


class Client(object):
    """
    Initializes the API for the client

    :param token: Authorization token
    :type token: str

    :param headers: Additional headers **except Authorization**
    :type headers: dict
    """

    def __init__(self, token: str, headers=None):
        """
        Initializes the API for the client

        :param token: Authorization token
        :type token: str
        """
        self.api = Api(token, headers)

    def follow(self, id: str) -> Response:
        """
        Subscribes to a user

        :param id: User id
        :type id: str


        :rtype: :class:`Response`
        """
        response = self.api.put('account/id/{}/follow'.format(id))
        return Response.de_json(response)

    def unfollow(self, id: str) -> Response:
        """
        Unsubscribes to a user

        :param id: User id
        :type id: str


        :rtype: :class:`Response`
        """
        response = self.api.delete('account/id/{}/follow'.format(id))
        return Response.de_json(response)

    def get_user(self, id: str) -> Response:
        """
        Gets a user profile

        :param id: User id
        :type id: str


        :rtype: :class:`Response`, :class:`Account`
        """
        response = self.api.get('account/id/{}'.format(id))
        response = Response.de_json(response)
        data = None
        error = None
        if hasattr(response, 'data'):
            data = Account.de_json(response.data)
        if hasattr(response, 'error'):
            error = Error.de_json(response.error)
        return Response(response.success, data=data, error=error)

    def like(self, id: str) -> Response:
        """
        Likes a byte

        :param id: Byte (post) id
        :type id: str


        :rtype: :class:`Response`
        """
        response = self.api.put('post/id/{}/feedback/like'.format(id))
        return Response.de_json(response)

    def dislike(self, id: str) -> Response:
        """
        Removes like from a byte

        :param id: Byte (post) id
        :type id: str


        :rtype: :class:`Response`
        """
        response = self.api.delete('post/id/{}/feedback/like'.format(id))
        return Response.de_json(response)

    def comment(self, id: str, text: str) -> Response:
        """
        Comments a byte

        :param id: Byte (post) id
        :type id: str

        :param text: Comment text
        :type id: str


        :rtype: :class:`Response`, :class:`Comment`
        """
        response = self.api.post('post/id/{}/feedback/comment'.format(id),
                                 json_data={
                                     'postID': id,
                                     'body': text
                                 })
        response = Response.de_json(response)
        data = None
        error = None
        if hasattr(response, 'data'):
            data = Comment.de_json(response.data)
        if hasattr(response, 'error'):
            error = Error.de_json(response.error)
        return Response(response.success, data=data, error=error)

    def delete_comment(self, id: str) -> Response:
        """
        Deletes a comment

        :param id: Comment id patterned by **{post id}-{comment id}**
        :type id: str


        :rtype: :class:`Response`
        """
        response = self.api.post('feedback/comment/id/{}'.format(id),
                                 json_data={
                                     'commentID': id
                                 })
        response = Response.de_json(response)
        return Response.de_json(response)

    def loop(self, id: str) -> Response:
        """
        Increments loop counter

        :param id: Byte (post) id
        :type id: str


        :rtype: :class:`Response`
        """
        response = self.api.post('post/id/{}/loop'.format(id))
        response = Response.de_json(response)
        data = None
        error = None
        if hasattr(response, 'data'):
            data = LoopCounter.de_json(response.data)
        if hasattr(response, 'error'):
            error = Error.de_json(response.error)
        return Response(response.success, data=data, error=error)

    def rebyte(self, id: str) -> Response:
        """
        Increments loop counter

        :param id: Byte (post) id
        :type id: str


        :rtype: :class:`Response`
        """
        response = self.api.post('rebyte',
                                 json_data={
                                     'postID': id
                                 })
        response = Response.de_json(response)
        data = None
        error = None
        if hasattr(response, 'data'):
            data = Rebyte.de_json(response.data)
        if hasattr(response, 'error'):
            error = response.error
        return Response(response.success, data=data, error=error)

    def get_colors(self) -> Response:
        """
        Gets available color schemes


        :rtype: :class:`Response`
        """
        response = self.api.get('account/me/colors')
        response = Response.de_json(response)
        data = None
        error = None
        if hasattr(response, 'data'):
            data = Colors.de_json(response.data)
        if hasattr(response, 'error'):
            error = response.error
        return Response(response.success, data=data, error=error)

    def set_info(self, bio: str = None, display_name: str = None,
                 username: str = None, color_scheme: int = None) -> Response:
        """
        Sets profile info

        :param bio: New bio
        :type bio: str

        :param display_name: New name to display
        :type display_name: str

        :param username: New username
        :type username: str

        :param color_scheme: Id of new color scheme
        :type color_scheme: int


        :rtype: :class:`Response`
        """
        data = {}
        if bio:
            data['bio'] = bio
        if display_name:
            data['displayName'] = display_name
        if username:
            data['username'] = username
        if color_scheme:
            data['colorScheme'] = color_scheme
        response = self.api.put('account/me',
                                data=data)
        return Response.de_json(response)

    def set_username(self, username: str) -> Response:
        """
        Sets username

        :param username: New username
        :type username: str


        :rtype: :class:`Response`
        """
        return self.set_info(username=username)

    def set_bio(self, bio: str) -> Response:
        """
        Sets bio

        :param bio: New bio
        :type bio: str


        :rtype: :class:`Response`
        """
        return self.set_info(bio=bio)

    def set_display_name(self, display_name: str) -> Response:
        """
        Sets name to display

        :param display_name: New name to display
        :type display_name: str


        :rtype: :class:`Response`
        """
        return self.set_info(display_name=display_name)

    def set_color_scheme(self, color_scheme: int) -> Response:
        """
        Sets color scheme

        :param color_scheme: Id of new color scheme
        :type color_scheme: str


        :rtype: :class:`Response`
        """
        return self.set_info(color_scheme=color_scheme)
