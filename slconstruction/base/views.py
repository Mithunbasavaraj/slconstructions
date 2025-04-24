from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm,ProfileForm,ProjectForm,Add_inventoryForm,Inventory_useForm,stocks_in_InventoryForm,Project_daily_work_detailsForm,Project_work_inspection_detailsForm,Material_shiftingForm,project_pre_planForm,project_plan_filesForm
from django.contrib import messages
from .models import Attendance,Profile,Project,Inventory,Inventory_use,stocks_in_Inventory,Project_daily_work_details,Project_work_inspection_details,Material_shifting,project_pre_plan,project_plan_files
from django.utils import timezone
from datetime import date
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    return render(request, "index.html",)

@login_required
def as_view(request):
    logout(request)
    return redirect("base:login")

@login_required
def register(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save()
   var.save()
   Profile.objects.create(user=var)
#    return redirect("base:login")
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup.html", {"form": form})

@login_required
def dashboard(request):
    post=Project.objects.all()
    content={
      "post":post
    }
    return render(request, "dashboard.html",content)

@login_required
def profile(request):
    post = Profile.objects.get(user=request.user)
    return render(request, "profile.html",{"post":post})

@login_required
def update_profile(request):
    current_record = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=current_record)
    if request.method=="POST":
     form = ProfileForm(request.POST or None, request.FILES, instance=current_record)
     if form.is_valid():
        form.save()
        messages.success(request, "Saved Success")
        return redirect('base:profile')
    return render(request, "edit-profile.html",{"form":form,})

@login_required
def project_create(request):
 form = ProjectForm()
 if request.method == "POST":
  form = ProjectForm(request.POST or None)
  if form.is_valid():
   form.save()
   messages.success(request, "Project Created Success")
   return redirect("base:dashboard")
 return render(request, "create_project.html", {"form": form})


#display project
@login_required
def project_details(request,pk):
 try:
    att=Attendance.objects.get(user=request.user,date=date.today())
 except Attendance.DoesNotExist:
    att=None  
 current_record = Project.objects.get(pk=pk)
 return render(request, "project_details.html", {"post":current_record,"att":att})

#display attendance
# display inventory
# 

@login_required
def project_edit(request,pk):
 current_record = Project.objects.get(pk=pk)
 form = ProjectForm(instance=current_record)
 if request.method == "POST":
  form = ProjectForm(request.POST or None,instance=current_record)
  if form.is_valid():
   form.save()
   messages.success(request, "Saved Success")
   return redirect("base:project_details" ,pk=pk)
 return render(request, "create_project.html", {"form": form})

@login_required
def project_delete(request,pk):
 current_record = Project.objects.get(pk=pk)
 current_record.delete()
 messages.success(request, "Project Deleted Successful")
 return redirect("base:dashboard")


  # add inventory //for admin and writer 
@login_required
def add_inventory(request,pk):
 current_record = Project.objects.get(pk=pk)
 form=Add_inventoryForm()    
 if request.method =='POST':
     form = Add_inventoryForm(request.POST, request.FILES)
     if form.is_valid():
      var = form.save(commit=False)
      var.user = request.user
      var.project = current_record
      var.save()
      messages.info(request, "Inventory Added")
      return redirect("base:project_details" ,pk=pk)
     else:
      messages.warning(request,'Please Enter valid input Something went wrong')
 context = {'form': form}
 return render(request, "addinventory.html", context)

@login_required
def add_inventory_more(request,pk):
 current_record = Project.objects.get(pk=pk)
 post=Inventory.objects.filter(project=current_record).order_by('-id')
 context = {'post': post}
 return render(request, "inventory_table.html", context)

@login_required
def add_inventory_details(request,pk):
 current_record = Inventory.objects.get(pk=pk)
 return render(request, "inventory-details.html", {"post":current_record})

@login_required
def add_inventory_delete(request,pk,inv):
 current_record = Inventory.objects.get(pk=pk)
 current_record.delete()
 return redirect("base:add_inventory_more" ,pk=inv)

  # used inventory //for admin and writer
@login_required
def used_inventory(request,pk):
 current_record = Project.objects.get(pk=pk)
 form=Inventory_useForm()    
 if request.method =='POST':
     form = Inventory_useForm(request.POST, request.FILES)
     if form.is_valid():
      var = form.save(commit=False)
      var.user = request.user
      var.project = current_record
      var.save()
      messages.info(request, "Inventory Updated")
      return redirect("base:project_details" ,pk=pk)
     else:
      messages.warning(request,'Please Enter valid input Something went wrong')
 context = {'form': form}
 return render(request, "usedinventory.html", context)

