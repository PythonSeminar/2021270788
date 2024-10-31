import csv

class Student:
    def __init__(self, name, student_id, grade,scores=None):
        #초기화 로직
        self.name=name
        self.student_id=int(student_id)
        self.grade=grade
        self.scores=scores if scores is not None else {}
    def __str__(self):
        scores_str = ', '.join(f"{subject}: {score}" for subject, score in self.scores.items())
        return f"Name: {self.name}, ID: {self.student_id}, Grade: {self.grade}, Scores: [{scores_str}]"

class StduentManagementSystem:
    
    def __init__(self):
        self.students=[] #리스트 초기화
    
    #학생 추가 로직
    def add_student(self, student):
        self.students.append(student)
    
    #학생 검색 로직
    def search_student(self,query):
        search=[student for student in self.students if student.student_id==int(query)]
        if search:
            for student in search:
                print(student)
        else:
            print("학생 정보가 없습니다.")
    
    # 학생 정보 수정 로직
    def update_student(self, student_id, updates):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            for key, value in updates.items():
                if key == "이름":
                    student.name = value
                elif key == "학년":
                    student.grade = value
                elif key == "점수":
                    student.scores.update(value)
            print("학생 정보가 수정되었습니다.")
        else:
            print("학생 정보가 없습니다.")

    # (학번으로) 학생 삭제 로직
    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.student_id == int(student_id):
                del self.students[i]
                print("학생 정보가 삭제되었습니다.")
                return

    # 전체 학생 목록 출력 로직
    def display_all_students(self):
        if self.students==None:
            print("유효한 학생 정보가 없습니다.")
        for student in self.students:
            print(student)

    # 성적 분석 로직
    def analyze_scores(self):
     if self.students:
        for student in self.students:
            # 각 학생의 점수 리스트 추출
            scores = list(student.scores.values())
            avg = sum(scores) / len(scores)
            high = max(scores)
            low = min(scores)
            print(student,"의 평균 점수",avg)
            print(student,"의 최고점",high)
            print(student,"의 최저점",low) 
     else:
        print("학생 정보가 없습니다.")
    
    # CSV 파일 저장 로직
    def save_to_file(self, filename):
        filename=input("파일명을 입력하시오: ")
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "student_id", "grade", "scores"]) #열 이름 작성
            for student in self.students:
                writer.writerow([student.name, student.student_id, student.grade, student.scores])#각 행 작성
        

    # CSV 파일 로드 로직
    def load_from_file(self, filename):
        with open(filename, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                   print(row)
      


# 메인 프로그램 로직
def main():
    sms = StduentManagementSystem()


    while True:
        print("1. 학생 추가")
        print("2. 학생 검색")
        print("3. 학생 정보 수정")
        print("4. 학생 삭제")
        print("5. 전체 학생 목록 출력")
        print("6. 성적 분석")
        print("7. 프로그램 종료")
        choice = input("원하는 작업을 선택하시오: ")

        #1번 선택시
        if choice == "1":
            name = input("이름 입력: ")
            student_id = int(input("학번 입력: "))
            grade = int(input("학년 입력: "))
            scores = {}
            while True:
                subject = input("과목 입력(입력이 끝나면 done 입력): ")
                if subject == "done":
                    break
                score = int(input("성적 입력: "))
                scores[subject] = score
            sms.add_student(Student(name, student_id, grade, scores))        
        #2번 선택시
        elif choice == "2":
            query = input("찾고싶은 학생의 학번을 입력하시오: ")
            sms.search_student(query)
        
        #3번 선택시
        elif choice == "3":
            student_id = int(input("수정할 학생의 학번을 입력하시오: "))
            updates = {}#updates는 dictionary
            print("수정할 정보를 입력하시오(수정할 정보가 아닐 시 엔터):")
            name = input("새로운 이름: ")
            if name:
                updates["이름"] = name
            grade = input("새로운 학년: ")
            if grade:
                updates["학년"] = int(grade)
            while True:
                subject = input("수정할 과목 입력(입력이 끝나면 done 입력): ")
                if subject == "done":
                    break
                score = int(input("새로운 성적 입력:" ))
                scores[subject] = score
            if scores:
                updates["과목"] = scores
            sms.update_student(student_id, updates)

        #4번 선택시
        elif choice == "4":
            student_id = int(input("삭제할 학생 학번 입력: "))
            sms.delete_student(student_id)
        
        #5번 선택시
        elif choice == "5":
            sms.display_all_students()
        
        #6번 선택시
        elif choice == "6":
            sms.analyze_scores()
        
        #7번 선택시
        elif choice == "7":
            filename=input("파일명 입력하시오: ")
            sms.save_to_file(filename)
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
