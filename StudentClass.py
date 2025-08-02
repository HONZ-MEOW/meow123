#七個班，每班50人
#顯示單科成績，顯示全部成績，顯示個人平均/全班
#三次段考成績
# class Class:
#^增加科目，^減少科目，總分，平均，加分，^設置成績，拿到成績
class Subject:
    def __init__(self,score_dict=None):
        # self._score=score_dict #賦值
        self._score={}
        for sub,value in score_dict.items():    #深拷貝
            self.Verify(value)
            self._score[sub]=value
    def Verify(self,score):
        if score<0 or score>100:
            raise ValueError("錯誤，成績非0~100")
    def SetScore(self,score,sub):
        if sub not in self._score:
            raise KeyError(f"錯誤，{sub}不存在")
        else:
            self.Verify(score)
            self._score[sub]=score
    def ShowScore(self,sub):
        try:
            print(self._score[sub])
        except KeyError:
            print(f"科目裡沒有{sub}")
    def AddSubject(self,sub,score):
        self.Verify(score)
        self.SubVerify_In(sub)
        self._score[sub]=score
    def DeleteSubject(self,sub):
        self.SubVerify_NotIn(sub) 
        del self._score[sub]
    def ShowAll(self):
        print(self._score)
    def SubVerify_In(self,sub):
        if sub in self._score:
            raise KeyError(f"已有{sub}")
    def SubVerify_NotIn(self,sub):
        if sub not in self._score:
            raise KeyError(f"沒有{sub}")
    def ReturnScore(self,sub):
        return self._score[sub]
    def GetTotalScore(self):
        sum=0
        for sub,value in self._score.items():
            sum+=value
        return sum
    def GetAverage(self):
        return self.GetTotalScore()/len(self._score)
class Test(Subject):
    def __init__(self,score_dict,t):
        super().__init__(score_dict)
        self._t=t    #int
    def Show_Info(self):
        print(f"這是第{self._t}次段考，總分是{self.GetTotalScore()}，平均是{self.GetAverage()}，",end="\t")
        self.ShowAll()
class Student(Subject):
    def __init__(self,multipleTest, name, id):
        self.__name=name
        self.__id=id
        self.__tests_dict={}
        for idx,(term_str,test_dict) in enumerate(multipleTest.items(),start=1):
            test=Test(test_dict,idx)
            # test_temp={}
            self.__tests_dict[term_str]=test
    # def Name(self):
    def ShowStudentInfo(self):
        print(f"{self.__name}{self.__id}")
        for idx,(term_str,test) in enumerate(self.__tests_dict.items(),start=1):
            print(test._t)
            print(test._score)








# x={"Chinese":-100,"Math":95,"English":99}
# Subject01=Subject(x)

# # x["Chinese"]=-100
# # Subject01.SetScore(90,"Math")
# # Subject01.ShowScore("Math")
# # Subject01.AddSubject("Science",69)
# # Subject01.DeleteSubject("Math")
# # Subject01.ShowAll()d
# # print(Subject01.GetTotalScore())
# # print(Subject01.GetAverage())
# # Test01=Test(x,1)
# # Test01.AddSubject("ComputerScience",85)
# # Test01.Show_Info()
# import random
# tests_dict={"Monthly Exam 01":x,"Monthly Exam 02":{"Chinese":98,"Math":55,"English":19},"Monthly Exam 03":{"Chinese":96,"Math":63,"English":79}}
# # Tony=Student(tests_dict,"Tony","5")
# # Tony.ShowStudentInfo()
# studentA=Student(tests_dict,"A",65)
# tests_dict["Monthly Exam 01"]["Chinese"]=-100
# studentA.ShowStudentInfo()
# first_name=["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
#     "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
#     "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
#     "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
#     "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
#     "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
#     "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
#     "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
#     "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
#     "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez"]
# name=["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth",
#     "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen",
#     "Christopher", "Nancy", "Daniel", "Margaret", "Matthew", "Lisa", "Anthony", "Betty", "Mark", "Dorothy",
#     "Donald", "Sandra", "Steven", "Ashley", "Paul", "Kimberly", "Andrew", "Donna", "Joshua", "Emily",
#     "Kenneth", "Carol", "Kevin", "Michelle", "Brian", "Amanda", "George", "Melissa", "Edward", "Deborah",
#     "Ronald", "Stephanie", "Timothy", "Rebecca", "Jason", "Sharon", "Jeffrey", "Laura", "Ryan", "Cynthia",
#     "Jacob", "Kathleen", "Gary", "Amy", "Nicholas", "Shirley", "Eric", "Angela", "Jonathan", "Helen",
#     "Stephen", "Anna", "Larry", "Brenda", "Justin", "Pamela", "Scott", "Nicole", "Brandon", "Emma",
#     "Benjamin", "Samantha", "Samuel", "Katherine", "Gregory", "Christine", "Frank", "Debra", "Alexander", "Rachel",
#     "Raymond", "Catherine", "Patrick", "Carolyn", "Jack", "Janet", "Dennis", "Ruth", "Jerry", "Maria"]
# for a in range(50):
#     d=["Chinese","Math","English"]
#     f=["Monthly Exam 01","Monthly Exam 02","Monthly Exam 03"]
#     stu_score=
#     stu_name=name[random.randint(0,99)]+first_name[random.randint(0,99)]
#     student=Student(random.randint(1,3),stu_name,a)

# # class Students:


    


# # Test02=Test()
# # Test03=Test()