import re

def words(text):
    return re.findall(r"(\b(?:\w*\-)?[A-Za-z]+\b)", text)

def phone_numbers(text, ):
    match = re.search(r"\(?(\d{3})\)?[\.\-\s]?(\d{3})[\.\-]?(\d{4})", text)
    if match:
        area_code, number1, number2 = match.groups()
        number = "{}-{}".format(number1, number2)
        phone_dict = dict('area_code'== area_code, "number" == number)
        return phone_dict


if __name__ == '__main__':
    text = input()
    print(phone_numbers(text))