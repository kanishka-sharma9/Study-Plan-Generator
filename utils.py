import base64

def encode_image_to_base64(uploaded_file):
    """
    Convert a Streamlit uploaded file to a base64 string.
    
    Args:
        uploaded_file (UploadedFile): File object from st.file_uploader()
    
    Returns:
        tuple: (base64_string, mime_type)
    """
    try:
        # Get the file extension
        file_type = uploaded_file.type
        
        # Determine MIME type
        mime_types = {
            'image/png': 'image/png',
            'image/jpeg': 'image/jpeg'
        }
        
        mime_type = mime_types.get(file_type, 'image/png')
        
        # Read the binary data directly from the uploaded file
        binary_data = uploaded_file.getvalue()
        
        # Encode to base64
        base64_encoded = base64.b64encode(binary_data)
        
        # Convert to string and remove b'' prefix
        return base64_encoded.decode('utf-8'), mime_type
        
    except Exception as e:
        raise Exception(f"Error encoding image: {str(e)}")