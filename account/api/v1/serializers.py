from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    # date_of_birth = serializers.DateField()
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm', 'date_of_birth')
        # fields = ('username', 'email', 'date_of_birth', 'password', 'password_confirm')

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data.get('username')
        )

        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError('passwords did not match')

        user.set_password(self.validated_data.get('password'))
        # user.set_date_of_birth(self.validated_data.get('date_of_birth'))
        user.save()

        return user
