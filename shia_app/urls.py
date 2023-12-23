from django.urls import path
from shia_app import views
from django.conf import settings
from django.conf.urls.static import static
app_name='shia_app'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('project_list', views.project_list, name='project_list'),
    path('delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('update/<int:id>/',views.update_project,name='update_project'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/',views.upload,name='upload'),
    path('email/',views.email,name='email'),
    path('bulk_email/', views.bulk_email, name='bulk_email'),
    path('project_status/',views.status,name='status'),
    path('edit/', views.edit_status, name='edit_status'),
    path('edit_project/', views.edit_project, name='edit_project'),
    path('update_edit/',views.update_edit,name='update_edit'),
      path('profile/', views.profile, name='profile'),
      path('profile_update',views.profile_update,name='profile_update'),
     path('delete_edit/<int:id>/', views.delete_edit, name='delete_edit'),
     
    path('projectdetails_edit', views.update_project_detail, name='update_project_detail'),
    path('project_detail', views.project_detail, name='project_detail'),
    path('project',views.project,name='project'),
    path('skill_management/',views.skill_management,name='skill_management'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
