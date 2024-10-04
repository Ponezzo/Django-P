from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Django는 User 모델을 직접 참조하는 것을 권장하지 않는다.
# 그래서 Django는 User 모델을 간접적으로 참조할 수 있는 방법을 별도로 제공한다.
from django.contrib.auth import get_user_model
# 현재 프로젝트에서 활성화 된 User 객체를 반환한다.

class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomerUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields =('first_name', 'last_name', 'email', )