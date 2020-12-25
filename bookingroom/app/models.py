from django.db import models

# Create your models here.
class Account(models.Model):
    class Status:
        OPEN = 0
        BOOKED = 1
    code = models.CharField(max_length=20,verbose_name="Mã tài khoản",unique=True)
    phone = models.CharField(max_length=15,verbose_name="Số điện thoại",null=False)
    name = models.CharField(max_length=50,verbose_name="Họ tên",null=False)
    password = models.CharField(max_length=15,verbose_name="Mật khẩu",null=False)
    gmail = models.CharField(max_length=40,verbose_name="Gmail")
    sex = models.CharField(max_length=5,verbose_name="Giới tính",null=False)
    image = models.ImageField(verbose_name="hình ảnh",upload_to='static/images_staff')
    birthday = models.DateField(verbose_name="Ngày sinh",null=False)
    address = models.CharField(verbose_name="Địa chỉ",max_length=200, null=True)
    lever = models.IntegerField(verbose_name="Loại tài khoản",null=True)
    status = models.IntegerField(verbose_name="Trạng thái tài khoản",null=True)
    def __str__(self):
        return self.name
class Post(models.Model):
    class Status:
        NEXT = 0
        CANCEL = 1
    code = models.ForeignKey(Account,verbose_name="Mã bài đăng",on_delete=models.PROTECT)
    price = models.FloatField(verbose_name="giá dùng")
    description = models.CharField(verbose_name="Mô tả",max_length=500)
    date = models.DateField(verbose_name="Thời gian đăng")
    phone = models.CharField(verbose_name="Số điện thoại liên hệ",max_length=15)
    image = models.ImageField(verbose_name="hình ảnh",upload_to='static/images')
    status = models.IntegerField(verbose_name="Tình trạng phòng")
    view = models.IntegerField(verbose_name="số lượt xem")
    def __str__(self):
        return self.code
class Bill(models.Model):
    code = models.ForeignKey(Post,verbose_name="Bài đăng",on_delete=models.PROTECT)
    money = models.FloatField(verbose_name="Tiền thanh toán")
    day = models.DateField(verbose_name="Thời gian")
    def __str__(self):
        return self.code