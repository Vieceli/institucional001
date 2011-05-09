# Create your views here.
from institucional001.contato.forms import Agenda_Visita_Form
from django.core.mail.message import EmailMessage
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

def agenda_visita_form(request):
    if request.POST:
        form = Agenda_Visita_Form(request.POST)
        if form.is_valid():
            nome=form.cleaned_data['nome'],
            email=form.cleaned_data['email'],
            assunto=form.cleaned_data['mensagem'],
            mensagem_site=form.cleaned_data['mensagem']
            mensagem = "Ola\nO %s Mandou a seguinte mensagem:\n%s" %(nome,mensagem_site)
            email = EmailMessage(assunto,mensagem, to=['veiodruida@gmail.com'])
            email.send()
            
            if request.is_ajax():
                return render_to_response('contato/sucesso.html')
            else:
               return redirect('contato_sucesso')
    else:
        form = Agenda_Visita_Form()

    return render_to_response('contato/form.html', locals(),context_instance=RequestContext(request))
