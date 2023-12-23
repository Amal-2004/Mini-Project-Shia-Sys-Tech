from django.shortcuts import render
from pyexpat.errors import messages

from django.shortcuts import render
from .models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project,projectdetail
from django.shortcuts import render, redirect
from shia_app.models import User, Signin
from datetime import timedelta
from django.contrib import messages
from django.http import HttpResponseRedirect
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User(username=username, email=email, password=password ,confirm_password=confirm_password)
            user.save()
            return redirect('shia_app:signin')
        else:
             
             
             return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        authenticated = True 
       
    

        try:

            user = User.objects.get(email=email, password=password)
            signin = Signin(email=email, password=password)
            signin.save()
            
            request.session['email'] = email
            request.session.set_expiry(28800)
            
            return redirect('shia_app:dashboard')  
        except User.DoesNotExist:
             error_message = 'Invalid email or password'
             return render(request, 'signin.html', {'error': error_message})
    else:
        if  'email' in request.session:


            return redirect('shia_app:dashboard') 
        else:
            return render(request,'signin.html')
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('shia_app:signin')         
    

def admin_panel(request):
    email = request.session.get('email')
    print(email)
    if not email:
        return redirect('shia_app:signin') #return render(request, 'admin_panel.html', {'email': email})
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            action= request.POST.get('action')
            
            user = User.objects.get(username=username)
        
            if action== 'make_admin':
                user.status = True
            elif action== 'depromote':
                user.status = False

            user.save()

        
            return redirect('shia_app:admin_panel')

        else:
        
            users = User.objects.all()

            context = {'users': users}
            return render(request, 'admin_panel.html', context)
    

def project_list(request):
    email = request.session.get('email')
    print(email)
    if not email:
        return redirect('shia_app:signin') #return render(request, 'admin_panel.html', {'email': email})
    else:
        if request.method == 'POST':
            project_name = request.POST['project_name']
            manager = request.POST['manager']
            resources = int(request.POST['resources'])
            male_count = int(request.POST['maleCount'])
            female_count = int(request.POST['femaleCount'])

            Project.objects.create(
                project_name=project_name,
                manager=manager,
                resources=resources,
                male_count=male_count,
                female_count=female_count
            )

            projectdetail.objects.create(
                projectname = project_name
            )
       
            return redirect('shia_app:project_list')
    
        projects = Project.objects.all()
        user = User.objects.filter()

        #print(User.objects.all())
        return render(request,'project list.html', {'projects': projects,'user':user})

def __str__(self):
        return self.project_name

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('shia_app:project_list')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from django.contrib import messages

def update_project(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == 'POST':
        project_name = request.POST['project_name']
        manager = request.POST['manager']
        resources = request.POST['resources']
        male_count = request.POST['maleCount']
        female_count = request.POST['femaleCount']
        project.project_name = project_name
        project.manager = manager
        project.resources = resources
        project.male_count = male_count
        project.female_count = female_count
        project.save()
        messages.success(request, 'Project updated successfully.')
        return redirect('shia_app:project_list')
    return render(request, 'update.html', {'project': project})

#count a user

def dashboard(request):
    email = request.session.get('email')
    print(email)
    if not email:
        return redirect('shia_app:signin') #return render(request, 'admin_panel.html', {'email': email})
    else:
        status=status_update.objects.all()
        datapack={'superusers':0,'totalusers':0,'editors':0,'publishers':0,
                'totalprojects':0,'totalclients':0}
        projects = Project.objects.all()
        superuser_count=User.objects.filter(status=1).count()
        totaluser_count=User.objects.count()
        editors_count=User.objects.filter(status=0).count()
        publishers_count=User.objects.filter(status=1).count()
        totalproject_count=Project.objects.count()
        totalclient_count=Project.objects.count()

        datapack['superusers']=superuser_count
        datapack['totalusers']=totaluser_count
        datapack['editors']=editors_count
        datapack['publishers']=publishers_count
        datapack['totalprojects']=totalproject_count
        datapack['totalclients']=totalproject_count
        return render(request,'dashboard.html', {'status':status,'projects': projects,'superuser_count':superuser_count,'totaluser_count':totaluser_count,'editors_count':editors_count,'publishers_count':publishers_count,'totalproject_count':totalproject_count,'totalclient_count':totalclient_count,"email":email})
    # file_upload


from django.core.mail import EmailMessage
from django.conf import settings
def email(request):
    email = request.session.get('email')
    print(email)
    if not email:
        return redirect('shia_app:signin') #return render(request, 'admin_panel.html', {'email': email})
    else:
        if request.method=='POST':
            name=request.POST['name']
            email=request.POST['email']
            message=request.POST['message']

            emails=EmailMessage(
                'Version Control Project Email',
                f'Hi {name}!\n Thank You For Contacting Us,This is message : \n\n{message}',
                settings.EMAIL_HOST_USER,
                [email],
            
            )
            emails.fail_silently=False # type: ignore
            emails.send()

        return render(request,'email.html')
'''
def content(request):
    projects=projectdetail.objects.all()
    return render(request,'content.html') #json
def project_details(request):
    
        projects=projectdetail.objects.all()
        print(projects)
        return render(request,'project detail.html',locals())
'''

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def bulk_email(request):
    email = request.session.get('email')
    print(email)
    if not email:
        return redirect('shia_app:signin') #return render(request, 'admin_panel.html', {'email': email})
    else:
        if request.method == 'POST':
            try:
                data = json.loads(request.body.decode('utf-8'))
                email_addresses = data.get('email', [])
                message = data.get('message', '')

                if not email_addresses:
                    return JsonResponse({'error': 'Please add at least one email address.'})

                

                send_mail(
                    'ShiaSys Project',  # Subject
                    message,         
                    'shiasysproject@gmail.com',  # Sender's email
                    email_addresses,  
                    fail_silently=False,
                )

                return JsonResponse({'success': 'Email sent successfully!'})
            except json.JSONDecodeError as e:
                return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)

        return render(request, 'bulk mail.html')


