from courses.courses_schema import CreateCoursesRequestSchema
from files.file_schema import CreateFileRequestSchema
from users.user_schema import CreateUserRequestSchema

from clients.courses.courses_client import get_private_course_client
from clients.exercises.exercises_client import get_private_exercise_client
from clients.files.files_client import get_private_file_client
from clients.privet_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_user_client
from tools.fakers import Fakers

request_data = CreateUserRequestSchema(
    email=f'{Fakers.get_random_email_for_user()}',
    password='12345',
    lastName='Nikita',
    firstName='Nikita',
    middleName='Nikita')

public_users_client = get_public_user_client()

create_user_response = public_users_client.create_user(request=request_data)

print(create_user_response.model_dump(by_alias=True))

authentication_user = AuthenticationUserSchema(
    email=request_data.email,
    password=request_data.password)

file_client = get_private_file_client(authentication_user)

course_client = get_private_course_client(authentication_user)

create_file_response = file_client.create_file(request=CreateFileRequestSchema(
    filename="file_test",
    directory="/test_data_file_directory",
    upload_file="./test_data/files/playwrite.png"
))

print(create_file_response.model_dump(by_alias=True))

create_course_request = CreateCoursesRequestSchema(
    title="first_test_course",
    maxScore=100,
    minScore=0,
    description="My first course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id)

create_course_response = course_client.create_course(request=create_course_request)

exercises_client = get_private_exercise_client(user=authentication_user)

print(create_course_response.model_dump(by_alias=True))

