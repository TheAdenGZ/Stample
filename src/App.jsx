import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import musicNote from '../public/music_15509.png'
import Stample from '../public/TheStamp.png'
import './App.css'

function App() {
   const [input1, setInput1] = useState('')
   const [input2, setInput2] = useState('')
     console.log(input1);
     console.log(input2);

   const [value1, setValue1] = useState('');
   const [value2, setValue2] = useState(''); 

  return (
    <>
      <div>   
        <a href="" target="_blank">
          <img src={Stample} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>STAMPLE</h1>
      
      <div className="card">
      <form action="/action_page.php">
        <label for="fname">Song name:</label><br/>
        <input type="text"onChange={(e) => setInput1(e.target.value)} id="fname" name="fname" value={input1}/><br/>
        <label for="lname">Artist name:</label><br/>
        <input type="text" onChange={(e) => setInput2(e.target.value)} id="lname" name="lname" value={input2}/><br/><br/>
        <input type="submit" value="Submit"/>
      </form>

      </div>
      <p className="read-the-docs">
       
      </p>
      <div>
        <p>Sample song and artist</p>
      <input 
        type="text" 
        value={value1} 
        disabled
        // onChange={e => setValue1(e.target.value)} 
        // readOnly
      />
      <input 
        type="text" 
        value={value2} 
        onChange={e => setValue2(e.target.value)}
        readOnly 
      />
    </div>
    </>
  )
}

export default App
