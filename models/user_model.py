from .base_model import BaseModel
from datetime import datetime

class UserModel(BaseModel):
    def __init__(self):
        super().__init__()
    
    def create_user(self, name, email):
        """Create a new user"""
        users = self.load_data('users')
        user = {
            'id': self.generate_id(users),
            'name': name,
            'email': email,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        users.append(user)
        self.save_data('users', users)
        return user
    
    def get_all_users(self):
        """Get all users"""
        return self.load_data('users')
    
    def get_user_by_id(self, user_id):
        """Get user by ID"""
        users = self.get_all_users()
        return next((u for u in users if u['id'] == user_id), None)
    
    def update_user(self, user_id, data):
        """Update user"""
        users = self.get_all_users()
        for i, user in enumerate(users):
            if user['id'] == user_id:
                users[i].update(data)
                users[i]['updated_at'] = datetime.now().isoformat()
                self.save_data('users', users)
                return users[i]
        return None
    
    def delete_user(self, user_id):
        """Delete user"""
        users = self.get_all_users()
        users = [u for u in users if u['id'] != user_id]
        self.save_data('users', users)
        return True