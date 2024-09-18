#학과 정보 입력 및 저장
major=input("학과명:")
stu_num=int(input("학생 수:"))
professor=input("담당 교수:")
year=int(input("학과 설립 연도:"))

majorinfo={'학과명':major,'학생수':stu_num,'담당교수':professor,'설립 연도':year}

#학생 정보 입력 및 저장
all_info=[]

for i in range(5):
    print(i+1,'번째 학생 정보를 입력하시오')
    name=input("이름:")
    IDnum=input("학번:")
    grade=float(input("학점:"))
    subject=eval(input("수강 과목:"))
    data=list(subject)
    stu_info={'이름':name,'학번':IDnum,'학점':grade,'수강 과목':data}
    all_info.append(stu_info)

#학과 정보 처리
a=majorinfo['학과명']
b=majorinfo['설립 연도']
print(a+str(b))
print(3*a)
print(len(a))

#학생 정보 처리
print(all_info[0])
print(all_info[4])
print(all_info[1:4])

del all_info[0]
print("새로운 학생 정보를 입력하시오")
name=input("이름:")
IDnum=input("학번:")
grade=float(input("학점:"))
subject=eval(input("수강 과목:"))
data=list(subject)
stu_info={'이름':name,'학점':IDnum,'학점':grade,'수강 과목':data}
all_info.append(stu_info)

print(all_info)

#학과 통계
grade_list=[g['학점'] for g in all_info]
grade_sum=sum(grade_list)
result=grade_sum/5

print("전체 학생의 평균 학점: "+str(round(result,2)))

count=0
for i in range(5):
    if round(grade_list[i],2)>=3.5:
        count+=1
print("3.5 이상: "+str(count))       

m=max(grade_list)
s=min(grade_list)
print("최고 학점: "+str(m))
print("최저 학점: "+str(s))