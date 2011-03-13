# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from joinform.forms import JoinForm
from joinform.forms import ChavurahForm
from django.template import RequestContext
from django.core.context_processors import csrf

def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = 'Title: ' + cd['title']+'\n'
            message = message + '\n First Name: ' + cd['firstname'] +'\n'
            message = message + '\n Last Name: ' + cd['lastname'] +'\n'
            message = message + '\n Birthday Date (MM/DD/YYYY): '+ cd['birthdate'] +'\n'
            message = message + '\n Marital Status: ' + cd['marital']+'\n'
            message = message + '\n Occupation: ' + cd['occupation']+'\n'
            message = message + '\n Firm/Business Name & Address: ' + cd['firm']+'\n'
            message = message + '\n Business Phone #: ' + cd['bphone']+'\n'
            message = message + '\n Home Phone #: ' + cd['hphone']+'\n'
            message = message + '\n Pager #: ' + cd['pager']+'\n'
            message = message + '\n Email Address: ' + cd['email']+'\n'
            message = message + '\n Home Address: ' + cd['homeA']+'\n'
            message = message + '\n Religious Background: ' + cd['religion']+'\n'
            message = message + '\n Please check all that apply: '+'\n'
            message = message + cd['previousjewish'].replace("u'","")+'\n'
            message = message + '\n I Can : '+'\n'
            message = message + cd['previousexp'].replace("u'","")+'\n'
            message = message + '\n Do you have an interest in any of the following \n committees/activities: '+'\n'
            message = message + cd['activity'].replace("u'","")+'\n'
            message = message + '\n Yahrzeits   I/We observe \n'
            if cd['hebrewdate'] == True:
                message = message + 'Hebrew Date \n'
            if cd['englishdate'] == True:
                message = message + 'English Date \n'
            message = message + '\n '+'{0:^30}'.format('-Name of Deceased Relative-')+ '{0:^15}'.format('-Relationship-')+'{0:^15}'.format('-Date of Death-')
            message = message + '\n '+'{0:^30}'.format(cd['nameofdeceased1'])+ '{0:-^15}'.format(cd['relationship1'])+'{0:-^15}'.format(cd['dateofdeath1'])
            message = message + '\n '+'{0:^30}'.format(cd['nameofdeceased2'])+ '{0:-^15}'.format(cd['relationship2'])+'{0:-^15}'.format(cd['dateofdeath2'])
            message = message + '\n '+'{0:^30}'.format(cd['nameofdeceased3'])+ '{0:-^15}'.format(cd['relationship3'])+'{0:-^15}'.format(cd['dateofdeath3'])
   
            
            message = message + '\n Number of Children: ' + cd['numofchild']
     
            message = message + '\n '+'{0:^16}'.format('-Name-')+ '{0:-^5}'.format('-Age-')+'{0:-^8}'.format('-Gender-')+'{0:-^7}'.format('-Grade-')+'{0:-^25}'.format('-Name of School/College-')+'{0:-^25}'.format('-Bar/Bat Mitzvah & Year-')+'{0:-^10}'.format('-Use Photo-')
	    message = message + '\n ' + '{0:-^16}'.format(cd['nameofchild1']) +'{0:-^5}'.format(cd['ageofchild1']) +'{0:-^8}'.format(cd['genderofchild1'])+'{0:-^7}'.format(cd['gradeofchild1'])+'{0:-^25}'.format(cd['nameofschool1'])+'{0:-^25}'.format(cd['barmitzvah1'])+'{0:-^10}'.format(str(cd['usephoto1']))
	    message = message + '\n ' + '{0:-^16}'.format(cd['nameofchild2']) +'{0:-^5}'.format(cd['ageofchild2']) +'{0:-^8}'.format(cd['genderofchild2'])+'{0:-^7}'.format(cd['gradeofchild2'])+'{0:-^25}'.format(cd['nameofschool2'])+'{0:-^25}'.format(cd['barmitzvah2'])+'{0:-^10}'.format(str(cd['usephoto2']))
	    message = message + '\n ' + '{0:-^16}'.format(cd['nameofchild3']) +'{0:-^5}'.format(cd['ageofchild3']) +'{0:-^8}'.format(cd['genderofchild3'])+'{0:-^7}'.format(cd['gradeofchild3'])+'{0:-^25}'.format(cd['nameofschool3'])+'{0:-^25}'.format(cd['barmitzvah3'])+'{0:-^10}'.format(str(cd['usephoto3']))
            message = message + '\n ' + '{0:-^16}'.format(cd['nameofchild4']) +'{0:-^5}'.format(cd['ageofchild4']) +'{0:-^8}'.format(cd['genderofchild4'])+'{0:-^7}'.format(cd['gradeofchild4'])+'{0:-^25}'.format(cd['nameofschool4'])+'{0:-^25}'.format(cd['barmitzvah4'])+'{0:-^10}'.format(str(cd['usephoto4']))
            message = message + '\n ' + '{0:-^16}'.format(cd['nameofchild5']) +'{0:-^5}'.format(cd['ageofchild5']) +'{0:-^8}'.format(cd['genderofchild5'])+'{0:-^7}'.format(cd['gradeofchild5'])+'{0:-^25}'.format(cd['nameofschool5'])+'{0:-^25}'.format(cd['barmitzvah4'])+'{0:-^10}'.format(str(cd['usephoto5']))
     
            message = message + '\n Special Talents or Skills: \n' + cd['specialtalent']+'\n'
            message = message + '\n Reasons for joining Temple Bat Yahm: \n' + cd['reasonsforjoin']+'\n'
            send_mail(
                cd['firstname'] +' '+ cd['lastname'] + ' Join Application',
                message,
                cd.get('email', 'noreply@example.com'),
                ['jointemplebatyahm@gmail.com'],
            )
            return render_to_response('return_form.html', {'form': form},context_instance=RequestContext(request))
    else:
        form = JoinForm()
    
    return render_to_response('join_form.html', {'form': form},context_instance=RequestContext(request))
    