@login_required
def used_inventory_more(request,pk):
 current_record = Project.objects.get(pk=pk)
 post=Inventory_use.objects.filter(project=current_record).order_by('-id')
 context = {'post': post}
 return render(request, "usedinventorytabel.html", context)

@login_required
def used_inventory_detail(request,pk):
 current_record = Inventory_use.objects.get(pk=pk)
 return render(request, "usedinventorydetail.html", {"post":current_record})

@login_required
def used_inventory_delete(request,pk,inv):
 current_record = Inventory_use.objects.get(pk=pk)
 current_record.delete()
 return redirect("base:used_inventory_more" ,pk=inv)

  # in stocks inventory //for admin and writer

@login_required
def in_stock_inventory(request,pk):
 current_record = Project.objects.get(pk=pk)
 form=stocks_in_InventoryForm()    
 if request.method =='POST':
     form = stocks_in_InventoryForm(request.POST, request.FILES)
     if form.is_valid():
      var = form.save(commit=False)
      var.user = request.user
      var.project = current_record
      var.save()
      messages.info(request, "Updated Inventory")
      return redirect("base:project_details" ,pk=pk)
     else:
      messages.warning(request,'Please Enter valid input Something went wrong')
 context = {'form': form}
 return render(request, "instockinventory.html", context)

@login_required
def in_stock_inventory_more(request,pk):
 current_record = Project.objects.get(pk=pk)
 post=stocks_in_Inventory.objects.filter(project=current_record).order_by('-id')
 context = {'post': post}
 return render(request, "instockinventory_table.html", context)

@login_required
def in_stock_inventory_details(request,pk):
 current_record = stocks_in_Inventory.objects.get(pk=pk)
 return render(request, "instockinventory-details.html", {"post":current_record})

@login_required
def in_stock_inventory_delete(request,pk,inv):
 current_record = stocks_in_Inventory.objects.get(pk=pk)
 current_record.delete()
 return redirect("base:in_stock_inventory_more" ,pk=inv)




# Project daily number of workers worker  //for admin and writer
@login_required
def daily_workers(request,pk):
 current_record = Project.objects.get(pk=pk)
 form=Project_daily_work_detailsForm()    
 if request.method =='POST':
     form = Project_daily_work_detailsForm(request.POST, request.FILES)
     if form.is_valid():
      var = form.save(commit=False)
      var.user = request.user
      var.project = current_record
      var.save()
      messages.info(request, "Added")
      return redirect("base:project_details" ,pk=pk)
     else:
      messages.warning(request,'Please Enter valid input Something went wrong')
 context = {'form': form}
 return render(request, "dailyworkrs.html", context )

@login_required
def daily_workers_list(request,pk):
 current_record = Project.objects.get(pk=pk)
 post=Project_daily_work_details.objects.filter(project=current_record).order_by('-id')
 context = {'post': post}
 return render(request, "dailyworkerstabel.html", context)

@login_required
def daily_workers_detail(request,pk):
 current_record = Project_daily_work_details.objects.get(pk=pk)
 context={"post":current_record}
 return render(request, "dailyworkrsdetail.html", context )

@login_required
def daily_workers_delete(request,pk,inv):
 current_record = Project_daily_work_details.objects.get(pk=pk)
 current_record.delete()
 return redirect("base:daily_workers_list" ,pk=inv)

# Project work inspection details by sup dep //for admin and writer

@login_required
def inspection(request,pk):
 current_record = Project.objects.get(pk=pk)
 form=Project_work_inspection_detailsForm()    
 if request.method =='POST':
     form = Project_work_inspection_detailsForm(request.POST, request.FILES)
     if form.is_valid():
      var = form.save(commit=False)
      var.user = request.user
      var.project = current_record
      var.save()
      messages.info(request, "Added")
      return redirect("base:project_details" ,pk=pk)
     else:
      messages.warning(request,'Please Enter valid input Something went wrong')
 context = {'form': form}
 return render(request, "inspection.html", context )

@login_required
def inspection_list(request,pk):
 current_record = Project.objects.get(pk=pk)
 post=Project_work_inspection_details.objects.filter(project=current_record).order_by('-id')
 context = {'post': post}
 print(post)
 return render(request, "inspectiontabel.html", context)

@login_required
def inspection_detail(request,pk):
 current_record = Project_work_inspection_details.objects.get(pk=pk)
 context={"post":current_record}
 return render(request, "inspectiondetails.html", context )

@login_required
def inspection_details_delete(request,pk,inv):
 current_record = Project_work_inspection_details.objects.get(pk=pk)
 current_record.delete()
 return redirect("base:inspection_list" ,pk=inv)


