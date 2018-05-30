import json

class strutil(object):

    @staticmethod
    def is_json(myjson):
        try:
            json_object = json.loads(myjson)
        except ValueError:
            return False
        return True