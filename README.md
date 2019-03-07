# python_API

This project was created for the company skygate

* I tested api in postman
* I use venv


# Launch

To launch a project you have to do a few steps:
* Install python3 in you computer
* Go to the project folder and launch terminal
* Install python packages

```
$pip3 install -r requirements.txt
```

* Make migrations

```
$python3 manage.py makemigrations
$python3 manage.py migrate
```

* Create user:

```
$python3 manage.py createsuperuser
```

* Launch a server

```
$python3 manage.py runserver
```
* Now you can use a api. You can send response from your browser, postman or another way. Communication is based on sending HTTP 
commands to http://127.0.0.1:8000/

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [External libraries](#external-libraries)
* [Guide](#guide)
* [Add data](#add-data)
* [Publish and unpublish exam sheet](#publish-and-unpublish-exam-sheet)
* [Get data (exam_sheet)](#get-data_answer)
* [Get data (answer_forms)](#get-data-questions-sheet)
* [Get data (question)](#get-data-questions)
* [Change and delete question](#change-and-delete-question)
* [Modify sheet title](#modify-sheet-title)
* [Author](#author)






## General info
My API was created based on REST patterns. Communication is based on sending HTTP 
commands to http://127.0.0.1:8000/ along with the requested data.
Replies are sent in JSON format. Data is sent in JSON format in commands.

This API provide creator to full control in created sheets. We can add, update and remove question.
We can mark answer and all answer sheet.

## Technologies

Project is created with:
* Python 3.6.7

I decide to use a default Django SQL: SQLite so first You must write in console
* $python manage.py makemigrations
* $python manage.py migrate





## External libraries

* django rest framework


# Guide

Authentication
Every API command sent needs authentication, which is obtained by sending HTTP headers:
- Key:Authorization,
- Value:Token 6587fd9ca7d7403b2a8f40a92b5f28d9e620f064

#### Getting a token
You can get a token:
```
Call: POST 127.0.0.1:8000/api-token-auth/
```
Required parameters:
- username(str),
- password(str)


## Add data

#### Creating a new exam sheet

```
Call: POST 127.0.0.1:8000/api/exam_sheet/
```

Required parameters:
- title(str)


#### Add question to exam sheet

If you are owner - you can create and add questions to the exam sheet

```
Call: POST 127.0.0.1:8000/api/exam_sheet/
```

Required parameters:
- sheet_id(int), 
- question_content(str), 
- max_score(int)



#### Creating a new answer sheet

You can create answer sheet

```
Call: POST 127.0.0.1:8000/api/answer_forms/
```

Required parameters:
- exam_sheet_id(int)


#### Add answer

You can create and add answers to the answer sheet

```
Call: POST 127.0.0.1:8000/api/exam_sheet/
```

Required parameters:
- answer_content(str), 
- question_id(int), 
- form_id(int)

## Publish and unpublish exam sheet

#### Publish exam sheet

You can publish your exam sheet

```
Call: GET 127.0.0.1:8000/api/exam_sheets/id/publish/
```

#### Unpublish exam sheet

You can unpublish your exam sheet
```
Call: GET 127.0.0.1:8000/api/exam_sheets/id/unpublish/
```

## Get data (exam_sheet)

#### You can get all exam sheet with questions

```
Call: GET 127.0.0.1:8000/api/exam_sheet/
```

#### You can get all your exam sheet with questions

```
Call: GET 127.0.0.1:8000/api/exam_sheet/my/
```

#### You can get one exam sheet with questions
```
Call: GET 127.0.0.1:8000/api/exam_sheet/id/
```

#### You can search exam sheet for title

```
Call: GET 127.0.0.1:8000/api/exam_sheets?title=phrase
```


## Get data (answer_forms)

#### You can get all your answer sheet with answers

```
Call: GET 127.0.0.1:8000/api/answer_forms/my
```

#### Owner exam sheet could get a answer form :

```
Call: GET 127.0.0.1:8000/api/answer_forms/id/
```

## Get data (question)

#### You can get one question:

```
Call: GET 127.0.0.1:8000/api/questions/id/
```

 If you creator you get all field , else you get not all field

## Change and delete question

#### Sheet owner can change question:

```
Call: PUT 127.0.0.1:8000/api/questions/id/
```

#### Sheet owner can delete question:

```
Call: DELETE 127.0.0.1:8000/api/questions/id/
```

## Modify sheet title


#### Sheet owner can change title exam sheet:

```
Call: PUT 127.0.0.1:8000/api/exam_sheets/id/
```

Required parameters:  
- title(str)

## Author

* Przemyslaw Kula
* https://github.com/pkula