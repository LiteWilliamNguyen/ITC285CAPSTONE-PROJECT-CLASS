from django.test import TestCase
from django.urls import reverse
from .models import Product, Monk, Member
from django.contrib.auth.models import User
from .forms import ProductForm, MonkForm, MemberForm
import datetime
# Create your tests here.

class ProductTest(TestCase):
    def test_string(self):
        type=Product(productname="Heart Sutras")
        self.assertEqual(str(type),type.productname)

    def test_table(self):
        self.assertEqual(str(Product._meta.db_table), 'Product')

class MonkTest(TestCase):
    def test_string(self):
        type=Monk(monkname="Henry Beckman")
        self.assertEqual(str(type),type.monkname)

    def test_table(self):
        self.assertEqual(str(Monk._meta.db_table), 'Monk')

class MemberTest(TestCase):
    def test_string(self):
        type=Member(membername="Bob Rylan")
        self.assertEqual(str(type),type.membername)

    def test_table(self):
        self.assertEqual(str(Member._meta.db_table), 'Member')


class Monk_Form_Test(TestCase):
    def setUp(self):
        self.user=User.objects.create(username="user1", password="P@ssw0rd1")
        self.monkname=Monk.objects.create(monkname='title1')
    

class Product_Form_Test(TestCase):
    def setUp(self):
        self.user=User.objects.create(username="user1", password="P@ssw0rd1")

    def test_MedicationForm(self):
        data={
            'productname': 'name1',
            'productdescription': 'some type',
            'productusage': 'some usage',
            'productquantity': int,
            'user': self.user,
            'productcost' : int
        }
        form=ProductForm(data=data)
        self.assertTrue(form.is_valid)

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetProductTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        self.med=Product.objects.create(medname='Heart Sutra',
        productdescription='some description',
        productusage='some usage',
        productwarning='some warning',
        productquantity=200,
        user=self.u,
        productcost=200)
        

    
        