import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import DOMPurify from 'dompurify';
import {RollbackOutlined} from '@ant-design/icons';
import { useNavigate } from 'react-router-dom';


const RecipeDetail = () => {
  const { id } = useParams();
  const [recipe, setRecipe] = useState(null);
  const navigate = useNavigate();

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

  const handleBack = () => {
    navigate('/home');
  };

  return (
    <div className="relative md:col-span-1">
      <h1 className="text-2xl font-bold mb-4">{recipe.name}</h1>
      <div className="relative mb-4">
        <img
          className="float-right mr-56 mb-4 w-6/12 h-2/5 object-cover rounded"
          src={recipe.imageURL}
          alt={recipe.name}
        />

        <div
          className="text-justify"
          dangerouslySetInnerHTML={{__html: DOMPurify.sanitize(recipe.content)}}
        ></div>
      </div>
      <button className= {"w-14 h-14 fixed bottom-4 right-4 bg-grey-700 text-white border-4 border-white py-2 px-4 rounded-full shadow-lg hover:bg-purple-10"} onClick={handleBack}>
        <RollbackOutlined  /></button>
    </div>
  );
};

export default RecipeDetail;
