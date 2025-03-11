import envTwitch
import requests


def get_access_token(cliente_id: str, client_secret: str) -> str:
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": cliente_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json().get("access_token")


def get_user_inf(token: str, client_id: str, login: str):
    url = "https://api.twitch.tv/helix/users"
    headers = {"Authorization": f"Bearer {token}", "Client-Id": client_id}
    params = {"login": login}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json().get("data", None)
    if not data:
        return None
    return data[0]


def get_total_followers(token: str, client_id: str, id: str) -> int:
    url = "https://api.twitch.tv/helix/channels/followers"
    headers = {"Authorization": f"Bearer {token}", "Client-Id": client_id}
    params = {"broadcaster_id": id}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json().get("total", 0)


CLIENT_ID = envTwitch.CLIENT_ID
CLIENT_SECRET = envTwitch.CLIENT_SECRET

users = ["rubius", "miguelrubivi", "thegrefg"]
users_data = []
not_found_users = []

token = get_access_token(CLIENT_ID, CLIENT_SECRET)

for username in users:
    user = get_user_inf(token, CLIENT_ID, username)
    if user is None:
        not_found_users.append(username)
    else:
        followers = get_total_followers(token, CLIENT_ID, user["id"])
        users_data.append(
            {
                "username": username,
                "created_at": user["created_at"],
                "followers": followers,
            }
        )

sort_by_followers = sorted(users_data, key=lambda x: x["followers"], reverse=True)
sort_by_date = sorted(users_data, key=lambda x: x["created_at"])

print("Ranking por numero de seguidores:")
for (
    id,
    user,
) in enumerate(sort_by_followers):
    print(f"{id + 1} - {user["username"]}: {user["followers"]} seguidores")

print("Ranking por antigüedad:")
for (
    id,
    user,
) in enumerate(sort_by_date):
    print(f"{id + 1} - {user["username"]}: Creado el {user["created_at"]}")

if not_found_users:
    print("Usuarios no encontrados:")
    for user in not_found_users:
        print(user)
