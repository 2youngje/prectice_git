# 3. 고급 문제

## 문제 4: 메타클래스를 이용한 싱글톤 패턴 구현
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class School(metaclass=Singleton):
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def get_top_student(self):
        # students 리스트에서 가장 높은 평균 점수를 가진 학생을 반환하는 메서드를 작성하세요.
        # GradedStudent 또는 그 자식 클래스의 인스턴스만 고려하세요.
        # YOUR CODE HERE

# School 클래스의 객체를 생성하고, 여러 학생을 추가한 후 최고 성적의 학생을 찾아보세요.
# YOUR CODE HERE