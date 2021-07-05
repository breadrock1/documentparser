from typing import Dict, Any

from Main.Parser.Objects.Object import Object


class Influence(Object):
    def __init__(self,
                 likes: int,
                 posts: int,
                 reposts: int,
                 accounts: int,
                 followers: int):

        super().__init__()

        self.likes = likes
        self.posts = posts
        self.reposts = reposts
        self.accounts = accounts
        self.followers = followers

    def getObject(self) -> Dict[str, Any]:
        return {
            'likes': self.likes,
            'posts': self.posts,
            'reposts': self.reposts,
            'accounts': self.accounts,
            'followers': self.followers
        }
