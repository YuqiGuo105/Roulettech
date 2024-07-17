import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { confirmSignUp } from '../authService';
import {useNavigate} from "react-router-dom";

const ConfirmSignUpPage = () => {
  const location = useLocation();
  const [username, setUsername] = useState('');
  const [code, setCode] = useState('');
  const [email, setEmail] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    if (location.state && location.state.email) {
      setUsername(location.state.email);
    }
  }, [location.state]);

  const handleConfirm = async () => {
    try {
      const response = await confirmSignUp(username, code);
      console.log('User confirmed:', response);
      navigate('/home');
    } catch (error) {
      console.error('Confirmation failed:', error);
    }
  };

  return (
    <div className={"space-x-2"}>
      <h1>Confirm Sign Up</h1>
      {/*<input type="text" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email"/>*/}
      <input className={"h-10 rounded-md border-2 border-white hover:border-purple-40"} type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username"/>
      <input className={"h-10 rounded-md border-2 border-white hover:border-purple-40"} type="text" value={code} onChange={(e) => setCode(e.target.value)} placeholder="Confirmation Code"/>
      <button className={"border-2 border-white"} onClick={handleConfirm}>Confirm</button>
    </div>
  );
};

export default ConfirmSignUpPage;

