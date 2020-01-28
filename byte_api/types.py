import json


class JsonDeserializable(object):
    @staticmethod
    def check_json(json_type):
        if type(json_type) == dict:
            return json_type
        elif type(json_type) == str:
            return json.loads(json_type)
        else:
            raise ValueError('json_type must be a json dict or string.')


class Error(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type: dict):
        obj = cls.check_json(json_type)
        code = obj['code']
        message = obj['message']
        return cls(code, message)

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


class Response(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type: dict):
        obj = cls.check_json(json_type)
        error = None
        data = None
        if 'error' in obj:
            error = Error.de_json(obj['error'])
        if 'data' in obj:
            data = obj['data']
        success = obj['success']
        return cls(success, data=data, error=error)

    def __init__(self, success: int, data=None, error=None):
        if data:
            self.data = data
        if error:
            self.error = error
        self.success = success


class Range(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type: dict):
        obj = cls.check_json(json_type)
        start = obj['start']
        stop = obj['stop']
        return cls(start, stop)

    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop


class Mention(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type: dict):
        obj = cls.check_json(json_type)
        account_id = obj['accountID']
        username = obj['username']
        text = obj['text']
        range = Range.de_json(obj['range'])
        byte_range = Range.de_json(obj['byteRange'])
        return cls(account_id, username, text, range, byte_range)

    def __init__(self, account_id: str, username: str,
                 text: str, range: Range, byte_range: Range):
        self.account_id = account_id
        self.username = username
        self.text = text
        self.range = range
        self.byte_range = byte_range


class Comment(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type: dict):
        obj = cls.check_json(json_type)
        id = obj['id']
        post_id = obj['postID']
        author_id = obj['authorID']
        body = obj['body']
        mentions = [
            Mention.de_json(mention) for mention in obj['mentions']
        ]
        date = obj['date']
        options = {}
        if 'accounts' in obj:
            options['accounts'] = {
                account: Account.de_json(obj['accounts'][account])
                for account in obj['accounts'].keys()
            }
        return cls(id, post_id, author_id, body, mentions, date, options)

    def __init__(self, id: str, post_id: str, author_id: str,
                 body: str, mentions: list, date: int, options: dict):
        self.id = id
        self.post_id = post_id
        self.author_id = author_id
        self.body = body
        self.mentions = mentions
        self.date = date
        for key in options:
            setattr(self, key, options[key])


class Post(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type: dict):
        obj = cls.check_json(json_type)
        id = obj['id']
        type = obj['type']
        author_id = obj['authorID']
        caption = obj['caption']
        allow_curation = obj['allowCuration']
        allow_remix = obj['allowRemix']
        mentions = [
            Mention.de_json(mention) for mention in obj['mentions']
        ]
        date = obj['date']
        video_src = obj['videoSrc']
        thumb_src = obj['thumbSrc']
        comment_count = obj['commentCount']
        like_count = obj['likeCount']
        liked_by_me = obj['likedByMe']
        loop_count = obj['loopCount']
        rebyted_by_me = obj['rebytedByMe']
        options = {}
        if 'category' in obj:
            options['category'] = obj['category']
        if 'comments' in obj:
            options['comments'] = [
                Comment.de_json(comment) for comment in obj['comments']
            ]
        return cls(id, type, author_id, caption,
                   allow_curation, allow_remix,
                   mentions, date, video_src, thumb_src,
                   comment_count, like_count, liked_by_me,
                   loop_count, rebyted_by_me, options)

    def __init__(self, id: str, type: int, author_id: str, caption: str,
                 allow_curation: bool, allow_remix: bool,
                 mentions: list, date: int, video_src: str, thumb_src: str,
                 comment_count: int, like_count: int, liked_by_me: bool,
                 loop_count: int, rebyted_by_me: bool, options: dict):
        self.id = id
        self.type = type
        self.author_id = author_id
        self.caption = caption
        self.allow_curation = allow_curation
        self.allow_remix = allow_remix
        self.mentions = mentions
        self.date = date
        self.video_src = video_src
        self.thumb_src = thumb_src
        self.comment_count = comment_count
        self.like_count = like_count
        self.liked_by_me = liked_by_me
        self.loop_count = loop_count
        self.rebyted_by_me = rebyted_by_me
        for key in options:
            setattr(self, key, options[key])


