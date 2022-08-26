from survey_class import Survey
a = 'what was your first language you learned\n'
print(a)
lan=Survey(a)
lan.show_questions()
print('\n')
while True:
    ans=input('Enter your response:- ')
    if ans=='q':
        break
    lan.store_responses(ans)
print("\nThank you to everyone who participated in the survey!")
lan.show_result()