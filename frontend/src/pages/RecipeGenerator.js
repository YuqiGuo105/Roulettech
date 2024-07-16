import React, { useState } from "react";
import axios from "axios";


const RecipeGenerator = () => {
  const [prompt, setPrompt] = useState('');
  const [recipe, setRecipe] = useState('');
  const [listening, setListening] = useState(false);

  const handleVoiceInput = () => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';

    recognition.onstart = () => setListening(true);
    recognition.onend = () => setListening(false);
    recognition.onerror = (event) => console.error(event.error);
    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setPrompt(transcript);
    };

    recognition.start();
  };

  const generateRecipe = async () => {
    try {
      const response = await axios.post(`${process.env.REACT_APP_BASE_URL}/api/generate-recipe/`, { prompt });
      const generatedRecipe = response.data.recipe;
      setRecipe(generatedRecipe);
      readRecipeAloud(generatedRecipe);
    } catch (error) {
      console.error('Error generating recipe:', error);
    }
  };

  const readRecipeAloud = (text) => {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    window.speechSynthesis.speak(utterance);
  };

  return (
    <div className="h-full bg-gray-100 flex flex-col items-center p-10 rounded-2xl">
      <h1 className="text-3xl font-bold text-center text-blue-500 mb-8">Generate Recipe</h1>
      <div className="w-full max-w-2xl bg-white p-6 rounded-lg shadow-md">
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter a description or ingredients..."
          className="w-full h-40 p-3 border border-gray-300 rounded-md shadow-sm mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
        />
        <div className="flex space-x-4 mb-4">
          <button
            onClick={handleVoiceInput}
            className={`px-4 py-2 rounded-md shadow-sm text-white ${listening ? 'bg-red-500' : 'bg-blue-500'} hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50`}
          >
            {listening ? 'Listening...' : 'Use Voice Input'}
          </button>
          <button
            onClick={generateRecipe}
            className="px-4 py-2 bg-green-500 rounded-md shadow-sm text-white hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-opacity-50"
          >
            Generate Recipe
          </button>
        </div>
        {recipe && (
          <div className="w-full bg-white p-4 rounded-md shadow-md">
            <h2 className="text-2xl font-bold mb-2">Generated Recipe</h2>
            <p className="mb-4">{recipe}</p>
            <button
              onClick={() => readRecipeAloud(recipe)}
              className="px-4 py-2 bg-blue-500 rounded-md shadow-sm text-white hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
            >
              Read Recipe Aloud
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default RecipeGenerator;
