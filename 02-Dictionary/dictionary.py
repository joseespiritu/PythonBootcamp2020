import json

class Main():
    def __init__(self):
        super().__init__()
        self.data = json.load(open("data.json"))
        print(self.data["smog"])

if __name__ == '__main__':
    Main()