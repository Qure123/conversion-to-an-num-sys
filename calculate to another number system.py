def is_valid(c):
    while True:
        if c.isdigit():
            return c
        else:
            c = input('Введите именно число!!:\n')
            continue
def calculate(in_b,num,fin_b):
    if fin_b == '10':
        result = 0
        for c in range(len(num)):
            if num[c].isdigit():
                result += int(num[c]) * int(in_b)**(len(num) -1 -c)
            else:
                result += (-55 + ord(num[c]))  * int(in_b)**(len(num) -1 -c)
        return result
    else:
        result = ''
        if not num.isdigit():
            for c in range(len(num)):
                if num[c].isalpha():
                    num = num[:c] + (ord(num[c]) - 65) + num[c+1:]
        while int(num) >= int(fin_b):
            a = divmod(int(num),int(fin_b)) #divmode(103,8) = (12,7)
            result += str(a[1]) if a[1] < 10 else chr(55+a[1])
            num = a[0]
        result += str(num)
        return result[::-1]
init_basis = is_valid(input('Введите первоначальную систему счисления, из которой вы хотите перевести ваше число (числом!!): \n'))
number = input('Введите ваше число:\n')
finit_basis = is_valid(input('Введите систему счисления, в которую вы хотите перевести ваше число (числом!!):\n'))
print(f'Ваше число в {finit_basis}-чной системе: {calculate(init_basis, number, finit_basis)}')