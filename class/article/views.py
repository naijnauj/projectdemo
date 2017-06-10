from django.shortcuts import render
from block.models import Block
from .models import Article
from .forms import ArticleForm
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic import DetailView
from django.core.paginator import Paginator

#def pagination(request,all_articles,ARTICLE_CNT_1PAGE = 3,next_link,previous_link):
   # page_no = int(request.GET.get("page_no","1"))
   # p = Paginator(all_articles,ARTICLE_CNT_1PAGE)
   # page_cnt = p.num_pages
  #  page_links = [i for i in
  #               range(page_no-5,page_no+6)
  #               if i>0 and i<=p.num_pages] #标页列表
   # previous_link = page_links[0]-1
   # next_link = page_links[-1]+1
   # page = p.page(page_no)
   # articles_objs = page.object_list
    
def article_list(request,block_id):
    ARTICLE_CNT_1PAGE = 5
    page_no = int(request.GET.get("page_no","1"))    
    #start_index = (page_no-1)*ARTICLE_CNT_1PAGE
    #end_index = page_no*ARTICLE_CNT_1PAGE
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    all_articles = Article.objects.filter(block=block,status=0).order_by("-id")
    p = Paginator(all_articles,ARTICLE_CNT_1PAGE)
    
    page_cnt = p.num_pages #总页数
    current_no = page_no
    page_links = [i for i in
               range(page_no-5,page_no+6)
               if i>0 and i<=p.num_pages] #标页列表
    previous_link = page_links[0]-1
    next_link = page_links[-1]+1   
    page = p.page(page_no)
    articles_objs = page.object_list
    #articles_objs = Article.objects.filter(block=block,status=0).order_by("-id")
    #articles_objs = Article.objects.filter(block=block,status=0).order_by("-id")[start_index:end_index]
    return render(request,"article_list.html",{"articles":articles_objs, "b":block})
     
def article_detail(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles_objs = Article.objects.filter(block=block,status=0).order_by("-id")
    return render(request,"article_detail.html",{"articles":articles_objs, "b":block})

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail_s.html'
    context_object_name = 'a'
    
    
class ArticleCreateView(View):
    template_name = 'article_create.html'
    
    def init_data(self,block_id):
        self.block_id = block_id
        self.block = Block.objects.get(id=block_id)
     
    def get(self,request,block_id):
        self.init_data(block_id)
        return render(request,self.template_name,{"b":self.block})
        
    def post(self,request,block_id):
        self.init_data(block_id)
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.block = self.block
            article.status = 0
            article.save()
            return redirect("/article/list/%s" %self.block_id)
        else:
            return render(request,self.template_name,{"b":self.block,"form":form})
            

    #def article_create(request,block_id):
 #   block_id = int(block_id)
  #  block = Block.objects.get(id=block_id)
   # if request.method == "GET":
    #    return render(request,"article_create.html",{"b":block})
    #else:
     #   form = ArticleForm(request.POST)
      #  if form.is_valid():
       #     article = form.save(commit=false)
        #    article.block = block
         #   article.status = 0
            #article = Article(block=block,title=form.cleaned_data["title"],
           # content=form.cleaned_data["content"],status=0)
          #  article.save()
         #   return redirect("/article/list/%s" %block_id) 
        #else:
          #  return render(request,"article_create.html",{"b":block,"form":form})
    
    
    
    
        #title = request.POST["title"].strip()
       # content = request.POST["content"].strip()
        #if not title or not content:
        #    return render(request,"article_create.html",
        #           {"b":block,"error":"标题和内容都不能为空","title":title,"content":content})
        #if len(title) > 100 or len(content) > 10000:
        #    return render(request,"article_create.html",
       #            {"b":block,"error":"标题或内容太长了"})
      #  article = Article(block=block,title=title,content=content,status=0)
      #  article.save()
      #  return redirect("/article/list/%s" %block_id) 