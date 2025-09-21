from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from datetime import datetime


def home(request):
    """Simple home page"""
    return render(request, 'home.html')


def upload_image(request):
    """Handle image upload"""
    if request.method == 'POST':
        if 'image' in request.FILES:
            uploaded_file = request.FILES['image']
            camera_id = request.POST.get('camera_id', 'test_camera')
            
            # Save the uploaded file
            file_name = f"uploads/{uploaded_file.name}"
            file_path = default_storage.save(file_name, ContentFile(uploaded_file.read()))
            
            # Show success message
            messages.success(request, f'Image uploaded successfully! File saved as: {file_name}')
            messages.info(request, 'AI detection will be implemented in the next step.')
            
            return redirect('upload_image')
        else:
            messages.error(request, 'Please select an image file.')
    
    return render(request, 'upload.html')

def results(request):
    """Display detection results"""
    image_path = request.GET.get('image', '')
    camera_id = request.GET.get('camera', 'Unknown')
    file_size = request.GET.get('size', 'Unknown')
    
    context = {
        'image_path': image_path,
        'camera_id': camera_id,
        'file_size': file_size,
    }
    
    return render(request, 'results.html', context)

def dashboard(request):
    """Dashboard view showing upload statistics"""
    # Get uploaded files from media directory
    uploads_dir = os.path.join(default_storage.location, 'uploads')
    recent_files = []
    total_uploads = 0
    
    if os.path.exists(uploads_dir):
        for filename in os.listdir(uploads_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                file_path = os.path.join(uploads_dir, filename)
                file_size = os.path.getsize(file_path)
                file_time = datetime.fromtimestamp(os.path.getctime(file_path))
                
                # Format file size
                if file_size > 1024 * 1024:
                    size_str = f"{file_size / (1024 * 1024):.1f} MB"
                else:
                    size_str = f"{file_size / 1024:.1f} KB"
                
                recent_files.append({
                    'name': filename,
                    'path': f'uploads/{filename}',
                    'size': size_str,
                    'time': file_time.strftime('%Y-%m-%d %H:%M')
                })
                total_uploads += 1
        
        # Sort by creation time (newest first)
        recent_files.sort(key=lambda x: x['time'], reverse=True)
        recent_files = recent_files[:10]  # Show only last 10
    
    # Count today's uploads (simplified)
    processed_today = len([f for f in recent_files if f['time'].startswith(datetime.now().strftime('%Y-%m-%d'))])
    
    context = {
        'total_uploads': total_uploads,
        'processed_today': processed_today,
        'recent_files': recent_files,
    }
    
    return render(request, 'dashboard.html', context)