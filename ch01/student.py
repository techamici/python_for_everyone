"""
Prompt the user for their name, and their scores.
Then calculate the GPA of the student and print it out.
"""
name = input("Enter your name: ")
maths = float(input("Enter Maths score: "))
english = float(input("Enter English score: "))
python = float(input("Enter Python score: "))

# Calculate GPA by averaging the scores
gpa = (maths + english + python)/3
print("GPA of", name, "is", gpa)
