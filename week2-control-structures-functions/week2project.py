def input_student_info():
   students=[]
   while True:
      print("학생 정보를 입력하세요(q 입력시 종료)")
      name=input("이름:")
      if name =="q":
        print("입력 종료")
        break
      grade=int(input("점수:"))
      stu_info={'이름':name,'점수':grade}
      students.append(stu_info)
   return students  

def calculate_grade(score):
    if score>=90:
        score="A"
    elif score>=80 and score<=89:
        score="B"
    elif score>=70 and score<=79:
        score="C"
    elif score>=60 and score<=69:
        score="D"
    elif score<60:
        score="F"
    return score

def print_results(students):
    for i in students:
        score=i['점수']
        level=calculate_grade(score)
        i['등급']=level
    print("학생 정보를 출력합니다\n",students)

def calculate_stats(students):
    s=[i['점수'] for i in students]
    p=sum(s)
    n=len(s)
    avg=p/n
    maximum=max(s)
    minimum=min(s)
    print("전체 평균 점수:",avg)
    print("최고 최저 점수:",maximum,minimum)

def main():
    students=[]
    students=input_student_info()
    print_results(students)
    calculate_stats(students)   

if __name__=="__main__" :
    main()
    








    



    
