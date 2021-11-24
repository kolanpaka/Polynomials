from string_modifers import *

'''hello world we are trying on new project called functions'''


class Polynomials:
    obj = String_tools()
    def __init__(self):
        pass

    def filter_poly(self,polynomial_a:str):
        obje1=String_tools()
        return obje1.poly_list(polynomial_a,boolen=True)
    def input_poly(self):
        degree=int(input("enter polynomial degree : "))
        list_coffecients=[]
        for i in range(degree+1):
            coffecient=int(input(f"enter your {i} degree coffecient : "))
            list_coffecients.insert(0,coffecient)
        return degree,list_coffecients
    def make_poly_dic(self,keys:int,values:list):
        dictn=dict(zip(range(keys,-1,-1),values))
        return dictn
    def make_dict(self,keys,values):
        dictn=dict(zip(keys,values))
        return dictn
    def print_poly(self,degree:list,coffecients:list,constants:list,variable:str):
        dict = self.make_dict(degree, coffecients)
        arrange_degree = sorted(degree, reverse=True)
        arrange_coff = list(dict[i] for i in arrange_degree)
        dict_poly=self.make_dict(arrange_degree,arrange_coff)
        if 0 in dict_poly.keys():
            v=dict_poly.pop(0)
            constants.append(v)
        poly_expr=""
        for d,c in dict_poly.items():
            if c!=0:
                if c==1:
                    c=""
                if dict_poly[d]<0:
                    poly_expr=poly_expr.removesuffix(" + ")
                    poly_expr+=" - "+str(abs(c))+variable+"^"+str(d)+" + "
                else:
                    poly_expr += str(c) + variable+"^" + str(d) + " + "
        poly_expr=poly_expr.removesuffix(" + ")
        if "1" + variable in poly_expr:
            poly_expr = poly_expr.replace("1" + variable, "x")
        poly_expr=poly_expr.removesuffix("^1")
        c1=str(sum(constants))
        if c1=="0":
            return poly_expr
        if not c1.startswith("-"):
            if poly_expr=="":
                return c1
            c1=" + "+c1
        else:
            c1=c1.removeprefix("-")
            c1=" - "+c1
        poly_expr=poly_expr+str(c1)
        return poly_expr
    def make_poly(self,degree:list,coffecients:list,constants:list):
        highest_degree=max(int(i) for i in degree)
    def degree(self,poly,variable,bool=None):
        variableyy="1"+variable
        val_str = Polynomials.obj.poly_list(poly,variable,variableyy, boolen=True)
        val_str=Polynomials.obj.power_up(variable,val_str)
        val_list =list(val_str)
        k=Polynomials.obj.indices_str("^",val_str)
        list_degree=[]
        for i in range(0,len(val_list)):
            if i in k:
                strg="".join(val_list[i+1:])
                list_e=Polynomials.obj.poly_list(strg)
                list_degree.append(list_e[0])
        if bool==True:
            return list_degree
        l1 = List_tools(list_degree)
        return l1.convert_int()
    def highest_degree(self,poly,variable):
        if self.degree(poly,variable):
            return max(self.degree(poly,variable))
        else:
            return 0
    def coffecients(self,poly,variable,bol=None):
        variablexx="1"+variable
        val_s=Polynomials.obj.poly_list(poly,variable,variablexx,boolen=True)
        val_l=list(val_s)
        index_x=Polynomials.obj.indices_str(variable,val_s)
        list_coff=[]
        for i in index_x:
            g=i-len(val_l)
            strg = "".join(val_s[:g])
            list_e = Polynomials.obj.poly_list(strg)
            list_coff.append(list_e[-1])
        if bol==True:
            return list_coff
        list_coff = List_tools(list_coff)
        return list_coff.convert_int()
    def constants(self,poly:str,variable,boolen=None):
        variableqq="1"+variable
        poly=Polynomials.obj.poly_list(poly,variable,variableqq,boolen=True)
        poly1=Polynomials.obj.power_up(variable,poly)
        Terms=self.poly_terms(poly1,variable)
        constant_list=[]
        for i in Terms:
            #if i[0]=="0":
                #continue
            if i.startswith("-") and i[1:].isdigit():
                constant_list.append(i)
            if i.isnumeric():
                constant_list.append(i)
        if boolen==True:
            constant_list=List_tools(constant_list)
            constant_list=constant_list.convert_int()
        return constant_list

    def poly_terms(self, f,variable):
        variableuu="1"+variable
        f=Polynomials.obj.poly_list(f,variable,variableuu,boolen=True)
        g=f[:]
        if g.startswith("-"):
            g=g.removeprefix("-")
        if f.count(variable) in [0,1] and f.count("+")==0 and g.count("-")==0 :
            return [f]
        x = Polynomials.obj.indices_str("+",f)
        y = Polynomials.obj.indices_str("-", f)
        z = sorted(x + y)
        if 0 in z:
            z.remove(0)
        ans = []
        k = 0
        j = 0
        for i in z:
            y = f[k:i]
            ans.append(y)
            k = z[j]
            j += 1
        if z:
            ans.append(f[z[len(z) - 1]:])
        ans = list(i.removeprefix("+") for i in ans)
        return ans


