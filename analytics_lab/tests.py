from django.test import TestCase
from models import Task,User,Status
from datetime import datetime
class model_test(TestCase):
    def test_task(self):
        user = User(email="ledidukh@gmail.com",name="Leonid")
        user.save()
        t = Task(assignee =user,name ="Animation",reel="REEL_01",seq="010",shot="SHOT_010",start_date = datetime.now(),end_date =datetime.now() )
        t.save()
        s = Status(status_name="Completed",task=t,date= datetime.now())
        s.save()
        self.assertEqual(Task.objects.get(name="Animation").reel,"REEL_01")
