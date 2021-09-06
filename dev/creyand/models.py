from django.db import models
from django.utils import timezone

# Create your models here.
class ADMIN_REQ(models.Model):
    admin_req_type=models.CharField(max_length=200)
    admin_req_tel_num=models.CharField(max_length=200)
    admin_req_time=models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'admin_req'

class CUST_PAY_INFO(models.Model):
    cust_pay_info_card_num=models.CharField(max_length=200)
    cust_pay_info_card_exp_date=models.DateTimeField(default=timezone.now)
    cust_pay_info_card_pwd=models.CharField(max_length=200)
    cust_pay_info_card_tel_num=models.CharField(max_length=200)
    cust_pay_info_mobile_num=models.CharField(max_length=200)
    cust_pay_info_time=models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'cust_pay_info'

class CUST_SHOP_CELL_LIST(models.Model):
    cust_shop_cell_list_name=models.CharField(max_length=200)
    cust_shop_cell_list_tel_num=models.CharField(max_length=200)
    cust_shop_cell_list_time=models.DateTimeField(default=timezone.now)
    cust_shop_cell_list_credit=models.CharField(max_length=200)

    class Meta:
        db_table = 'cust_shop_cell_list'

class MBR_LOGIN(models.Model):
    mbr_login_id=models.CharField(max_length=200)
    mbr_login_pw=models.CharField(max_length=200)
    mbr_login_time=models.DateTimeField(default=timezone.now)
    mbr_login_req=models.CharField(max_length=200)

    class Meta:
        db_table = 'mbr_login'

class MBR_SGN(models.Model):
    sign_name=models.CharField(max_length=200)
    sign_gender=models.CharField(max_length=200)
    sign_birth=models.DateTimeField(default=timezone.now)
    sign_phone=models.CharField(max_length=200)
    sign_group=models.CharField(max_length=200)
    sign_store_name=models.CharField(max_length=200)
    sign_Address=models.CharField(max_length=200)
    sign_id=models.CharField(max_length=200)
    sign_pw=models.CharField(max_length=200)

    class Meta:
        db_table = 'mbr_sgn'

class REG_SHOP(models.Model):
    reg_shop_name=models.CharField(max_length=200)
    reg_shop_tel_num=models.CharField(max_length=200)
    reg_shop_credit=models.CharField(max_length=100)

    class Meta:
        db_table = 'reg_shop'

class SHOP_SVC(models.Model):
    shop_svc_name=models.CharField(max_length=200)
    shop_service_tel_num=models.CharField(max_length=200)
    shop_service_addr=models.CharField(max_length=200)

    class Meta:
        db_table = 'shop_svc'