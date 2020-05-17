#*********************
#python imports
#*********************
import datetime
#*********************
#vendor imports
#*********************
import jwt

def generate_user_token(param_user_id,param_algo,param_secret_key,param_timeout):
    """
    generate unique token for a user
    """
    payload={}
    payload["exp"] = datetime.datetime.utcnow()+datetime.timedelta(
        days=0,seconds=param_timeout
    )
    payload["iat"] = datetime.datetime.utcnow()
    payload["sub"] = param_user_id
    token=jwt.encode(
        payload,param_secret_key,
        algorithm=param_algo
    )
    return token.decode('utf-8')

def verify_user_token(token,param_secret_key):
    """
    verify a token validity and expiration for a user
    """
    try:
        payload = jwt.decode(token, param_secret_key)
        return payload
    except jwt.ExpiredSignatureError:
        return ("expired_token")
    except jwt.InvalidTokenError:
        return ("invalid_token")