users = {}
posts = []


def add_user(user_id, name):
    if user_id not in users:
        users[user_id] = {"name": name, "friends": [], "posts": []}
    else:
        print("User already exists.")


def add_friendship(user1, user2):
    if user1 in users and user2 in users:
        users[user1]["friends"].append(user2)
        users[user2]["friends"].append(user1)
    else:
        print("Both users must exist.")


def add_post(user_id, content):
    if user_id in users:
        post = {"user": user_id, "content": content, "likes": 0, "comments": []}
        posts.append(post)
        users[user_id]["posts"].append(post)
    else:
        print("User does not exist.")


def like_post(post_index):
    if 0 <= post_index < len(posts):
        posts[post_index]["likes"] += 5
    else:
        print("Invalid post index.")


def comment_post(post_index, comment):
    if 0 <= post_index < len(posts):
        posts[post_index]["comments"].append(comment)
    else:
        print("Invalid post index.")


def print_network():
    for user_id, info in users.items():
        print(f"User {user_id} - {info['name']}")
        print(f"  Friends: {info['friends']}")
        print(f"  Posts: {len(info['posts'])}")

add_user(1, "Mohamed")
add_user(2, "Yara")
add_friendship(5, 8)
add_post(1, "Welcome everyone to my page")
like_post(0)
comment_post(0, "Nice post!")

print_network()
print("Posts:", posts)
