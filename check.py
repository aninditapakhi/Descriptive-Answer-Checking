import language_check
tool=language_check.LanguageTool('en-US')
input=open("mp.txt","r")
count=0

text=str(input.read())
txtlen=len(text.split())
setxt = set(text.split())
setlen = len(setxt)
matches=tool.check(text)
#print("Error:",matches)
print("No. of Errors:",len(matches))
noOfError=len(matches)
if noOfError<=5:
    marks=10
elif noOfError<=10:
    marks=8
elif noOfError<=15:
    marks=5
else:
    marks=3
    
if setlen>(txtlen/2):
    marks+=10
else:
    marks+=5
print("Marks:",marks)
