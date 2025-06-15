subject_marks =[('english',66),('science',90),('maths',98)]
print("original list of tuples")
print(subject_marks)
subject_marks.sort(key=lambda x:x[1])
print("\nSorting the list of tuples")
print(subject_marks)
