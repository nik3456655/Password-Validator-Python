print(f"{'Валидатор пароля':-^40}")
while True:
    porol=input("Придумайте надежный пароль! ")
    has_digit=False
    has_upper=False
    has_lower=False
    has_spec=False

    for char in porol:
        if char.isdigit():
            has_digit=True
        if char.isupper():
            has_upper=True
        if char.islower():
            has_lower=True
        if not char.isalnum():
            has_spec=True

    if len(porol) < 8:
        print("Пароль слишком короткий! Нужна длина от 8 символов.\n")
        print("-"*40)
    elif not has_digit:
        print("Пароль ненадежный: добавьте хотя бы одну цифру!\n")  
        print("-"*40)
    elif not has_upper:
        print("Пароль ненадежный: добавьте хотя бы одну заглавную букву!\n")
        print("-"*40)
    elif not has_lower:
        print("Пароль ненадежный: добавьте хотя бы одну строчную букву!\n")
        print("-"*40)
    elif not has_spec:
            print("Пароль ненадежный: добавьте хотя бы один спецсимвол (!, @, #, $, % и т.д.)!\n")
            print("-"*40)
    else:
        print(f"Отлично! Пароль '{porol}' принят — он действительно надежный!")
        break
print("-"*40)