from django.db import models
from cloudinary.models import CloudinaryField



class Location(models.Model):
    name = models.CharField(max_length =80, unique='True')
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        
        
    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
        
    
    def delete_location(self):
        self.delete()
    

class Category(models.Model):
    name = models.CharField(max_length =80, unique='True')
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
    
    def save_category(self):
            self.save()
    
    def delete_category(self):
        self.delete()
    
    

class Image(models.Model):
    name = models.CharField(max_length =80)
    description = models.TextField()
    location = models.ForeignKey(Location,  on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category,  on_delete=models.DO_NOTHING)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo = CloudinaryField('photo')
    
    class Meta:
        ordering = ["pub_date"]
        verbose_name = "Image"
        verbose_name_plural = "Images"
    
    def summary(self):
        return self.description[:100]+" ......"
    
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def save_image(self):
        self.save()
    
    
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        pass
        

    def get_image_by_id(cls):
        images = cls.objects.get(pk=id)
        return images
    
    def search_image(category):
        pass
    
    def filter_by_location(location):
        pass
    
    
    @classmethod
    def search_by_category(cls,search_term):
        searched_images = cls.objects.filter(category__icontains = search_term)
        return searched_images
    
 
    
    
    
    
