def make_name(first, last, middle=''):
    if middle:
        really_name = f"{first} {middle} {last}"
    else:
        really_name = f"{first} {last}"
    return really_name.title()

class collect_info:
    def __init__(self):
        self.answers = []

    def collect(self, answer):
        self.answers.append(answer)

    def show(self):
        print("Collect results:")
        for answer in self.answers:
            print(f"- {answer.title()}")
