import pyudemy
import os
from dotenv import load_dotenv

load_dotenv()

client = pyudemy.PyUdemy(os.environ["UDEMY_ACCESS_TOKEN"])
# res = client.get_subscribed_courses()
courses = client.search_course("python")
print("Got {} courses".format(len(courses)))
course = client.get_course_info(courses[0].id)
print("Got course {} with id {}".format(course.title, course.id))
course_curriculum = client.get_course_curriculum(course.id)
print("There are {} chapters in the course".format(len(course_curriculum)))
for chapter in course_curriculum:
    print("Chapter {} - {} has {} lectures".format(chapter.id,
          chapter.title, len(chapter.lectures)))
