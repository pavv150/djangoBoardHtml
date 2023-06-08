from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Board
# Create your views here.

def index(request):
    return render(request,'board/index.html')

def list(request):
    board = Board.objects.all()
    con = {
        'board':board
    }
    return render(request,'board/list.html',con)

def regist(request):
    if request.method == 'GET':
        return render(request,'board/regist.html')
    else:
        title =request.POST['title']
        writer = request.POST['writer']
        content = request.POST['content']
        
        Board.objects.create(title=title,writer=writer,content=content)
        return HttpResponseRedirect(reverse('board:list'))
    
def detail(request,id):
    board = Board.objects.get(id=id)
    board.incrementReadCount()
    con = {
        'board':board
    }
    return render(request,'board/detail.html',con)

def edit(request,id):
    if request.method == 'GET':
        return render(request,'board/edit.html')
    else:
        title =request.POST['title']
        writer = request.POST['writer']
        content = request.POST['content']
        Board.objects.filter(id=id).update(title=title,writer=writer,content=content)
        return HttpResponseRedirect(reverse('board:detail',args=[id]))
    
def delete(request,id):
    if request.method == 'GET':
        board = Board.objects.get(id=id)
        con = {
        'board':board
        }
        return render(request, 'board/delete.html',con)
    else:
        Board.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('board:list'))