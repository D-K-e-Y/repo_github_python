class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

if __name__ != '':
    my_list = []

    while True:
        user_input = input("__For Exit enter 'Q'__\nEnter your data: ")

        if user_input == "Q":
            break

        try:
            if not user_input.isdigit():
                raise NotNumberError(f"'{user_input}' has not numerical format!")

            my_list.append(int(user_input))

        except:
            print(NotNumberError)

    print(my_list)
###test