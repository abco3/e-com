from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse



# Create your models here.
CATEGORY_CHOICES = (
    ('SB', 'Shirts And Blouses'),
    ('TS', 'T-Shirts'),
    ('SK', 'Skirts'),
    ('HS', 'Hoodies&Sweatshirts')
)

LABEL_CHOICES = (
    ('S', 'sale'),
    ('N', 'new'),
    ('P', 'promotion')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

PROVINCE_CHOICES = (
    ("กรุงเทพมหานคร","กรุงเทพมหานคร"), ("กาญจนบุรี","กาญจนบุรี"), ("กาฬสินธุ์","กาฬสินธุ์"), ("กำแพงเพชร","กำแพงเพชร"), ("ขอนแก่น","ขอนแก่น"), ("จันทบุรี","จันทบุรี"), ("ฉะเชิงเทรา","ฉะเชิงเทรา"), ("ชลบุรี","ชลบุรี"), ("ชัยนาท","ชัยนาท"), ("ชัยภูมิ","ชัยภูมิ"), ("ชุมพร","ชุมพร"), ("เชียงราย","เชียงราย"), ("เชียงใหม่","เชียงใหม่"), ("ตรัง","ตรัง"), ("ตราด","ตราด"), ("ตาก","ตาก"), ("นครนายก","นครนายก"), ("นครปฐม","นครปฐม"), ("นครพนม","นครพนม"), ("นครราชสีมา","นครราชสีมา"), ("นครศรีธรรมราช","นครศรีธรรมราช"), ("นครสวรรค์","นครสวรรค์"), ("นนทบุรี","นนทบุรี"), ("นราธิวาส","นราธิวาส"), ("น่าน","น่าน"), ("บึงกาฬ","บึงกาฬ"), ("บุรีรัมย์","บุรีรัมย์"), ("ปทุมธานี","ปทุมธานี"), ("ประจวบคีรีขันธ์","ประจวบคีรีขันธ์"), ("ปราจีนบุรี","ปราจีนบุรี"), ("ปัตตานี","ปัตตานี"), ("พระนครศรีอยุธยา","พระนครศรีอยุธยา"), ("พะเยา","พะเยา"), ("พังงา","พังงา"), ("พัทลุง","พัทลุง"), ("พิจิตร","พิจิตร"), ("พิษณุโลก","พิษณุโลก"), ("เพชรบุรี","เพชรบุรี"), ("เพชรบูรณ์","เพชรบูรณ์"), ("แพร่","แพร่"), ("ภูเก็ต","ภูเก็ต"), ("มหาสารคาม","มหาสารคาม"), ("มุกดาหาร","มุกดาหาร"), ("แม่ฮ่องสอน","แม่ฮ่องสอน"), ("ยโสธร","ยโสธร"), ("ยะลา","ยะลา"), ("ร้อยเอ็ด","ร้อยเอ็ด"), ("ระนอง","ระนอง"), ("ระยอง","ระยอง"), ("ราชบุรี","ราชบุรี"), ("ลพบุรี","ลพบุรี"), ("เลย","เลย"), ("ลำปาง","ลำปาง"), ("ลำพูน","ลำพูน"), ("ศรีสะเกษ","ศรีสะเกษ"), ("สกลนคร","สกลนคร"), ("สงขลา","สงขลา"), ("สตูล","สตูล"), ("สมุทรปราการ","สมุทรปราการ"), ("สมุทรสงคราม","สมุทรสงคราม"), ("สมุทรสาคร","สมุทรสาคร"), ("สระแก้ว","สระแก้ว"), ("สระบุรี","สระบุรี"), ("สิงห์บุรี","สิงห์บุรี"), ("สุโขทัย","สุโขทัย"), ("สุพรรณบุรี","สุพรรณบุรี"), ("สุราษฎร์ธานี","สุราษฎร์ธานี"), ("สุรินทร์","สุรินทร์"), ("หนองคาย","หนองคาย"), ("หนองบัวลำภู","หนองบัวลำภู"), ("อ่างทอง","อ่างทอง"), ("อำนาจเจริญ","อำนาจเจริญ"), ("อุดรธานี","อุดรธานี"), ("อุตรดิตถ์","อุตรดิตถ์"), ("อุทัยธานี","อุทัยธานี"), ("อุบลราชธานี","อุบลราชธานี")
)


class Slide(models.Model):
    caption1 = models.CharField(max_length=100)
    caption2 = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    image = models.ImageField(help_text="Size: 1920x570")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.caption1, self.caption2)

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    banner = models.ImageField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:category", kwargs={
            'slug': self.slug
        })


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    stock_no = models.CharField(max_length=10)
    description_short = models.CharField(max_length=50)
    description_long = models.TextField()
    image = models.ImageField()
    image2 = models.ImageField(null=True,blank=True)
    image3 = models.ImageField(null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'BillingAddress', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'BillingAddress', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    reciept = models.FileField(upload_to='reciept', null=True)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a BillingAddress
    (Failed Checkout)
    3. Payment
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=10, null=True)
    street_address = models.CharField(max_length=100, null=True)
    province = models.CharField(max_length=50, choices = PROVINCE_CHOICES,default = '1')
    amphur = models.CharField(max_length=50, null=True)
    tambol = models.CharField(max_length=50, null=True)
    zip = models.CharField(max_length=5)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'BillingAddresses'


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"

class MobilePhone(models.Model):
    model = models.CharField(max_length=50)