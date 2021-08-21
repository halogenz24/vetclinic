from django import forms
from .models import Appointment, TakeAppointment


class CreateAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = "Full Name"
        self.fields['image'].label = "Image"
        self.fields['department'].label = "Department"
        self.fields['start_time'].label = "Start Time"
        self.fields['clinic_name'].label = "Clinic Name"
        self.fields['qualification_name'].label = "Qualification"
        self.fields['institute_name'].label = "Institute"

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Full Name',
            }
        )

        self.fields['department'].widget.attrs.update(
            {
                'placeholder': 'Select Your Service',
            }
        )

        self.fields['start_time'].widget.attrs.update(
            {
                'placeholder': 'Ex : 9 AM',
            }
        )
        self.fields['end_time'].widget.attrs.update(
            {
                'placeholder': 'Ex: 5 PM',
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'Ex : Dasmarinas City Cavite',
            }
        )

        self.fields['clinic_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Clinic Name',
            }
        )

        self.fields['qualification_name'].widget.attrs.update(
            {
                'placeholder': 'Ex : Doctor of Veterinary Medicine, DVM',
            }
        )

        self.fields['institute_name'].widget.attrs.update(
            {
                'placeholder': 'Ex : TUP',
            }
        )

    class Meta:
        model = Appointment
        fields = ['full_name', 'image', 'department', 'start_time', 'end_time', 'location',
                  'clinic_name', 'qualification_name', 'institute_name']

    def is_valid(self):
        valid = super(CreateAppointmentForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(CreateAppointmentForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment


class TakeAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TakeAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['appointment'].label = "Choose Your veterinarian"
        self.fields['full_name'].label = "Full Name"
        self.fields['phone_number'].label = "Phone Number"
        self.fields['pet_name'].label = "Pet name"
        self.fields['Gender_pet'].label = "Gender Pet"
        self.fields['Time_pet'].label = "Time "
        self.fields['message'].label = "Message"

        self.fields['appointment'].widget.attrs.update(
            {
                'placeholder': 'Choose Your veterinarian',
            }
        )

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'Write Your Name',
            }
        )

        self.fields['phone_number'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
            }
        )

        self.fields['pet_name'].widget.attrs.update(
            {
                'placeholder': 'Write your petname',
            }
        )

        self.fields['Gender_pet'].widget.attrs.update(
            {
                'placeholder': 'Gender',
            }
        )
        self.fields['Time_pet'].widget.attrs.update(
            {
                'placeholder': 'Comfort Time',
            }
        )

        self.fields['message'].widget.attrs.update(
            {
                'placeholder': 'Write a short message',
            }
        )

    class Meta:
        model = TakeAppointment
        fields = ['appointment', 'full_name','pet_name' ,'phone_number','Gender_pet','Time_pet','message']

    def is_valid(self):
        valid = super(TakeAppointmentForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(TakeAppointmentForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment




class TakeUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TakeUpdateForm, self).__init__(*args, **kwargs)
        self.fields['appointment'].label = "Choose Your veterinarian"
        self.fields['full_name'].label = "Full Name"
        self.fields['phone_number'].label = "Phone Number"
        self.fields['pet_name'].label = "Pet name"
        self.fields['Gender_pet'].label = "Gender Pet"
        self.fields['Time_pet'].label = "Time "
        self.fields['message'].label = "Message"

        self.fields['appointment'].widget.attrs.update(
            {
                'placeholder': 'Choose Your veterinarian',
            }
        )

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'Write Your Name',
            }
        )

        self.fields['phone_number'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
            }
        )

        self.fields['pet_name'].widget.attrs.update(
            {
                'placeholder': 'Write your petname',
            }
        )

        self.fields['Gender_pet'].widget.attrs.update(
            {
                'placeholder': 'Gender',
            }
        )
        self.fields['Time_pet'].widget.attrs.update(
            {
                'placeholder': 'Comfort Time',
            }
        )

        self.fields['message'].widget.attrs.update(
            {
                'placeholder': 'Write a short message',
            }
        )

    class Meta:
        model = TakeAppointment
        fields = ['appointment', 'full_name','pet_name' ,'phone_number','Gender_pet','Time_pet','message']

    def is_valid(self):
        valid = super(TakeUpdateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(TakeUpdateForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment

