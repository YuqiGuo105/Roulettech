import React, { useState } from 'react';
import { signUp } from '../authService';
const SignUpPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const handleSignUp = async () => {
    try {
      const response = await signUp(username, password, email);
      console.log('Sign-up successful:', response);
    } catch (error) {
      console.error('Sign-up failed:', error);
    }
  };

  return (
    <div>
      <h1>Sign Up</h1>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
      <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
      <button onClick={handleSignUp}>Sign Up</button>
    </div>
  );
};

export default SignUpPage;

