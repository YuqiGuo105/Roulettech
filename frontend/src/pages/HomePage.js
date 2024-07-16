import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import RecipeList from "../components/RecipeList";
import RecipeForm from "../components/RecipeForm";
import RecipeGenerator from "./RecipeGenerator";

function parseJwt(token) {
  if (!token) {
    return null;
  }

  const base64Url = token.split('.')[1];
  const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
  const jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function (c) {
    return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  }).join(''));
  return JSON.parse(jsonPayload);
}

const HomePage = () => {
  const navigate = useNavigate();
  const [userName, setUserName] = useState('');
  const [post, setPost] = useState(false);
  useEffect(() => {
    const idTokenEncoded = sessionStorage.getItem('idToken');
    if (idTokenEncoded) {
      const idToken = parseJwt(idTokenEncoded);
      if (idToken && idToken.email) {
        setUserName(idToken.email);
      } else {
        console.log("User name not found in ID token.");
      }
    } else {
      console.log("No ID token found in sessionStorage.");
    }
  }, []);

  const handleLogout = () => {
    sessionStorage.clear();
    navigate('/login');
  };
  const handleGenerate = () => {
    navigate('/generate');
  };

  return (
    <div>
      <h1 className={"text-3xl font-bold text-center text-white"}>Hello {userName}</h1>

      {
        post ? <RecipeForm posterId={userName}></RecipeForm> : <RecipeList></RecipeList>
      }

      <button className={"w-1/4 outline outline-offset-2 outline-blue-500"} onClick={(e) => setPost(!post)}>Post
      </button>
      <button className={"w-1/4 outline outline-offset-2 outline-blue-500"} onClick={handleGenerate}>Generate
      </button>
      <button className={"w-1/4 outline outline-offset-2 outline-blue-500"} onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default HomePage;
