import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import User


designation_choice = (
   ("Engineer", "Engineer"),
   ("Department Engineer", "Department Engineer"),
   ("Supervisor", "Supervisor"),
   ("Site Supervisor", "Site Supervisor"),
   ("Site Worker Writer", "Site Worker Writer"),
   ("Mestri", "Mestri"),
   ("Worker", "Worker"),

)
worker_choice = (
("Gare Workers","Gare Workers"),
("Male Helper","Male Helper"),
("Female Helper","Female Helper"),
("Paint Workers","Paint Workers"),
("Electrical Workers","Electrical Workers"),
("Plumbing Workers","Plumbing Workers"),
("Granite Workers","Granite Workers"),
("Tile Workers","Tile Workers"),
("Welding Workers","Welding Workers"),
("Aluminum Window Workers","Aluminum Window Workers"),
("ACC Workers","ACC Workers"),
("Stone Cladding Workers","Stone Cladding Workers"),
("Batch Workers","Batch Workers"),
("Structural Workers","Structural Workers"),
("Borewell Workers","Borewell Workers"),
("Street Light Workers","Street Light Workers"),
("UPS Workers","UPS Workers"),
("CC Camera Workers","CC Camera Workers"),
("LED Name Board Workers","LED Name Board Workers"),


)
product_choice = (
("M Sand", "M Sand"),
("P Sand", "P Sand"),
("Cement", "Cement"),
("Stone - 20mm", "Stone - 20mm"),
("Stone - 40mm", "Stone - 40mm"),
("Stone - 60mm", "Stone - 60mm"),
("RMC", "RMC"),
("Steel", "Steel"),
("Granite", "Granite"),
("Aluminum Window", "Aluminum Window"),
("ACP", "ACP"),
("Sanitary Item", "Sanitary Item"),
("Electric Item", "Electric Item"),
("Bricks", "Bricks"),
("Concrete Solid Blocks 4", "Concrete Solid Blocks 4"),
("Concrete Solid Blocks 6", "Concrete Solid Blocks 6"),
("Concrete Solid Blocks 8", "Concrete Solid Blocks 8"),
("PVC Pipes", "PVC Pipes"),
("GI Pipes", "GI Pipes"),
("Borewell Pumpset Materials", "Borewell Pumpset Materials"),
("School desk and furniture", "School desk and furniture"),
("Green Board and Notice Board", "Green Board and Notice Board"),
("UPS and Batteries", "UPS and Batteries"),
("LED Street light", "LED Street light"),
("Street light High Mast Poles", "Street light High Mast Poles"),
("Stones", "Stones"),

)
vehicle_choice={
    ("JCB", "JCB"),
    ("Tractor", "Tractor"),
    ("Tipper", "Tipper"),
    ("Lorre", "Lorre"),
    ("Tata-ace", "Tata-ace"),
    ("Canter", "Canter"),   
    ("Auto", "Auto"),   
}
Material_name_choice={
    ("Debris", "Debris"), 
    ("M Sand", "M Sand"),
("P Sand", "P Sand"),
("Cement", "Cement"),
("Stone - 20mm", "Stone - 20mm"),
("Stone - 40mm", "Stone - 40mm"),
("Stone - 60mm", "Stone - 60mm"),
("RMC", "RMC"),
("Steel", "Steel"),
("Granite", "Granite"),
("Aluminum Window", "Aluminum Window"),
("ACP", "ACP"),
("Sanitary Item", "Sanitary Item"),
("Electric Item", "Electric Item"),
("Bricks", "Bricks"),
("Concrete Solid Blocks 4", "Concrete Solid Blocks 4"),
("Concrete Solid Blocks 6", "Concrete Solid Blocks 6"),
("Concrete Solid Blocks 8", "Concrete Solid Blocks 8"),
("PVC Pipes", "PVC Pipes"),
("GI Pipes", "GI Pipes"),
("Borewell Pumpset Materials", "Borewell Pumpset Materials"),
("School desk and furniture", "School desk and furniture"),
("Green Board and Notice Board", "Green Board and Notice Board"),
("UPS and Batteries", "UPS and Batteries"),
("LED Street light", "LED Street light"),
("Street light High Mast Poles", "Street light High Mast Poles"),
("Stones", "Stones"), 
    
    
}
state_choice={
     ("Karnataka","Karnataka"),
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh","Arunachal Pradesh"),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Delhi","Delhi"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jharkhand","Jharkhand"),
    ("Kerala","Kerala"),
    ("Maharashtra","Maharashtra"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("TamilNadu","TamilNadu"),
    ("Tripura","Tripura"),
    ("Telangana","Telangana"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),
    ("Jammu & Kashmir","Jammu & Kashmir"),
    ("Ladakh","Ladakh"),
    ("Andaman & Nicobar","Andaman & Nicobar"),
    ("Chandigarh","Chandigarh"),
    ("Lakshadweep","Lakshadweep"),
    ("Puducherry","Puducherry"),
    ("Dadra & Nagar Haveli & Daman & Diu","Dadra & Nagar Haveli & Daman & Diu"),
    
}
gender_choice={
    ("Male","Male"),
    ("Female","Female"),
    ("Others","Others"),
}
marital_status_choice={
    ("Single","Single"),
    ("Married","Married"),
    
}
class User(AbstractUser):
   designation = models.CharField(max_length = 20, choices = designation_choice, null=True, blank=True)

   def __str__(self):
      return self.email
   
class Profile(models.Model) :
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   address=models.TextField(default="", blank=True)
   image=models.ImageField(upload_to='profile/' ,blank=True,)
   occupation=models.CharField(max_length=155, default="", blank=True)
   gender=models.CharField(max_length=55, choices = gender_choice, default="", blank=True)
   marital_status=models.CharField(max_length=155, choices=marital_status_choice, default="", blank=True)
   age=models.IntegerField( default=0, blank=True)
   nationality=models.CharField(max_length=55, default="", blank=True)
   state=models.CharField(max_length=155,choices = state_choice, default="", blank=True)
   aadhar=models.CharField(max_length=55, default="", blank=True)
   pan=models.CharField(max_length=55, default="", blank=True)
   bank_account=models.CharField(max_length=55, default="", blank=True)
   bank_account_name=models.CharField(max_length=155, default="", blank=True)
   bank_account_bank_name=models.CharField(max_length=155, default="", blank=True)
   bank_account_branch_name=models.CharField(max_length=155, default="", blank=True)
   ifsc_code=models.CharField(max_length=55, default="", blank=True)
   role = models.CharField(max_length = 135, choices = worker_choice, null=True, blank=True)

   def __str__(self):
     return self.user.first_name
   

    
class Project(models.Model):
   # user = models.ForeignKey(User, on_delete=models.CASCADE)
   project_name=models.CharField(max_length=255, default="", blank=True)
   address=models.TextField(default="", blank=True)
   date = models.DateTimeField(auto_now_add=True, blank=True)

   def __str__(self):
      return self.project_name
    
class Attendance(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
   date = models.DateField(default=timezone.now)
   punch_in = models.TimeField(null=True, blank=True)
   lunch_start = models.TimeField(null=True, blank=True)
   lunch_end = models.TimeField(null=True, blank=True)
   punch_out = models.TimeField(null=True, blank=True)
   punch_in_photo = models.ImageField(upload_to='attendance/' ,blank=True,)
   punch_out_photo= models.ImageField(upload_to='attendance/' ,blank=True,)
   lunch_in_photo= models.ImageField(upload_to='attendance/' ,blank=True,)
   lunch_out_photo= models.ImageField(upload_to='attendance/' ,blank=True,)
   punch_in_lon=models.CharField(max_length=255, default="", blank=True)
   punch_in_lat=models.CharField(max_length=255, default="", blank=True)
   punch_out_lon=models.CharField(max_length=255, default="", blank=True)
   punch_out_lat=models.CharField(max_length=255, default="", blank=True)
   lunch_start_lon=models.CharField(max_length=255, default="", blank=True)
   lunch_start_lat=models.CharField(max_length=255, default="", blank=True)
   lunch_end_lon=models.CharField(max_length=255, default="", blank=True)
   lunch_end_lat=models.CharField(max_length=255, default="", blank=True)

   def get_work_duration(self):
        if self.punch_in and self.punch_out:
            punch_in_dt = datetime.datetime.combine(self.date, self.punch_in)
            punch_out_dt = datetime.datetime.combine(self.date, self.punch_out)
            work_duration = punch_out_dt - punch_in_dt

            lunch_duration = datetime.timedelta()
            if self.lunch_start and self.lunch_end:
                lunch_start_dt = datetime.datetime.combine(self.date, self.lunch_start)
                lunch_end_dt = datetime.datetime.combine(self.date, self.lunch_end)
                lunch_duration = lunch_end_dt - lunch_start_dt

            return work_duration - lunch_duration
        return None

   def formatted_work_duration(self):
        duration = self.get_work_duration()
        if duration:
            total_seconds = int(duration.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes = remainder // 60
            return f"{hours:02}:{minutes:02}"
        return False
   
   def __str__(self):
      return self.user.first_name
  
class Inventory(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
   name=models.CharField(max_length=255, choices=product_choice,default="", blank=True)
   qty=models.CharField(max_length=25, default="", blank=True)
   price=models.CharField(max_length=25, default="", blank=True)
   image=models.ImageField(upload_to='inventory/' ,blank=True,)
   invoice_image=models.ImageField(upload_to='inventory/' ,blank=True,)
   date = models.DateTimeField(auto_now_add=True, blank=True)
   lon=models.CharField(max_length=255, default="", blank=True)
   lat=models.CharField(max_length=255, default="", blank=True)

   def __str__(self):
        return self.name

class stocks_in_Inventory(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
   name=models.CharField(max_length=255, choices=product_choice,default="", blank=True)
   qty=models.CharField(max_length=25, default="", blank=True)
   price=models.CharField(max_length=25, default="", blank=True)
   image=models.ImageField(upload_to='inventory/' ,blank=True,)
   date = models.DateTimeField(auto_now_add=True, blank=True)
   lon=models.CharField(max_length=255, default="", blank=True)
   lat=models.CharField(max_length=255, default="", blank=True)

   def __str__(self):
        return self.name

class Inventory_use(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
   name=models.CharField(max_length=255, choices=product_choice,default="", blank=True)
   qty=models.CharField(max_length=25, default="", blank=True)
   image=models.ImageField(upload_to='inventory/' ,blank=True,)
   date = models.DateTimeField(auto_now_add=True, blank=True)
   lon=models.CharField(max_length=255, default="", blank=True)
   lat=models.CharField(max_length=255, default="", blank=True)

   def __str__(self):
        return self.name
   
   
class Project_daily_work_details(models.Model):
   date = models.DateTimeField(auto_now_add=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project,  blank=True, null=True, on_delete=models.CASCADE)
   no_of_workers=models.CharField(max_length=25, default="", blank=True)
   image=models.ImageField(upload_to='uploads/' ,blank=True,)
   project_work_status=models.CharField(max_length=225, default="", blank=True,)
   lon=models.CharField(max_length=255, default="", blank=True)
   lat=models.CharField(max_length=255, default="", blank=True)

   def __str__(self):
       return self.user.first_name

class Project_work_inspection_details(models.Model):
   date = models.DateTimeField(auto_now_add=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project,  blank=True, null=True, on_delete=models.CASCADE)
   no_of_workers=models.CharField(max_length=25, default="", blank=True)
   image=models.ImageField(upload_to='uploads/' ,blank=True,)
   project_work_status=models.CharField(max_length=225, default="", blank=True,)
   lon=models.CharField(max_length=255, default="", blank=True)
   lat=models.CharField(max_length=255, default="", blank=True)

   def __str__(self):
       return self.user.first_name
    
class Material_shifting(models.Model):
   date = models.DateTimeField(auto_now_add=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project,  blank=True, null=True, on_delete=models.CASCADE, related_name="from_project")
   to_project = models.ForeignKey(Project,  blank=True, null=True, on_delete=models.CASCADE, related_name="to_project")
   vehicle= models.CharField(max_length=255, choices=vehicle_choice,default="", blank=True)
   image=models.ImageField(upload_to='uploads/' ,blank=True,)
   Material_name=models.CharField(max_length=225,choices=Material_name_choice, default="", blank=True,)
   lon=models.CharField(max_length=255, default="", blank=True)
   lat=models.CharField(max_length=255, default="", blank=True)

   def __str__(self):
       return self.user.first_name


class project_pre_plan(models.Model):
   date = models.DateTimeField(auto_now_add=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project_name=models.CharField(max_length=255, default="", blank=True)
   address=models.TextField(default="", blank=True)

   def __str__(self):
       return self.project_name
   
   
class project_plan_files(models.Model):
   file = models.FileField(upload_to='uploads/')
   file_name=models.CharField(max_length=255, default="", blank=True)
   project_pre_plan = models.ForeignKey(project_pre_plan, on_delete=models.CASCADE)
   date = models.DateTimeField(auto_now_add=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
       return self.file_name

#group of bill for who
#multiple files for upload
#bill generate
#bill items

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    # other client details
    def __str__(self):
       return self.name
    
class bill_files(models.Model):
   file = models.FileField(upload_to='uploads/')
   file_name=models.CharField(max_length=255, default="", blank=True)
   Client = models.ForeignKey(Client, on_delete=models.CASCADE)
   date = models.DateTimeField(auto_now_add=True, blank=True)

   def __str__(self):
       return self.file_name
   
class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50, unique=True)
    date_issued = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # other invoice details
    def __str__(self):
       return self.date_issued

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    # other item details
    def __str__(self):
       return self.quantity