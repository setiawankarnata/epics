from django import forms
from .models import Company, Peserta, Topik, Departemen, Meeting, Forum, Activity


class CreateForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = "__all__"
        widgets = {
            'nama_forum': forms.TextInput(attrs={'class': 'form-control'}, ),
            'keterangan': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CreateMeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = "__all__"
        exclude = ["meeting2peserta"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meeting Name'}),
            'meeting_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}, format='%H:%M'),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}, format='%H:%M'),
            'organizer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organizer'}),
            'notulen': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Notulen'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'meeting2forum': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Forum'}),
        }


class UpdateDepartemenForm(forms.ModelForm):
    class Meta:
        model = Departemen
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama divisi/departemen'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'dir_in_charge': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direktur in charge'}),
            'dept_head_in_charge': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Dept Head in charge'}),
            'email_dir_in_charge': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Direktur'}),
            'email_dept_head_in_charge': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email Dept Head'}),
        }


class UpdateForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = '__all__'
        widgets = {
            'nama_forum': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Forum'}),
            'keterangan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keterangan'}),
        }


class CreateDepartemenForm(forms.ModelForm):
    class Meta:
        model = Departemen
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama divisi/departemen'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


class CreateActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        exclude = ('activity2topik', 'activity2user', 'expired')
        widgets = {
            'date_activity': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'readonly': True},
                                             format='%Y-%m-%d'),
            'keterangan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keterangan'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }


class UpdateActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        exclude = ('activity2topik', 'activity2user', 'expired')
        widgets = {
            'date_activity': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'readonly': True},
                                             format='%Y-%m-%d'),
            'keterangan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keterangan'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }


class CreatePicaForm(forms.ModelForm):
    class Meta:
        model = Topik
        fields = '__all__'
        exclude = ('topik2meeting', 'topik2user', 'expired')
        widgets = {
            'issued_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'topik2departemen': forms.Select(attrs={'class': 'form-control'}),
            'topik2company': forms.Select(attrs={'class': 'form-control'}),
            'nama_topik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Topik'}, ),
            'problem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Problem'}),
            'action': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Solution'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }


class UpdatePicaForm(forms.ModelForm):
    class Meta:
        model = Topik
        fields = '__all__'
        exclude = ('topik2meeting', 'topik2user')
        widgets = {
            'issued_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # 'topik2meeting': forms.Select(attrs={'class': 'form-control'}),
            'topik2departemen': forms.Select(attrs={'class': 'form-control'}),
            'topik2company': forms.Select(attrs={'class': 'form-control'}),
            'nama_topik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama topik'}, ),
            'problem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Problem'}),
            'action': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Solution'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }


class UpdatePicaActionForm(forms.ModelForm):
    class Meta:
        model = Topik
        fields = ('nama_topik', 'problem', 'action', 'due_date')
        widgets = {
            'nama_topik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama topik'}, ),
            'problem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Problem'}),
            'action': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Solution'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Code'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'})
        }


class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'})
        }


class CreatePesertaForm(forms.ModelForm):
    class Meta:
        model = Peserta
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name peserta'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
            'peserta2company': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Company'}),
            'peserta2departemen': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Departemen'}),
            'bod': forms.NullBooleanSelect(attrs={'class': 'form-control', 'placeholder': 'BOD?'}),
        }


class UpdatePesertaForm(forms.ModelForm):
    class Meta:
        model = Peserta
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name peserta'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
            'peserta2company': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Company'}),
            'peserta2departemen': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Departemen'}),
            'bod': forms.NullBooleanSelect(attrs={'class': 'form-control', 'placeholder': 'BOD?'}),
        }
