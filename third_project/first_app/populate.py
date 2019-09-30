import os
os.environ.setdefault('DJANGO_SETTING_MODULES','third_project.settings')
import django
django.setup()
import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker
fakegen=Faker()
topics=['search','Social','Marketplace','News','Games']
def add_topic():
    t = Topc.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=S):
    for entry in range(N):
        top=add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        webpg=Webpage.object.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=='__main__':
    print("populating script !")
    populate(20)
    print("populating complete")
