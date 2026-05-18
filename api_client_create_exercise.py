from courses.courses_schema import CreateCoursesRequestSchema
from exercises.exercises_shema import (CreateExerciseRequestSchema,
                                       GetExercisesQuerySchema)
from files.file_schema import CreateFileRequestSchema
from privet_http_builder import AuthenticationUserSchema
from users.user_schema import CreateUserRequestSchema

from clients.courses.courses_client import get_private_course_client
from clients.exercises.exercises_client import get_private_exercise_client
from clients.files.files_client import get_private_file_client
from clients.users.public_users_client import get_public_user_client
from tools.fakers import Fakers

public_users_client = get_public_user_client()

request_data = CreateUserRequestSchema(
    email=f'{Fakers.get_random_email_for_user()}',
    password='12345',
    lastName='Nikita',
    firstName='Nikita',
    middleName='Nikita')

authentication_user = AuthenticationUserSchema(
    email=request_data.email,
    password=request_data.password)


file_data = CreateFileRequestSchema(
    filename="test_123",
    directory="/directory",
    upload_file="./test_data/files/playwrite.png"
)

create_user_response = public_users_client.create_user(request=request_data)

file_client = get_private_file_client(user=authentication_user)

upload_file_response = file_client.create_file(request=file_data)

print(f"Create file data: {upload_file_response.model_dump(by_alias=True)}")

create_course_request = CreateCoursesRequestSchema(
    title="first_test_course",
    maxScore=100,
    minScore=0,
    description="My first course",
    estimatedTime="2 weeks",
    previewFileId=upload_file_response.file.id,
    createdByUserId=create_user_response.user.id)

course_client = get_private_course_client(authentication_user)

create_course_response = course_client.create_course(request=create_course_request)

create_exercise_request = CreateExerciseRequestSchema(
    title="TEST-ex",
    courseId=create_course_response.course.id,
    maxScore=100,
    minScore=0,
    orderIndex=12,
    description="My first exercise",
    estimatedTime="2 weeks",
)

print(f"Create course data: {create_course_response.model_dump(by_alias=True)}")

exercises_client = get_private_exercise_client(user=authentication_user)

exercises_client.create_exercise(request=create_exercise_request)

get_exercises_response = exercises_client.get_exercises(query=GetExercisesQuerySchema(
    courseId=create_course_response.course.id
))
print(f"Get exercises data: {get_exercises_response.model_dump(by_alias=True)}")