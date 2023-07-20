// import React from 'react';
// import AppRoutes from './AppRoutes';

// const App = () => {
//   return (
//     <div className="App">
//       <header>
//         <h1>Leaf Stone</h1>
//       </header>
//       <AppRoutes />
//     </div>
//   );
// };

// export default App;
import React, {useEffect, useState} from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import PropertyList from './components/PropertyList';
import PropertyDetails from './components/PropertyDetails';
import Favorites from './components/Favorites';
import NavBar from './components/NavBar';
import Home from './components/Home';
import PropertyContainer from './components/PropertyContainer.js';
import PropertyCard from './components/PropertyCard'

const App = () => {

  const [properties, setProperties] = useState([])
  
  useEffect(() => {
    fetch('/properties/')
    .then(r => r.json())
    .then(data => setProperties(data))
  },[])
  
  return (
    <Router>
      <NavBar />
      <div className="App">
       <Routes>
        <Route path="/properties" component={PropertyList} properties={properties} />
        <Route path="/Property/:id" component={PropertyDetails} />
        <Route path="/Favorites" component={Favorites} />
        <Route exact path="/" element={<Home properties={properties} />} />
      </Routes>
      </div>
    </Router>
  );
};

export default App;
