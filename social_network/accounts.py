class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        self.posts.append(post)
        post.set_user(self)

    def get_timeline(self):
        result = []
        for user in self.following:
            for post in user.posts:
                result.append(post)
        return result
        
        
    def follow(self, other):
        self.following.append(other)
