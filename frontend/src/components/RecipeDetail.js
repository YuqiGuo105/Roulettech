import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import DOMPurify from 'dompurify';

const RecipeDetail = () => {
  const { id } = useParams();
  const [recipe, setRecipe] = useState(null);

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_BASE_URL}/api/recipes/${id}/`)
      .then(response => {
        setRecipe(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the recipe!', error);
      });
  }, [id]);

  if (!recipe) {
    return <div>Loading...</div>;
  }

  return (
    <div className="relative md:col-span-1">
      <h1 className="text-2xl font-bold mb-4">{recipe.name}</h1>
      <div className="relative mb-4">
        <div
          className="text-justify"
          dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(recipe.content) }}
        ></div>
        <img
          className="absolute top-0 left-1/2 transform -translate-x-1/2 w-6/12 h-2/5 ml-4 object-cover rounded"
          src={recipe.imageURL}
          alt={recipe.name}
        />
      </div>
    </div>
  );
};

export default RecipeDetail;
