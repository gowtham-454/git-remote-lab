def login(username, password):
    if username and password:
        return {"token": "jwt_token_here", "user": username}
    return None

def logout(token):
    return True
