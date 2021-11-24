




class String_tools:
    def __init__(self):
        pass
    def filter_out(self,string):
        j1=list(string)
        while " " in j1:
            j1.remove(" ")
        return "".join(j1)
    def append_numeric(self,string,symbol=None):
        string=self.filter_out(string)
        list_5 = list(string)
        ans = []
        k = ""
        l = 0

        for i in list_5:
            if i.isnumeric():
                k += i
                l = l + 1
                if l == len(list_5):
                    ans.append(k)
                    break
            else:
                l += 1
                ans.append(k)
                if i == symbol:
                    k = symbol
                else:
                    k = ""
                if k == "":
                    continue
        while "" in ans:
            ans.remove("")
        return ans
    def indices_str(self,symbol:str,string4:str):
        string3=self.filter_out(string4)
        list_w=list(string3)
        order=0
        list_ans=[]
        for i in list_w:
            if i==symbol:
                list_ans.append(order)
            order+=1
        return list_ans
    def multiple_replace(self,old_symb:str,new_symb:str,string1:str):
        string = self.filter_out(string1)
        list_1=list(string)
        while old_symb in list_1:
            list_1[int(list_1.index(old_symb))]=str(new_symb)
        return "".join(list_1)
    def string_changer(self,index,value,string2:str):
        string1 = self.filter_out(string2)
        list1=list(string1)
        for i in range(0, len(list(string1))):
            if i == index:
                list1[index] = value
        print("".join(list1))
    def multiple_str_changer(self,indexs:list,values:list,string:str):
        string = self.filter_out(string)
        list_9=list(string)
        for i in range(0,len(indexs)):
            list_9[int(indexs[i])]=str(values[i])
        x="".join(list_9)
        return x
    def no_beside_numeric(self,indexs:list,string_2:str):
        string_2 = self.filter_out(string_2)
        str_list=list(string_2)
        list_ans=[]
        for i in indexs:
            if i==0:
                list_ans.append(i)
                continue
            if not str_list[i - 1].isnumeric():
                list_ans.append(i)
        return list_ans
    def same_value_changer(self,indexes:list,value:str,string):
        string = self.filter_out(string)
        k=list(string)
        for i in indexes:
            k[int(i)]=str(value)
        return "".join(k)
    def poly_deg_modifer(self,string,variable="x"):
        k = self.indices_str("^", string)
        q = self.indices_str(variable, string)
        q = list(int(i) + 1 for i in q)
        list_str = list(self.filter_out(string))
        c = 0
        for i in q:
            if i not in k:
                list_str.insert(int(i + c), "^1")
                c += 1

        return "".join(list_str)
    def fd_no(self,index:int,string:str):
        list_e=[]
        val_str = self.poly_list(string, boolen=True)
        val_list = list(val_str)
        strg = "".join(val_list[index + 1:])
        val_list = self.poly_list(strg)
        return val_list[0]
    def bk_no(self,index,string):
        listw=[]
        val_str = self.poly_list(string, boolen=True)
        val_list = list(val_str)
        ind=index-len(val_list)
        strg = "".join(val_list[:ind])
        val_list = self.append_numeric(strg,"-")
        return val_list[-1]
    def power_up(self,variable,poly1):
        symbol="1"+variable
        str2 = self.poly_list(poly1,variable,symbol, boolen=True)
        n = self.indices_str("^", str2)
        k=self.indices_str(variable,str2)
        list_ind=[]
        if len(n)>len(k):
            for i in n:
                if i-1 in k:
                    continue
                else:
                    list_ind.append(int(i))
        list_vsl=[]
        list_sym=[]
        for i in list_ind:
            exp = self.fd_no(i, str2)
            cof = self.bk_no(i, str2)
            old = str(cof) + "^" + str(exp)
            new = str(int(cof) ** int(exp))
            list_sym.append(old)
            list_vsl.append(new)
        for i in range(len(list_sym)):
            str2=str2.replace(list_sym[i],list_vsl[i])
        return str2


    def poly_list(self,string:str,variable="x",symbol="1x",boolen=None):
        if len(string)>=1:
            if string[0].strip()=="+":
                string=string.removeprefix("+")
        string=self.filter_out(string)
        list_s=list(string)
        s_1=self.indices_str(variable,string)
        s_2=self.no_beside_numeric(s_1,string)
        s_3=self.same_value_changer(s_2,symbol,string)
        s_4=self.poly_deg_modifer(s_3,variable)
        s_5=self.append_numeric(s_4,"-")
        if boolen==True:
            return s_4
        else:
            return s_5
    def extract_symbol(self,string,*exc):
        strings=[]
        for i in string:
            if not i.isnumeric() and i not in exc:
                strings.append(i)
        return strings


class List_tools:
    def __init__(self,list_q):
        self.list_q=list_q
    def convert_int(self):
        return list(int(i) for i in self.list_q)

