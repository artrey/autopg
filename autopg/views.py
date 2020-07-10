from django.shortcuts import render

from .utils import create_db_in_pg
from .forms import DatabaseCreateForm


def create_database_view(request):
    template_name = 'autopg/index.html'

    context = {}

    if request.method == 'POST':
        form = DatabaseCreateForm(request.POST)
        if form.is_valid():
            db = form.save(commit=False)
            db.username = db.name
            try:
                create_db_in_pg(db.name, db.username, db.password)
                db.save()
                db.host = ''
                context['db'] = db
            except Exception as ex:
                context['error'] = str(ex)
    else:
        form = DatabaseCreateForm()

    context['form'] = form

    return render(request, template_name, context)
