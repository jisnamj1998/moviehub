from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Movie
from myapp.forms import MovieForm,MovieModelForm
# Create your views here.

class MovieListView(View):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all()

        return render(request,"movie_list.html",{"data":qs})
    
class MovieCreateView(View):
    def get(self,request,*args,**kwargs):

        form_instance=MovieModelForm()

        return render (request,"movie_create.html",{"form":form_instance})   
    
    def post(self,request,*args,**kwargs):

        form_instance=MovieModelForm(request.POST)

        if form_instance.is_valid():

            # data=form_instance.cleaned_data

            # Movie.objects.create(**data)
            form_instance.save()

            return redirect("movie-list")
        
        else:
             return render(request,"movie_create.html",{"form":form_instance})

class MovieDetailView(View):

    def get(self,request,*args,**kwargs):

        #kwargs contains id
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        return render(request,"movie_details.html",{"data":qs})
    

class MovieDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie.objects.get(id=id).delete()
        return redirect("movie-list")    


class MovieUpdateView(View):
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_object=Movie.objects.get(id=id) #query set

        # dictionary={
        #     "title":movie_object.title,
        #     "year":movie_object.year,
        #     "director":movie_object.director,
        #     "run_time":movie_object.run_time,
        #     "language":movie_object.language,
        #     "genre":movie_object.genre
        # }
        # form_instance=MovieForm(initial=dictionary)#dictionay
        form_instance=MovieModelForm(instance=movie_object)

        return render(request,"movie_update.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=MovieModelForm(request.POST)

        id=kwargs.get("pk")

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Movie.objects.filter(id=id).update(**data)
            

            return redirect("movie-list")
        else:

            return render(request,"movie_update.html",{"form":form_instance})
        

