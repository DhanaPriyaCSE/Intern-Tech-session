class Department:
    def __init__(self,department_name,student_list,subject_offered):
        self.department_name=department_name
        self.student_list=student_list
        self.subject_offered=subject_offered
    def display_students_in_department(self):
        print("The Student List of ",self.department_name)
        for student in self.student_list:
                print(student[1].title())
                
def morethan_3_course_choosen_dept_name(*departments):
    depart_name=[]
    for department in departments:
        students=department.student_list
        for student in students:
            if len(student[2])>=3 and department.department_name not in depart_name:
               depart_name.append(department.department_name)
    print('The morethan 3 subject choosen department name:',' '.join(depart_name))

def overlapping_subjects_in_departments(*departments):
   overlapping_subject=set(department_of_cse.subject_offered).intersection(set(department_of_it.subject_offered),set(department_of_ece.subject_offered))  
   print("The overlapping subjects are:",' '.join(overlapping_subject))
        
    
department_of_cse=Department("CSE",[['101','priya',['OS','DS','DAA','AI']],['102','manisha',['CN','DS','CNS']],['102','bharathi',['AI','PDS']]],['OS','DS','DAA','CN','CNS','AI','PDS'])
department_of_it=Department("IT",[['201','vino',['OS','WP','DAA']],['202','hema',['COA','CA','CNS']],['203','pavish',['SE','DM','PDS']]],['OS','WP','DAA','COA','CNS','SE','PDS','DM'])
department_of_ece=Department("ECE",[['301','bama',['DSP','DS','MP']],['303','muki',['CN','EE','CNS']],['303','catherin',['OS','AI','PDS']]],['DSP','DS','OS','MP','CN','CNS','AI','PDS','EE'])


given_department_name=input("Enter the any one of the department name from below \n CSE \t ECE \t IT: \n")

if given_department_name.upper()=='CSE':
   department_of_cse.display_students_in_department()
elif given_department_name.upper()=='ECE':
    department_of_ece.display_students_in_department()
elif given_department_name.upper()=='IT':
    department_of_it.display_students_in_department()
else:
     print("Enter the prper input:")

morethan_3_course_choosen_dept_name(department_of_cse,department_of_it,department_of_ece)

overlapping_subjects_in_departments(department_of_cse,department_of_it,department_of_ece)


'''
output

Enter the any one of the department name from below 
 CSE 	 ECE 	 IT: 
cse
The Student List of  CSE
Priya
Manisha
Bharathi
The morethan 3 subject choosen department name: CSE IT ECE
The overlapping subjects are: CNS OS PDS


'''

