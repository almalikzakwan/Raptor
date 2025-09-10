from models.status_model import StatusModel
from raptor.core.app import Response
import json

class ApiController:
    def __init__(self):
        self.status_model = StatusModel()
    
    def status(self, request):
        """API status endpoint - GET /api/v1/status"""
        try:
            request_info = {
                'method': request.method,
                'path': request.path,
                'user_agent': request.headers.get('user-agent', 'Unknown')
            }
            self.status_model.log_request(request_info)
            
            status_data = self.status_model.get_system_status()
            
            # Add routing information
            status_data.update({
                'routing': {
                    'style': 'Laravel-inspired',
                    'features': ['named_routes', 'route_parameters', 'route_groups', 'middleware'],
                    'total_routes': 'Dynamic'
                }
            })
            
            return Response(json.dumps(status_data, indent=2), 200, 'application/json')
            
        except Exception as e:
            error_response = {"error": str(e), "status": "error"}
            return Response(json.dumps(error_response), 500, 'application/json')
    
    def health(self, request):
        """Simple health check - GET /api/v1/health"""
        health_data = {
            "status": "healthy",
            "timestamp": self.status_model.get_system_status()["timestamp"],
            "service": "Raptor Framework",
            "routing": "Laravel-style"
        }
        return Response(json.dumps(health_data), 200, 'application/json')
