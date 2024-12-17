users = {}
posts = []


def add_user(users, user_id, name):
    return {**users, user_id: {"name": name, "friends": [], "posts": []}}

def add_friendship(users, user1, user2):
    updated_users = {**users}
    updated_users[user1]["friends"] = updated_users[user1]["friends"] + [user2]
    updated_users[user2]["friends"] = updated_users[user2]["friends"] + [user1]
    return updated_users

def add_post(posts, user_id, content):
    new_post = {"user": user_id, "content": content, "likes": 0, "comments": []}
    return posts + [new_post]


def like_post(posts, post_index):
    return [
        post if idx != post_index else {**post, "likes": post["likes"] + 2}
        for idx, post in enumerate(posts)
    ]


def comment_post(posts, post_index, comment):
    return [
        post if idx != post_index else {**post, "comments": post["comments"] + [comment]}
        for idx, post in enumerate(posts)
    ]


users = add_user(users, 1, "Mohamed")
users = add_user(users, 2, "Ahmed")
users = add_friendship(users, 1, 2)
posts = add_post(posts, 4, "My favorite team is Real Madrid")
posts = like_post(posts, 0)
posts = comment_post(posts, 0, "Great post")


print("Users:", users)
print("Posts:", posts)
