from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from base.models import Profile,Project,Inventory,Inventory_use,stocks_in_Inventory,Project_daily_work_details,Project_work_inspection_details,Material_shifting,project_pre_plan,project_plan_files
from django import forms


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','first_name','last_name','email','password1','password2','designation']


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields =('__all__')
		exclude = ('user',)
            
class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields =('__all__')
		exclude = ('date',)

class Add_inventoryForm(forms.ModelForm):
	class Meta:
		model = Inventory
		fields =('__all__')
		exclude = ('user','project',)

class Inventory_useForm(forms.ModelForm):
	class Meta:
		model = Inventory_use
		fields =('__all__')
		exclude = ('user','project',)

class stocks_in_InventoryForm(forms.ModelForm):
	class Meta:
		model = stocks_in_Inventory
		fields =('__all__')
		exclude = ('user','project',)

class Project_daily_work_detailsForm(forms.ModelForm):
	class Meta:
		model = Project_daily_work_details
		fields =('__all__')
		exclude = ('user','project',)

class Project_work_inspection_detailsForm(forms.ModelForm):
	class Meta:
		model = Project_work_inspection_details
		fields =('__all__')
		exclude = ('user','project',)

class Material_shiftingForm(forms.ModelForm):
	class Meta:
		model = Material_shifting
		fields =('__all__')
		exclude = ('user',)

class project_pre_planForm(forms.ModelForm):
	class Meta:
		model = project_pre_plan
		fields =('__all__')
		exclude = ('user',)

class project_plan_filesForm(forms.ModelForm):
	class Meta:
		model = project_plan_files
		fields =('__all__')
		exclude = ('user','project_pre_plan',)