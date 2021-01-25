from django.shortcuts import render, redirect,get_object_or_404   #常用的轉入前端的參數
import requests                                                   #client向server要求的行為
from django.conf import settings
from django.http import HttpResponse                              #在無網頁下，利用http直接做的伺服器回復
from django.http import HttpResponseRedirect                      #伺服器的路徑進行重定向
from django.contrib import auth                                   #導入Django內建相關身份認證函數
from django.contrib.auth.decorators import login_required         #導入Django login_requirement（確保登入的行為）

# Create your views here.

#首頁設定
def home(request):
    #進入網頁馬上給予home.html做顯示
    return render(request,'home.html')