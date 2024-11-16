// App.js
import React, { useState } from 'react';
import './App.css';
import UrlIp from './components/UrlInputForm';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <UrlIp id="url" />
    </div>
  );
}

export default App;
