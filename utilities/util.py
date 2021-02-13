import json
import secrets

# Usage: Take entire trefle response and just slap it into json_trim.


def json_trim(response):
    targ_struct = response['data'][0]
    wanted_attributes = ['common_name','scientific_name','family_common_name','image_url']
    ret = dict()
    for val in targ_struct:
        if val in wanted_attributes:
            ret[val] = targ_struct[val]
    return ret


def test_trim():
    json_path = 'example_response.json'
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    print(json_trim(data))


def gen_hash():
    return secrets.token_urlsafe(16)