from shia_app.models import User, Signin,File
def upload(request):
    email = request.session.get('email')
    print(email)
    if not email:
        return redirect('shia_app:signin') #return render(request, 'admin_panel.html', {'email': email})
    else:
        if request.method=='POST':
            project_name = request.POST['project_name']
            for file in request.FILES.getlist('file'):
                File.objects.create(project_name=project_name,file=file)
            
            return redirect('shia_app:upload')
            
        files= File.objects.all()
        return render(request,'file upload.html', {'files': files})        
        

from django.shortcuts import render, redirect, get_object_or_404
from .models import Edit
def edit_project(request):  
    email = request.session.get('email')
    print(email)
    if not email:
        return redirect('shia_app:signin') #return render(request, 'admin_panel.html', {'email': email})
    else:
        if request.method == 'POST':
            
            resource_name = request.POST['resource_name']
            task= request.POST['task']
            

            Edit.objects.create(
                resource_name=resource_name,
                task=task,
            
            )
            

       
            return redirect('shia_app:edit_project')
        projects = Edit.objects.all()
    

        #print(User.objects.all())
        return render(request,'project edit.html', {'projects': projects})
    
def update_edit(request):
   
    if request.method == 'POST':
         
        id=request.POST.get('project_id')
        project = get_object_or_404(Edit ,id=id)
        resource_name = request.POST['resource_name']
        task=request.POST['task']
        print(resource_name, task)
        project.resource_name = resource_name
        project.task = task
        project.save()
        return redirect('shia_app:edit_project')
    return render(request, 'project edit.html')

def delete_edit(request, id):
    project = get_object_or_404(Edit, id=id)
    project.delete()
    return redirect('shia_app:edit_project')


#status

from django.shortcuts import render, redirect, get_object_or_404
from .models import status_update
def status(request):
    email = request.session.get('email')
    print(email)
    if not email:
        return redirect('shia_app:signin') #return render(request, 'admin_panel.html', {'email': email})
    else:

        projects = status_update.objects.all()
        return render(request,'project status.html', {'projects': projects})


from django.shortcuts import render, get_object_or_404, redirect
from .models import status_update
def edit_status(request):
   
    if request.method == 'POST':
         
        id=request.POST.get('id')
        project = get_object_or_404(status_update ,id=id)
        progress = request.POST.get('progress')
        status = request.POST.get('status')
        print(progress, status)
        project.Progress = progress
        project.Status = status
        project.save()
        return redirect('shia_app:status')
    return render(request, 'project status.html')


from django.shortcuts import render, redirect
from .models import UserProfile
from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from django.http import JsonResponse

def profile(request):
    email = request.session.get('email')
    #username = request.session.get('username')
    print(email)
    return render(request,'profile.html',locals())      
from .models import UserProfile
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt        
def profile_update(request):
   
    if request.method == 'POST':
        user_name = request.POST['user_names']
        
        email = request.POST['emails']
      
        mobile_no = request.POST['ph_no']
        emp_id = request.POST['emp_id']
        dob = request.POST['birth']
        join_date = request.POST['date']
        user_type = request.POST['user_type']
        
        profile_image = request.POST['base64']
        
        profile = UserProfile(
        username=user_name,
        email=email,
        mobileno=mobile_no,
        emp_id=emp_id,
        dob=dob,
        join_date=join_date,
        super_user=user_type,
        profile_image_base64=profile_image
        )
      
        profile.save() 
            
    return JsonResponse({'success': 'profile successfully!'})
    
  

from django.shortcuts import render, redirect
from .models import projectdetail
import json
def project(request):
    email = request.session.get('email')
    #username = request.session.get('username')
    print(email)
    return render(request,'project detail.html')
def project_detail(request):
       project_details = projectdetail.objects.all().values()
       print(project_details)
       return JsonResponse(list(project_details), safe=False)
       
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt        

def update_project_detail(request):
    if request.method == 'POST':
        
        id=request.POST['id']
        edited_data = request.POST['editedLogData']
        project_detail=projectdetail.objects.get(id=id)
        project_detail.log=edited_data
        #print(edited_data)
        project_detail.save()

    return JsonResponse({'ms': 'Project detail updated successfully'})


def skill_management(request):
    email = request.session.get('email')
    print(email)
    if not email:
        return redirect('shia_app:signin') #return render(request, 'admin_panel.html', {'email': email})
    else:
        return render(request,'skill management.html')