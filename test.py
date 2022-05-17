import pyudemy
import os

client = pyudemy.PyUdemy(os.environ["UDEMY_ACCESS_TOKEN"])
res = client.get_subscribed_courses()
print(res)