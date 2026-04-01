from django.shortcuts import render

# --- SUBJECTS VIEWS ---
def subjects_list(request):
    return render(request, 'subjects_list.html')

def subject_detail(request):
    return render(request, 'subject_detail.html')
