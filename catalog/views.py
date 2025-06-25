# from django.http import HttpResponse
# from django.core.management import call_command
# from django.contrib.auth import get_user_model

# def run_setup(request):
#     call_command('migrate')

#     User = get_user_model()
#     if not User.objects.filter(username='admin').exists():
#         User.objects.create_superuser('admin', 'admin@example.com', 'adminpass123')

#     return HttpResponse("Migrations applied and superuser created.")
    