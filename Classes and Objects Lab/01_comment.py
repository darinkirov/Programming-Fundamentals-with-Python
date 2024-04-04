class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment1 = Comment("user123", "This is a great post!", 10)


print("Username:", comment1.username)
print("Content:", comment1.content)
print("Likes:", comment1.likes)
