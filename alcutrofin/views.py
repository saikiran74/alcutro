from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import All,Contactus

#browsers
def brave(request):
    return render(request,'browsers_brave.html')
def firefox(request):
    return render(request,'browsers_firefox.html')
def internet_explorer(request):
    return render(request,'browsers_internet explorer.html')

#social media
def twitter(request):
    return render(request,'socialmedia_twitter.html')
def whatsapp(request):
    return render(request,'socialmedia_whatsapp.html')

#meetings
def ciscowebex(request):
    return render(request,'meeting_ciscowebex.html')
def zoom(request):
    return render(request,'meeting_zoom.html')


def chrome(request):
    return render(request,'chrome.html')
def windows(request):
    return render(request,'windows.html')
def google(request):
    post=All.objects.all()
    return render(request,'google.html',{'post':post})
def microsoft(request):
    post=All.objects.all()
    return render(request,'microsoft.html',{'post':post})
def youtube(request):
    return render(request,'youtube.html')
def googleadword(request):
    return render(request,'googleadword.html')
def googleanalytics(request):
    return render(request,'googleanalytics.html')
def googleappmaker(request):
    return render(request,'googleappmaker.html')
def googlecalendar(request):
    return render(request,'googlecalendar.html')
def googlechat(request):
    return render(request,'googlechat.html')
def googlechrome(request):
    return render(request,'googlechrome.html')
def googlecontacts(request):
    return render(request,'googlecontacts.html')
def googledocs(request):
    return render(request,'googledocs.html')
def googledrawing(request):
    return render(request,'googledrawing.html')
def googledrive(request):
    return render(request,'googledrive.html')
def googleearth(request):
    return render(request,'googleearth.html')
def googleforms(request):
    return render(request,'googleforms.html')
def googlegmail(request):
    return render(request,'googlegmail.html')
def googlegroups(request):
    return render(request,'googlegroups.html')
def googlehangout(request):
    return render(request,'googlehangout.html')
def googlekeep(request):
    return render(request,'googlekeep.html')
def googlemeet(request):
    return render(request,'googlemeet.html')
def googlephotos(request):
    return render(request,'googlephotos.html')
def googlesheet(request):
    return render(request,'googlesheet.html')
def googlesite(request):
    return render(request,'googlesite.html')
def googleslides(request):
    return render(request,'googleslides.html')
def googlewebdesigner(request):
    return render(request,'googlewebdesigner.html')
def googleyoutube(request):
    return render(request,'googleyoutube.html')
def microsoftcalendar(request):
    return render(request,'microsoftcalendar.html')
def microsoftedge(request):
    return render(request,'microsoftedge.html')
def microsoftexcel(request):
    return render(request,'microsoftexcel.html')
def microsoftgamebar(request):
    return render(request,'microsoftgamebar.html')
def microsoftgroove(request):
    return render(request,'microsoftgroove.html')
def microsoftmail(request):
    return render(request,'microsoftmail.html')
def microsoftmap(request):
    return render(request,'microsoftmap.html')
def microsoftmoviesandtv(request):
    return render(request,'microsoftmoviesandtv.html')
def microsoftoutlook(request):
    return render(request,'microsoftoutlook.html')
def microsoftpaint(request):
    return render(request,'microsoftpaint.html')
def microsoftpaint3d(request):
    return render(request,'microsoftpaint3d.html')
def microsoftphotos(request):
    return render(request,'microsoftphotos.html')
def microsoftpowerpoint(request):
    return render(request,'microsoftpowerpoint.html')
def microsoftskype(request):
    return render(request,'microsoftskype.html')
def microsoftteams(request):
    return render(request,'microsoftteams.html')
def microsoftvoicerecorder(request):
    return render(request,'microsoftvoicerecorder.html')
def microsoftwindows(request):
    return render(request,'microsoftwindows.html')
def microsoftword(request):
    return render(request,'microsoftword.html')
def microsoftworkpad(request):
    return render(request,'microsoftworkpad.html')





def favourite(request):
    post=All.objects.all()
    return render(request,'favourite.html',{'post':post}) 
def addfavourite(request,pk):
    if(request.method=='POST'):
        fav=get_object_or_404(All,id=pk)
        if fav.favourite.filter(id=request.user.id).exists():
            fav.favourite.remove(request.user)
        else:
            fav.favourite.add(request.user)
        return redirect('/')
    else:
        return redirect('/')
def createaccount(request):
    if request.method=='POST':
        username= request.POST['username']
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        if password1==password2:
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username already exist')
                return render(request,'index.html')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'email already exist')
                return render(request,'index.html')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                
                user.save()
                return render(request,'index.html')
        else:
            messages.info(request,'password did not matched')
            return render(request,'index.html')
        return redirect('/')
        
    else:
        return render(request,'index.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def index(request):
    post=All.objects.all()
    return render(request,'index.html',{'post':post})
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username ,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid username and password')
            return redirect('index')
    else:
        return render(request,'signin.html')


def contact(request):
    if request.method=='POST':
        print("ki")
        ob=Contactus()
        ob.name=request.POST['name']
        ob.email=request.POST['email']
        ob.querry=request.POST['querry']
        ob.save()
        return redirect('index')
    else:
        return render(request,'contactus.html')

def google(request):
    post=All.objects.all()
    return render(request,'google.html',{'post':post})
def microsoft(request):
    post=All.objects.all()
    return render(request,'microsoft.html',{'post':post})
def socialmedia(request):
    post=All.objects.all()
    return render(request,'socialmedia.html',{'post':post})
def browsers(request):
    post=All.objects.all()
    return render(request,'browsers.html',{'post':post})
#pages
def termsandconditions(request):
    return render(request,'pages/termsandconditions.html')
def privacyandpolicy(request):
    return render(request,'pages/privacyandpolicy.html')
def contactus(request):
    return render(request,'pages/contactus.html')
def aboutus(request):
    return render(request,'pages/aboutus.html')
