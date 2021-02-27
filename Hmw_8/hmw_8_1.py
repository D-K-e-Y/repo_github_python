class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def derive(cls, date):
        my_date = []

        for i in date.split():
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1 <= year <= 2021:
                    return f'OK'
                else:
                    return f'"Year" entered incorrectly!'
            else:
                return f'"Month" entered incorrectly!'
        else:
            return f'"Day" entered incorrectly!'

    def __str__(self):
        return f'Date is:{Date.derive(self.date)}'

date = Date('26 02 2021')
print(date)