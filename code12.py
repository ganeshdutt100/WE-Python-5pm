# a  =  ["a", "b" ,  "c"]
# 
# student  = {
#       "name" : "abc", 
#        "age" :  23,
#        "course" :  "Python" 
# } 
# 
# menu =  {
#     "Burger":50,
#     "Chowmein": 60,
#     "Momos": 90
# }
# print(menu["Chowmein"])

# order  =   "Momos"
# print("order : " ,  order)
# print("Bill  :  ", menu["Momos"])
# a =  [1,2,3,4,5,6]

# for i  in menu:
#     print(i)
# menu["Momos"]
# for item in menu:
#     print(item , " : " , menu[item])

# keys  , item
# value 
# student["name"] =  "rahul"
# student.pop("age")
# 
# print(student)


# crud  
# create  ,read   , update  , delete 

# key , value  
# name  : Ganesh Dutt
# aValue  =  ["name" , "a" ,  "age" , 25]
# 
# report_card  = {
#     "Math":95,
#     "Eng": 80,
#     "Hindi":65,
#     "Science": 87 
# }

# print(report_card) 
# total  =  0
# for subject in report_card:
#     marks  =  report_card[subject]
#     print(subject ,  " : ",marks  )
#     total  = total + marks
# print( "totalMarks :  " ,   total)    
# 
# # gm  
# # gn 
# 
# # gm    = 

# slang_dct  =  {
#     "gm":"Good mornig",
#     "gn":"Good night",
#     "pls":"Please",
#     "np":"No Problem ",
# 
# }
# 
# user_word  =  input("Enter your word [gm  ,  gn ,  pls , np]")
# 
# if user_word  in slang_dct:
#     means =  slang_dct[user_word ]
#     print(means)
# else:
#     print("sorry ")    

password_vault={
    "Instagram" : "Insta@123",
    "Netflix":"Net@123",
    "Gmail":"G@123"

}


print("original password  :  " , password_vault )
password_vault["Instagram"] =  "kuchbhi"
print(password_vault["Instagram"])
password_vault.pop("Netflix")
print(password_vault)