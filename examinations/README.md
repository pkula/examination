My API was created based on REST patterns. Communication is based on sending HTTP 
commands to http://127.0.0.1:8000/ along with the requested data.
Replies are sent in JSON format.


This API provide creator to full control in created sheets. We can add, update and remove question.
We can mark answer and all answer sheet.



I decide to use a default Django SQL: SQLite so first You must write in console
$python manage.py makemigrations
$python manage.py migrate




Authentication
Every API command sent needs authentication, which is obtained by sending HTTP headers:

*Key:Authorization,
*Value:Token 6587fd9ca7d7403b2a8f40a92b5f28d9e620f064

Data is sent in JSON format in commands.

################################################################################################
##Getting a token
You can get a token:

###Call: POST 127.0.0.1:8000/api-token-auth/
Required parameters:
username(str),
password(str)


##Creating a new exam sheet

###Call: POST 127.0.0.1:8000/api/exam_sheet/

Required parameters:
title(str)


##Add question to exam sheet
You can create and add questions to the exam sheet

###Call: POST 127.0.0.1:8000/api/exam_sheet/

Required parameters:
sheet_id(int), question_content(str), max_score(int)



##Creating a new answer sheet
You can create answer sheet

###Call: POST 127.0.0.1:8000/api/answer_forms/

Required parameters:
exam_sheet_id(int)



##Add answer
You can create and add answers to the answer sheet

###Call: POST 127.0.0.1:8000/api/exam_sheet/

Required parameters:
answer_content(str), question_id(int), form_id(int)




################################################################################################

##You can get all exam sheet with questions

###Call: GET 127.0.0.1:8000/api/exam_sheet/


##You can get all your exam sheet with questions

###Call: GET 127.0.0.1:8000/api/exam_sheet/my/


##You can get one exam sheet with questions

###Call: GET 127.0.0.1:8000/api/exam_sheet/id/



##You can search exam sheet for title

###Call: GET 127.0.0.1:8000/api/exam_sheets?title=phrase





#############################################################################


##You can get all your answer sheet with answers

###Call: GET 127.0.0.1:8000/api/answer_forms/my



##Owner exam sheet could get a answer form :

###Call: GET 127.0.0.1:8000/api/answer_forms/id/


###########################################################################

##You can get one question:

###Call: GET 127.0.0.1:8000/api/questions/id/


