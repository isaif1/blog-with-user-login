from django.views.generic import ListView, DeleteView

from . models import Articles

class ArticleListView(ListView):
	model=Articles
	template_name='home.html'	




class ArticleDetailView(DeleteView):
	model=Articles
	template_name = 'detail.html'
	context_object_name='blushes'