from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from django.core.paginator import Paginator
from farmland_app.models import *

# Create your views here.


class IndexPageView(View):
    def get(self, request):
        fresh = ServiceView.objects.all()
        explore = ExploreProject.objects.all()
        complete = CompletedProject.objects.all()
        return render(request, 'farmland_app/index.html', {'vegitable': fresh, 'explore':explore,
        'complete':complete})

  


class AboutPageView(View):
    def get(self, request):
        return render(request, 'farmland_app/about.html')


class BlogPageView(View):
    def get(self, request):
        blog = BlogModel.objects.all()
        return render(request, 'farmland_app/blog.html', {'blog':blog})

class BlogSinglePageView(View):
    def get(self, request):
        return render(request, 'farmland_app/blog-single.html')

class ContactPageView(View):
    def get(self, request):
        image = ContactImage.objects.all()
        return render(request, 'farmland_app/contact.html', {'data':image ,})

    def post(self, request):
        contact = FarmerContactUs()
        full_name = request.POST.get('name')
        subject = request.POST.get('subject')
        email_address = request.POST.get('email')
        message = request.POST.get('message')

        contact.full_name = full_name
        contact.subject = subject
        contact.email_address = email_address
        contact.message = message
        contact.save()
        messages.success(request, "Contact Record Submitted Successfully..!!!", {full_name})
        print(full_name, subject, email_address, message)

        return redirect('/')




class ProjectPageView(View):
    def get(self, request):
        project = ProjectView.objects.all()
        paginator = Paginator(project, per_page=6) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'farmland_app/project.html',{'project':project, 'page_obj':page_obj})



########## Service Page View Request Estimate Start here ###########

class ServicesPageView(View):
    def get(self, request):
        services_type = ServiceType.objects.all()
        requests = RequestAnEstimate.objects.all()
        ask_question = AskQuestions.objects.all()
        ans = AnswerList.objects.all()

        services = ServiceView.objects.all()
        print(services)
        
        # print(ask_question)
        # print(ans)
        
        return render(request, 'farmland_app/services.html',{'services_type':services_type, 'req': requests,
        'question':ask_question, 'answer': ans, 'service':services})

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        massage = request.POST.get('massage')
        service_id = request.POST.get('service')
        service = ServiceType.objects.get(id=service_id)
        RequestAnEstimate.objects.create(
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            massage = massage,
            service_type = service
        )
        # messages.success(request, "Request Record Submitted Successfully..!!!", {first_name})
        print(first_name, last_name, phone_number, service, massage,)

        return redirect('/')



########## Service Page View Request Estimate end here ###########

class EmailSubscribeView(View):
    def post(self, request):
        subscribe = EmailSubscribers()
        email = request.POST.get('subscribeemail')

        subscribe.email = email
        subscribe.save()                      
      
        messages.success(request, "Email Subscribe Successfully..!!!", {email})
        print(email)

        return redirect('/')













