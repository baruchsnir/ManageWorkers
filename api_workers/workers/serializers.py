from rest_framework import serializers
from .models import Job, Worker, Department


class WorkerSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    # picture.source = picture.source.replace('/assets/','/static/')
    # picture = serializers.SerializerMethodField()
    class Meta:
        model = Worker
        fields = ["emploee_id", "first_name", "last_name", "email", "phone_number", "hire_date", "job_id", "salary",
                  "commission_pct", "manager_id", "department_id", "picture"]
        def get_image(self, obj):
            return self.context['request'].build_absolute_uri( obj.image.url)

        # def get_photo_url(self, car):
        #     request = self.context.get('request')
        #     if photo and hasattr(photo, 'url'):
        #         photo_url = car.photo.url
        #         return request.build_absolute_uri(photo_url)
        #     else:
        #         return None


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["department_id", "url", "name"]


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["job_id", "url", "name"]
