import React, { useState } from "react";
import { useStytch, useStytchSession, useStytchUser } from "@stytch/nextjs";

/*
The Profile component is shown to a user that is logged in.

This component renders the full User and Session object for education. 

This component also includes a log out button which is accomplished by making a method call to revoking the existing session
*/
const Profile = () => {
  const stytch = useStytch();
  // Get the Stytch User object if available
  const { user } = useStytchUser();
  // Get the Stytch Session object if available
  const { session } = useStytchSession();
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [isRecording, setIsRecording] = useState(false);
  const [mediaRecorder, setMediaRecorder] = useState(null);
  const [audioBlob, setAudioBlob] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);

  const handleSubmit = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await fetch('/api/submitInput', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ inputValue }),
      });

      if (!response.ok) {
        throw new Error('Failed to submit input');
      }

      const data = await response.json();
      console.log('API response:', data);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleAudioClick = async () => {
    if (isRecording) {
      mediaRecorder.stop();
      setIsRecording(false);
      return;
    }

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream);
      setMediaRecorder(recorder);

      const chunks = [];
      recorder.ondataavailable = (e) => chunks.push(e.data);
      recorder.onstop = () => {
        const blob = new Blob(chunks, { type: 'audio/webm' });
        setAudioBlob(blob);
        stream.getTracks().forEach(track => track.stop());
      };

      recorder.start();
      setIsRecording(true);
    } catch (err) {
      console.error('Error accessing microphone:', err);
      setError('Microphone access denied');
    }
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedFile(file);
    }
  };

  return (
    <div className="card">
      <h1>Hellooooo!</h1>
      <h2>How can I help you today?</h2>
      {/* <pre className="code-block">
        <code>{JSON.stringify(user, null, 2)}</code>
      </pre>

      <h2>Session object</h2>
      <pre className="code-block">
        <code>{JSON.stringify(session, null, 2)}</code>
      </pre>
      <p>
        You are logged in, and a Session has been created. The SDK stores the
        Session as a token and a JWT in the browser cookies as{" "}
        <span className="code">stytch_session</span> and{" "}
        <span className="code">stytch_session_jwt</span> respectively.
      </p> */}
      <div className='mt-4'>
        <label htmlFor='inputBox' className='block text-sm font-medium text-gray-700'> </label>
        <div className='flex gap-2 items-center'>
          <input
            id='inputBox'
            type='text'
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            className='flex-1 mt-1 block rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'
          />
        
        </div>
      </div>
      <div className='flex gap-2 mt-4'>
        <button
          type='button'
          className='p-2 text-gray-500 hover:text-gray-700 focus:outline-none transition-transform transform hover:scale-110'
          onClick={handleAudioClick}
        >
          <svg xmlns='http://www.w3.org/2000/svg' className='h-[10px] w-[10px]' viewBox='0 0 20 20' fill='currentColor' strokeWidth='1.5'>
            <path fillRule='evenodd' d='M7 4a3 3 0 016 0v4a3 3 0 11-6 0V4zm4 10.93A7.001 7.001 0 0017 8a1 1 0 10-2 0A5 5 0 015 8a1 1 0 00-2 0 7.001 7.001 0 006 6.93V17H6a1 1 0 100 2h8a1 1 0 100-2h-3v-2.07z' clipRule='evenodd' />
          </svg>
        </button>
        <input
          type='file'
          id='fileInput'
          className='hidden'
          onChange={handleFileChange}
        />
        <label
          htmlFor='fileInput'
          className='p-2 text-gray-500 hover:text-gray-700 focus:outline-none transition-transform transform hover:scale-110 cursor-pointer'
        >
          <svg xmlns='http://www.w3.org/2000/svg' className='h-[10px] w-[10px]' viewBox='0 0 20 20' fill='currentColor' strokeWidth='1.5'>
            <path fillRule='evenodd' d='M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z' clipRule='evenodd' />
          </svg>
        </label>
      </div>
      <button
        onClick={handleSubmit}
        disabled={isLoading}
        className='mt-2 inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2'
      >
        {isLoading ? '✉️' : '✉️'}
      </button>
      {error && <p className='mt-2 text-sm text-red-600'>{error}</p>}
      {/* Revoking the session results in the session being revoked and cleared from browser storage. The user will return to Login.js */}
      <button className="primary" onClick={() => stytch.session.revoke()}>
        Log out
      </button>
    </div>
  );
};

export default Profile;
