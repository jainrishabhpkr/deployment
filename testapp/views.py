from django.shortcuts import render
from testapp.forms import Inputform
# Create your views here.


def fibonacci(n):
    i = 0
    First_Value = 1
    Second_Value = 1
    while(i < n):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next

           i = i + 1
    return Second_Value


def homeview(request):
    form = Inputform()

    if request.method=="POST":
        form = Inputform(request.POST)

        if form.is_valid():
            input = request.POST.get('input')
            fib_ans = fibonacci(int(input))
            mydict = {'answer':fib_ans}
            print(input)
            return render(request,'testapp/answer.html',context=mydict)

    return render(request,'testapp/home.html',{'form':form})
