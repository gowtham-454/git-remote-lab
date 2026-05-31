def login(username, password):
    if not username or not password:
        return None
    if username and password:
        return {"token": "jwt_token_here", "user": username}
    return None

def logout(token):
    if not token:
        return False
    return True
