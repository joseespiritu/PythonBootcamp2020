import json

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("You have enter wrong word, please check!")


class Main:
    def __init__(self):
        super().__init__()

        self.word = input("Enter the  word you want to search: ")
        self.output = translate(self.word)
        if type(self.output) == list:
            for item in self.output:
                print(item)
        else:
            print(self.output)


if __name__ == '__main__':
    Main()
