# CS329E Elements of Software Engineering
# Group: Technocats
# Project 3

## Here are some foundational class structures, to be fully fleshed out and implemented in later releases

class Assignment(object):

    skills = {} # dictionary of skills and their associated difficulty values
    name = ""
    description = ""
    assignmentType = "" # homework, quiz, test, or project
    completed = False
    
    def __init__(self, name, assignmentType):
        self.name = name
        self.assignmentType = assignmentType

    def __str__(self):
        output1 = (self.assignmentType + ": " + self.name + "\n\t" + self.description + "\n\n" + "Relevant Skills and Difficulties: " + "\n")
        output2 = ("   Skill: Difficulty" + "\n")
        output3 = ""
        for skill, difficulty in self.skills.items():
            output3 += ("   " + skill + ": " + str(difficulty) + "\n")
        return(output1 + output2 + output3)

    def addSkill(self, name, difficulty):
        if name in self.skills.keys():
            print("Skill already exists for this assignment. Overwriting Difficulty: " + str(self.skills.get(name)) + " to Difficulty: " + str(difficulty))
        self.skills[name] = difficulty
        
    def removeSkill(self, name):
        if name in self.skills.keys():
            del self.skills[name]
        else:
            print("Skill does not exist for this assignment")

    def addDescription(self, desc):
        self.description = desc

    def getSkillList(self):
        return list(self.skills.keys())

    def getSkillDict(self):
        return self.skills

    def getTotalExperience(self):
        return sum(list(self.skills.values()))

    def setType(self, typeSet):
        self.assignmentType = typeSet

    def setComplettionStatus(self, completement):
        self.completed = completement
        
class Course(object):
    syllabus = "" # syllabus file
    students = [] # list of students
    assignments = [] # list of assignments
    quests = [] # list of quests
    levelTable = {} # table of levels and corresponding point values for determining student level

    # method for uploading assignments
    # method for adding students
    # method for adding quests
    # method for setting levelTable values
    # method for generating report
    # methods for getting/setting Data

class Student:
    firstName = ""
    lastName = ""
    userID = ""
    skills = {} # dictionary of skills the student has progression in
    questsCompleted = [] # list of competed quests
    assignemntsCompleted = [] # list of completed assignments

class Instructor:
    firstName = ""
    lastName = ""
    userID = ""
    courses = [] # list of courses the instructor is teaching
    
def main():
    # miscellaneous testing
    test = Assignment("Example Assignemnt", "Quiz")
    print(test.name)
    test.addSkill("adeptness", 20)
    test.addSkill("adeptness", 15)
    print(test.skills)
    test.removeSkill("sdfds")
    test.removeSkill("adeptness")
    print(test.skills)
    test.addSkill("adeptness", 15)
    test.addSkill("acuity", 15)
    print(test.getSkillList())
    print(test.getSkillDict())
    print(test.getTotalExperience())
    test.addDescription("This is an example assignment")
    print(test)
main()
    
