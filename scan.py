'''
This is the CMPT 120 Fall 2017 Final Project: Scantron Processing.
With this program you will able to process scantron data into a
comma separated value table and display statistics on the input data.

by: Andrew Eng and Ivy Ren
'''
import turtle as t
#######################################################

def read_string_list_from_file(the_file):
    '''
    GENERIC READING OF TEXT FILE
    USE AS TEMPLATE, INCORPORATE IN YOUR FILE
    GENERATES A LIST OF STRINGS, ONE STRING PER ELEMENT
    AUTHOR: Diana Cukierman

    Assumptions:
    1) the_file is in the same directory (folder) as this program 
    2) the_file contains one student per "line"  
    3) lines are separated by "\n", that is, after each "line" (student)
       in the file  there is a return ("\n") . Also there is (one single)
       return ("\n") after the last line  in the_file
    4) Thhis function returns a list of strings
    '''
    
    fileRef = open(the_file,"r")      # opening file to be read
    localList=[]                      # new list being constructed
    for line in fileRef:
        string = line[0:len(line)-1]  # -1: eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)      # appends a new element
                                      # of type string to the list
        
    fileRef.close()  
        
    
    print ("\n JUST TO TRACE, the local list of strings is:\n")
    for element in localList:
        print (element)  # element is a string for one student
    
        
    return localList

def write_result_to_file(lres,the_file):
    
    '''
    Creates a text output file from a list of strings
    AUTHOR: Diana Cukierman
    
    Assumptions:
    1) lres is a list of strings, where each string
       will be one line in the output file
    2) the_file will contain the name fo the output file.
       for this porgram it shoudl be a name with .csv extension
    3) it is assumed that each string in lres already includes
       the character "\n" at the end
    4) the resulting file will be in the same directory (folder) as this program 
    5) the resulting file will  contain one student data per line 
    '''
    
    fileRef = open(the_file,"w") # opening file to be written
    for line in lres:
        fileRef.write(line)
                                    
    fileRef.close()
    return


def letterAnswers(st):
    '''
    this function will translate the numerical answer key to a letter answer key
    '''
    res = ""
    for i in range(len(st)):
        if st[i] == "1":
            res += "A "
        if st[i] == "2":
            res += "B "
        if st[i] == "3":
            res += "C "
        if st[i] == "4":
            res += "D "
        if st[i] == "5":
            res += "E "
    return res

def maxPts(st):
    '''
    this function will receive
    a string, and will return the
    sum off all float values in a string
    '''
    res = 0.0
    for i in range(len(st)):
        res = res + float(st[i])
    return res

def correctAnsAll(st):
    
    resultstring = ""
    for i in range(len(st)):
        student_x = st[i].split()
        count = 0
        for i in range(len(student_x[1])):
            if student_x[1][i] == answer_key[0][i]:
                count += float(ans[i])
        resultstring = resultstring + student_x[0] + "," + str(count) + "," + str(count/maxPts(ans)*100) + "\n"
    print("This is the output that will be saved\n",resultstring)
    write_result_to_file(resultstring,"OUT_results.csv")

      
            
