import pandas as pd

df = pd.read_csv(r'/attendance-dashboard/rithik.csv',
                 names=['reg_no.', 'name', 'time', 'date', 'attendance'])
# print(df.head(1))
# class1=df.loc[df.time >="15:00:00"]
# class2=df.loc[df.time >="11:00:00"]
web = df[(df["time"] >= "11:00:00") & (df["time"] <= "12:00:00")]
daa = df[(df["time"] >= "15:00:00") & (df["time"] <= "16:00:00")]
# print(class2)

classes = [web, daa]
class1 = input('enter the subject')
if class1 == 'web':
    print(web)
elif class1 == 'daa':
    print(daa)
else:
    print("enter the subject")
classes = [web, daa]
name1 = str(input('enter the name'))
if name1 == name1:
    print(web[web['name'] == name1])
elif name1 == name1:
    print(daa[daa['name'] == name1])
else:
    print("enter the correct name")
hello = web[web['name'] == name1]
print(hello.count())
