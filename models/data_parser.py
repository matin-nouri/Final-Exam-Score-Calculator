import json


class JsonParser:
    def __init__(self, filename):
        self.data = None
        self.dt = None
        self.filename = filename

    def read(self):
        with open(f"data/{self.filename}.json", "r+") as file:
            self.data = file.read()
            file.close()
        self.dt = json.loads(self.data)
        return self.dt
