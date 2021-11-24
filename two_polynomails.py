

from string_modifers import String_tools
from polyma import *

class add_poly:
    def __init__(self,expression,variable):
        self.expression=expression
        self.variable=variable
    def add(self):
        our_equ=String_tools().power_up(self.variable,self.expression)
        constants_poly = Polynomials().constants(our_equ, self.variable, True)
        degree_eq = Polynomials().degree(our_equ, self.variable)
        coff_poly = Polynomials().coffecients(our_equ, self.variable)
        if our_equ.count(self.variable)==1:
            if Polynomials().coffecients(our_equ,self.variable,True)[0]+self.variable+"^0"==our_equ:
                return Polynomials().coffecients(our_equ,self.variable,True)[0]
            return Polynomials().print_poly(degree_eq,coff_poly,constants_poly,self.variable)
        Terms = Polynomials().poly_terms(our_equ, self.variable)
        degree_eq=sorted(degree_eq,reverse=True)
        j = []
        count = []
        for i in degree_eq:
            if i in j:
                continue
            count.append((i, degree_eq.count(i)))
            j.append(i)
        list2=list( self.variable+"^"+str(i[0]) for i in count )
        run=True
        k=-1
        ans=""
        while run:
            f=0
            cf=0
            if k+1== len(list2):
                break
            for i in Terms:
                if list2[k] in i and list2[k]==i[-len(list2[k]):]:
                    cf+=Polynomials().coffecients(i,self.variable)[0]
            if  not str(cf).startswith("-"):
                cf="+"+str(cf)
            ans+=str(cf)+list2[k]
            k+=1
        ans1=Polynomials().print_poly(Polynomials().degree(ans,self.variable),Polynomials().coffecients(ans,self.variable),constants_poly,self.variable)
        if ans1=="":
            return 0
        return ans1
    def add_two_poly(self,polynomial):
        if not polynomial.startswith("-") :
            total=self.expression+"+"+polynomial
        else:
            total = self.expression+polynomial
        return add_poly(total,self.variable).add()
    def sub_poly(self,polynomial2):
        if not polynomial2.startswith("-"):
            polynomial2="+"+polynomial2
        polyma=polynomial2[:]
        plus_sign=String_tools().indices_str("+",polynomial2)
        minus_sign=String_tools().indices_str("-",polyma)
        func=String_tools().same_value_changer(plus_sign,"-",polynomial2)
        func=String_tools().same_value_changer(minus_sign,"+",func)
        return add_poly(self.expression+func,self.variable).add()
    def mul_two_poly(self,anthor_expr):
        our_equ = String_tools().power_up(self.variable, self.expression)
        if our_equ.count(self.variable)>=1:
            our_equ=add_poly(our_equ,self.variable).add()
        constants_poly = Polynomials().constants(our_equ, self.variable, True)
        sum1=sum(constants_poly)
        degree_eq = Polynomials().degree(our_equ, self.variable)
        coff_poly = Polynomials().coffecients(our_equ, self.variable)
        our_equ2 = String_tools().power_up(self.variable,anthor_expr)
        if our_equ2.count(self.variable)>=1:
            our_equ2= add_poly(our_equ2, self.variable).add()
        constants_poly2 = Polynomials().constants(our_equ2, self.variable, True)
        sum2 = sum(constants_poly2)
        degree_eq2 = Polynomials().degree(our_equ2, self.variable)
        coff_poly2 = Polynomials().coffecients(our_equ2, self.variable)
        dict_self=Polynomials().make_dict(degree_eq,coff_poly)
        dic_other=Polynomials().make_dict(degree_eq2,coff_poly2)
        if sum1!=0:
            dict_self[0] = sum1
        if sum2!=0:
            dic_other[0] = sum2
        mul_degree=[]
        mul_coffecients=[]
        for degree1,coff1 in dict_self.items():
            for degree2,coff2 in dic_other.items():
                product=coff1*coff2
                mul_coffecients.append(product)
                sums_d=degree1+degree2
                mul_degree.append(sums_d)
        expr=""
        for i in range(len(mul_degree)):
            if not str(mul_coffecients[i]).startswith("-") and i!=0:
                mul_coffecients[i]="+"+str(mul_coffecients[i])
            expr+=str(mul_coffecients[i])+self.variable+"^"+str(mul_degree[i])
        mult_expresiion=add_poly(expr,self.variable).add()
        return mult_expresiion
    def substutie_value(self,term:int):
        valy=0
        expressadd=self.add()
        express=String_tools().poly_list(expressadd,self.variable,"1"+self.variable,True)
        constantx=Polynomials().constants(express,self.variable,True)
        coffecientx=Polynomials().coffecients(express,self.variable)
        degreex=Polynomials().degree(express,self.variable)
        dict_eval=Polynomials().make_dict(degreex,coffecientx)
        sumx=0
        for deg,cof in dict_eval.items():
            sumx+=cof*(term**deg)
        if constantx:
            valy=constantx[0]
        return sumx+valy
    def find_zeroes_poly(self):
        zeroes=[]
        degree=Polynomials().highest_degree(self.expression,self.variable)
        for i in range(0,1000*degree):
            k=self.substutie_value(i)
            l=self.substutie_value(int("-"+str(i)))
            if k==0:
                zeroes.append(i)
            if l==0:
                zeroes.append(int("-"+str(i)))
            if len(zeroes)==degree:
                break
        if len(zeroes)!=degree:
            print("I Tried so hard , to compute this problem but i found only this".title())
            print(f"I checked {1000*degree} negative and positive values".title())
        else:
            print(f"yahhhh! i found all the zeros of the polynomial {self.expression} ".title())
        return zeroes
