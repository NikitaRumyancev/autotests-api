from clients.courses.courses_client import get_private_course_client, CreateCoursesRequestDict
from clients.exercises.exercises_client import get_private_exercise_client, GetExercisesResponseDict, \
    GetExercisesQueryDict, CreateExerciseRequestDict
from clients.files.files_client import get_private_file_client, CreateFileRequestDict
from clients.privet_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_user_client, CreateUserRequestDict
from tools.fakers import Fakers

public_users_client = get_public_user_client()

request_data = CreateUserRequestDict(
    email=f'{Fakers.get_random_email_for_user()}',
    password='12345',
    lastName='Nikita',
    firstName='Nikita',
    middleName='Nikita')

authentication_user = AuthenticationUserDict(
    email=request_data['email'],
    password=request_data['password'])


file_data = CreateFileRequestDict(
    filename="test_123",
    directory="/directory",
    upload_file="./test_data/files/playwrite.png"
)

create_user_response = public_users_client.create_user(request=request_data)

file_client = get_private_file_client(user=authentication_user)

upload_file_response = file_client.create_file(request=file_data)

print(f"Create file data: {upload_file_response}")

create_course_request = CreateCoursesRequestDict(
    title="first_test_course",
    maxScore=100,
    minScore=0,
    description="My first course",
    estimatedTime="2 weeks",
    previewFileId=upload_file_response["file"]["id"],
    createdByUserId=create_user_response["user"]["id"])

course_client = get_private_course_client(authentication_user)

create_course_response = course_client.create_course(request=create_course_request)

create_exercise_request = CreateExerciseRequestDict(
    title="TEST-ex",
    courseId=create_course_response["course"]["id"],
    maxScore=100,
    minScore=0,
    orderIndex=12,
    description="My first exercise",
    estimatedTime="2 weeks",
)

print(f"Create course data: {create_course_response}")

exercises_client = get_private_exercise_client(user=authentication_user)

exercises_client.create_exercise(request=create_exercise_request)

print(create_course_response)

get_exercises_response = exercises_client.get_exercises(query=GetExercisesQueryDict(
    courseId=create_course_response["course"]["id"]
))
print(f"Get exercises data: {get_exercises_response}")