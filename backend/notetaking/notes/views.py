from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import Memo
from .serializers import MemoSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
def index(request):
    memo = Memo.objects.all()
    return render(request, 'index.html',{'memo':memo})

def add(request):
    return render(request, 'add.html')

def addrec(request):
    x = request.POST['title']
    y = request.POST['message']
    memo = Memo(title = x, message = y)
    memo.save()
    return redirect("/")

def delete(request, id):
    memo = Memo.objects.get(id=id)
    memo.delete()
    return redirect("/")

def update(request, id):
    memo = Memo.objects.get(id=id)
    return render(request,'update.html',{'memo':memo})

def uprec(request, id):
    x = request.POST['title']
    y = request.POST['message']
    memo = Memo.objects.get(id=id)
    memo.title = x
    memo.message = y
    memo.save()
    return redirect("/")




class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer
    permission_classes = [AllowAny]  



'''
POST (Create a new Memo)
URL: POST /api/memos/
Description: This will create a new Memo object.
Example JSON Body:
json
Copy code
{
  "title": "Meeting Reminder",
  "message": "Team meeting at 10 AM.",
  "date": "2024-10-20T10:00:00Z"
}

PATCH (Partially update an existing Memo)
URL: PATCH /api/memos/{id}/ (replace {id} with the ID of the memo you want to update)
Description: This will partially update a Memo object (you only send the fields you want to update).
Example JSON Body:
json
Copy code
{
  "message": "Team meeting at 11 AM."
}


DELETE (Delete a Memo)
URL: DELETE /api/memos/{id}/ (replace {id} with the ID of the memo you want to delete)
Description: This will delete the specified Memo object.
Example:
You don’t need a JSON body for DELETE requests. Simply call the URL DELETE /api/memos/1/ (assuming the id is 1), and it will delete that memo.





GET (List all Memos)
URL: GET /api/memos/
Description: This will return a list of all Memo objects.
Example Response:
json
Copy code
[
  {
    "id": 1,
    "title": "Meeting Reminder",
    "message": "Team meeting at 10 AM.",
    "date": "2024-10-20T10:00:00Z"
  },
  {
    "id": 2,
    "title": "Project Update",
    "message": "Please submit your project updates by Friday.",
    "date": "2024-10-21T14:00:00Z"
  }
]



GET (Retrieve a single Memo)
URL: GET /api/memos/{id}/ (replace {id} with the ID of the memo you want to retrieve)
Description: This will return the details of a single Memo object.
Example Response:
json
Copy code
{
  "id": 1,
  "title": "Meeting Reminder",
  "message": "Team meeting at 10 AM.",
  "date": "2024-10-20T10:00:00Z"
}



POST: /api/memos/ – Create a new memo.
PATCH: /api/memos/{id}/ – Update a memo.
DELETE: /api/memos/{id}/ – Delete a memo.
GET: /api/memos/ – List all memos.
GET: /api/memos/{id}/ – Retrieve a specific memo.

'''

