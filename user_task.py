



import polyma
import helloadd
import string_modifers


print("Hello, usesr welcome to Polynomial world".title())
print("how can i help you ??")
print("here are the some features i can done ")
print(" 1.  i can arrange polynomial in correct order  ".title())
print(" 2.  i can find coffecients, degrees, constants  and Terms of the Polynomial".title())
print(" 3.  i can say you highest degree of the Polynomial".title())
print(" 4.  i can evalute expression".title())
print(" 5.  i can add ,sub amd mutiply two polynomials".title())
print( "6.  i can substutie value in the Polynomial".title())
print(" 7.  i can tell you the zeroes of the Polynomial ".title())


try:
    run=True
    variable=""
    some=False
    while run:
        function = input(f"f(variable):  ")
        function_d=function[:]
        if function_d.startswith("-"):
            function_d=function_d.removeprefix("-")
        if function_d.isnumeric():
            some=True
            variable="x"
        function = string_modifers.String_tools().filter_out(function)
        if some==False:
            variable = string_modifers.String_tools().extract_symbol(function, "^", "+", "-")[0]
        k = int(input("what is your task :  "))
        cosmo = polyma.Polynomials().coffecients(function, variable)
        degreeo = polyma.Polynomials().degree(function, variable)
        constants = polyma.Polynomials().constants(function, variable,True)
        polyno_terms = polyma.Polynomials().poly_terms(function, variable)
        if k == 1:
            printd = polyma.Polynomials().print_poly(degreeo, cosmo, constants, variable)
            print(printd)
        elif k == 2:
            useri = int(input(" 1: coffecients 2: degree  3: constants 4: Terms "))
            if useri == 1:
                print(cosmo)
            elif useri == 2:
                print(degreeo)
            elif useri == 3:
                print(constants)
            elif useri == 4:
                print(polyno_terms)
            else:
                print("invallid data")
        elif k == 3:
            print(polyma.Polynomials().highest_degree(function, variable))
        elif k == 4:
            print(helloadd.add_poly(function, variable).add())
        elif k == 5:
            c = int(input("1: add ,2: sub ,3: multply "))
            first = input("input your First expression : ")
            second = input("input your second expression : ")
            new_obj = helloadd.add_poly(first, variable)
            if c == 1:
                print(new_obj.add_two_poly(second))
            elif c == 2:
                print(new_obj.sub_poly(second))
            elif c == 3:
                print(new_obj.mul_two_poly(second))
            else:
                print("your input is not vallid ")
                exit(new_obj)
        elif k == 6:
            user = int(input("input value to substutie : "))
            print(helloadd.add_poly(function, variable).substutie_value(user))
        elif k == 7:
            print(helloadd.add_poly(function, variable).find_zeroes_poly())
        else:
            print("improper input")
except Exception as e:
    print(e)
    print("Technical Issue contact xxxxxxxxxx")

else:
    print("----------------------------------Thank you--------------------------------------------------------Thank you------------------------------------------")







