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
import React from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import PropertyList from './PropertyList';
import PropertyDetails from './PropertyDetails';
import Favorites from './Favorites';
import NavBar from './NavBar';
import Home from './Home';

const App = () => {
  return (
    <Router>
      <NavBar />
      <div className="App">
       <Routes>
        <Route path="/properties" component={PropertyList} />
        <Route path="/Property/:id" component={PropertyDetails} />
        <Route path="/Favorites" component={Favorites} />
        <Route exact path="/" component={Home} />
      </Routes>
      </div>
    </Router>
  );
};

export default App;
