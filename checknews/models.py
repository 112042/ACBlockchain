from django.db import models
import django.utils.timezone as timezone

# Create your models here.

#建立立委身份認證的欄位資料表
class authCommittee(models.Model): 
    id=models.AutoField(auto_created = True, primary_key = True)
    c_name=models.CharField('註冊姓名',max_length=255)         #立委名字
    c_author=models.CharField('註冊身份',max_length=255)       #立委身份
    c_authId=models.CharField('註冊身分證',max_length=255,default='')       #立委身份證
    c_mail=models.CharField('註冊信箱',max_length=255)         #立委信箱
    c_cellphone=models.CharField('註冊電話',max_length=255)    #立委電話
    c_address=models.CharField('註冊服務處',max_length=255)      #立委通訊處
    c_created_at=models.DateTimeField(auto_now = True)    #節點發建立時間  (自動獲取目前時間)
    
    def __str__(self):
        return self.c_name+'\t'+self.c_authId

#建立立委助理身份認證的欄位資料表
class authAssistant(models.Model): 
    committeeId=models.ForeignKey(authCommittee,verbose_name='隸屬身份',on_delete=models.CASCADE)     #關聯立委的id
    a_name=models.CharField('註冊姓名',max_length=255)           #名字
    a_mail=models.CharField('註冊信箱',max_length=255)           #信箱
    a_cellphone=models.CharField('註冊電話',max_length=255)      #電話
    a_created_at=models.DateTimeField(auto_now = True)    #節點發建立時間  (自動獲取目前時間)

    class Meta:
        unique_together=("committeeId","a_name")
    
    def __str__(self):
        return self.a_name+'\t'+'\t'+str(self.committeeId)



