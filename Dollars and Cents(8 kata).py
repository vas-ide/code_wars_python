def format_money(amount):
    # your formatting code here
    string = str(amount)
    if string[0] == '$':
        amount = float(string[1:])
        print(f'${float(amount)}')
        print("${0:.2f}".format(amount))
        return f'${float(amount)}'
    else:
        print(f'${float(amount)}')
        print("${0:.2f}".format(amount))
        return f'${float(amount)}'



format_money(39.99)
format_money(39.99)
format_money('$45.1')
format_money('$2')
format_money(2)
format_money('$3.00')