import React, { useState } from 'react';
import axios from 'axios';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import {useNavigate} from "react-router-dom";
const RecipeForm = ({ posterId }) => {
  const [name, setName] = useState('');
  const [content, setContent] = useState('');
  const [imageFile, setImageFile] = useState(null);
  const navigate = useNavigate();
  const handleImageUpload = async () => {
    if (!imageFile) return null;

    try {
      // Step 1: Get the presigned URL from Django backend
      const presignedUrlResponse = await axios.get(`${process.env.REACT_APP_BASE_URL}/api/presigned-url/`, {
        params: {
          file_name: imageFile.name,
          content_type: imageFile.type,  // Ensure correct parameter name
        },
      });

      const { presigned_url } = presignedUrlResponse.data;

      // Step 2: Upload the image to S3 using the presigned URL
      await axios.put(presigned_url, imageFile, {
        headers: {
          'Content-Type': imageFile.type,
        },
      });

      // Return the URL without query parameters
      return presigned_url.split('?')[0];
    } catch (error) {
      console.error('Error uploading image:', error);
      if (error.response) {
        console.error('Response data:', error.response.data);
      }
      return null;
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    // Upload the image and get the URL
    const imageUrl = await handleImageUpload();
    if (!imageUrl) {
      console.error('Image upload failed');
      return;
    }

    const recipe = {
      name,
      posterId,
      imageURL: imageUrl,
      content,
    };

    console.log('Submitting recipe:', recipe);

    try {
      const response = await axios.post(`${process.env.REACT_APP_BASE_URL}/api/recipes/`, recipe);
      console.log('Recipe created:', response.data);
      alert('Success');
      navigate('/home');
    } catch (error) {
      console.error('There was an error creating the recipe!', error);
      if (error.response) {
        console.error('Response data:', error.response.data);
      }
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-xl mx-auto p-4 bg-white shadow-md rounded-lg">
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">Name:</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">Image:</label>
        <input
          type="file"
          className="w-full px-3 py-2 border border-gray-300 text-gray-700 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          onChange={(e) => setImageFile(e.target.files[0])}
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">Content:</label>
        <div className="h-64 pb-10">
          <ReactQuill
            value={content}
            onChange={setContent}
            className="bg-white h-full text-gray-700"
            theme="snow"
          />
        </div>
      </div>
      <button type="submit" className="w-11/12 bg-blue-500 text-white font-bold py-2 px-4 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">
        Submit
      </button>
    </form>
  );
};

export default RecipeForm;

