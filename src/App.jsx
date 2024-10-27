import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import musicNote from '../public/music_15509.png'
import Stample from '../public/TheStamp.png'
import './App.css'

function App() {
   const [input1, setInput1] = useState('')
   const [input2, setInput2] = useState('')

   const handleChange = (event) => {
    const { name , value} = event.target;

    
    if (name === 'input1') {
      setInput1(value);
    } else if (name === 'input2') {
      setInput2(value);
    }
  };

  return (
    <>
      <div>   
        <a href="" target="_blank">
          <img src={Stample} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>STAMPLE</h1>
      Input song title:
      <div className="card">

       <input type="text" value={input1} onChange={(e) => setInput1(e.target.value)} name='input1' />
      <p></p>
        <p>
          Input artist:
        </p>
      <input type="text" value={input2} onChange={handleChange} name='input2' />
      <p></p>
      </div>
      <p className="read-the-docs">
        Stample will find the time stamps of samples in music
      </p>

      <form action="/action_page.php">
        <label for="fname">Song name:</label><br/>
        <input type="text" id="fname" name="fname" value=""/><br/>
        <label for="lname">Artist name:</label><br/>
        <input type="text" id="lname" name="lname" value=""/><br/><br/>
        <input type="submit" value="Submit"/>
      </form>
    </>
  )
}

export default App
