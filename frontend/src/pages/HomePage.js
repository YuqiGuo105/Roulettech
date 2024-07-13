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

  const idTokenEncoded = sessionStorage.getItem('idToken');
  const accessTokenEncoded = sessionStorage.getItem('accessToken');
  const refreshToken = sessionStorage.getItem('refreshToken');

  const idToken = parseJwt(idTokenEncoded);
  const accessToken = parseJwt(accessTokenEncoded);

  if (idTokenEncoded) {
    console.log("Amazon Cognito ID token encoded: " + idTokenEncoded);
    console.log("Amazon Cognito ID token decoded: ", idToken);
  } else {
    console.log("No ID token found in sessionStorage.");
  }

  if (accessTokenEncoded) {
    console.log("Amazon Cognito access token encoded: " + accessTokenEncoded);
    console.log("Amazon Cognito access token decoded: ", accessToken);
  } else {
    console.log("No access token found in sessionStorage.");
  }

  console.log("Amazon Cognito refresh token: ", refreshToken);
  console.log("Amazon Cognito example application. Not for use in production applications.");

  const handleLogout = () => {
    sessionStorage.clear();
    navigate('/login');
  };

  return (
    <div>
      <h1>Hello World</h1>
      <p>See console log for Amazon Cognito user tokens.</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default HomePage;
