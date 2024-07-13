// src/services/authService.js
const {
  CognitoIdentityProviderClient,
  SignUpCommand,
  ConfirmSignUpCommand,
  InitiateAuthCommand,
} = require("@aws-sdk/client-cognito-identity-provider");

const client = new CognitoIdentityProviderClient({
  region: "us-east-2",
});

const signUp = async (username, password) => {
  const command = new SignUpCommand({
    ClientId: process.env.REACT_APP_COGNITO_CLIENT_ID,
    Username: username,
    Password: password,
  });

  try {
    const response = await client.send(command);
    return response;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

const confirmSignUp = async (username, code) => {
  const command = new ConfirmSignUpCommand({
    ClientId: process.env.REACT_APP_COGNITO_CLIENT_ID,
    Username: username,
    ConfirmationCode: code,
  });

  try {
    const response = await client.send(command);
    return response;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

const signIn = async (username, password) => {
  const command = new InitiateAuthCommand({
    AuthFlow: "USER_PASSWORD_AUTH",
    ClientId: process.env.REACT_APP_COGNITO_CLIENT_ID,
    AuthParameters: {
      USERNAME: username,
      PASSWORD: password,
    },
  });

  try {
    const response = await client.send(command);
    return response.AuthenticationResult;
  } catch (error) {
    console.error(error);
    throw error;
  }
};

module.exports = { signUp, confirmSignUp, signIn };
