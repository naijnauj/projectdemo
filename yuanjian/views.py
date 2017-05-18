from django.shortcuts import render

def index(request):
    block_infos = [{"name":"运维专区","desc":"运维学习讨论区","manager":"admin"},
	            {"name":"Django","desc":"Django学习讨论区","manager":"admin"},
			    {"name":"部落建设","desc":"杨颖看过来","manager":"admin"}]

    return render(request,"index.html",{"blocks":block_infos})