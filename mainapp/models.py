from django.db import models
from django.utils import timezone


class Post(models.Model) :
    title = models.CharField(max_length = 200) #제목
    author = models.CharField(max_length = 200) #작성자
    pub_date = models.DateTimeField(default  = timezone.now) #작성일
    image = models.ImageField(upload_to = 'images/') #사진
    body = models.TextField() #내용
    rent_date = models.CharField(max_length =200) #대여가능일
    price = models.PositiveIntegerField() #가격
    PARCEL_CHOICES = [('가능','가능'),('불가능','불가능')]
    choice_parcel = models.CharField(max_length=10, choices=PARCEL_CHOICES, default='가능') #택배가능여부
    use = models.TextField() #용도
    REGION_SIDO_CHOICES = [('서울특별시','서울특별시'),('부산광역시','부산광역시'),('대구광역시','대구광역시'),('인천광역시','인천광역시'),('광주광역시','광주광역시'),('대전광역시','대전광역시'),('울산광역시','울산광역시'),('세종특별자치시','세종특별자치시'),('경기도','경기도'),('강원도','강원도'),('충청북도','충청북도'),('충청남도','충청남도'),('전라북도','전라북도'),('전라남도','전라남도'),('경상북도','경상북도'),('경상남도','경상남도'),('제주특별자치도','제주특별자치도')]
    region_sido = models.CharField(max_length=30, choices=REGION_SIDO_CHOICES, default= "==========")  #지역(시/도)
    region_sigungu = models.CharField(max_length = 10) #지역(군/구)
    region_rest = models.CharField(max_length = 20) #지역(남은 주소)
    sort = models.CharField(max_length = 10) #기종(캠코더/DSLR/미러리스)
    
    def __str__(self):
      return self.title

class Comment(models.Model) :
    post = models.ForeignKey('mainapp.Post', on_delete=models.CASCADE, related_name = 'comments')
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    is_secret = models.BooleanField()
    is_accepted = models.BooleanField()

    def __str__(self):
        return self.text

