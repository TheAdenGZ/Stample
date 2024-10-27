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
<<<<<<< HEAD
      
      <div className="card">
=======
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

>>>>>>> ee56e5386f4b8fd2836bab032412001341d5e280
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
