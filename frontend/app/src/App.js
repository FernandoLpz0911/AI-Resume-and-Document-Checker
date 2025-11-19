import logo from './logo.svg';
import josh from './josh.png'
import './App.css';
import './balls.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={josh} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <header> 
          <text className='balls'>
            Andres, Esteban, and Fez
          </text>
          <space> </space>LIKES BALLS
        </header>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