def correctAnsSome(st):
    names = []
    
    for i in range(len(st)):
        student_x = st[i].split()
        names.append(student_x[0])
    
    flag = True
    j = 0
    res = 0
    resultstring = ""
    while (j < len(student_input)//2) and flag == True:
        select_student = input("Select a student, or type END(not case sensitive) to finish: ")
        if select_student in names:
            student_x = st[names.index(select_student)].split()
            count = 0.0
            for i in range(len(student_x[1])):
                if student_x[1][i] == answer_key[0][i]:
                    count += float(ans[i])
            print("Student", select_student, "got", count, "points!")
            resultstring = resultstring + select_student + "," + str(count) + "," + str(count/maxPts(ans)*100) + "\n"
            write_result_to_file(resultstring,"OUT_results.csv")
            j = j + 1
        elif select_student.lower() == "end":
            flag = False
        else:
            print("This name is not in the data, try again!")
    print("This is the output that will be saved\n",resultstring)

def highestScore():
    split_scores = ""
    highest_score = 0
    for i in range(len(resulting_students)):
        split_scores = resulting_students[i].split(",")
        #print(split_scores)                                             #TRACE to be removed
        if float(split_scores[1])> float(highest_score):
            highest_score = split_scores[1]
    return highest_score

def averageScore():
    split_scores = ""
    total = 0
    average = 0
    for i in range(len(resulting_students)):
        split_scores = resulting_students[i].split(",")
        total = total + float(split_scores[1])
        #print(total)                                                    #TRACE to be removed
    return total/len(resulting_students)


def correctAnsCount():
    names = []
    
    for i in range(len(individual_input)):
        student_x = individual_input[i].split()
        names.append(student_x[0])
        #print(student_x)
    answerCount = []
    res_names = []
    for i in range(len(answer_key[0])):
        answerCount.append(0)
    for i in range(len(resulting_students)):
        split_scores = resulting_students[i].split(",")
        res_names.append(split_scores[0])
        if res_names[i] in names:
            student_x = individual_input[names.index(res_names[i])].split()
            for i in range(len(student_x[1])):
                if student_x[1][i] == answer_key[0][i]:
                    answerCount[i] += 1
    return answerCount

def hardestQ():
    hardest = []
    smallest = min(answerCount)
    for i in range(len(answerCount)):
        if answerCount[i] == smallest:
            hardest.append(i+1)
    return hardest

def distribPercent():
    ranges = []
    res_scores = []
    for i in range(1,11):
        ranges.append(i*10)
    #print(ranges) #[10,20,30,40..]
    distrib = []
    for i in range(0,10):
        distrib.append(0)
    for i in range(len(resulting_students)):
        res_names = resulting_students[i].split(",")
        res_scores.append(res_names[2])

    i = 0
    j = 0
    while i < len(res_scores) and j < 10:
        if float(res_scores[i]) > ranges[j]:
            j += 1
        else:
            distrib[j] += 1
            j = 0
            i += 1
    return distrib

def distanceQ():
    names = []
    
    for i in range(len(individual_input)):
        student_x = individual_input[i].split()
        names.append(student_x[0])
        #print(student_x)
        
    flag = True
    res_names = []
    flag2 = True
    while flag == True:
        dist = 0
        dis_q1 = int(input("Enter q1, starting from 1, or type 0 to end:"))
        if dis_q1 == 0:
            flag = False
            flag2 = False
        elif dis_q1 >= len(answer_key[0])+1:
            print("Your input was not understood. Try again!")
            flag2 = False
        else:
            dis_q2 = int(input("Enter q2, starting from 1:"))
            if dis_q2 >= len(answer_key[0])+1 or dis_q2 == 0:
                print("Your input was not understood. Try again!")
                flag2 = False
            else:
                for i in range(len(individual_input)):
                    student_x = individual_input[i].split()
                    if (student_x[1][dis_q1-1] == answer_key[0][dis_q1-1]) and (student_x[1][dis_q2-1] == answer_key[0][dis_q2-1]) or (student_x[1][dis_q1-1] != answer_key[0][dis_q1-1]) and (student_x[1][dis_q2-1] != answer_key[0][dis_q2-1]):
                        print("The distance for", student_x[0], "is 0")
                    if (student_x[1][dis_q1-1] == answer_key[0][dis_q1-1]) and (student_x[1][dis_q2-1] != answer_key[0][dis_q2-1]) or (student_x[1][dis_q1-1] != answer_key[0][dis_q1-1]) and (student_x[1][dis_q2-1] == answer_key[0][dis_q2-1]):
                        dist += 1
                        print("The distance for", student_x[0], "is 1")
                flag2 = True
        if flag2 == True:
            print("The distance between questions", dis_q1,"and",dis_q2,"is",dist)
            

def turtleDraw(st):
    t.left(180)
    t.penup()
    t.forward(300)
    t.left(180)
    t.pendown()
    for i in range(len(st)):
        t.fillcolor("blue")
        t.begin_fill()
        t.forward(25)
        t.left(90)
        t.forward(25*int(st[i]))
        t.left(90)
        t.forward(25)
        t.left(90)
        t.forward(25*int(st[i]))
        t.left(90)
        t.forward(25)
        t.end_fill()
        t.forward(25)
###################TOP LEVEL

student_input = read_string_list_from_file("xxxxxx.txt") # IMPORTANT!! change xxxxxx.txt to input file
answer_key = read_string_list_from_file("xxxxxx.txt")    # IMPORTANT!! change xxxxxx.txt to input file
individual_input = list(student_input)                          #put individual student name and input into a list
ans = answer_key[1].split()                                     #split values for answer key into individual strings

print("\n")
print("Welcome to the CMPT 120 Scantron Processing system")
print("This system will process scantron files in the the same folder as this program.")
print("\n")
print("There are", len(student_input), "students in this class")
print("There are", len(answer_key[0]), "questions in this data")
print("The answer key is: ", letterAnswers(answer_key[0]))
print("The maximum possible points are:", maxPts(ans))
flag = True
while flag == True:
    processing = input("Type ALL (not case sensitive) to process the whole class, or type SEL(not case sensitive to process selected students (up to half of class): ")
    if processing.lower() == "all":
        correctAnsAll(individual_input)
        flag = False
    elif processing.lower() == "sel":
        correctAnsSome(individual_input)
        flag = False
    else:
        print("Please try again, the input was not understood.")
print
print("======================================")
print("Here are the statistics!")
print("======================================")
resulting_students = read_string_list_from_file("OUT_results.csv") #read output data after processed
print("\nThe highest score was:",highestScore())
print("The average score was:",averageScore())
print("The number of students processed was:",len(resulting_students))
print("Number of times each answer was answered correctly:")
answerCount = correctAnsCount()
print(answerCount)
print("The hardest questions were:",hardestQ())
print("Distribution points:",distribPercent(),"\n(This is considering ranges between [10,20,30,40,50,60,70,80,90,100])")
flag2 = True
while flag2 == True:
    askGraph = input("Would you like to graph the distribution? (Y/N):")
    if askGraph.lower() == "y":
        turtleDraw(distribPercent())
        flag2 = False
    elif askGraph.lower() == "n":
        print("Graphing the distribution was skipped.")
        flag2 = False
    else:
        print("Please try again, the input was not understood.")
flag3 = True
while flag3 == True:
    askDist = input("Would you like to calculate the 'distance' between each question? (Y/N):")
    if askDist.lower() == "y":
        distanceQ()
        flag3 = False
    elif askDist.lower() == "n":
        flag3 = False
    else:
        print("Please try again, the input was not understood.")
print("All statistics are complete! Goodbye!")
    

    


