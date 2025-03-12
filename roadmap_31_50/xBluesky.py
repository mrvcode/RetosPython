from datetime import datetime


class SocialNetwork:

    def __init__(self):
        self.post_id = 0  # Cambié "post" a "post_id" para inicializar el contador
        self.users = {}
        self.post = {}

    def register_user(self, user_id: str, name: str):

        if user_id in self.users:
            print(f"El usuario con ID {user_id} ya existe en la red social.")
            return

        self.users[user_id] = {
            "name": name,
            "following": set(),
            "followers": set(),
            "post": [],
        }

        print(
            f"El usuario con nombre '{name}' [ID: {user_id}] ha sido registrado en la red social."
        )

    def follow_user(self, user_id: str, follow_id: str):

        if user_id not in self.users or follow_id not in self.users:
            print("Al menos uno de los usuarios no existe en la red social.")
            return

        self.users[user_id]["following"].add(follow_id)
        self.users[follow_id]["followers"].add(user_id)
        print(f"{self.users[user_id]['name']} sigue a {self.users[follow_id]['name']}")

    def unfollow_user(self, user_id: str, unfollow_id: str):
        if user_id not in self.users or unfollow_id not in self.users:
            print("No existe el usuario. No se puede realizar la acción.")
            return

        self.users[user_id]["following"].discard(unfollow_id)
        self.users[unfollow_id]["followers"].discard(user_id)
        print(
            f"{self.users[user_id]['name']} dejó de seguir a {self.users[unfollow_id]['name']}"
        )

    def create_post(self, user_id: str, text: str):

        if user_id not in self.users:
            print(f"El usuario '{user_id}' no existe en la red social.")
            return

        if len(text) > 200:  # Corregido "let" a "len"
            print("El texto del post debe tener menos de 200 caracteres.")
            return

        self.post_id += 1

        post_id = self.post_id

        self.post[post_id] = {
            "user_id": user_id,
            "text": text,
            "create_at": datetime.now(),
            "likes": set(),
        }

        self.users[user_id]["post"].append(post_id)

        print("Post creado correctamente")

    def delete_post(self, post_id: int):

        if post_id not in self.post:
            print("El post no existe.")
            return

        user_id = self.post[post_id]["user_id"]
        self.users[user_id]["post"].remove(post_id)
        del self.post[post_id]
        print("Post eliminado correctamente.")

    def like_post(self, user_id: str, post_id: int):

        if user_id not in self.users:
            print(f"El usuario '{user_id}' no existe en la red social.")
            return
        if post_id not in self.post:
            print(
                f"El post '{post_id}' no existe en la red social."
            )  # Corregido user_id por post_id
            return

        self.post[post_id]["likes"].add(user_id)
        print(f"Nuevo like en post '{post_id}'.")

    def unlike_post(self, user_id: str, post_id: int):

        if user_id not in self.users:
            print(f"El usuario '{user_id}' no existe en la red social.")
            return
        if post_id not in self.post:
            print(
                f"El post '{post_id}' no existe en la red social."
            )  # Corregido user_id por post_id
            return

        self.post[post_id]["likes"].discard(user_id)
        print(f"Like eliminado en post '{post_id}'.")

    def view_user_feed(self, user_id: str):

        if user_id not in self.users:
            print(f"El usuario '{user_id}' no existe en la red social.")
            return

        feed = sorted(
            (self.post[post_id] for post_id in self.users[user_id]["post"]),
            key=lambda x: x["create_at"],
            reverse=True,
        )[:10]

        for post in feed:
            print(
                f"""
ID usuario: {post["user_id"]}
Usuario: {self.users[post["user_id"]]["name"]}  
Texto: {post["text"]}
Fecha: {post["create_at"]}
Likes: {len(post["likes"])}
                    """
            )

    def view_following_feed(self, user_id: str):

        if user_id not in self.users:
            print(f"El usuario '{user_id}' no existe en la red social.")
            return

        following_post_ids = (
            []
        )  # Cambié el nombre a "following_post_ids" (sin 's' adicional)

        for following_id in self.users[user_id]["following"]:
            following_post_ids.extend(
                self.users[following_id]["post"]
            )  # Corregido para usar la variable following_id

        feed = sorted(
            (self.post[post_id] for post_id in following_post_ids),
            key=lambda x: x["create_at"],
            reverse=True,
        )[:10]

        for post in feed:
            print(
                f"""
ID usuario: {post["user_id"]}
Usuario: {self.users[post["user_id"]]["name"]} 
Texto: {post["text"]}
Fecha: {post["create_at"]}
Likes: {len(post["likes"])}
                    """
            )


social_network = SocialNetwork()

social_network.register_user("mrvcode", "Miguel RV")
social_network.register_user("mouredev", "Brais Moure")

social_network.create_post("mrvcode", "¡Hola, mundo!")
social_network.create_post("mrvcode", "¡Hola, mundo!2")
social_network.create_post("mrvcode", "¡Hola, mundo!3")

social_network.create_post("mouredev", "¡Hola, planeta!")
social_network.create_post("mouredev", "¡Hola, planeta!2")
social_network.create_post("mouredev", "¡Hola, planeta!3")


social_network.follow_user("mouredev", "mrvcode")

social_network.like_post("mouredev", 1)

social_network.view_user_feed("mouredev")
social_network.view_following_feed("mouredev")