class Feed(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type: dict):
        obj = cls.check_json(json_type)
        posts = [
            Post.de_json(post) for post in obj['data']['posts']
        ]
        success = obj['success']
        options = {}
        if 'cursor' in obj['data']:
            options['cursor'] = obj['data']['cursor']
        if 'accounts' in obj['data']:
            options['accounts'] = {
                account: Account.de_json(obj['data']['accounts'][account])
                for account in obj['data']['accounts'].keys()
            }
        return Response(success, cls(posts, options))

    def __init__(self, posts: list, options: dict):
        self.posts = posts
        for key in options:
            setattr(self, key, options[key])


class Color(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type: dict):
        obj = cls.check_json(json_type)
        background = obj['background']
        foreground = obj['foreground']
        id = obj['id']
        return cls(background, foreground, id)

    def __init__(self, background: str, foreground: str, id: int):
        self.background = background
        self.foreground = foreground
        self.id = id


class Colors(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type: dict):
        obj = cls.check_json(json_type)
        colors = [
            Color.de_json(color) for color in obj['colors']
        ]
        return cls(colors)

    def __init__(self, colors: list):
        self.colors = colors


class Account(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type: dict):
        obj = cls.check_json(json_type)
        background_color = obj['backgroundColor']
        follower_count = obj['followerCount']
        following_count = obj['followingCount']
        foreground_color = obj['foregroundColor']
        id = obj['id']
        is_channel = obj['isChannel']
        loop_count = obj['loopCount']
        loops_consumed_count = obj['loopsConsumedCount']
        registration_date = obj['registrationDate']
        username = obj['username']
        options = {}
        if 'avatarURL' in obj:
            options['avatar_url'] = obj['avatarURL']
        if 'isDeactivated' in obj:
            options['is_deactivated'] = obj['isDeactivated']
        if 'isRegistered' in obj:
            options['is_registered'] = obj['isRegistered']
        if 'isBlocked' in obj:
            options['is_blocked'] = obj['isBlocked']
        if 'bio' in obj:
            options['bio'] = obj['bio']
        if 'isFollowing' in obj:
            options['is_following'] = obj['isFollowing']
        if 'isFollowed' in obj:
            options['is_followed'] = obj['isFollowed']
        if 'isSuspended' in obj:
            options['is_suspended'] = obj['isSuspended']
        if 'displayName' in obj:
            options['display_name'] = obj['displayName']
        return cls(background_color,
                   follower_count, following_count,
                   foreground_color, id, is_channel,
                   loop_count, loops_consumed_count,
                   registration_date, username, options)

    def __init__(self, background_color: str,
                 follower_count: int, following_count: int,
                 foreground_color: str, id: str, is_channel: bool,
                 loop_count: int, loops_consumed_count: int,
                 registration_date: int, username: str, options: dict):
        self.background_color = background_color
        self.follower_count = follower_count
        self.following_count = following_count
        self.foreground_color = foreground_color
        self.id = id
        self.is_channel = is_channel
        self.loop_count = loop_count
        self.loops_consumed_count = loops_consumed_count
        self.registration_date = registration_date
        self.username = username
        for key in options:
            setattr(self, key, options[key])


class LoopCounter(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type: dict):
        obj = cls.check_json(json_type)
        id = obj['postID']
        loop_count = obj['loopCount']
        return cls(id, loop_count)

    def __init__(self, id: str, loop_count: int):
        self.id = id
        self.loop_count = loop_count


class Rebyte(JsonDeserializable):
    @classmethod
    def de_json(cls, json_type: dict):
        obj = cls.check_json(json_type)
        accounts = {
            account: Account.de_json(obj['accounts'][account])
            for account in obj['accounts'].keys()
        }
        author_id = obj['authorID']
        date = obj['date']
        id = obj['id']
        post = Post.de_json(obj['post'])
        return cls(accounts, author_id, date, id, post)

    def __init__(self, accounts: dict, author_id: str,
                 date: int, id: str, post: Post):
        self.accounts = accounts
        self.author_id = author_id
        self.date = date
        self.id = id
        self.post = post