def chavurah(request):
    if request.method == 'POST':
        form = ChavurahForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = 'Title: ' + cd['title']+'\n'
            message = message + '\n First Name: ' + cd['firstname'] +'\n'
            message = message + '\n Last Name: ' + cd['lastname'] +'\n'
            message = message + '\n Birthday Date (MM/DD/YYYY): '+ cd['birthdate'] +'\n'
            
            message = message + '\n Occupation: ' + cd['occupation']+'\n'
            message = message + '\n Business Phone #: ' + cd['bphone']+'\n'
            message = message + '\n Home Phone #: ' + cd['hphone']+'\n'
            message = message + '\n Cell Phone #: ' + cd['cphone']+'\n'
            message = message + '\n Email Address: ' + cd['email']+'\n'
            message = message + '\n Home Address: ' + cd['homeA']+'\n'
            message = message + '\n Number of Children: ' + cd['numofchild']
            message = message + '\n '+'{0:>16}'.format('Name')+ '{0:>5}'.format('Age')+'{0:>8}'.format('Gender')+'{0:>7}'.format('Grade')+'{0:>25}'.format('Name of School/College')+'{0:>25}'.format('Bar/Bat Mitzvah & Year')
            message = message + '\n ' + '{0:>16}'.format(cd['nameofchild1']) +'{0:>5}'.format(cd['ageofchild1']) +'{0:>8}'.format(cd['genderofchild1'])+'{0:>7}'.format(cd['gradeofchild1'])+'{0:>25}'.format(cd['nameofschool1'])+'{0:>25}'.format(cd['barmitzvah1'])
            message = message + '\n ' + '{0:>16}'.format(cd['nameofchild2']) +'{0:>5}'.format(cd['ageofchild2']) +'{0:>8}'.format(cd['genderofchild2'])+'{0:>7}'.format(cd['gradeofchild2'])+'{0:>25}'.format(cd['nameofschool2'])+'{0:>25}'.format(cd['barmitzvah2'])
            message = message + '\n ' + '{0:>16}'.format(cd['nameofchild3']) +'{0:>5}'.format(cd['ageofchild3']) +'{0:>8}'.format(cd['genderofchild3'])+'{0:>7}'.format(cd['gradeofchild3'])+'{0:>25}'.format(cd['nameofschool3'])+'{0:>25}'.format(cd['barmitzvah3'])
            message = message + '\n ' + '{0:>16}'.format(cd['nameofchild4']) +'{0:>5}'.format(cd['ageofchild4']) +'{0:>8}'.format(cd['genderofchild4'])+'{0:>7}'.format(cd['gradeofchild4'])+'{0:>25}'.format(cd['nameofschool4'])+'{0:>25}'.format(cd['barmitzvah4'])
            message = message + '\n Indications of how important Chavurah factors are \n Criteria: '
            message = message + '\n Chavurah with couples only: ' + cd['couples']
            message = message + '\n Chavurah with singles only: ' + cd['singles']
            message = message + '\n Chavurah in which most activities include children: ' + cd['childrenactivities']
            message = message + '\n Chavurah with children similar in age to my children:  ' + cd['similarage']
            message = message + '\n Chavurah with children of mixed ages: ' + cd['mixedages']
            message = message + '\n Chavurah: '
            message = message + '\n Celebrates Jewish Holidays: ' + cd['celebrates']
	    message = message + '\n Includes Social Activities: ' + cd['socialactivities']
	    message = message + '\n Discussions/Speaker: ' + cd['discussions']
	    message = message + '\n Sports/Sporting Event: ' + cd['sports']
            
  
            message = message + '\n Other Members Intersted In Forming Chavurah With: \n' + cd['othermembers']+'\n'
            message = message + '\n Name of Current Chavurah and Members (If any): \n' + cd['currentchavurah']+'\n'
            send_mail(
                cd['firstname'] +' ' +cd['lastname'] + ' Chavurah Application',
                message,
                cd.get('email', 'noreply@example.com'),
                ['jointemplebatyahm@gmail.com'],
            )
            return render_to_response('return_form.html', {'form': form},context_instance=RequestContext(request))
    else:
        form = ChavurahForm()
    
    return render_to_response('chavurah_form.html', {'form': form},context_instance=RequestContext(request))
 