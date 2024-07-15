import React, { useEffect, useState } from "react";
import axios from 'axios';
import { Link } from "react-router-dom";

const RecipeList = () => {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_BASE_URL}/api/recipes/`)
      .then(response => {
        setRecipes(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the recipes!', error);
      });
  }, [])

  return (
    <div>
      <ul>
        {recipes.map(recipe => (
          <li key={recipe.id}>
            <img src={recipe.imageURL} alt={recipe.name} />
            <Link to={`/recipes/${recipe.id}`}>{recipe.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RecipeList;
