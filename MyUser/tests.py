from .models import User
import json
users = User.objects.all()
print(json.dumps(users))