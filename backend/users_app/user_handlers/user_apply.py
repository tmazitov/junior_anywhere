from django.http import JsonResponse
from ..models import UserResume
from ..models import UserVacancyApply

def get_user_resume(request, userId):
    resume = UserResume.objects.filter(user_id=userId).first()
    if resume:
        data = {
            'id': resume.id,
            'user_id': resume.user_id,
            'name': resume.name,
            'experience': resume.experience,
            'description': resume.description,
            'skills': resume.skills,
            'is_with_degree': resume.is_with_degree
        }
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Resume not found'}, status=404)
    

def create_user_resume(request, userId):
    if request.method == 'POST':
        data = json.loads(request.body)
        resume = UserResume.objects.create(
            user_id=userId,
            name=data['name'],
            experience=data['experience'],
            description=data['description'],
            skills=data['skills'],
            is_with_degree=data['is_with_degree']
        )
        return JsonResponse({'message': 'Resume created', 'id': resume.id}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

def apply_vacancy(request, vacancyId):
    if request.method == 'POST':
        data = json.loads(request.body)
        application = UserVacancyApply.objects.create(
            user_id=data['user_id'],
            resume_id=data['resume_id'],
            vacancy_id=vacancyId,
            company_id=data['company_id'],
            message=data['message'],
            status=0
        )
        return JsonResponse({'message': 'Application submitted', 'id': application.id}, status=201)
    
def cancel_application(request, vacancyId, applyId):
    application = UserVacancyApply.objects.filter(id=applyId, vacancy_id=vacancyId).first()
    if application:
        application.status = 3
        application.save()
        return JsonResponse({'message': 'Application cancelled'}, status=200)
    else:
        return JsonResponse({'error': 'Application not found'}, status=404)