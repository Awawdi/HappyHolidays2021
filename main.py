import string
from datetime import date
from pattern.text.en import superlative


class NewYear:
    name = list(string.ascii_uppercase[1:3])
    name.insert(1, 'M')
    Personal_development = True
    values = ["diversity", "inclusion", "equity"]
    Goal = "Autonomous Digital Enterprise"

    def greeting(self):
        print(f"From our {''.join(self.name)} family to yours",
              f"we wish you the {superlative('happy')} of holiday seasons",
              f"and the very best for {date.today().year + 1}!")


new_year = NewYear()
new_year.greeting()
