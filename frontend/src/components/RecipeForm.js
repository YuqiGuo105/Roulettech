import React, { useState } from 'react';
import axios from 'axios';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';

const RecipeForm = ({ posterId }) => {
  const [name, setName] = useState('');
  const [content, setContent] = useState('');
  const [imageFile, setImageFile] = useState(null);

  const handleImageUpload = async () => {
    if (!imageFile) return null;
    return 'https://natashaskitchen.com/wp-content/uploads/2020/07/General-Tsos-Chicken-4.jpg';
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const imageUrl = await handleImageUpload();

    const recipe = {
      name,
      posterId,
      imageURL: imageUrl,
      content,
    };

    console.log('Submitting recipe:', recipe); // Log the recipe object

    axios.post(`${process.env.REACT_APP_BASE_URL}/api/recipes/`, recipe)
      .then(response => {
        console.log('Recipe created:', response.data);
      })
      .catch(error => {
        console.error('There was an error creating the recipe!', error);
        if (error.response) {
          console.error('Response data:', error.response.data); // Log the response data
        }
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Name:</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
      </div>
      <div>
        <label>Image:</label>
        <input type="file" onChange={(e) => setImageFile(e.target.files[0])} required />
      </div>
      <div>
        <label>Content:</label>
        <ReactQuill value={content} onChange={setContent} />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default RecipeForm;
