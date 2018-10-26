from django.conf import settings
from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
CATEGORY_CHOICES = (
	('coat', 'coat'),
	('jacket', 'jacket'),
	('dress', 'dress'),
	('jumpsuit', 'jumpsuit'),
	('shirt/blouse', 'shirt/blouse'),
	('t-shirt', 't-shirt'),
	('bodysuit', 'bodysuit'),
	('sweatshirt', 'sweatshirt'),
	('pants', 'pants'),
	('jeans', 'jeans'),
	('shorts', 'shorts'),
	('skirt', 'skirt'),
	('shoes', 'shoes'),
	('bags', 'bags'),
	('accessory', 'accessory'),
)

SEASON_CHOICES = (
	('spring', 'spring'),
	('summer', 'summer'),
	('fall', 'fall'),
	('winter', 'winter')
)





class Closet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	catagory = MultiSelectField(choicec = CATEGORY_CHOICES)
	season = MultiSelectField(choicec = SEASON_CHOICES)
	picture = models.ImageField(blank=True)
	create_at = models.DateTimeField(auto_now=True)
