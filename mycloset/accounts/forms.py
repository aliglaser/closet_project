from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.files.images import get_image_dimensions

class UserCreateForm(UserCreationForm):
	class Meta:
		fields = ("username", "email", "password1", "password2", "avatar", "date_of_birth")
		model = get_user_model()


		def clean_avatar(self):
			avatar = self.cleaned_data['avatar']

			try:
				w, h = get_image_dimensions(avatar)
				max_width = max_height = 500
				if w > max_width or h > max_height:
					raise forms.ValidationError(
						'Please use an image that is '
						'%s x %s pixels or smaller.' % (max_width, max_height))
					main, sub = avatar.content_type.split('/')
				if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
					raise forms.ValidationError(u'Please use a JPEG, GIF or PNG image.')
				if len(avatar) > (20 * 1024):
					raise forms.ValidationError('Avatar file size may not exceed 20k.')

			except AttributeError:
				pass
			return avatar

		def save(self, commit=True):
			# Save the provided password in hashed format
			user = super().save(commit=False)
			user.set_password(self.cleaned_data["password1"])
			user.avatar = clean_avatar()
			if commit:
				user.save()
			return user        
