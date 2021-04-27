import re

#1 задание.
def validate_str(str_):
    car_number_pattern = r'(\w{1})(\d{3})(\w{2})(\d{2,3})'
    res = re.search(car_number_pattern, str_)
    if res != None:
        return f'Номер {res.group()[:-2]} валиден. Регион: {res.group(4)}.'
    return 'Номер не валиден'

#2 задание.
def del_repeats(str_):
    return re.sub(r'\b([^\W\d_]+)(\s+\1)+\b', r'\1', re.sub(r'\W+', ' ', str_).strip(), flags=re.I)

#3 задание
def acr(word):
    li = re.findall(r'\b(\w)', word)
    result = ''
    for i in li:
        result += i
    return result.upper()

#4 задание

emails = ['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com']

def email(li):
    pattern_email = r'\@\w+\.\w+'
    dict_ = {}
    for i in li:
        li1 = re.findall(pattern_email, i)
        for j in li1:
            dict_[j] = 1
    return dict_

print(email(emails))