from django.shortcuts import render
from django.db import connection
from .models import t1
# Create your views here.
def list(request):
    sql = "select * from t1_t1"
    cursor = connection.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()

    aa = t1.objects.raw("select * from t1_t1")

    a = t1.objects.all()

    x = 0
    y=[]
    for i in range(1,100):
        ri = np.random.randint(1,1000)
        y.append(ri)
        plt.plot(y)
        plt.pause(0.1)
    plt.show()

    return render(request,'t1/list.html',{'datas':datas, 'a':a,'aa':aa})


