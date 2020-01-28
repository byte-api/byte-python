import pytest
from byte_api.types import *


def test_json():
    json_type_dict = {
        'test': 123
    }
    assert JsonDeserializable.check_json(json_type_dict) == json_type_dict
    json_type_str = '{"test": 123}'
    assert JsonDeserializable.check_json(json_type_str) == json_type_dict
    with pytest.raises(ValueError):
        json_type_int = 123
        JsonDeserializable.check_json(json_type_int)


def test_error():
    data = {
        'code': 1,
        'message': 'test message'
    }
    error = Error.de_json(data)
    assert error.code == data['code']
    assert error.message == data['message']


def test_response():
    data = {
        'data': {'1': 2},
        'error': {
            'code': 1,
            'message': 'test message'
        },
        'success': 1
    }
    response = Response.de_json(data)
    assert response.data == data['data']
    assert type(response.error) == Error
    assert response.success == data['success']


def test_range():
    data = {
        'start': 0,
        'stop': 10
    }
    range = Range.de_json(data)
    assert range.start == data['start']
    assert range.stop == data['stop']


def test_mention():
    data = {
        'accountID': 'TEST',
        'username': 'bixnel',
        'text': '@bixnel',
        'range': {
            'start': 61,
            'stop': 75
        },
        'byteRange': {
            'start': 67,
            'stop': 81
        }
    }
    mention = Mention.de_json(data)
    assert mention.account_id == data['accountID']
    assert mention.username == data['username']
    assert mention.text == data['text']
    assert type(mention.range) == Range
    assert type(mention.byte_range) == Range


def test_account():
    data = {
        'backgroundColor': '#000000',
        'followerCount': 0,
        'followingCount': 0,
        'foregroundColor': '#CCD6E9',
        'id': 'test_id',
        'isChannel': False,
        'loopCount': 0,
        'loopsConsumedCount': 0,
        'registrationDate': 1580228662,
        'username': 'bixnel',
        'avatarURL': 'avatar/url',
        'isDeactivated': False,
        'isRegistered': True,
        'isBlocked': False,
        'bio': 'test bio',
        'isFollowing': False,
        'isFollowed': False,
        'isSuspended': False,
        'displayName': 'byte-api'
    }
    account = Account.de_json(data)
    assert account.background_color == data['backgroundColor']
    assert account.follower_count == data['followerCount']
    assert account.following_count == data['followingCount']
    assert account.foreground_color == data['foregroundColor']
    assert account.id == data['id']
    assert account.is_channel == data['isChannel']
    assert account.loop_count == data['loopCount']
    assert account.loops_consumed_count == data['loopsConsumedCount']
    assert account.registration_date == data['registrationDate']
    assert account.username == data['username']
    assert account.avatar_url == data['avatarURL']
    assert account.is_deactivated == data['isDeactivated']
    assert account.is_registered == data['isRegistered']
    assert account.is_blocked == data['isBlocked']
    assert account.bio == data['bio']
    assert account.is_following == data['isFollowing']
    assert account.is_followed == data['isFollowed']
    assert account.is_suspended == data['isSuspended']
    assert account.display_name == data['displayName']


def test_comment():
    data = {
        'id': 'TEST_ID',
        'postID': 'TEST_POST',
        'authorID': 'TEST_AUTHOR',
        'body': 'test test',
        'mentions': [],
        'date': 1580089742,
        'accounts': {
            'test_id': {
                'avatarURL': 'avatar/url',
                'backgroundColor': '#000000',
                'followerCount': 0,
                'followingCount': 0,
                'foregroundColor': '#CCD6E9',
                'id': 'test_id',
                'isBlocked': False,
                'isChannel': False,
                'isFollowed': False,
                'isFollowing': False,
                'loopCount': 0,
                'loopsConsumedCount': 0,
                'registrationDate': 1580228662,
                'username': 'bixnel'
            }
        }
    }
    comment = Comment.de_json(data)
    assert comment.id == data['id']
    assert comment.post_id == data['postID']
    assert comment.author_id == data['authorID']
    assert comment.body == data['body']
    assert comment.mentions == data['mentions']
    assert comment.date == data['date']
    assert type(comment.accounts) == dict
    assert type(comment.accounts['test_id']) == Account


