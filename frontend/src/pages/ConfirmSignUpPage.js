import React, { useState } from 'react';
import { confirmSignUp } from '../authService';

const ConfirmSignUpPage = () => {
  const [username, setUsername] = useState('');
  const [code, setCode] = useState('');

  const handleConfirm = async () => {
    try {
      const response = await confirmSignUp(username, code);
      console.log('User confirmed:', response);
    } catch (error) {
      console.error('Confirmation failed:', error);
    }
  };

  return (
    <div>
      <h1>Confirm Sign Up</h1>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
      <input type="text" value={code} onChange={(e) => setCode(e.target.value)} placeholder="Confirmation Code" />
      <button onClick={handleConfirm}>Confirm</button>
    </div>
  );
};

export default ConfirmSignUpPage;
