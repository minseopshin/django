from rest_framework import serializers
from.models import ADMIN_REQ, CUST_PAY_INFO, CUST_SHOP_CELL_LIST, SHOP_SVC, REG_SHOP, MBR_SGN, MBR_LOGIN

class ADMIN_REQ_seializers(serializers.ModelSerializer):
    class Meta:
        model = ADMIN_REQ
        fields = '__all__'

class CUST_PAY_INFO_seializers(serializers.ModelSerializer):
    class Meta:
        model = CUST_PAY_INFO
        fields=('CUST_PAY_INFO_CARD_NUM','CUST_PAY_INFO_CARD_EXP_DATE','CUST_PAY_INFO_CARD_PWD',
                'CUST_PAY_INFO_CARD_TEL_NUM','CUST_PAY_INFO_MOBILE_NUM','CUST_PAY_INFO_TIME')

class CUST_SHOP_CELL_LIST_seializers(serializers.ModelSerializer):
    class Meta:
        model = CUST_SHOP_CELL_LIST
        fields=('CUST_SHOP_CELL_LIST_NAME','CUST_SHOP_CELL_LIST_TEL_NUM','CUST_SHOP_CELL_LIST_TIME','CUST_SHOP_CELL_LIST_CREDIT')

class MBR_LOGIN_seializers(serializers.ModelSerializer):
    class Meta:
        model = MBR_LOGIN
        fields=('MBR_LOGIN_ID','MBR_LOGIN_PW','MBR_LOGIN_TIME','MBR_LOGIN_REQ')

class MBR_SGN_seializers(serializers.ModelSerializer):
    class Meta:
        model = MBR_SGN
        fields=('SIGN_NAME','SIGN_GENDER','SIGN_BIRTH','SIGN_PHONE','SIGN_GROUP',
                'SIGN_STORE_NAME','SIGN_ADDRESS','SIGN_ID','SIGN_PW')

class REG_SHOP_seializers(serializers.ModelSerializer):
    class Meta:
        model = REG_SHOP
        fields=('REG_SHOP_NAME','REG_SHOP_TEL_NUM','REG_SHOP_CREDIT')

class SHOP_SVC_seializers(serializers.ModelSerializer):
    class Meta:
        model = SHOP_SVC
        fields=('SHOP_SVC_NAME','SHOP_SERVICE_TEL_NUM','SHOP_SERVICE_ADDR')
