import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

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
    return <div>Loading</div>;
  }

  return (
    <div>
      <h1>{recipe.name}</h1>
      <img src={recipe.imageURL} alt={recipe.name} />
      <p>{recipe.content}</p>
    </div>
  );
};

export default RecipeDetail;
