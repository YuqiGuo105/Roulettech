import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { signIn, signUp } from '../authService';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [isSignUp, setIsSignUp] = useState(false);
  const navigate = useNavigate();

  const handleSignIn = async (e) => {
    e.preventDefault();
    try {
      const session = await signIn(email, password);
      console.log('Sign in successful', session);
      if (session && session.AccessToken && session.IdToken) {
        localStorage.setItem('accessToken', session.AccessToken);
        localStorage.setItem('idToken', session.IdToken);
        localStorage.setItem('refreshToken', session.RefreshToken);
        navigate('/home');
      } else {
        console.error('Session tokens were not set properly.');
      }
    } catch (error) {
      alert(`Sign in failed: ${error.message}`);
    }
  };

  const handleSignUp = async (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      alert('Passwords do not match');
      return;
    }
    try {
      await signUp(email, password);
      alert('Sign up successful. Please check your email for the confirmation code.');
      navigate('/confirm', { state: { email } });
    } catch (error) {
      alert(`Sign up failed: ${error.message}`);
    }
  };

  return (
    <div className="flex items-center justify-center">
      <div className="bg-gradient-to-r from-blue-10 to-purple-20 via-purple-10 p-8 rounded-lg shadow-xl border-2 border-gray-300 max-w-md w-full">
        <h1 className="text-3xl font-bold mb-6 text-center text-white">Welcome</h1>
        <h4 className="text-lg mb-6 text-center text-white">
          {isSignUp ? 'Sign up to create an account' : 'Sign in to your account'}
        </h4>
        <form onSubmit={isSignUp ? handleSignUp : handleSignIn}>
          <div className="mb-4">
            <input
              className="w-full p-3 border border-gray-300 rounded-lg"
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Email"
              required
            />
          </div>
          <div className="mb-4">
            <input
              className="w-full p-3 border border-gray-300 rounded-lg"
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Password"
              required
            />
          </div>
          {isSignUp && (
            <div className="mb-4">
              <input
                className="w-full p-3 border border-gray-300 rounded-lg"
                id="confirmPassword"
                type="password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                placeholder="Confirm Password"
                required
              />
            </div>
          )}
          <button type="submit" className="w-11/12 bg-blue-700 text-white p-3 rounded-lg hover:bg-blue-800 transition-all duration-300">
            {isSignUp ? 'Sign Up' : 'Sign In'}
          </button>
        </form>
        <button
          onClick={() => setIsSignUp(!isSignUp)}
          className="bg-gray-200 text-blue-700 p-3 rounded-lg hover:bg-gray-300 mt-4 transition-all duration-300"
        >
          {isSignUp ? 'Already have an account? Sign In' : 'Need an account? Sign Up'}
        </button>
      </div>
    </div>
  );
};

export default LoginPage;

