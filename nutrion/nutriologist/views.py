import datetime
from datetime import datetime,timezone, timedelta

from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.urls import reverse


from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth import logout
from django.core.paginator import Page
from django.core.paginator import Paginator



import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView




from .forms import LoginForm
from .forms import SearchBarForm
from .forms import GoogleCalendarForm

from .models import Patients
from .models import Appointment
from .models import PatientStats

# Create your views here.
from .serializers import UserSerializer
import json


class GoogleCalendarAuth():

    def __init__(self):
        self.scope = ["https://www.googleapis.com/auth/calendar"]
        self.creds = None
        self.service = None

    def sing_in(self):

         if os.path.exists('token.pickle'):
             with open('token.pickle', 'rb') as token:
                 self.creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
         if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.scope)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

         service = build('calendar', 'v3', credentials=self.creds)
         self.service = service

    def create_event(self,new_event):

        event = self.service.events().insert(calendarId='primary',body=new_event).execute()
        print("Event created: {}".format(event.get('htmlLink')))



class LoginAdminView(View):

    template_name = 'Formulars/login.html'
    form_class = LoginForm
    def get(self, request):
        return render(request, self.template_name, {'form':self.form_class})
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password= password)
            if user is not None:
                login(request, user)
                g = GoogleCalendarAuth()
                #print(g.scope)
                g.sing_in()


                return redirect('/home/')
            else:
                messages.warning(request, 'error')
                return render(request, self.template_name, {'form':form})

class HomeAdminView(ListView):

    paginate_by = 5
    template_name = 'Backoffice/home.html'

    queryset = Appointment.objects.all()

    def get_queryset(self):

        appointment = Appointment.objects.filter(nutriologist_id = self.request.user.id).order_by('date_start')#.select_related('patient_name')
        print(appointment)

        return appointment

class ClientsAdminView(FormMixin, ListView):

    template_name = 'Backoffice/clients.html'
    form_class = SearchBarForm
    paginate_by = 5
    queryset = Patients.objects.all()

    query_string = None

    def get_success_url(self, *args):

        return reverse_lazy('clients_search_view', args=[self.query_string])

    def get_queryset(self):
        patients = Patients.objects.filter(nutrioligist_id=self.request.user.id)
        return patients

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():

            return self.form_valid(form)


    def form_valid(self, form):
        search = form.cleaned_data['search_bar']
        self.query_string = search
        return super().form_valid(form)

class ClientsAdminQueryView(View):

    template_name = 'Backoffice/Query/query_clients.html'

    def get(self, request, query):

        patients = Patients.objects.filter(firstname__contains=query).filter(nutrioligist_id=request.user.id)
        print(patients)

        return render(request, self.template_name, {'patients':patients})

class CalendarAdminView(View):

    template_name = 'Backoffice/citas.html'

    def get(self, request):
        patients = Patients.objects.filter(nutrioligist_id=request.user.id).order_by('-firstname')

        form = GoogleCalendarForm()
        form.fields['patient'].queryset = patients

        return render(request, self.template_name, {'form':form, 'patient':patients})

    def post(self, request):

        g = GoogleCalendarAuth()

        form =  GoogleCalendarForm(request.POST)

        new_event = None

        #print(form.cleaned_data['date_start'])

        if form.is_valid():
            summary = form.cleaned_data['title']
            print(summary)
            location = form.cleaned_data['location']
            description = form.cleaned_data['description']
            date_start = form.cleaned_data['date_start']
            end_date = form.cleaned_data['date_end']
            start_hour = form.cleaned_data['start_hour']
            end_time = form.cleaned_data['end_time']
            attendees = form.cleaned_data['patient']
            print(attendees.id)



            split_date_start = str(date_start).split("-")
            start_time  = str(start_hour).split(":")

            split_date_end = str(end_date).split("-")
            end_hour = str(end_time).split(":")

            combined_date_start = datetime(int(split_date_start[0]), int(split_date_start[1]), int(split_date_start[2]), int(start_time[0]), int(start_time[1]) )

            combined_date_end = datetime(int(split_date_end[0]), int(split_date_end[1]), int(split_date_end[2]), int(end_hour[0]), int(end_hour[1]) )

            timezone = "America/Mazatlan"

            new_event = {
                'summary':summary,
                'location':location,
                'description':description,
                'start':{
                    'dateTime':combined_date_start.strftime("%Y-%m-%dT%H:%M:%S"),
                    'timeZone':timezone
                },
                'end':{
                    'dateTime':combined_date_end.strftime("%Y-%m-%dT%H:%M:%S"),
                    'timeZone':timezone
                },
                'attendees':[
                    {'email':attendees.email}
                ]
            }

            #print(new_event)
            g.sing_in()
            g.create_event(new_event)
            #event = self.service.events().insert(calendarId='primary',body=new_event).execute()
            #print("Event created: {}".format(event.get('htmlLink')))

            #GoogleCalendarAuth()
            print(new_event)

            new_appointment_obj = Appointment(patient_name = attendees,
                        nutriologist = self.request.user,
                        title = summary,
                        date_start  = combined_date_start,
                        date_end = combined_date_end,
                        place = location,

                        description = description)

            new_appointment_obj.save()
            return redirect('/appointments/')

        return render(request, self.template_name, {'form':form})




class AddClientAdminView(CreateView):

    template_name = 'Formulars/add_client.html'
    model = Patients

    fields = ['firstname','lastname','age', 'sex', 'cellphone', 'email']

    def form_valid(self, form):
        #Creamos el objeto en memoria
        self.object = form.save(commit=False)
        self.object.nutrioligist_id = self.request.user.id
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('add_client_view')

class SingleClientView(DetailView):

    template_name = 'Backoffice/Query/client_detail.html'
    #patient_id = None
    def get_queryset(self):
        patients = Patients.objects.filter(nutrioligist_id=self.request.user.id)
        #print(patients)
        return patients


def logout_view(request):
    logout(request)
    return redirect('/login/')
