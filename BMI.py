#bmi.py
weight,height=eval(input("体重（公斤）,身高（米）"))
bmi=weight/pow(height, 2)
print("{:.3f}".format(bmi))
if bmi<=18.5:
    a,b="偏瘦","偏瘦"
elif 18.5<bmi<=24:
    a,b="正常","正常"
elif 24<bmi<=25:
    a,b='正常',"偏胖"
elif 25<bmi<=28:
    a,b='偏胖','偏胖'
elif 28<bmi<=30:
    a,b='偏胖','肥胖'
else:
    a,b='肥胖','肥胖'
print("国际BMI:{0},国内BMI:{1}".format(a,b))
