import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import musicNote from '../public/music_15509.png'
import './App.css'

function App() {
   const [inputValue, setInputValue] = useState('')

   const handleChange = (event) => {
   setInputValue(event.target.value);
   }

  return (
    <>
      <div>   
        <a href="https://react.dev" target="_blank">
          <img src={musicNote} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>STAMPLE</h1>
      hi
      <div className="card">
      <input type="text" value={inputValue} onChange={handleChange} />
      <p>You entered: {inputValue}</p> 
        <p>
          Input song name here
        </p>
      </div>
      <p className="read-the-docs">
        Stample will find the time stamps of samples in music
      </p>
    </>
  )
}

export default App
