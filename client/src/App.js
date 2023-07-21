import { useState, useEffect } from "react";
import { Routes, Route, useNavigate } from "react-router"
import Home from "./components/Home"
import Nav from "./components/Nav"
import PropertyContainer from "./components/PropertyContainer";
import PropertyDetail from "./components/PropertyDetail";
import PropertyForm from "./components/PropertyForm";
import PropertyEditForm from "./components/PropertyEditForm";

const App = () => {
  const [properties, setProperties] = useState([])
  const [editProperty, setEditProperty] = useState(null)
  const nav = useNavigate()
  useEffect(() => {
    fetchAllProperties()
  }, [])

  const fetchAllProperties = () => {
    fetch("http://127.0.0.1:5555/properties")
    .then(res => res.json())
    .then(allProperties => {
      
      setProperties(allProperties)
    })
  }

  const postProperty = propertyFormData => {
    const postReqObj = {
      method: "POST",
      headers: {
        "content-type": "application/json"
      },
      body: JSON.stringify(propertyFormData)
    }
    fetch("http://127.0.0.1:5555/properties", postReqObj)
    .then(r => r.json())
    .then(newPropertyObj => {
      console.log(newPropertyObj)
      setProperties([...properties, newPropertyObj])
      nav(`/properties/${newPropertyObj.id}`)
    })
  }

  const patchProperty = (propertyFormData, id) => {
    const patchReqObj = {
      method: "PATCH",
      headers: {
        "content-type": "application/json"
      },
      body: JSON.stringify(propertyFormData),
    }
    fetch(`http://127.0.0.1:5555/properties/${id}`, patchReqObj)
    .then(res => res.json())
    .then((updatedProperty) => {
      console.log(updatedProperty)
      setProperties((prevProps) => 
        prevProps.map((p) => (p.id === id ? updatedProperty : p))
      )
      nav(`/properties`)
    })
  }

  const deleteProperty = id => {
    fetch(`http://127.0.0.1:5555/properties/${id}`, {method: "DELETE"} 
    )
    .then(data => {
      console.log(data)
      setProperties(prevProps => prevProps.filter(p => p.id !== id))
    })
  }

  return (
    <div>
      <Nav />
      <Routes>
        <Route exact path="/properties/new" element={<PropertyForm postProperty={postProperty}/>}/>
        <Route path="/properties/edit/:id" element={<PropertyEditForm editProperty={editProperty} patchProperty={patchProperty}/>} />
        <Route path="/properties/:id" element={<PropertyDetail/>}/>
        <Route path="/properties" element={<PropertyContainer properties={properties} setEditProperty={setEditProperty} deleteProperty={deleteProperty}/>}/>
        <Route path="/" element={<Home />}/>
      </Routes>
    </div>
  )
}

export default App




































// // import React from 'react';
// // import AppRoutes from './AppRoutes';

// // const App = () => {
// //   return (
// //     <div className="App">
// //       <header>
// //         <h1>Leaf Stone</h1>
// //       </header>
// //       <AppRoutes />
// //     </div>
// //   );
// // };

// // export default App;
// import React, {useEffect, useState} from 'react';
// import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
// import PropertyList from './components/PropertyList';
// import PropertyDetails from './components/PropertyDetails';
// import Favorites from './components/Favorites';
// import NavBar from './components/NavBar';
// import Home from './components/Home';
// import PropertyContainer from './components/PropertyContainer.js';
// import PropertyCard from './components/PropertyCard'

// const App = () => {

//   const [properties, setProperties] = useState([])
  
//   useEffect(() => {
//     fetch('/properties/')
//     .then(r => r.json())
//     .then(data => setProperties(data))
//   },[])
  
//   return (
//     <Router>
//       <NavBar />
//       <div className="App">
//        <Routes>
//         <Route path="/properties" component={PropertyList} properties={properties} />
//         <Route path="/Property/:id" component={PropertyDetails} />
//         <Route path="/Favorites" component={Favorites} />
//         <Route exact path="/" element={<Home properties={properties} />} />
//       </Routes>
//       </div>
//     </Router>
//   );
// };

// export default App;
