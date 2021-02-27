class ZeroDivision:
    def __init__(self, numeral, significant):
        self.numeral = numeral
        self.significant = significant

    @staticmethod
    def division(numeral, significant):
        try:
            return(numeral / significant)
        except:
            return('Zero Division!')

numbers = ZeroDivision.division(100, 0)
print(numbers)