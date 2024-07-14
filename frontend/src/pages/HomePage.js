import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

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

  return (
    <div>
      <h1>Hello {userName}</h1>
      <p>See console log for Amazon Cognito user tokens.</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default HomePage;