def test_post():
    data = {
        'id': 'TEST',
        'type': 0,
        'authorID': 'TETS_AUTHOR',
        'caption': '',
        'allowCuration': True,
        'allowRemix': False,
        'category': 'wierd',
        'mentions': [
            {
                'accountID': 'TEST',
                'username': 'bixnel',
                'text': '@bixnel',
                'range': {
                    'start': 61,
                    'stop': 75
                },
                'byteRange': {
                    'start': 67,
                    'stop': 81
                }
            }
        ],
        'date': 1580089743,
        'videoSrc': 'TEST_VIDEO',
        'thumbSrc': 'TEST_THUMB',
        'commentCount': 0,
        'comments': [
            {
                'id': 'TEST_ID',
                'postID': 'TEST_POST',
                'authorID': 'TEST_AUTHOR',
                'body': 'test test',
                'mentions': [],
                'date': 1580089742,
                'accounts': {
                    'test_id': {
                        'avatarURL': 'avatar/url',
                        'backgroundColor': '#000000',
                        'followerCount': 0,
                        'followingCount': 0,
                        'foregroundColor': '#CCD6E9',
                        'id': 'test_id',
                        'isBlocked': False,
                        'isChannel': False,
                        'isFollowed': False,
                        'isFollowing': False,
                        'loopCount': 0,
                        'loopsConsumedCount': 0,
                        'registrationDate': 1580228662,
                        'username': 'bixnel'
                    }
                }
            }
        ],
        'likeCount': 0,
        'likedByMe': False,
        'loopCount': 0,
        'rebytedByMe': False
    }
    post = Post.de_json(data)
    assert post.id == data['id']
    assert post.type == data['type']
    assert post.author_id == data['authorID']
    assert post.caption == data['caption']
    assert post.allow_curation == data['allowCuration']
    assert post.allow_remix == data['allowRemix']
    assert post.category == data['category']
    assert all(type(mention) == Mention for mention in post.mentions)
    assert post.date == data['date']
    assert post.video_src == data['videoSrc']
    assert post.thumb_src == data['thumbSrc']
    assert post.comment_count == data['commentCount']
    assert all(type(comment) == Comment for comment in post.comments)
    assert post.like_count == data['likeCount']
    assert post.liked_by_me == data['likedByMe']
    assert post.loop_count == data['loopCount']
    assert post.rebyted_by_me == data['rebytedByMe']


def test_color():
    data = {
        'background': '#000000',
        'foreground': '#CCD6E9',
        'id': 1
    }
    color = Color.de_json(data)
    assert color.background == data['background']
    assert color.foreground == data['foreground']
    assert color.id == data['id']


def test_colors():
    data = {
        'colors': [
            {
                'background': '#000000',
                'foreground': '#CCD6E9',
                'id': 1
            },
            {
                "background": "#00B6B6",
                "foreground": "#E2E9FF",
                "id": 2
            }
        ]
    }
    colors = Colors.de_json(data)
    assert all(type(color) == Color for color in colors.colors)


def test_loop_counter():
    data = {
        'postID': 'test_id',
        'loopCount': 10
    }
    loop_counter = LoopCounter.de_json(data)
    assert loop_counter.id == data['postID']
    assert loop_counter.loop_count == data['loopCount']


def test_rebyte():
    data = {
        'accounts': {
            'test_id': {
                'backgroundColor': '#000000',
                'followerCount': 0,
                'followingCount': 0,
                'foregroundColor': '#CCD6E9',
                'id': 'test_id',
                'isChannel': False,
                'loopCount': 0,
                'loopsConsumedCount': 0,
                'registrationDate': 1580228662,
                'username': 'bixnel',
                'avatarURL': 'avatar/url',
                'isDeactivated': False,
                'isRegistered': True,
                'isBlocked': False,
                'bio': 'test bio',
                'isFollowing': False,
                'isFollowed': False,
                'isSuspended': False,
                'displayName': 'byte-api'
            }
        },
        'authorID': 'AUTHOR_ID',
        'date': 1580228662,
        'id': 'TEST_ID',
        'post': {
            'id': 'TEST',
            'type': 0,
            'authorID': 'TETS_AUTHOR',
            'caption': '',
            'allowCuration': True,
            'allowRemix': False,
            'category': 'wierd',
            'mentions': [
                {
                    'accountID': 'TEST',
                    'username': 'bixnel',
                    'text': '@bixnel',
                    'range': {
                        'start': 61,
                        'stop': 75
                    },
                    'byteRange': {
                        'start': 67,
                        'stop': 81
                    }
                }
            ],
            'date': 1580089743,
            'videoSrc': 'TEST_VIDEO',
            'thumbSrc': 'TEST_THUMB',
            'commentCount': 0,
            'comments': [
                {
                    'id': 'TEST_ID',
                    'postID': 'TEST_POST',
                    'authorID': 'TEST_AUTHOR',
                    'body': 'test test',
                    'mentions': [],
                    'date': 1580089742,
                    'accounts': {
                        'test_id': {
                            'avatarURL': 'avatar/url',
                            'backgroundColor': '#000000',
                            'followerCount': 0,
                            'followingCount': 0,
                            'foregroundColor': '#CCD6E9',
                            'id': 'test_id',
                            'isBlocked': False,
                            'isChannel': False,
                            'isFollowed': False,
                            'isFollowing': False,
                            'loopCount': 0,
                            'loopsConsumedCount': 0,
                            'registrationDate': 1580228662,
                            'username': 'bixnel'
                        }
                    }
                }
            ],
            'likeCount': 0,
            'likedByMe': False,
            'loopCount': 0,
            'rebytedByMe': False
        }
    }
    rebyte = Rebyte.de_json(data)
    assert all(type(rebyte.accounts[account]) == Account
               for account in rebyte.accounts.keys())
    assert rebyte.author_id == data['authorID']
    assert rebyte.date == data['date']
    assert rebyte.id == data['id']
    assert type(rebyte.post) == Post
