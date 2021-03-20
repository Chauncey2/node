from explore import FrozenJson
import json

JSON = './data/osconfeed.json'


def load_json(path):
    with open(path, 'r') as fr:
        content = json.loads(fr.read())
    return content


if __name__ == '__main__':
    json_content = load_json(path=JSON)
    grad = FrozenJson(json_content)
    print(len(grad.Schedule.speakers))
