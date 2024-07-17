import { CognitoUserPool, CognitoUser, AuthenticationDetails } from 'amazon-cognito-identity-js';

const poolData = {
  UserPoolId: process.env.REACT_APP_COGNITO_REGION, // Your user pool id here
  ClientId: process.env.REACT_APP_COGNITO_CLIENT_ID // Your client id here
};

const userPool = new CognitoUserPool(poolData);

export const signUp = (email, password) => {
  return new Promise((resolve, reject) => {
    userPool.signUp(email, password, [], null, (err, result) => {
      if (err) {
        console.error('Sign Up Error:', err);
        reject(err);
        return;
      }
      resolve(result);
    });
  });
};

export const signIn = (email, password) => {
  return new Promise((resolve, reject) => {
    const authenticationDetails = new AuthenticationDetails({
      Username: email,
      Password: password,
    });

    const user = new CognitoUser({
      Username: email,
      Pool: userPool,
    });

    user.authenticateUser(authenticationDetails, {
      onSuccess: (result) => {
        console.log('Authentication successful:', result);
        const tokens = {
          AccessToken: result.getAccessToken().getJwtToken(),
          IdToken: result.getIdToken().getJwtToken(),
          RefreshToken: result.getRefreshToken().getToken(),
        };
        console.log('Extracted tokens:', tokens);
        resolve(tokens);
      },
      onFailure: (err) => {
        console.error('Sign In Error:', err);
        reject(err);
      },
    });
  });
};

export const confirmSignUp = (username, code) => {
  return new Promise((resolve, reject) => {
    const user = new CognitoUser({
      Username: username,
      Pool: userPool,
    });

    user.confirmRegistration(code, true, (err, result) => {
      if (err) {
        console.error('Confirmation Error:', err);
        reject(err);
        return;
      }
      resolve(result);
    });
  });
};
