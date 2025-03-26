from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)  # ✅ Read-only to avoid errors
    assigned_users_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )  # ✅ Accept user IDs for assignment

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'completed_at', 
                  'task_type', 'status', 'assigned_users', 'assigned_users_ids']

    def create(self, validated_data):
        assigned_users_ids = validated_data.pop('assigned_users_ids', [])  # ✅ Extract user IDs
        task = Task.objects.create(**validated_data)  # ✅ Create task without users
        task.assigned_users.set(User.objects.filter(id__in=assigned_users_ids))  # ✅ Assign users
        return task


class TaskAssignmentSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    user_ids = serializers.ListField(
        child=serializers.IntegerField()
    )
