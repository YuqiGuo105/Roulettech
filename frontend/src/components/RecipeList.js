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
    <div className="grid grid-cols-2 gap-4 p-4">
      {recipes.map(recipe => (
        <div key={recipe.id} className="relative bg-white shadow-md rounded-lg overflow-hidden">
          <div className="relative overflow-hidden group">
            <img src={recipe.imageURL} alt={recipe.name} className="w-full h-48 object-cover transition-transform duration-300 group-hover:scale-110" />
            <div className="absolute bottom-0 left-0 w-full bg-white bg-opacity-50 text-white p-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
              <h3 className="text-3xl font-semibold text-white">
                <Link to={`/recipes/${recipe.id}`}>{recipe.name}</Link>
              </h3>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default RecipeList;
