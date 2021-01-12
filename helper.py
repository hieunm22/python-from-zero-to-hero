import re
import base64
import json
import time
from time import time
import hashlib
import hmac

def hmacsha256(key_b64, to_sign):
    key = base64.b64decode(key_b64)
    signed_hmac_sha256 = hmac.HMAC(key, to_sign.encode(), hashlib.sha256)
    digest = signed_hmac_sha256.digest()
    return base64.b64encode(digest).decode()

def normalized_encode_string(str):
  normalized = str.replace('_', '/').replace('-', '+')
  len_str = len(normalized) % 4
  if len_str == 2:
    normalized += "=="
  if len_str == 3:
    normalized += "="
  return normalized  

def base64_decode(base64_message):
  try:
    normalized = normalized_encode_string(base64_message) 
    return base64.b64decode(normalized)
  except:
    return 'error'

def validate_token(token):
  match = re.search('^([a-zA-Z0-9\-_]+)?\.([a-zA-Z0-9\-_]+)?\.([a-zA-Z0-9\-_]+)?$', token)
  if match is not None:
    decode_header = base64_decode(match.group(1))
    decode_claims = base64_decode(match.group(2))
    # print(decode_claims)
    # print(match.group(1))
    # print(match.group(2))
    claims = json.loads(decode_claims)
    sign = hmacsha256(match.group(0) + "." + match.group(1), "my_secret_key")
    # print('sign_calc  =', sign)
    # print('sign_token =', match.group(3))
    exp_int = int(claims['exp'])
  return {
    "isValid": exp_int > time() and sign == match.group(3),
    "claims": claims
  }