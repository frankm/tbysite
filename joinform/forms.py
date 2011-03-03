from django import forms

class JoinForm(forms.Form):
    TITLE = (
    ('MR', 'Mr.'),
    ('MS', 'Ms.'),
    ('MRS', 'Mrs.'),
    ('MI', 'Miss'),
    ('DR', 'Dr.'),
    )
    title = forms.ChoiceField(TITLE)
    firstname = forms.CharField(label='First Name')
    lastname = forms.CharField(label='Last Name')
    birthdate = forms.CharField(label = 'Birthdate (MM/DD/YYYY)')
    
    MARRY = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
    )
    marital = forms.ChoiceField(MARRY, label='Marital Status')
    occupation = forms.CharField()
    firm = forms.CharField(label='Firm/Business Name & Address')
    bphone = forms.CharField(label='Business Phone (XXX-XXX-XXXX)', required = False)
    hphone = forms.CharField(label='Home Phone (XXX-XXX-XXXX)')
    pager = forms.CharField(label='Pager #', required = False )
    email = forms.EmailField()
    homeA = forms.CharField(label='Home Address')
    RELIGIOUSB = (
        ('REFORM', 'Reform'),
        ('CONSERVATIVE', 'Conservative'),
        ('RECONSTRUCTIONISt', 'Reconstructionist'),
        ('ORTHODOX', 'Orthodox'),
        ('JEWISH UNAFFILIATED', 'Jewish Unaffiliated'),
        ('OTHER', 'Other'),
        )
    religion = forms.ChoiceField(RELIGIOUSB,label = 'Religious Background', required = False)
    ALLTHATAPPLY = (
        ('BAR/BAT_MITZVAH', 'Bar/Bat Mitzvah'),
        ('CONFIRMATION', 'Confirmation'),
        ('JEWISH_DAY_SCHOOL', 'Jewish Day School'),
        ('HEBREW_HIGH', 'Hebrew High'),
        ('RELIGIOUS_SCHOOL', 'Religious School'),
        )
    previousjewish = forms.CharField(label='Please check all that apply',widget=forms.CheckboxSelectMultiple(choices=ALLTHATAPPLY),required=False)
    
    numofyears = forms.CharField(label='# of Years',required=False)
    CANYOU = (
        ('READ/SPEAK_HEBREW/YIDDISH', 'Read Hebrew/Speak Hebrew/Speak Yiddish'),
        ('LEAD_SERVICES_IN_HEBREW', 'Lead Services In Hebrew'),
        ('LEAD_SERVICES_IN_ENGLISH', 'Lead Services In English'),
        ('CHANT_TORAH', 'Chant Torah or Haftarah'),
        ('TEACH_RELIGIOUS_SCHOOL', 'Teach Religious School'),
        ('SING_IN_CHOIR', 'Sing in Choir'),
        )
    previousexp = forms.CharField(label='Can you',widget=forms.CheckboxSelectMultiple(choices=CANYOU),required=False)
    ACTIVITIES = (
        ('ADULT_EDUCATION', 'Adult Education'),
        ('ADULT_BNAI_MITAVAH', 'Adult B`nai Mitzvah'),
        ('CHAVURAH', 'Chavurah'),
        ('CHOIR', 'Choir'),
        ('FINANCE', 'Finance'),
        ('FUNDRAISING', 'Fundraising'),
        ('ISRAEL_TRIP', 'Israel Trip'),
        ('ISRAEL_ADVOCACY', 'Israel Advocacy'),
        )
    ACTIVITIES2 = (
        ('KEHILAT_CHESED', 'Kehilat Chesed'),
        ('MARKETING', 'Marketing'),
        ('MEMBERSHIP', 'Membership'),
        ('PRESCHOOL_COMMITTEE', 'Preschool Committee'),
        ('RELIGIOUS_LIFE', 'Religious Life'),
        ('RELIGIOUS_SCHOOL_CO', 'Religious School Co.'),
        ('SISTERHOOD/WTBY', 'Sisterhood/WTBY'),
        ('SOCIAL_ACTION', 'Social Action'),
        )
    activity = forms.CharField(label='Do you have any interest in any of the following committees/activities',widget=forms.CheckboxSelectMultiple(choices=ACTIVITIES),required=False)
    activity2 = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=ACTIVITIES2),required = False)
    hebrewdate = forms.BooleanField(label = 'Hebrew Date', required = False)
    englishdate = forms.BooleanField(label = 'English Date', required = False)
    
    nameofdeceased1 = forms.CharField(label = 'Name of Deceased Relative:', required = False)
    relationship1 = forms.CharField(label = 'Relationship:',required = False)
    dateofdeath1 = forms.CharField(label = 'Date of Death',required = False)

    nameofdeceased2 = forms.CharField(label = 'Name of Deceased Relative:', required = False)
    relationship2 = forms.CharField(label = 'Relationship:',required = False)
    dateofdeath2 = forms.CharField(label = 'Date of Death',required = False)    

    nameofdeceased3 = forms.CharField(label = 'Name of Deceased Relative:', required = False)
    relationship3 = forms.CharField(label = 'Relationship:',required = False)
    dateofdeath3 = forms.CharField(label = 'Date of Death',required = False)

    numofchild = forms.CharField(label = 'Number of Children:')
    nameofchild1 = forms.CharField(label = 'Name:',required = False)
    ageofchild1 = forms.CharField(label = 'Age',required = False)
    genderofchild1 = forms.CharField(label = 'Gender',required = False)
    gradeofchild1 = forms.CharField(label = 'Grade',required = False)
    nameofschool1 = forms.CharField(label = 'Name of School/College', required = False)
    barmitzvah1 = forms.CharField(label = 'Bar/Bat Mitzvah & Year', required = False)
    usephoto1 = forms.BooleanField(label = 'Use Photo in TBY Materials', required = False)

    nameofchild2 = forms.CharField(label = 'Name:',required = False)
    ageofchild2 = forms.CharField(label = 'Age',required = False)
    genderofchild2 = forms.CharField(label = 'Gender',required = False)
    gradeofchild2 = forms.CharField(label = 'Grade',required = False)
    nameofschool2 = forms.CharField(label = 'Name of School/College', required = False)
    barmitzvah2 = forms.CharField(label = 'Bar/Bat Mitzvah & Year', required = False)
    usephoto2 = forms.BooleanField(label = 'Use Photo in TBY Materials', required = False)

    nameofchild3 = forms.CharField(label = 'Name:',required = False)
    ageofchild3 = forms.CharField(label = 'Age',required = False)
    genderofchild3 = forms.CharField(label = 'Gender',required = False)
    gradeofchild3 = forms.CharField(label = 'Grade',required = False)
    nameofschool3 = forms.CharField(label = 'Name of School/College', required = False)
    barmitzvah3 = forms.CharField(label = 'Bar/Bat Mitzvah & Year', required = False)
    usephoto3 = forms.BooleanField(label = 'Use Photo in TBY Materials', required = False)

    nameofchild4 = forms.CharField(label = 'Name:',required = False)
    ageofchild4 = forms.CharField(label = 'Age',required = False)
    genderofchild4 = forms.CharField(label = 'Gender',required = False)
    gradeofchild4 = forms.CharField(label = 'Grade',required = False)
    nameofschool4 = forms.CharField(label = 'Name of School/College', required = False)
    barmitzvah4 = forms.CharField(label = 'Bar/Bat Mitzvah & Year', required = False)
    usephoto4 = forms.BooleanField(label = 'Use Photo in TBY Materials', required = False)

    nameofchild5 = forms.CharField(label = 'Name:',required = False)
    ageofchild5 = forms.CharField(label = 'Age',required = False)
    genderofchild5 = forms.CharField(label = 'Gender',required = False)
    gradeofchild5 = forms.CharField(label = 'Grade',required = False)
    nameofschool5 = forms.CharField(label = 'Name of School/College', required = False)
    barmitzvah5 = forms.CharField(label = 'Bar/Bat Mitzvah & Year', required = False)
    usephoto5 = forms.BooleanField(label = 'Use Photo in TBY Materials', required = False)
    
    specialtalent = forms.CharField(label='Special talent or skills',widget=forms.Textarea,required = False)
    reasonsforjoin = forms.CharField(label = 'Reasons for joining Temple Bat Yahm',widget=forms.Textarea, required = False)

    def clean_birthdate(self):
        birthdate = self.cleaned_data['birthdate']
        if not len(birthdate) == 10:
            raise forms.ValidationError('Incorrect format. Please follow MM/DD/YYYY')
        date = birthdate.split('/')
        year = date.pop()
        day = date.pop()
        month = date.pop()
        if not year.isdigit() and not len(year) == 4:
            raise forms.ValidationError('Incorrect format. Please follow MM/DD/YYYY')
        if not day.isdigit() and not len(day) == 2:
            raise forms.ValidationError('Incorrect format. Please follow MM/DD/YYYY')
        if not month.isdigit() and not len(month) == 2:
            raise forms.ValidationError('Incorrect format. Please follow MM/DD/YYYY')        
        return birthdate

    def clean_bphone(self):
        bphone = self.cleaned_data['bphone']
        if not len(bphone) == 12:
            raise forms.ValidationError('Incorrect format. Please follow XXX-XXX-XXXX')
        bphoneformatted = bphone.split('-')
        linenumber = bphoneformatted.pop()
        prefix = bphoneformatted.pop()
        areacode = bphoneformatted.pop()
        if not linenumber.isdigit() and not len(linenumber) == 4:
            raise forms.ValidationError('Incorrect format. Please follow XXX-XXX-XXXX')
        if not prefix.isdigit() and not len(prefix) == 3:
            raise forms.ValidationError('Incorrect format. Please follow XXX-XXX-XXXX')
        if not areacode.isdigit() and not len(areacode) == 3:
            raise forms.ValidationError('Incorrect format. Please follow XXX-XXX-XXXX')        
        return bphone

    def clean_hphone(self):
        hphone = self.cleaned_data['hphone']
        if not len(hphone) == 12:
            raise forms.ValidationError('Incorrect format. Please follow XXX-XXX-XXXX')
        hphoneformatted = hphone.split('-')
        linenumber = hphoneformatted.pop()
        prefix = hphoneformatted.pop()
        areacode = hphoneformatted.pop()
        if not linenumber.isdigit() and not len(linenumber) == 4:
            raise forms.ValidationError('Incorrect format. Please follow XXX-XXX-XXXX')
        if not prefix.isdigit() and not len(prefix) == 3:
            raise forms.ValidationError('Incorrect format. Please follow XXX-XXX-XXXX')
        if not areacode.isdigit() and not len(areacode) == 3:
            raise forms.ValidationError('Incorrect format. Please follow XXX-XXX-XXXX')        
        return hphone