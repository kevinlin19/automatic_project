class Check_Number:
    def __init__(self, number):
        self.number = number

    def is_phone_number_wore(self):
        number = str(self.number)
        if len(number) != 12:
            return False
        for i in range(4):
            if not number[i].isdecimal():
                return False
        if number[4] != '-':
            return False
        for i in range(5, 8):
            if not number[i].isdecimal():
                return False
        if number[8] != '-':
            return False
        for i in range(9, 12):
            if not number[i].isdecimal():
                return False

        return True

    def print_ans(self):
        if self.is_phone_number_wore():
            print(self.number + ' is cellphone number.')
        else:
            print(self.number + ' is not cellphone number.')


Check_Number('0255-554-242').print_ans()