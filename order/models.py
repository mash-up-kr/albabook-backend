from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class OrderInfo(models.Model):
    table_info = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer_num = models.IntegerField()
    payment = models.BooleanField()
    # 총 금액, 알바생 정보 필요
    price_sum = models.IntegerField(default=0)

    def __str__(self):
        return f'담당자: , 주문번호: {self.id}'

    def get_bill(self):
        price_sum = 0
        order_detail_list = self.orderdetail_set.all()
        for order in order_detail_list:
            price_sum += order.menu_info.price * order.menu_count
        return price_sum

    def save(self, *args, **kwargs):
        # 총 금액 계산해서 저장하도록 한다
        super().save(*args, **kwargs)


class OrderDetail(models.Model):
    order_info = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    menu_info = models.ForeignKey(Menu, on_delete=models.CASCADE)
    menu_count = models.IntegerField()

    def __str__(self):
        return f'주문번호: {self.order_info}, 메뉴 정보: {self.menu_info}, 수량: {self.menu_count}'
