from helper import helper

Categories = """
1.Quantitative Problems
2.Logical Reasoning
3.Verbal Reasoning
"""
print(Categories)
choice = int(input("Selct your choice of Topic : "))
if choice == 1:
    Category_name = "Quantitative"
    topic_name = input("Enter the Topic name (for ex:  Profit and Loss) : ")
    no_of_questions = int(input("Enter the  number of questions: "))
    helper(Category_name, topic_name, no_of_questions)

if choice == 2:
    Category_name = "Logical Reasoning"
    topic_name = input("Enter the Topic name (for ex: Analogy ) : ")
    no_of_questions = int(input("Enter the  number of questions: "))
    helper(Category_name, topic_name, no_of_questions)

if choice == 3:
    Category_name = "Verbal Reasoning"
    topic_name = input("Enter the Topic name (for  ex: Tenses) :  ")
    no_of_questions = int(input("Enter the  number of questions: "))
    helper(Category_name, topic_name, no_of_questions)