# material shifting details //for admin and writer
@login_required
def material_shifting(request):
 form=Material_shiftingForm()    
 if request.method =='POST':
     form = Material_shiftingForm(request.POST, request.FILES)
     if form.is_valid():
      var = form.save(commit=False)
      var.user = request.user
      var.save()
      messages.info(request, "Added")
      return redirect("base:dashboard")
     else:
      messages.warning(request,'Please Enter valid input Something went wrong')
 context = {'form': form}
 return render(request, "meterialshifting.html",context )

@login_required
def material_shifting_list(request):
 post=Material_shifting.objects.all()
 context = {'post': post}
 return render(request, "meterialshoftingtabel.html", context)
  
@login_required
def material_shifting_detail(request,pk):
 post=Material_shifting.objects.get(pk=pk)
 context = {'post': post}
 return render(request, "merterialshiftingdetail.html", context)

@login_required
def material_shifting_delete(request,pk):
 post=Material_shifting.objects.get(pk=pk)
 post.delete()
 return redirect("base:dashboard")






 #attendance


# punch in

@login_required
def punch_in(request,pk):
   if request.method=="POST": 
    image = request.FILES.get('image')
    lon=request.POST.get("lon")
    lat=request.POST.get("lat")
    project_record = Project.objects.get(pk=pk)
    query=Attendance(user=request.user,project=project_record,date=date.today(),punch_in=timezone.now().time(),punch_in_photo=image,punch_in_lon=lon,punch_in_lat=lat)
    query.save()
    messages.info(request, "Punched In Successfully")
    return redirect("base:project_details" ,pk=pk)

# lunch start
@login_required
def lunch_start(request,pk):
   if request.method=="POST": 
    image = request.FILES.get('image')
    lon=request.POST.get("lon")
    lat=request.POST.get("lat")
    post = Attendance.objects.get(user=request.user,date=date.today())
    post.lunch_start=timezone.now().time()
    post.lunch_start_lat=lat
    post.lunch_start_lon=lon
    post.lunch_in_photo=image
    post.save()
    messages.info(request, "Saved Successfully")
    return redirect("base:project_details" ,pk=pk)

# lunch end
@login_required
def lunch_end(request,pk):
   if request.method=="POST": 
    image = request.FILES.get('image')
    lon=request.POST.get("lon")
    lat=request.POST.get("lat")
    post = Attendance.objects.get(user=request.user,date=date.today())
    post.lunch_end=timezone.now().time()
    post.lunch_end_lat=lat
    post.lunch_end_lon=lon
    post.lunch_out_photo=image
    post.save()
    messages.info(request, "Saved Successfully")
 
    return redirect("base:project_details" ,pk=pk)

# punch out
@login_required
def punch_out(request,pk):
   if request.method=="POST": 
    image = request.FILES.get('image')
    lon=request.POST.get("lon")
    lat=request.POST.get("lat")
    post = Attendance.objects.get(user=request.user,date=date.today())
    post.punch_out=timezone.now().time()
    post.punch_out_lat=lat
    post.punch_out_lon=lon
    post.punch_out_photo=image
    post.save()
    messages.info(request, "Punch Out Successfully")
 
    return redirect("base:project_details" ,pk=pk)

@login_required
def project_plan(request):
 form = project_pre_planForm()
 if request.method == "POST":
  form = project_pre_planForm(request.POST or None)
  if form.is_valid():
    var = form.save(commit=False)
    var.user = request.user
    var.save()
    messages.success(request, "Project Created Success")
    return redirect("base:project_plan_list")
 return render(request, "create_project.html", {"form": form})

@login_required
def project_plan_list(request):
 post=project_pre_plan.objects.all().order_by("-id")
 return render(request, "project-plan.html", {"post": post})

@login_required
def project_plan_details(request,pk):
 post=project_pre_plan.objects.get(pk=pk)
 files=project_plan_files.objects.filter(project_pre_plan=post)
 form = project_plan_filesForm()
 if request.method == "POST":
  form = project_plan_filesForm(request.POST or None, request.FILES)
  if form.is_valid():
    var = form.save(commit=False)
    var.user = request.user
    var.project_pre_plan = post
    var.save()
    messages.success(request, "Project Created Success")
    return redirect("base:project_plan_details", pk=pk)
 return render(request, "project-plan-details.html", {"post":post,"files":files,"form":form})






#view attendance 
#list of profile to admin
#profile details
#display inventory in all projects dashboard sidebar link




# writer add attendance to worker //for admin and writer
# add users to project //for admin