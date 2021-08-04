from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json;
import time;


from .models import User, Post, PostForm


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@csrf_exempt
@login_required
def new_posts(request):
    if request.method == "GET":
        return render(request, "network/new_posts.html", {
            "postform": PostForm()
        });
     
    elif request.method == "POST":
        #print(request.POST);
        json_object = json.loads(request.body);
        json_object["author"] = request.user;
        #print(json_object);
        post_to_save = Post(author = json_object["author"], content = json_object["content"])
        post_to_save.save();
        return JsonResponse(post_to_save.serialize())
        
        #---DJANGO implementation:
        #postForm = PostForm(request.POST);
        #if postForm.is_valid():
        #    post_to_save = Post(author = request.user, content = postForm.cleaned_data["content"])
        #    post_to_save.save();
        #    return JsonResponse(post_to_save.serialize());
   
@csrf_exempt
@login_required   
def posts(request):
    # can return either all posts, if no additional query paramters are given, or only those of followed people
    # For the latter option, add the 'followers' query-parameter

    if request.method == "GET" and "followers" in request.GET and request.GET["followers"]:
        posts_of_users_followed = Post.objects.filter(author__in = request.user.follows.all());
        
        print(posts_of_users_followed)
        return returnPosts(request, posts_of_users_followed)

    if request.method == "GET":
        posts = Post.objects.all();
        
        
        return returnPosts(request, posts);
        
    
@csrf_exempt
@login_required    
def all_posts(request):
    
        return render(request, "network/all_posts.html");
        
@csrf_exempt
@login_required
def profile(request, other_user_name):
    if request.method == "GET":

        displayed_user = User.objects.get(username=other_user_name);

        followed_users = displayed_user.follows.all();
        following_users = displayed_user.followers.all();

        return render(request, "network/profile.html", {
            "displayed_user" : displayed_user,
            "follows" : str(len(followed_users)),
            "following" : str(len(following_users))
        });
    
    elif request.method == "PUT":
        added_user = json.loads(request.body);
        #print(added_user["follow"]);
        #print("Should I unfollow?: " + str(added_user["unfollow"]));
        
        
        if not added_user["unfollow"]:
            if added_user["follow"] == request.user.username:
                return HttpResponse(status=400);
            
            else: 
                user_to_follow = User.objects.get(username=added_user["follow"])
                request.user.addFollower(user_to_follow);
                request.user.save();
                return HttpResponse(status=200);
                
        else: 
            user_to_stop_following = User.objects.get(username=added_user["follow"])
            if user_to_stop_following in request.user.follows.all():
                #print("Is good!");
                request.user.follows.remove(user_to_stop_following);
                user_to_stop_following.followers.remove(request.user);
                user_to_stop_following.save();
                return HttpResponse(status=200);
            else: 
                return HttpResponse(status=404);
            
def returnPosts(request, posts):
    post_list = [];
        
    #print("Get start is: " + request.GET.get("start","0"));
    #print("Get end is: " + request.GET.get("end","5"));

        
    if int(request.GET.get("end", 5)) <= len(posts):
        
        for i in range(int(request.GET.get("start",0)), int(request.GET.get("end", 5))):
            post_list.append(posts[i].serialize());
                
            
            
        time.sleep(0.5);
    else:
        remaining_in_database = len(posts) - int(request.GET.get("start", 0));
        for i in range(int(request.GET.get("start",0)), int(request.GET.get("start",0)) + remaining_in_database):
            post_list.append(posts[i].serialize());
                
       # print(post_list);
            
        time.sleep(0.5);
        
        
    return JsonResponse(post_list, safe=False);


    
def profile_posts(request, other_user_name):
    if request.method == "GET":
        #print(other_user_name);
        posts = Post.objects.all().filter(author=User.objects.get(username=other_user_name).id);
        return returnPosts(request, posts);
    else:
        return JsonResponse({"error":"error"})

@csrf_exempt
@login_required
def following(request):
    followed = [];
    
    return render(request, "network/following.html");
        