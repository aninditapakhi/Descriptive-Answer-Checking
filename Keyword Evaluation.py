total=len(kw)
percentage=(c/total)*100
if(percentage>=90):
    print("Score:20/20")
elif(percentage>=80 or percentage<90):
    print("Score:18/20")
elif(percentage>=70 or percentage<80):
    print("Score:16/20")
elif(percentage>=60 or percentage<80):
    print("Score:14/20")
elif(percentage>=50 or percentage<60):
    print("Score:12/20")
else:
    print("Score:10/20")
