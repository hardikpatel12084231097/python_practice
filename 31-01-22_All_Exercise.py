#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#introduction of python
# history of python
# features of python
# application of python

# how to download python and install 
# how to download IDE  and use  -  ex first open cmd and write pip install jupyter notebook


# In[ ]:


# what is module. types of module and how to install external module  ex. pip install flask


# In[ ]:


# what is pip  pip is a package manager


# In[ ]:


#what is repl (read evaluate print loop) for ex in cmd 3+4 work as a calculator


# In[ ]:


# what is comment  - comment are used to (code are more readable)


# In[ ]:


types of comment 1. single line comment (#), 1. multiline comment ('''comment''')


# In[ ]:


# First Python Program Print Hello World!-------


# In[1]:


print("Hello World!")


# In[ ]:


# variable


# In[ ]:


# variable are container for store a value


# In[ ]:


# for ex. a=10    a is a variable and 10 is a value


# In[2]:


# Rules for define variable


# In[ ]:


# 1. variable are contain alphabets, digits and underscore.
# 2. variable name start only alphabet or underscore.
# 3. variable can't start with number.
# 4. in variable can not use white space or symbols.
# 5. variable name are case-sensitive


# In[3]:


# what is data types


# In[4]:


# data type means which types of data can be store in a variable...


# In[12]:



# list of data types in python...
# 1) number 
#     integer
#     float
#     complex number

# 2) sequence types
#     string
#     list
#     tuple
   
# 3) dictionary

# 4) set



# In[ ]:


# integer data types


# In[13]:


# positive value or negative value in integer


# In[14]:


a=10


# In[15]:


print(a)


# In[16]:


a=-10


# In[17]:


a


# In[18]:


# type() function is used to find a data type


# In[19]:


a=20


# In[20]:


type(a)


# In[22]:


print(a,type(a))


# In[23]:


a=10.5   #float data type 


# In[24]:


print(a, type(a))


# In[25]:


a=10+5j


# In[26]:


print(type(a))


# In[27]:


print(a.real)


# In[28]:


print(a.imag)


# In[29]:


print(a.conjugate())


# In[30]:


a="31"


# In[31]:


a


# In[32]:


print(a,type(a))


# In[33]:


# type casting


# In[34]:


# convert a one datatype into another datatype


# In[37]:


a=int('10')


# In[38]:


type(a)


# In[42]:


a=str(10)


# In[43]:


a


# In[44]:


type(a)


# In[47]:


a=float(40)


# In[48]:


type(a)


# In[58]:


c1=int('10')


# In[ ]:


b1=int('20')


# In[1]:


a=input()


# In[2]:


a=input("Enter first name:-")


# In[3]:


type(a)


# In[2]:


a=int(input("enter first number:-"))
b=int(input("enter second number:-"))
sum=a+b
print(sum)


# In[3]:


print(type(sum))


# In[10]:


# there are main two types of data type


# In[11]:


# 1) mutable - you can add , delete, update element   ex list, dictionary


# In[13]:


# 2)  immutable - can not change element ex integer, float, complex number, string, tuple, set


# In[14]:


# string data type


# In[16]:


# string is sequence of character and inclosed in a quotes


# In[17]:


a='hello' # single quote


# In[18]:


a


# In[19]:


a="hello" # double quote


# In[20]:


a


# In[21]:


a='''Python Lists - W3Schoolshttps://www.w3schools.com › python › python_lists
Lists are used to store multiple items in a single variable. Lists are one of
4 built-in data types in Python used to store collections of data, the other 3 are ...'''  # triple quote use in multiline string


# In[23]:


a


# In[24]:


# string slicing   - get a range of character


# In[25]:


# using index  [0,1,2,3,4---- -1,-2,-3-----]


# In[26]:


a="Hello"


# In[27]:


a


# In[28]:


print(a[1])


# In[31]:


print(a[-5])


# In[34]:


print(a[1:])


# In[36]:


print(a[:-3])


# In[37]:


print(a[:4])


# In[38]:


a


# In[39]:


print(a[0:5:2])


# In[40]:


print(a[::-1])


# In[52]:


print(a[0:5:2])


# In[53]:


# string function


# In[54]:


a="Hello World"


# In[55]:


a


# In[56]:


print(len(a))        # find the length of string


# In[57]:


a.count('Hello')    # returns number of times   character,word


# In[58]:


a.count('W')


# In[59]:


print(a.count('o'))


# In[65]:


print("original string :-",a)
print("uppercase:-",a.upper())
print("lowercase",a.lower())
print("capitalize:-",a.capitalize())
print("title", a.title())
print(a.swapcase())


# In[67]:


print("original string:-",a)


# In[68]:


print(a.isupper())


# In[70]:


print(a.islower())


# In[71]:


print(a.isalpha())


# In[72]:


print(a.isalnum())


# In[73]:


print(a.isdigit())


# In[74]:


a


# In[75]:


print(a.center(50))


# In[76]:


print(a.find('W'))


# In[77]:


print(a.replace('World','Python'))


# In[78]:


a="             hello         "


# In[79]:


a


# In[80]:


print(a.strip())


# In[84]:


a='@hello   kk@'


# In[85]:


a


# In[86]:


print(a.strip('@'))


# In[87]:


a='Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other'


# In[88]:


a


# In[89]:


a.partition('single')


# In[90]:


a='hello python how are you'


# In[91]:


a


# In[93]:


a.split(" ")


# In[94]:


s=a.split('python')


# In[95]:


s


# In[96]:


"PHP".join(s)


# In[ ]:


# string concatenate


# In[97]:


a='hello'


# In[98]:


b='python'


# In[100]:


print(a+" "+b)


# In[110]:


a="\tLists are used to store multiple items in a\ single variable.\n Lists are one of 4 built-in data types in"


# In[111]:


print(a)


# In[113]:


print(a.index('List'))


# In[115]:


print(a.translate('store'))


# In[116]:


# list


# In[117]:


# list is a mutable data type, [], store multiple value in a single variable,list are defined items in as ordered, duplicate value are allowed...


# In[121]:


l1=['hello','python',10,10.5,10]


# In[123]:


print(l1)


# In[122]:


type(l1)


# In[124]:


print(l1[1])


# In[125]:


print(l1[-1])


# In[126]:


print(l1[0:3])


# In[128]:


print(l1[-4:-1])


# In[129]:


print(len(l1))


# In[130]:


l1


# In[132]:


l1[2]=200


# In[133]:


print(l1)


# In[135]:


l1.append("300")


# # 

# In[136]:


l1


# In[137]:


l1.insert(1,"PHP")


# In[138]:


l1


# In[139]:


l1.remove("PHP")


# In[140]:


l1


# In[141]:


l1.pop()


# In[142]:


l1


# In[143]:


l1.pop(5)


# In[144]:


l1


# In[146]:


l1=[10,20,30,40]


# In[147]:


l1


# In[148]:


l1.insert(1,50)


# In[149]:


l1


# In[150]:


l1.sort()


# In[151]:


l1


# In[152]:


l1.sort(reverse=True)


# In[153]:


l1


# In[154]:


l1


# In[155]:


l1.reverse()


# In[156]:


l1


# In[158]:


l2=[50,'hardik',40]


# In[159]:


l2


# In[160]:


l1.extend(l2)


# In[161]:


l1


# In[162]:


l2.clear()


# In[163]:


l2


# In[164]:


l1


# In[165]:


l3=l1.copy()


# In[166]:


l3


# In[167]:


l3.index('hardik')


# In[168]:


l1.count(40)


# In[169]:


# tuple   - tuple is a immutable datatype, (), tuple element defined in a order, duplicate value allowed.


# In[182]:


t1=('hello',10,20,50,"python",10)


# In[183]:


t1


# In[184]:


type(t1)


# In[185]:


t1[1]


# In[186]:


t1[4]


# In[187]:


t1[0:4]


# In[188]:


t1.index(10)


# In[189]:


t1.index(50)


# In[190]:


t1.count(20)


# In[191]:


t1.count(60)


# In[192]:


t1


# In[193]:


t1.count(10)


# In[194]:


# dictionary


# In[195]:


# dictionary is a muttable data type   means changed, {}, duplicate value not allowed


# In[196]:


d1={
    'name':'hardik',
    'age':34
}


# In[197]:


type(d1)


# In[198]:


d1['name']="sonu"


# In[199]:


d1


# In[200]:


d1['address']='vadnagar'


# In[201]:


d1


# In[202]:


d1['age']


# In[203]:


d1.get('name')


# In[204]:


d1.keys()


# In[205]:


d1.values()


# In[206]:


d1.items()


# In[207]:


d1['age']


# In[208]:


d1.get('name')


# In[209]:


d1['education']="BCA"


# In[210]:


d1


# In[211]:


d1.setdefault("course","python")


# In[212]:


d1


# In[213]:


d1['course']="PHP"


# In[214]:


d1


# In[217]:


d1.update({'course':'python'})


# In[218]:


d1


# In[219]:


print(dir(dict))


# In[220]:


d2=d1.copy()


# In[221]:


print(d2)


# In[222]:


d2.clear()


# In[223]:


d2


# In[224]:


d1


# In[225]:


print(d1)


# In[226]:


d1.popitem()


# In[227]:


print(d1)


# In[228]:


d1.pop('age')


# In[229]:


d1


# In[230]:


print(len(d1))


# In[232]:


d1.setdefault("course_name","PHP")


# In[233]:


d1


# In[234]:


print(len(d1))


# In[235]:


d1['course_name']


# In[237]:


d1.get('education')


# In[238]:


print(d1)


# In[239]:


d1['name']='hardik'


# In[240]:


d1


# In[241]:


print(d1)


# In[242]:


d1.update({'address':'sipor'})


# In[243]:


print(d1)


# In[244]:


d1['color']="red"


# In[245]:


print(d1)


# In[247]:


fruits={
    'name':'mango',
    'price':30
}


# In[248]:


fruits


# In[249]:


fruits.clear()


# In[250]:


fruits


# In[251]:


d1


# In[252]:


d2=d1.copy()


# In[253]:


print(d2)


# In[254]:


d1.get('name')


# In[255]:


d1.pop('address')


# In[256]:


d1


# In[258]:


d1.popitem()


# In[259]:


d1['color']="green"


# In[260]:


d1


# In[261]:


d1.setdefault("result","pass")


# In[262]:


d1


# In[263]:


d1.update({'resulr':'fail'})


# In[264]:


d1


# In[265]:


# set


# In[266]:


s1={'hello','java',10}


# In[267]:


s1


# In[268]:


type(s1)


# In[269]:


s1.add('php')


# In[270]:


s1


# In[271]:


s1.add(10)


# In[272]:


s1


# In[273]:


print(len(s1))


# In[276]:


print(dir(set))


# In[10]:


s2={'hello',10,20,10.5}


# In[11]:


print(s2)


# In[13]:


s2.pop()


# In[14]:


s2


# In[277]:


s1.pop()


# In[278]:


s1


# In[279]:


s1.add(50)


# In[280]:


s1


# In[281]:


s1.add(20)


# In[282]:


s1


# In[283]:


s1.pop()


# In[284]:


s1


# In[286]:


s1.pop()


# In[287]:


s1.remove('php')


# In[288]:


s1


# In[289]:


s1.add(80)


# In[290]:


s1


# In[291]:


s1.discard(20)


# In[292]:


s1


# In[293]:


s1.clear()


# In[294]:


s1


# In[295]:


s1={30,40,60,'hello'}


# In[296]:


s1


# In[298]:


len(s1)


# In[299]:


s1.add(100)


# In[300]:


s1


# In[301]:


s1.remove(30)


# In[302]:


s1


# In[304]:


s1.discard(60)


# In[305]:


s1


# In[308]:


s1={10,30,60,70}      #in intersection return common record
s2={30,50,60,10,80}


# In[309]:


s1.intersection(s2)


# In[310]:


s1.union(s2)


# In[311]:


s1.difference(s2)


# In[312]:


s2.difference(s1)


# In[315]:


s1={'hello','python',10,20,10}


# In[316]:


s1


# In[317]:


type(s1)


# In[318]:


s1.add(70)


# In[319]:


s1


# In[320]:


s1.remove(20)


# In[321]:


s1


# In[322]:


s1.discard(10)


# In[323]:


s1


# In[324]:


s2=s1.copy()


# In[325]:


s2


# In[326]:


s1


# In[327]:


len(s1)


# In[328]:


s2.clear()


# In[329]:


s2


# In[330]:


s1={10,20,40,50}
s2={30,10,50}


# In[331]:


s1.intersection(s2)


# In[332]:


s1.union(s2)


# In[335]:


s1.difference(s2)


# In[336]:


s2.difference(s1)


# In[337]:


# operator


# In[338]:


# an operator are used to operate a value


# In[339]:


# operator are used to perform operation on variable and values


# In[340]:


# 1) arithmetic operator (+,-,*,/,%,//,**)


# In[341]:


a=10


# In[342]:


b=30


# In[343]:


sum=a+b


# In[344]:


sum


# In[345]:


a="hello"


# In[346]:


b="python"


# In[349]:


sum=a+ " "+b


# In[350]:


sum


# In[351]:


# subtraction


# In[352]:


a=10


# In[353]:


b=5


# In[354]:


sub=a-b


# In[355]:


sub


# In[356]:


mul=10*5


# In[357]:


mul


# In[358]:


div=10/4


# In[359]:


div


# In[360]:


10%5


# In[361]:


11%2


# In[362]:


10/5


# In[363]:


10//2


# In[364]:


10//5


# In[365]:


2**3


# In[17]:


a='*'


# In[18]:


a*10


# In[ ]:





# In[366]:


# assignment operator


# In[367]:


a=10


# In[368]:


print(a)


# In[369]:


a+=10


# In[370]:


a


# In[371]:


a-=10


# In[372]:


a


# In[373]:


a*=10


# In[374]:


a


# In[376]:


a=5


# In[378]:


a*10


# In[379]:


a='*'


# In[380]:


a*10


# In[381]:


# comparison oerator


# In[384]:


10>9


# In[385]:


10<8


# In[386]:


10==10


# In[387]:


10==0


# In[388]:


10>=5


# In[389]:


10<=4


# In[390]:


10!=10


# In[391]:


10!=8


# In[392]:


# logical operator


# In[393]:


# and


# In[395]:


10>3 and 5<9 and 10==10


# In[396]:


'hello',10,1,0


# In[398]:


10 and 1 and 'hello'


# In[399]:


0 and 'hi'


# In[400]:


20 and 30 and False and " "


# In[401]:


10 and "" and 20


# In[19]:


10 and [] and False


# In[ ]:




