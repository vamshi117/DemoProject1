from django.shortcuts import render
import datetime
import time

# Create your views here.
def datetimefunction(request):
    date1 = datetime.datetime.now();
    print(date1);
    date2 = time.ctime();
    dict1 = {"Server_datetime":date1,"server_datetime2":date2}
    return render(request,'FristApp/datetime.html', context=dict1)

def student_datetime(request):
    date1 = datetime.datetime.now();
    date2 = time.ctime();
    rollno = 1001;
    sname = "sai";
    marks = 95;
    dict1 = {'server_datetime':date1,'server_datetime2':date2,'rollno':rollno,'sname':sname,'marks':marks};
    return render(request,'FristApp/student_date_time.html',context=dict1);

def wishes2(request):
    date1 = datetime.datetime.now()
    msg1 = "Hello user ....! Good";
    hr = int(date1.strftime('%H'));
    if hr<12:
        msg1+= 'Morning!!!'
    elif hr<16:
        msg1+='Afternoon!!!'
    elif hr<20:
        msg1+='Evening !!!'
    else:
        msg1 = 'Hello User....Very Good Night!!'
    dict1={'date1':date1, 'msg1':msg1}
    return render(request,'FristApp/wishes.html',context=dict1);