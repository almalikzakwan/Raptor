from .base_model import BaseModel
from datetime import datetime

class StatusModel(BaseModel):
    def __init__(self):
        super().__init__()
    
    def get_system_status(self):
        """Get current system status"""
        return {
            "status": "success",
            "message": "Raptor Framework API is running",
            "version": "1.0.0",
            "framework": "Raptor MVC",
            "python_version": "3.9+",
            "ssl_enabled": True,
            "timestamp": datetime.now().isoformat(),
            "architecture": "MVC (Model-View-Controller)"
        }
    
    def log_request(self, request_info):
        """Log API requests for monitoring"""
        logs = self.load_data('api_logs')
        log_entry = {
            "id": self.generate_id(logs),
            "timestamp": datetime.now().isoformat(),
            "method": request_info.get('method'),
            "path": request_info.get('path'),
            "user_agent": request_info.get('user_agent', 'Unknown')
        }
        logs.append(log_entry)
        self.save_data('api_logs', logs)
        return log_entry