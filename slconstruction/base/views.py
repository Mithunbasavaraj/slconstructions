import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm,ProfileForm,ProjectForm,Add_inventoryForm,Inventory_useForm,stocks_in_InventoryForm,Project_daily_work_detailsForm,Project_work_inspection_detailsForm,Material_shiftingForm,project_pre_planForm,project_plan_filesForm,Material_shifting_editForm,Material_shifting_receivedForm,RegisterUserForm1
from django.contrib import messages
from .models import Attendance,Profile,Project,Inventory,Inventory_use,stocks_in_Inventory,Project_daily_work_details,Project_work_inspection_details,Material_shifting,project_pre_plan,project_plan_files,User,Project_investor,Material_shifting_received  
from datetime import date
from django.db.models import Q

def home(request):
    return render(request, "index.html",)

@login_required
def as_view(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect("base:login")

@login_required
def register(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save()
   var.save()
   p=Profile.objects.create(user=var)
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
   messages.success(request, "User Create Success")
#    return redirect("base:login")
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup.html", {"form": form})




@login_required
def register_engineer(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Engineer"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})

@login_required
def register_department_engineer(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Department Engineer"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})

@login_required
def register_supervisor(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Supervisor"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})


@login_required
def register_site_supervisor(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Site Supervisor"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})

@login_required
def register_site_worker_writer(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Site Worker Writer"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})

@login_required
def register_mestri(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Mestri"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})

@login_required
def register_worker(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Worker"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})

@login_required
def register_supplier(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Supplier"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})


@login_required
def register_founder(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Founder"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})

@login_required
def register_owner(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Owner"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})

@login_required
def register_chairman(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Chairman"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})

@login_required
def register_ceo(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "CEO"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})

@login_required
def register_partner(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Partner"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})



@login_required
def register_shop_owner(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Shop Owner"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})


@login_required
def register_investor(request):
 if request.method == "POST":
  form = RegisterUserForm(request.POST or None)
  if form.is_valid():
   var = form.save(commit=False)
   var.designation = "Investor"
   var.save()
   p=Profile.objects.create(user=var)
   messages.success(request, "User Create Success")
   return redirect('base:admin_update_profile', pk=p.id,u=var.id)
 else:
  form = RegisterUserForm()
 return render(request, "registration/signup1.html", {"form": form})


 

@login_required
def dashboard(request):
    post=Project.objects.all().order_by('-id')
    if request.user.designation == "Founder" or request.user.designation == "Investor":
      post=Project_investor.objects.filter(user=request.user).order_by('-id')
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
 all_att=Attendance.objects.filter(user=request.user).order_by('-id')

 context={
   "post":current_record,
   "att":att,
   "date":date.today(),
   "all_att":all_att
   }
 
 return render(request, "project_details.html", context)

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
def add_inventory_all(request):
 post=Inventory.objects.all().order_by("-id")
 context = {'post': post}
 return render(request, "inventory_table-all.html", context)

@login_required
def add_inventory_details(request,pk):
 current_record = Inventory.objects.get(pk=pk)
 return render(request, "inventory-details.html", {"post":current_record})

@login_required
def add_inventory_delete(request,pk,inv):
 current_record = Inventory.objects.get(pk=pk)
 current_record.delete()
 return redirect("base:add_inventory_more" ,pk=inv)

@login_required
def add_inventory_edit(request,pk):
  current_record = Inventory.objects.get(pk=pk)
  form = Add_inventoryForm(instance=current_record)
  if request.method=="POST":
     form = Add_inventoryForm(request.POST or None, request.FILES, instance=current_record)
     if form.is_valid():
        form.save()
        messages.success(request, "Saved Success")
        return redirect('base:add_inventory_details', pk=pk)
  return render(request, "addinventory-edit.html",{"form":form,})

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

@login_required
def used_inventory_all(request):
 post=Inventory_use.objects.all().order_by("-id")
 context = {'post': post}
 return render(request, "usedinventorytabel-all.html", context)

@login_required
def used_inventory_edit(request,pk):
  current_record = Inventory_use.objects.get(pk=pk)
  form = Inventory_useForm(instance=current_record)
  if request.method=="POST":
     form = Inventory_useForm(request.POST or None, request.FILES, instance=current_record)
     if form.is_valid():
        form.save()
        messages.success(request, "Saved Success")
        return redirect('base:used_inventory_detail', pk=pk)
  return render(request, "usedinventory-edit.html",{"form":form,})


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
def in_stock_inventory_all(request):
 post=stocks_in_Inventory.objects.all().order_by("-id")
 context = {'post': post}
 return render(request, "instockinventory_table-all.html", context)

@login_required
def in_stock_inventory_details(request,pk):
 current_record = stocks_in_Inventory.objects.get(pk=pk)
 return render(request, "instockinventory-details.html", {"post":current_record})

@login_required
def in_stock_inventory_delete(request,pk,inv):
 current_record = stocks_in_Inventory.objects.get(pk=pk)
 current_record.delete()
 return redirect("base:in_stock_inventory_more" ,pk=inv)

@login_required
def in_stock_inventory_edit(request,pk):
  current_record = stocks_in_Inventory.objects.get(pk=pk)
  form = stocks_in_InventoryForm(instance=current_record)
  if request.method=="POST":
     form = stocks_in_InventoryForm(request.POST or None, request.FILES, instance=current_record)
     if form.is_valid():
        form.save()
        messages.success(request, "Saved Success")
        return redirect('base:in_stock_inventory_details', pk=pk)
  return render(request, "instockinventory-edit.html",{"form":form,})

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
def daily_workers_all(request):
 post=Project_daily_work_details.objects.all().order_by("-id")
 context = {'post': post}
 return render(request, "dailyworkerstabel-tabel.html", context)

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

@login_required
def daily_workers_edit(request,pk):
  current_record = Project_daily_work_details.objects.get(pk=pk)
  form = Project_daily_work_detailsForm(instance=current_record)
  if request.method=="POST":
     form = Project_daily_work_detailsForm(request.POST or None, request.FILES, instance=current_record)
     if form.is_valid():
        form.save()
        messages.success(request, "Saved Success")
        return redirect('base:daily_workers_detail', pk=pk)
  return render(request, "dailyworkrs-edit.html",{"form":form,})

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
def Project_work_inspection_details_all(request):
 post=Project_work_inspection_details.objects.all().order_by("-id")
 context = {'post': post}
 return render(request, "inspectiontabel-all.html", context)

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

@login_required
def inspection_details_edit(request,pk):
  current_record = Project_work_inspection_details.objects.get(pk=pk)
  form = Project_work_inspection_detailsForm(instance=current_record)
  if request.method=="POST":
     form = Project_work_inspection_detailsForm(request.POST or None, request.FILES, instance=current_record)
     if form.is_valid():
        form.save()
        messages.success(request, "Saved Success")
        return redirect('base:inspection_detail', pk=pk)
  return render(request, "inspection-edit.html",{"form":form,})

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
 messages.success(request, "Deleted Success")
 return redirect("base:dashboard")

@login_required
def material_shifting_edit(request,pk):
  current_record = Material_shifting.objects.get(pk=pk)
  form = Material_shifting_editForm(instance=current_record)
  if request.method=="POST":
     form = Material_shifting_editForm(request.POST or None, request.FILES, instance=current_record)
     if form.is_valid():
        form.save()
        messages.success(request, "Saved Success")
        return redirect('base:material_shifting_detail', pk=pk)
  return render(request, "meterialshifting-edit.html",{"form":form,})

# material shifting received recived
@login_required
def material_shifting_received(request,pk):
 current_record = Project.objects.get(pk=pk)
 form=Material_shifting_receivedForm()
 if request.method =='POST':
     form = Material_shifting_receivedForm(request.POST, request.FILES)
     if form.is_valid():
      var = form.save(commit=False)
      var.user = request.user
      var.project = current_record
      var.save()
      messages.info(request, "Saved Successfully")
      return redirect("base:project_details",pk=pk)
     else:
      messages.warning(request,'Please Enter valid input Something went wrong')
 context = {'form': form}
 return render(request, "meterialshifting-recived.html",context )

#display material shifting received
@login_required
def material_shifting_received_list(request,pk):
 current_record = Project.objects.get(pk=pk)
 post=Material_shifting_received.objects.filter(project=current_record).order_by('-id')
 context = {'post': post}
 return render(request, "meterialshifting-recived-tabel.html", context)

@login_required
def material_shifting_received_list_all(request):
 post=Material_shifting_received.objects.all().order_by('-id')
 context = {'post': post}
 return render(request, "meterialshifting-recived-tabel-all.html", context)


#details of material shifting received
@login_required
def material_shifting_received_detail(request,pk):
 current_record = Material_shifting_received.objects.get(pk=pk)
 context = {'post': current_record}
 return render(request, "meterialshifting-recived-details.html", context)

 #delete material shifting received
@login_required
def material_shifting_received_delete(request,pk,p):
 current_record = Material_shifting_received.objects.get(pk=pk)
 current_record.delete()
 messages.success(request, "Deleted Success")
 return redirect("base:material_shifting_received_list",pk=p)


@login_required
def material_shifting_received_edit(request,pk,p):
 current_record = Material_shifting_received.objects.get(pk=pk)
 project_record = Project.objects.get(pk=p)
 form = Material_shifting_receivedForm(instance=current_record)
 if request.method=="POST":
  form = Material_shifting_receivedForm(request.POST or None, request.FILES, instance=current_record) 
  var = form.save(commit=False)
  var.project = project_record
  var.save()
  messages.success(request, "Saved Success")
  return redirect("base:material_shifting_received_list",pk=p)
 return render(request, "meterialshifting-recived-edit.html",{"form":form,})

# Project_investor
@login_required
def project_investor(request,pk):
 post=Project.objects.get(pk=pk)
 project_investor=Project_investor.objects.filter(project=post)
 print(project_investor)
 current_record = User.objects.filter(Q(designation__icontains="Investor") | Q(designation__icontains="Partner"))
 print(current_record)
 if request.method=="POST":
  investor=request.POST.get("investor")
  if Project_investor.objects.filter(user=User.objects.get(pk=investor),project=post).exists():
   messages.warning(request, "Investor or partner already exists")
   return redirect("base:project_details",pk=pk)
  else:
   project_investor=Project_investor(user=User.objects.get(pk=investor),project=post)
   project_investor.save()
   messages.success(request, "Saved Success")
   return redirect("base:project_details",pk=pk)
 return render(request, "add-investor.html",{"post":current_record,"project":post,"investor":project_investor})
 
     

#list of investor
@login_required
def list_of_investor(request):
 project_investor=Project_investor.objects.all().order_by('-id')
 return render(request, "investor-list.html",{"post":project_investor})


#delete investor
@login_required
def delete_investor(request,pk):
 current_record = Project_investor.objects.get(pk=pk)
 current_record.delete()
 messages.success(request, "Deleted Success")
 return redirect("base:list_of_investor")

 #attendance
@login_required
def punch_in(request,pk):
   if request.method=="POST": 
    image = request.FILES.get('image')
    lon=request.POST.get("lon")
    lat=request.POST.get("lat")
    project_record = Project.objects.get(pk=pk)
    query=Attendance(user=request.user,project=project_record,date=date.today(),punch_in=datetime.datetime.now().strftime("%H:%M:%S"),punch_in_photo=image,punch_in_lon=lon,punch_in_lat=lat)
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
    post.lunch_start=datetime.datetime.now().strftime("%H:%M:%S")
    post.lunch_start_lat=lat
    post.lunch_start_lon=lon
    post.lunch_in_photo=image
    project_record = Project.objects.get(pk=pk)
    post.project_lunch_start=project_record
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
    post.lunch_end=datetime.datetime.now().strftime("%H:%M:%S")
    post.lunch_end_lat=lat
    post.lunch_end_lon=lon
    post.lunch_out_photo=image
    project_record = Project.objects.get(pk=pk)
    post.project_lunch_end=project_record
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
    post.punch_out=datetime.datetime.now().strftime("%H:%M:%S")
    post.punch_out_lat=lat
    post.punch_out_lon=lon
    post.punch_out_photo=image
    project_record = Project.objects.get(pk=pk)
    post.project_punch_out=project_record
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
def project_plan_name_edit(request,pk):
  current_record = project_pre_plan.objects.get(pk=pk)
  form = project_pre_planForm(instance=current_record)
  if request.method=="POST":
     form = project_pre_planForm(request.POST or None, request.FILES, instance=current_record)
     if form.is_valid():
        form.save()
        messages.success(request, "Saved Success")
        return redirect('base:project_plan_details', pk=pk)
  return render(request, "create_project.html",{"form":form,})

@login_required
def project_plan_name_delete(request,pk):
 current_record = project_pre_plan.objects.get(pk=pk)
 current_record.delete()
 messages.success(request, "Deleted Success")
 return redirect("base:project_plan_list")

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
 return render(request, "project-plan-details.html", {"project":post,"files":files,"form":form})

@login_required
def project_plan_delete(request,pk,re):
 post=project_plan_files.objects.get(pk=pk)
 post.delete()
 messages.success(request, "Deleted Success")
 return redirect("base:project_plan_details", pk=re)

@login_required
def project_plan_edit(request,pk):
  current_record = project_plan_files.objects.get(pk=pk)
  form = project_plan_filesForm(instance=current_record)
  if request.method=="POST":
     form = project_plan_filesForm(request.POST or None, request.FILES, instance=current_record)
     if form.is_valid():
        form.save()
        messages.success(request, "Saved Success")
        return redirect('base:project_plan_details', pk=pk)
  return render(request, "project-plan-details.html",{"form":form,})

@login_required
def user_attendance(request):
    post=Attendance.objects.filter(user=request.user).order_by('-id')
    return render(request, "attednance-tabel.html",{"post":post,})

@login_required
def all_attendance(request):
    to_date=date.today()
    if request.GET.get('date'):
      to_date=request.GET.get('date')
    post=Attendance.objects.filter(date=to_date).order_by('-id')
    return render(request, "attednance-tabel-all-today.html",{"post":post,})

@login_required
def worker_list(request):
   post=User.objects.all().order_by('-id')  
   return render(request, "workers-list.html",{"post":post,})

@login_required
def worker_attendance_list(request,pk):
  user=User.objects.get(pk=pk)
  post=Attendance.objects.filter(user=user).order_by('-id')
  from_date=request.GET.get('from_date')
  to_date=request.GET.get('to_date')
  if from_date and to_date:
    post=Attendance.objects.filter(user=user,date__gte=from_date,date__lte=to_date).order_by('-id')
  return render(request, "attednance-tabel-all.html",{"post":post,})


@login_required
def attendance_details(request,pk): 
    post=Attendance.objects.get(pk=pk)
    return render(request, "attendance-details.html",{"post":post,})

@login_required
def admin_profile(request,pk):
    user=User.objects.get(pk=pk)
    post=Profile.objects.get(user=user)
    return render(request, "profile-admin.html",{"post":post,})

@login_required
def admin_update_profile(request,pk,u):
    current_record = Profile.objects.get(pk=pk)
    form = ProfileForm(instance=current_record)
    if request.method=="POST":
     form = ProfileForm(request.POST or None, request.FILES, instance=current_record)
     if form.is_valid():
        form.save()
        messages.success(request, "Saved Success")
        return redirect('base:admin_profile', pk=u)
    return render(request, "edit-profile.html",{"form":form,})

#bills

@login_required
def bills(request):
  post=bills.objects.all().order_by('-id')
  return render(request, "bills.html",{"post":post,})




