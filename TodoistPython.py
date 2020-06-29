#importieren halt

from todoist.api import TodoistAPI
import uuid, requests, json
import todoist
from recipe_scrapers import scrape_me


api = todoist.TodoistAPI('4a4b544cda03b10fe4d68c9e203e9451c6923418')
api.sync()
AllTasks = (api.state['items'])


#findet alle unteraufgaben dieser aufgabe
Seas = 3857315376
TaskId = 3857315376
def PrintTask(TaskId):
    i = 0
    for x in AllTasks:
        i += 1
        if (AllTasks[i]['parent_id']) == TaskId:
            print(AllTasks[i]['content'])

"print(api.items.get_by_id(x))"



#Bewegt die Aufgabe nach Condition

def MoveRecipe():
    item_1 = api.items.get_by_id(2234945333)
    item_2 = api.items.get_by_id(3857807619)
    if (item_1['checked'] == 0) and (item_2['checked'] == 0):
        item = api.items.get_by_id(3857315376)
        item.move(project_id=2234945333)
        api.commit()
    elif (item_1['checked'] or item_2['checked']) == 1:
        item = api.items.get_by_id(3857315376)
        item.move(project_id=2234945472)
        api.commit()



    
#Sagt von jeder ID die Project ID
Ok = requests.get("https://api.todoist.com/rest/v1/projects", headers={"Authorization": "Bearer %s" % '4a4b544cda03b10fe4d68c9e203e9451c6923418'}).json()
[{u'comment_count': 0, u'id': 1234, u'name': u'Inbox'}]

def GetProjectID():
    i = 0
    for x in Ok:
        print((Ok[i])['id'])
        print((Ok[i])['name'])
        print("\n")
        i += 1



eingabe = input("Welche url?")
link = eingabe
scraper = scrape_me(link)

x = (len(list(scraper.ingredients())))

Taskname =(link + ' (' + str(scraper.title()) + ')'+ ' [' + (str(scraper.total_time()) + 'm]'))

task1 = api.items.add((Taskname), project_id=2234937268)

i = 0
while i < x:
    api.items.add(((list(scraper.ingredients())[i])), parent_id=task1['id'])
    i += 1
    api.commit()


scraper.yields()
scraper.ingredients()
scraper.instructions()
scraper.image()
scraper.links()


lol = (requests.get(
    "https://api.todoist.com/rest/v1/tasks",
    params={
        "project_id": 2234925955
    }, headers={
        "Authorization": "Bearer %s" % '4a4b544cda03b10fe4d68c9e203e9451c6923418'
    }).json())

lel = (requests.get(
    "https://api.todoist.com/rest/v1/tasks",
    params={
        "project_id": 2234937268
    }, headers={
        "Authorization": "Bearer %s" % '4a4b544cda03b10fe4d68c9e203e9451c6923418'
    }).json())




i = 0
j = 0
for x in lol:
    for y in lel:
        if (lol[i])['content'] != (lel[j])['content']:
            print('na')
        else:
            print((lel[j])['content'])
            taskToClose = ((lel[j])['id'])
            string_in_string = "https://api.todoist.com/rest/v1/tasks/{}/close".format(taskToClose)
            requests.post(string_in_string, headers={"Authorization": "Bearer %s" % '4a4b544cda03b10fe4d68c9e203e9451c6923418'})

        j += 1
    i += 1
    j = 0
    



