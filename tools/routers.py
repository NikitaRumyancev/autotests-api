from enum import Enum


class APIRouters(str, Enum):
    USERS = "/api/v1/users"
    AUTHENTICATION = "/api/v1/authentication"
    COURSES = "/api/v1/courses"
    EXERCISES = "/api/v1/exercises"
    FILES = "/api/v1/files"


    def __str__(self):
        return self.value