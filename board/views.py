from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .models import Board
# Create your views here.
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from .forms import BoardModelForm
def index(request):
    return render(request,'board/index.html')

class List(ListView):
    model = Board
    
# def list(request):
#     board = Board.objects.all()
#     con = {
#         'board':board
#     }
#     return render(request,'board/list.html',con)

class Regist(CreateView):
    model = Board
    form_class = BoardModelForm
    success_url = reverse_lazy('board:list')
    
    
    # 'button_label'=변수명 이라는걸 html에 {{button_label}} 써야함
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['button_label'] = '등록'
    #     return context
        
        
    
# def regist(request):
#     if request.method == 'GET':
#         return render(request,'board/regist.html')
#     else:
#         title =request.POST['title']
#         writer = request.POST['writer']
#         content = request.POST['content']
        
#         Board.objects.create(title=title,writer=writer,content=content)
#         return HttpResponseRedirect(reverse('board:list'))
    
class Detail(DetailView):
    model = Board
    def get_object(self):
        item = super().get_object()
        item.incrementReadCount()
        return item
# def detail(request,id):
#     board = Board.objects.get(id=id)
#     board.incrementReadCount()
#     con = {
#         'board':board
#     }
#     return render(request,'board/detail.html',con)


class Edit(UpdateView):
    model = Board
    form_class = BoardModelForm
    
    #이 방법으로는  reverse_lazy('board:list') 값을 가져올수 없기에 get_success_url(self)를 써주는것
    #get_success_url(self) 이 함수는 UpdateView의 부모 상속을 받은것
    # success_url = reverse_lazy('board:list') action의 값을 들고 리스트에 다시 재요청
    
    success_url = '이것은 super().get_success_url() '
    
    def get_success_url(self):
        print(super().get_success_url())
        return reverse('board:detail', args=(self.object.id,))
    
     # 'button_label'=변수명 이라는걸 html에 {{button_label}} 써야함
    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
    #     context['button_label'] = '수정'
    #     return context
    
# def edit(request,id):
#     if request.method == 'GET':
#         return render(request,'board/edit.html')
#     else:
#         title =request.POST['title']
#         writer = request.POST['writer']
#         content = request.POST['content']
#         Board.objects.filter(id=id).update(title=title,writer=writer,content=content)
#         return HttpResponseRedirect(reverse('board:detail',args=[id]))
  
  
class Delete(DeleteView):
    model = Board
    success_url = reverse_lazy('board:list')
    
# def delete(request,id):
#     if request.method == 'GET':
#         board = Board.objects.get(id=id)
#         con = {
#         'board':board
#         }
#         return render(request, 'board/delete.html',con)
#     else:
#         Board.objects.get(id=id).delete()
#         return HttpResponseRedirect(reverse('board:list'))